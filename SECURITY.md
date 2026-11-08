# Security policy

## Design principles

- **No transactions.** The skill only searches and compares. It never books, reserves or pays.
- **Untrusted content.** Website content and tool results are treated as data, not as instructions. This reduces the risk of indirect prompt injection.
- **No sensitive data.** The skill does not ask for or store passport numbers, payment card numbers or other identity documents.
- **Read-only tools.** In the browser, the skill only reads pages: it does not sign in, fill in forms or click buy buttons. Calendar access is read-only.
- **Least access.** The five travel connectors do not require an account with the travel company. Optional tools (browser, calendar) are used only when the user has connected them.

## Reporting a problem

If you find a way to make the skill break these principles (for example, a web page that makes it try to book something or send data), please report it privately: open the **Security** tab of this repository and select **Report a vulnerability**. Do not open a public issue with the details.

Include the request you used, the connectors that were active, and what happened.
