# HW6 - AI-Driven API Test Generator Design

## Goal

Generate auditable API test cases and Postman/Newman artifacts from the EShop API specification,
requirements, security rules, and selected endpoint.

## Inputs

- API specification:
- Requirements:
- Selected endpoint:
- Security rules:
- State model:
- Student configuration:

## Output Artifacts

- Test cases:
- Postman collection:
- Environment/data files:
- AI audit entries:
- Summary:

## Self-Drawn Diagram

- Diagram file:
- Tool used:
- Student confirmation that the diagram is self-drawn:

## Pseudocode

```text
function generateApiTests(spec, requirements, endpoint, config):
    contract = extractContract(spec, endpoint)
    rules = mapRequirements(requirements, contract.feature)
    domains = deriveDomains(contract.parameters, rules)
    securityCases = deriveSecurityCases(contract, rules.security)
    stateCases = deriveStateCases(contract, rules.stateModel)
    schemaCases = deriveSchemaCases(contract.responseSchema)
    candidateCases = merge(domains, securityCases, stateCases, schemaCases)
    rankedCases = deduplicateAndRank(candidateCases, targetMinimum=35)
    postmanArtifacts = emitPostman(rankedCases, config)
    auditLog = recordPromptsAndHumanReview()
    return rankedCases, postmanArtifacts, auditLog
```
