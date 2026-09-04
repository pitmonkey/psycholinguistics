"""Structural checks on the plugin: the manifest parses, the skill exists,
its frontmatter is well formed, and every reference it names resolves."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
SKILL = ROOT / "skills" / "profile" / "SKILL.md"


def frontmatter():
    match = re.match(r"^---\n(.*?)\n---\n", SKILL.read_text(), re.S)
    assert match, "SKILL.md must open with a YAML frontmatter block"
    return match.group(1)


def test_manifest_is_valid_json():
    data = json.loads(MANIFEST.read_text())
    assert data["name"] == "psycholinguistics"
    assert len(data["description"]) > 40


def test_skill_file_exists():
    assert SKILL.is_file(), "skills/profile/SKILL.md is missing"


def test_frontmatter_names_the_skill():
    assert re.search(r"^name: profile$", frontmatter(), re.M)


def test_frontmatter_description_is_substantive():
    match = re.search(r"^description: (.+)$", frontmatter(), re.M)
    assert match, "frontmatter needs a description"
    assert len(match.group(1)) > 60, "description must say when to use the skill"


def test_every_named_reference_resolves():
    named = set(re.findall(r"references/[a-z0-9_-]+\.md", SKILL.read_text()))
    for rel in sorted(named):
        assert (SKILL.parent / rel).is_file(), f"SKILL.md names {rel} but it does not exist"
