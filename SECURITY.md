# Security Policy

## Supported Versions

The following versions of this project are currently supported with security updates:

| Version | Status        |
|--------|---------------|
| main   | Supported     |

Older or experimental branches may not receive security fixes.

---

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please do **not** open a public issue directly.

Instead, please:

1. Email me at: emmaconaghanty@gmail.com
2. Include:
   - A clear description of the issue
   - Steps to reproduce (if possible)
   - Any relevant logs, screenshots, or proof-of-concept code

I will:

- Acknowledge your report as soon as possible
- Investigate the issue
- Plan a fix or mitigation
- Provide an approximate timeline for the resolution where possible

Please avoid:

- Exploiting the vulnerability beyond what is necessary to demonstrate it
- Accessing, modifying, or deleting data that you do not own
- Performing denial-of-service testing without prior permission

---

## Disclosure Policy

Once a fix is prepared and released:

- The vulnerability may be documented in the project’s changelog, release notes, or issues.
- You may be credited in the notes if you wish (and only if you explicitly agree).

This project does **not** currently operate a paid bug bounty program.

---

## Security Best Practices (for Users)

If you deploy or run this project, you are encouraged to:

- Keep your dependencies up to date (this repository uses Dependabot to help with that)
- Rotate any credentials or API keys if you suspect compromise
- Avoid committing secrets (passwords, tokens, private keys) to the repository
