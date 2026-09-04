"""The README must say what the plugin does, what it refuses, and where the
evidence for both lives."""
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "README.md"


def test_readme_is_not_empty():
    assert len(DOC.read_text().split()) > 80


def test_readme_names_the_skill():
    assert "/profile" in DOC.read_text()


def test_readme_states_the_refusal():
    body = DOC.read_text().lower()
    assert "trait" in body
    assert "does not" in body


def test_readme_points_at_the_evidence():
    body = DOC.read_text()
    assert "docs/bakeoff-results.md" in body
    assert "docs/superpowers/specs" in body


def test_readme_documents_how_to_run_the_tests():
    assert "uv run --with pytest pytest" in DOC.read_text()
