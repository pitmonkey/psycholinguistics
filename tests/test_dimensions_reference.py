"""The dimensions reference must define every dimension the output contract
can emit, keep the three tiers separate, and carry the failure cases the
bakeoff surfaced."""
import re
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "skills" / "profile" / "references" / "dimensions.md"

TIER_1 = ["attention", "temporal", "certainty", "agency", "analytic", "complexity"]
TIER_2 = ["valence", "emotion", "arousal", "stance"]


def text():
    return DOC.read_text()


def test_file_exists():
    assert DOC.is_file()


def test_every_tier_1_dimension_is_defined():
    for name in TIER_1:
        assert re.search(rf"^### {name}\b", text(), re.M), f"no section for Tier 1 dimension {name}"


def test_every_tier_2_dimension_is_defined():
    for name in TIER_2:
        assert re.search(rf"^### {name}\b", text(), re.M), f"no section for Tier 2 dimension {name}"


def test_tiers_are_separate_sections():
    for heading in ["## Tier 1", "## Tier 2", "## Tier 3"]:
        assert heading in text(), f"missing {heading}"


def test_tier_3_is_refused_not_scored():
    tier_3 = text().split("## Tier 3", 1)[1]
    assert "unavailable" in tier_3.lower()
    for banned in ["big five", "extraversion", "neuroticism"]:
        assert banned in tier_3.lower(), f"Tier 3 must name {banned} as out of scope"
    assert "low confidence" not in tier_3.lower(), "Tier 3 is refused, never reported at low confidence"


def test_topic_versus_expression_failure_case_is_documented():
    assert "death of fear is certain" in text(), "the topic-vs-expression trap must be shown"


def test_disgust_anger_seam_is_documented():
    body = text().lower()
    assert "disgust" in body and "anger" in body
    assert "6 of 15" in body, "the measured disgust/anger confusion rate must be stated"
