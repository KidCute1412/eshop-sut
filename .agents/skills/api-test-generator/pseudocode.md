# Algorithmic Pseudocode: AI-Driven API Test Generator
**Author:** Le Tuan Lok (`23127404`)  
**Course:** Software Testing (CS300) — FIT HCMUS  
**Assignment ID:** `HW06-AI`  
**Bloom-AI Level:** `G9.5 Create`  

---

```text
ALGORITHM GenerateApiTestSuite(specDocument, endpointConfig, studentConfig)
    INPUT:
        specDocument: Markdown specification or OpenAPI 3.0 YAML object
        endpointConfig: Record { route: String, method: Enum[GET, POST, PUT, DELETE], pool: Enum[A, B, C] }
        studentConfig: Record { studentId: "23127404", targetHost: "http://localhost:3000" }
    
    OUTPUT:
        postmanCollection: RFC-Compliant Postman Collection v2.1.0 JSON object
        dataDrivenDataset: Array of parameterized test case records (JSON)

    BEGIN
        // -------------------------------------------------------------
        // LAYER 1: CONTRACT EXTRACTION & PARSING
        // -------------------------------------------------------------
        endpointSchema <- ParseEndpointContract(specDocument, endpointConfig.route)
        parameters <- ExtractParameters(endpointSchema)  // Path, Query, Header, Body
        roles <- ExtractAuthorizationRules(endpointSchema)
        stateModel <- ExtractLifecycleTransitions(endpointSchema)
        
        // -------------------------------------------------------------
        // LAYER 2: METHODOLOGY TEST GENERATION ENGINES
        // -------------------------------------------------------------
        validPartitions <- {}
        invalidPartitions <- {}
        FOR EACH param IN parameters DO
            validPartitions[param] <- GenerateValidClasses(param.type, param.constraints)
            invalidPartitions[param] <- GenerateInvalidClasses(param.type, param.constraints)
        END FOR
        
        bvaTestCases <- []
        FOR EACH orderedParam IN parameters.GetOrderedNumericsAndLengths() DO
            onPoints <- GetBoundaryValues(orderedParam)
            offPoints <- GetAdjacentValues(onPoints)
            inPoints <- GetRepresentativeValidValues(orderedParam)
            bvaTestCases <- CombineBoundaryPoints(onPoints, offPoints, inPoints)
        END FOR

        validTransitions <- []
        invalidTransitions <- []
        IF stateModel IS NOT NULL THEN
            validTransitions <- GenerateValidStatePaths(stateModel.graph)
            invalidTransitions <- GenerateInvalidStateViolations(stateModel.terminalStates, stateModel.unsupportedEdges)
        END IF

        secCases <- []
        secCases.Append(InjectSqlInjectionVectors(parameters))
        secCases.Append(InjectXssVectors(parameters))
        secCases.Append(InjectAuthBypassVectors(roles))
        secCases.Append(InjectRoleEscalationVectors(roles))
        secCases.Append(InjectPlaintextPasswordAudit(endpointSchema))

        // -------------------------------------------------------------
        // LAYER 3: COMBINATORIAL SYNTHESIS & AUDIT MATRIX
        // -------------------------------------------------------------
        rawSuite <- Combine(validPartitions, invalidPartitions, bvaTestCases, validTransitions, invalidTransitions, secCases)
        annotatedSuite <- ApplyAuditLabelsAndOracles(rawSuite)
        
        // -------------------------------------------------------------
        // LAYER 4: POSTMAN ARTIFACT SYNTHESIS
        // -------------------------------------------------------------
        preRequestScript <- GeneratePreRequestScript(headerKey="X-Student-Id", studentId=studentConfig.studentId)
        testAssertionScripts <- GenerateChaiAssertionSuite(endpointSchema.responseContract)

        postmanCollection <- BuildCollectionJson(
            name = Concatenate("Auto-Generated - ", endpointConfig.route, " - ", studentConfig.studentId),
            endpoint = endpointConfig.route,
            method = endpointConfig.method,
            preRequest = preRequestScript,
            tests = testAssertionScripts
        )

        dataDrivenDataset <- ExportJsonDataset(annotatedSuite)

        RETURN (postmanCollection, dataDrivenDataset)
    END
```
