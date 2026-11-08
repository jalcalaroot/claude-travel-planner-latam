# Security policy

## Design principles

- **No transactions.** The skill only searches and compares. It never books, reserves or pays.
- **Untrusted content.** Website content and tool results are treated as data, not as instructions. This reduces the risk of indirect prompt injection.
- **No sensitive data.** The skill does not ask for or store passport numbers, payment card numbers or other identity documents.
- **Least access.** The recommended connectors do not require an account. Optional tools (browser, calendar) are used only when the user has connected them.

## Reporting a problem

If you find a way to make the skill break these principles (for example, a web page that makes it try to book something or send data), please open a private security advisory in this repository instead of a public issue.

Include the request you used, the connectors that were active, and what happened.
