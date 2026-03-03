# Threat Model - LLMSecurityGuard

## Assets
- User prompts
- LLM responses
- API gateway
- Audit logs
- Nonces and MCP signatures

## Threats (STRIDE)
- **Spoofing:** Unauthorized users sending prompts
- **Tampering:** Prompt modification
- **Repudiation:** Missing audit logs
- **Information Disclosure:** Sensitive output leaking
- **Denial of Service:** Rate-limit abuse
- **Elevation of Privilege:** Users exceeding roles

## Mitigations
- Authentication & RBAC
- MCP signatures & nonces
- Input & output sanitization
- Manual review for high-risk prompts
- Logging & monitoring
- Rate limiting