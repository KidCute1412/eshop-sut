"""
Pseudocode for the HW06 AI-driven API test generator.

This is design pseudocode, not a production implementation. It describes how the generator
would transform the API specification and requirement documents into auditable API tests.
"""


def generate_api_tests(source_files, selected_features, student_config):
    sources = load_sources(source_files)
    security_rules = extract_security_rules(sources["README.md"])
    setup_model = extract_setup_model(sources["setup_guide.md"])
    assignment_rules = extract_assignment_rules(sources["HW06"])

    all_feature_artifacts = []

    for feature_id in selected_features:
        endpoint_contracts = parse_endpoint_contracts(
            api_spec=sources["api_specification.md"],
            feature_id=feature_id,
        )

        feature_rules = map_feature_requirements(
            readme=sources["README.md"],
            feature_id=feature_id,
        )

        feature_cases = []
        raw_ai_outputs = []

        for contract in endpoint_contracts:
            contract.requirement_refs = feature_rules.refs
            contract.security_refs = map_security_refs(contract, security_rules)
            contract.ambiguities = detect_ambiguities(contract, feature_rules)

            domains = derive_domain_partitions(contract)
            boundaries = derive_boundary_values(contract, feature_rules)
            auth_cases = derive_auth_cases(contract)
            security_cases = derive_security_cases(contract, security_rules)
            state_cases = derive_state_cases(contract, feature_rules)
            schema_cases = derive_schema_cases(contract)

            deterministic_seed_cases = merge_case_ideas(
                domains,
                boundaries,
                auth_cases,
                security_cases,
                state_cases,
                schema_cases,
            )

            prompt = build_ai_prompt(
                contract=contract,
                feature_rules=feature_rules,
                security_rules=security_rules,
                deterministic_seed_cases=deterministic_seed_cases,
                assignment_rules=assignment_rules,
            )

            raw_ai_output = call_ai_model(prompt)
            raw_ai_outputs.append(raw_ai_output)

            ai_cases = parse_ai_test_table(raw_ai_output)
            normalized_cases = normalize_cases(ai_cases, contract, feature_id)
            feature_cases.extend(normalized_cases)

        candidate_cases = deduplicate_and_rank(feature_cases)
        candidate_cases = assign_stable_ids(candidate_cases, prefix=f"{feature_id}-API")

        validation_report = validate_candidate_cases(
            candidate_cases,
            sources=sources,
            setup_model=setup_model,
            assignment_rules=assignment_rules,
        )

        reviewed_cases = human_review_gate(
            candidate_cases,
            validation_report,
            allowed_labels=["VALID", "INVALID", "INCOMPLETE"],
        )

        human_added_cases = collect_human_added_cases(
            feature_id=feature_id,
            minimum=5,
            focus=["security", "state", "schema", "boundary", "SUT-specific risk"],
        )

        final_cases = apply_human_corrections(
            reviewed_cases=reviewed_cases,
            human_added_cases=human_added_cases,
            preserve_ids=True,
        )

        postman_items = emit_postman_items(
            final_cases,
            base_url_var="{{baseUrl}}",
            student_id_var="{{studentId}}",
            setup_model=setup_model,
        )

        feature_artifacts = {
            "feature_id": feature_id,
            "contracts": endpoint_contracts,
            "raw_ai_outputs": raw_ai_outputs,
            "candidate_cases": candidate_cases,
            "final_cases": final_cases,
            "postman_items": postman_items,
            "gap_analysis": compare_ai_vs_human(candidate_cases, final_cases),
        }

        all_feature_artifacts.append(feature_artifacts)

    collection = assemble_postman_collection(
        feature_artifacts=all_feature_artifacts,
        collection_name="HW06 EShop API Testing",
        student_config=student_config,
    )

    environment = assemble_postman_environment(
        base_url=student_config.base_url,
        student_id=student_config.student_id,
        credentials=setup_model.seed_credentials,
    )

    ci_workflow = emit_github_actions_workflow(
        backend_startup=setup_model.backend_startup,
        collection_path="reports/HW6/postman/HW06_FR01_FR07_FR17.postman_collection.json",
        environment_path="reports/HW6/postman/HW06_local.postman_environment.json",
        report_path="reports/HW6/newman/report.html",
    )

    write_markdown_reports(all_feature_artifacts)
    write_postman_files(collection, environment)
    write_ci_files(ci_workflow)
    write_ai_audit(all_feature_artifacts)

    return {
        "features": all_feature_artifacts,
        "collection": collection,
        "environment": environment,
        "ci_workflow": ci_workflow,
    }


def derive_domain_partitions(contract):
    cases = []
    for field in contract.request_fields:
        if field.required:
            cases.append(missing_field_case(contract, field))
            cases.append(empty_field_case(contract, field))
            cases.append(null_field_case(contract, field))

        cases.append(valid_representative_case(contract, field))
        cases.append(wrong_type_case(contract, field))

        if field.enum_values:
            cases.append(invalid_enum_case(contract, field))

        if field.unique:
            cases.append(duplicate_value_case(contract, field))

    return cases


def derive_boundary_values(contract, feature_rules):
    cases = []
    for field in contract.request_fields:
        constraints = find_constraints(field, feature_rules)

        if constraints.min_length is not None:
            cases.extend([
                length_case(contract, field, constraints.min_length - 1, expected="reject"),
                length_case(contract, field, constraints.min_length, expected="accept"),
            ])

        if constraints.min_value is not None:
            cases.extend([
                numeric_case(contract, field, constraints.min_value - 1, expected="reject"),
                numeric_case(contract, field, constraints.min_value, expected="accept"),
            ])

        if constraints.max_value is not None:
            cases.extend([
                numeric_case(contract, field, constraints.max_value, expected="accept"),
                numeric_case(contract, field, constraints.max_value + 1, expected="reject"),
            ])

        if constraints.date_required:
            cases.append(invalid_date_case(contract, field))
            cases.append(future_date_case(contract, field))

    return cases


def derive_auth_cases(contract):
    if not contract.auth_required:
        return []

    cases = [
        missing_token_case(contract),
        malformed_token_case(contract),
    ]

    if contract.required_role == "admin":
        cases.append(valid_user_token_for_admin_endpoint_case(contract))
        cases.append(valid_admin_token_case(contract))
    else:
        cases.append(valid_user_token_case(contract))

    return cases


def derive_security_cases(contract, security_rules):
    cases = []

    if security_rules.includes("SEC-02"):
        cases.append(access_without_auth_case(contract))

    if security_rules.includes("SEC-03"):
        cases.append(role_escalation_case(contract))
        cases.append(identity_injection_case(contract))

    if security_rules.includes("SEC-04"):
        cases.append(xss_like_payload_case(contract))

    if security_rules.includes("SEC-05"):
        cases.append(sql_injection_like_payload_case(contract))

    if security_rules.includes("SEC-01"):
        cases.append(sensitive_data_leakage_case(contract))

    return applicable_only(cases, contract)


def human_review_gate(candidate_cases, validation_report, allowed_labels):
    reviewed = []
    for case in candidate_cases:
        issue_list = validation_report.issues_for(case.id)

        if not issue_list:
            case.ai_review_label = "VALID"
            case.review_reason = "Supported by source of truth and executable."
        elif issue_list.contains_only_minor_setup_gaps():
            case.ai_review_label = "INCOMPLETE"
            case.review_reason = issue_list.summary()
        else:
            case.ai_review_label = "INVALID"
            case.review_reason = issue_list.summary()

        reviewed.append(case)

    return reviewed


def update_results_from_newman(final_cases, newman_output, evidence_files):
    parsed_results = parse_newman_output(newman_output)

    for case in final_cases:
        result = parsed_results.find_by_case_id(case.id)
        if result is None:
            case.actual_result = "No execution result found"
            case.status = "Not Executed"
            continue

        case.actual_result = format_http_result(result)
        case.status = "PASS" if result.passed else "FAIL"

        matching_evidence = evidence_files.find(case.id)
        if matching_evidence:
            case.evidence = matching_evidence.relative_link

    return final_cases
