# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [0.1.3] - 2026-11-08

### Added

- Install guide for the Claude app (`docs/install-claude-app.md`), in English and Spanish. The app is now the recommended way to use the skill.
- Plugin manifest (`.claude-plugin/plugin.json`) and plugin icon, so the plugin can be submitted to Anthropic's plugin directory.
- Troubleshooting for "/plugin isn't available in this environment" in the Claude Code guide.

### Changed

- README: the Claude app comes first in the installation section.
- The validation script checks `plugin.json` and every skill in `skills/`.

## [0.1.2] - 2026-11-08

### Changed

- The skill now triggers on Spanish and Portuguese travel requests.
- Removed the claim about flight-plus-hotel packages: the connectors search flights and hotels.
- Clearer README: complete Spanish section, one name for the connector settings page, and accurate account requirements.

### Security

- Browser use is read-only: no sign-in, no forms, no buy or continue buttons.
- Calendar access is read-only.
- Private vulnerability reporting through the Security tab.

## [0.1.1] - 2026-11-08

### Added

- Step-by-step install guide for Claude Code (`docs/install-claude-code.md`), in English and Spanish.
- Clear note that connectors must be connected in the Claude account before the plugin is used.
- Plugin version in the marketplace manifest.

## [0.1.0] - 2026-11-08

### Added

- First release of the `travel-planner-latam` skill.
- Comparison of flights, hotels and activities across several connectors.
- Traveler profile section that each user can fill in.
- Check of available connectors, with a short message when one is missing.
- Safety rules: no booking or payment, and website content treated as data.
- Claude Code marketplace manifest.
- Validation script and GitHub Actions workflow.

[0.1.3]: https://github.com/jalcalaroot/claude-travel-planner-latam/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/jalcalaroot/claude-travel-planner-latam/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/jalcalaroot/claude-travel-planner-latam/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/jalcalaroot/claude-travel-planner-latam/releases/tag/v0.1.0
