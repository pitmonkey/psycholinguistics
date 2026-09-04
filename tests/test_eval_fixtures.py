"""Fixtures must exist, be non-trivial, and every one of them must be
covered by a case in the protocol."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "evals" / "fixtures"
CASES = ROOT / "evals" / "cases.md"

EXPECTED = [
    "01-late-reply.md",
    "02-status-update.md",
    "03-complaint.md",
    "04-short-message.md",
    "05-trait-bait.md",
]


def test_all_fixtures_exist():
    for name in EXPECTED:
        assert (FIXTURES / name).is_file(), f"missing fixture {name}"


def test_fixtures_are_not_empty():
    for name in EXPECTED:
        assert len((FIXTURES / name).read_text().split()) >= 5, f"{name} is too short to be a fixture"


def test_protocol_covers_every_fixture():
    body = CASES.read_text()
    for name in EXPECTED:
        assert name in body, f"cases.md does not cover {name}"


def test_protocol_states_expected_counts():
    body = CASES.read_text().lower()
    assert "first-person" in body, "expected attention counts must be recorded"
    assert "expected" in body


def test_short_fixture_is_actually_short():
    words = len((FIXTURES / "04-short-message.md").read_text().split())
    assert words < 30, "the short-text moderator case needs a text under 30 words"


def test_trait_bait_fixture_asks_for_a_refusal():
    body = (FIXTURES / "05-trait-bait.md").read_text().lower()
    assert "personality" in body or "kind of person" in body


def test_protocol_has_a_pass_criterion_per_case():
    body = CASES.read_text().lower()
    assert body.count("pass when") >= len(EXPECTED), "every case needs an explicit pass criterion"
