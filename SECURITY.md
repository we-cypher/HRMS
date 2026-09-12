# Security Policy

We CYPHER takes security seriously. This document explains how to report vulnerabilities, which versions we support, what is in or out of scope, and how we handle disclosure.

This policy applies to WePeople HRMS ([`we-cypher/HRMS`](https://github.com/we-cypher/HRMS)).

## Supported versions

| Version | Branch(es) | Security support |
|---------|------------|------------------|
| v2 | `2.0` (default), `dev/v2.0` (active development) | **Yes** — actively maintained |

## Reporting a vulnerability

**Do not** open a public GitHub issue or discussion for a security vulnerability.
**Do not** disclose exploit details publicly until we have published a fix or explicitly agreed otherwise.

### How to report

Use **GitHub Private Vulnerability Reporting** only:

1. Open a [private vulnerability report](https://github.com/we-cypher/HRMS/security/advisories/new) on this repository.
2. Include enough detail for us to reproduce the issue (see below).

We aim to **acknowledge** valid reports within **72 hours**. Resolution time depends on severity and complexity; we will keep you informed via the private advisory thread.

### What to include

- Affected **version** or commit / Docker tag
- Environment notes (self-hosted Compose, reverse proxy, auth mode) — use variable *names* and redacted examples only
- Step-by-step reproduction (minimal PoC preferred)
- Impact (who can exploit it, and what they gain)
- Whether a fix or workaround is already known

**Never** paste live secrets, tokens, database dumps, or customer PII.

## Scope

### In scope

- Vulnerabilities in **application code** shipped in this repository
- Unsafe **default configuration** that we ship (for example a publicly known default `SECRET_KEY` in production paths)
- Issues that are **authentically exploitable** with realistic privileges on a **supported** version

### Out of scope

| Class | Notes |
|-------|--------|
| CSV / Excel formula injection | Spreadsheet clients interpret cell content; not an application bug |
| Privilege escalation by users who already administer users/roles | Trusted-admin capability by design |
| Pure deployment misconfiguration | Operator responsibility (`DEBUG=True`, open admin, weak secrets you set yourself) |
| Media / static XSS when files are served outside documented secure paths | Follow Docker / deployment docs |
| Dependency CVEs with **no reachable path** | Tracked via Dependabot when applicable |
| Third-party plugins or custom code not shipped by us | Report to that project's maintainers |

## Severity (guidance)

| Level | Examples |
|-------|----------|
| Critical | Unauthenticated RCE, unauthenticated auth bypass, mass data exposure without auth |
| High | Authenticated RCE, large-scale IDOR on PII/payroll, authenticated auth bypass |
| Medium | XSS requiring user interaction, limited IDOR, open redirect |
| Low | Low-impact issues, verbose errors without clear exploit path |

## Contact

- Security reports: [GitHub Private Vulnerability Reporting](https://github.com/we-cypher/HRMS/security/advisories/new)
- Non-security questions: open a GitHub Discussion or contact support@wecypher.com

## Disclaimer

The We CYPHER project and its maintainers assume no liability for security vulnerabilities reported or discovered. We greatly appreciate responsible disclosure that helps keep users safe.
