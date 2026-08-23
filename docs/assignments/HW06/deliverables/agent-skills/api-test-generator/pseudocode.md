# Pseudocode: AI-Driven API Test Generator Architecture

## System Overview
The test generator autonomously transforms API specifications (Markdown / OpenAPI 3.0) into structured, executable Postman collections and data-driven test datasets.

```text
ALGORITHM GenerateApiTestSuite(specDocument, endpointConfig):
    Input:
        specDocument: Markdown or OpenAPI YAML string
        endpointConfig: Target endpoint route, method, schema
    Output:
        postmanCollection: RFC-compliant Postman Collection JSON v2.1.0
        dataDrivenDataset: Array of parameterized test execution iterations
        auditTraceabilityMatrix: Complete mapping of test cases to EP/BVA/State/Security tags

    BEGIN
        1. PARSE SPECIFICATION:
            endpointSchema <- ParseEndpointContract(specDocument, endpointConfig.route)
            parameters <- ExtractParameters(endpointSchema)  // Path, Query, Header, Body
            roles <- ExtractAuthorizationRules(endpointSchema)
            stateModel <- ExtractLifecycleTransitions(endpointSchema)

        2. EQUIVALENCE PARTITIONING (EP):
            FOR EACH param IN parameters DO:
                validPartitions[param] <- GenerateValidClasses(param.type, param.constraints)
                invalidPartitions[param] <- GenerateInvalidClasses(param.type, param.constraints)
            END FOR

        3. BOUNDARY VALUE ANALYSIS (BVA):
            FOR EACH orderedParam IN parameters WHERE orderedParam.isOrdered() DO:
                onPoints <- GetBoundaryValues(orderedParam)
                offPoints <- GetAdjacentValues(onPoints)
                inPoints <- GetRepresentativeValidValues(orderedParam)
                bvaTestCases <- CombineBoundaryPoints(onPoints, offPoints, inPoints)
            END FOR

        4. STATE TRANSITION SYNTHESIS:
            IF stateModel EXISTS THEN:
                validTransitions <- GenerateValidStatePaths(stateModel.graph)
                invalidTransitions <- GenerateInvalidStateViolations(stateModel.terminalStates, stateModel.unsupportedEdges)
            END IF

        5. SECURITY & OWASP RULE INJECTION (SEC-01..SEC-07):
            secCases <- []
            secCases += GenerateSqlInjectionPayloads(parameters)
            secCases += GenerateXssPayloads(parameters)
            secCases += GenerateRbacPrivilegeEscalationTests(roles)
            secCases += GenerateMissingTokenAndTamperedJwtTests()

        6. TEST COMBINATION & AUDIT MATRIX COMPILATION:
            rawSuite <- Combine(validPartitions, invalidPartitions, bvaTestCases, validTransitions, invalidTransitions, secCases)
            annotatedSuite <- ApplyAuditLabelsAndOracles(rawSuite)

        7. POSTMAN ARTIFACT GENERATION:
            preRequestScript <- GeneratePreRequestScript(headerKey="X-Student-Id", studentId="23127404")
            testAssertionScripts <- GenerateChaiAssertionSuite(endpointSchema.responseContract)
            
            postmanCollection <- BuildCollectionJson(
                name="AI Generated Suite",
                route=endpointConfig.route,
                method=endpointConfig.method,
                preRequest=preRequestScript,
                tests=testAssertionScripts
            )
            dataDrivenDataset <- ExportJsonDataset(annotatedSuite)

        RETURN postmanCollection, dataDrivenDataset, annotatedSuite
    END
```
