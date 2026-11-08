"""Validate the marketplace manifest and every skill it lists.

Checks:
- .claude-plugin/marketplace.json is valid JSON with the required fields.
- Every listed skill folder exists and contains SKILL.md.
- SKILL.md has YAML frontmatter with a valid name and a description.
- The skill name matches its folder name.

Run: python scripts/validate.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME = 64
MAX_DESCRIPTION = 1024

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path}: missing YAML frontmatter")
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def check_skill(skill_dir: Path) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail(f"{skill_dir}: SKILL.md not found")
        return
    fields = read_frontmatter(skill_file)
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME_RE.match(name) or len(name) > MAX_NAME:
        fail(f"{skill_file}: invalid name '{name}'")
    if name != skill_dir.name:
        fail(f"{skill_file}: name '{name}' does not match folder '{skill_dir.name}'")
    if not description:
        fail(f"{skill_file}: description is empty")
    elif len(description) > MAX_DESCRIPTION:
        fail(f"{skill_file}: description is longer than {MAX_DESCRIPTION} characters")
    if "<" in description or ">" in description:
        fail(f"{skill_file}: description must not contain angle brackets")


def main() -> int:
    manifest_path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read {manifest_path}: {exc}")
        return 1

    for field in ("name", "owner", "plugins"):
        if field not in manifest:
            fail(f"marketplace.json: missing '{field}'")

    for plugin in manifest.get("plugins", []):
        for field in ("name", "description", "source"):
            if field not in plugin:
                fail(f"marketplace.json: plugin missing '{field}'")
        for skill in plugin.get("skills", []):
            check_skill((ROOT / skill).resolve())

    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
