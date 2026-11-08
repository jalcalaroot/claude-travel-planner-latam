# Contributing

Thank you for your interest in this project. Contributions are welcome, especially from travelers in Latin America.

## Good contributions

- Regional knowledge: airline hubs, common connections, local payment options for your country.
- Support for a new connector from the Claude connector directory.
- Fixes when a connector changes its behavior.
- Clearer instructions or better examples.

## How to contribute

1. Open an issue first to describe the change.
2. Fork the repository and create a branch.
3. Make your change. Keep the skill instructions in simple English.
4. Run `claude plugin validate . --profile directory` and make sure that all checks pass. The same checks also run on every pull request.
5. Add a line to `CHANGELOG.md` under a new "Unreleased" section.
6. Open a pull request.

## Rules

- Do not include personal data (names, passport numbers, booking codes, emails) in examples or issues.
- Do not add instructions that make the skill book, reserve or pay.
- Do not add connector URLs that you have not verified with the provider documentation.
