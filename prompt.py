

CANNED_PROMPTS = {
    "/cve": """Analyze the following CVE in detail:
CVE ID: {cve_id}
Provide:
- Description and root cause (map to CWE)
- CVSS score and attack vector
- Affected products and versions
- Proof of concept or exploit details if available
- Remediation and mitigation steps
- Related CVEs or vulnerability chains
Severity tag: [CRITICAL/HIGH/MEDIUM/LOW]""",

    "/codereview": """Perform a security code review on the following code:
Language: {language}
Code:
{code}
Provide:
- Identified vulnerabilities with line references
- CWE and OWASP category for each finding
- Vulnerable pattern explanation
- Secure code alternative for each finding
- Overall risk rating""",

    "/threatmodel": """Create a threat model for the following application:
Application: {app_description}
Provide:
- Application attack surface
- STRIDE analysis (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege)
- Top 5 threats ranked by risk
- Recommended security controls for each threat
- Data flow diagram description""",

    "/bugbounty": """Analyze the following bug bounty writeup or vulnerability report:
Target: {target}
Vulnerability: {description}
Provide:
- Vulnerability class and root cause
- OWASP and CWE mapping
- Attack chain and business impact
- Key takeaways for defenders
- Similar vulnerabilities to look for in other applications""",

    "/secadvisory": """Summarize the following security advisory:
Advisory: {advisory}
Provide:
- Affected product and versions
- Vulnerability summary in plain English
- Severity and exploitability
- Recommended immediate actions
- Patch or workaround availability""",

    "/authnreview": """Analyze the following authentication or authorization implementation:
Description: {description}
Provide:
- Identified weaknesses in auth flow
- Relevant CVEs or known attack patterns
- OAuth/JWT/SSO specific issues if applicable
- Privilege escalation possibilities
- Recommended fixes and best practices""",

    "/help": """Available commands:
/cve {cve_id} - Analyze a CVE in depth
/codereview {language} {code} - Security code review
/threatmodel {app_description} - Generate threat model
/bugbounty {target} {description} - Analyze bug bounty writeup
/secadvisory {advisory} - Summarize security advisory
/authnreview {description} - Review authentication implementation
/clear - Reset conversation history
/save - Save current session
/load - Load previous session
/history - Show conversation history
/quit - Exit"""
}