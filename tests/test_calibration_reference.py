"""The calibration reference must carry the moderators, the downgrade rules
and the refusal list, each stated concretely enough to act on."""
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "skills" / "profile" / "references" / "calibration.md"


def text():
    return DOC.read_text().lower()


def test_file_exists():
    assert DOC.is_file()


def test_genre_and_task_moderator_is_present():
    assert "genre" in text() and "task" in text()


def test_demographic_moderation_is_documented():
    body = text()
    assert "first-person" in body
    assert "did not" in body or "not among" in body, "state that the marker failed to transfer across groups"


def test_short_text_moderator_is_present():
    assert "short" in text()


def test_performed_text_moderator_is_present():
    assert "performed" in text() or "rehearsed" in text()


def test_refusal_list_is_explicit():
    body = text()
    for item in ["trait", "clinical", "predict"]:
        assert item in body, f"refusal list must cover {item}"


def test_downgrade_rules_are_actionable():
    body = text()
    assert "drop the row" in body, "there must be a rule for removing a row, not only softening it"
    assert "high" in body and "medium" in body and "low" in body
