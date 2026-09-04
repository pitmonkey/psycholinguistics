"""The skill body must state the procedure in order, define the output
contract, and point at both references."""
import re
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "skills" / "profile" / "SKILL.md"


def text():
    return DOC.read_text()


def test_placeholder_is_gone():
    assert "Task 4" not in text(), "the Task 1 placeholder line must be replaced"


def test_both_references_are_named():
    body = text()
    assert "references/dimensions.md" in body
    assert "references/calibration.md" in body


def test_procedure_reads_for_sense_before_scoring():
    body = text().lower()
    sense = body.index("once for sense")
    counts = body.index("count the tier 1")
    assert sense < counts, "reading for sense must come before any counting"


def test_output_contract_shows_table_then_evidence():
    body = text()
    assert "| dimension" in body, "the contract must show the table header"
    assert body.index("| dimension") < body.index("counter-evidence"), "table comes before evidence"


def test_counter_evidence_is_required():
    body = text().lower()
    assert "counter-evidence" in body
    assert "required" in body


def test_every_tier_2_row_needs_a_quoted_span():
    body = text().lower()
    assert "quoted span" in body
    assert "does not appear" in body or "drop" in body


def test_tier_3_refusal_is_stated_in_the_skill_itself():
    body = text().lower()
    assert "trait" in body
    assert "unavailable" in body or "not report" in body


def test_confidence_values_are_the_three_defined_ones():
    found = set(re.findall(r"\b(high|medium|low)\b", text().lower()))
    assert found == {"high", "medium", "low"}
