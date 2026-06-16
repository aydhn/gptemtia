from artifact_metadata.metadata_models import (
    ResearchArtifact, ArtifactCard, build_research_artifact_id,
    build_artifact_card_id, build_reproducibility_check_id,
    research_artifact_to_dict, artifact_card_to_dict
)

def test_build_ids_deterministic():
    id1 = build_research_artifact_id("path/to/file.txt")
    id2 = build_research_artifact_id("path/to/file.txt")
    assert id1 == id2
    assert id1.startswith("art_")

    cid1 = build_artifact_card_id(id1, "model_card")
    cid2 = build_artifact_card_id(id1, "model_card")
    assert cid1 == cid2
    assert cid1.startswith("crd_")

    rid1 = build_reproducibility_check_id(id1, "check1")
    rid2 = build_reproducibility_check_id(id1, "check1")
    assert rid1 == rid2
    assert rid1.startswith("rep_")

def test_dataclass_to_dict():
    ra = ResearchArtifact("id1", "path", "model_artifact", "mod1", "title", "desc", "time", "hash", 100, "use", "status", ["warn"])
    d = research_artifact_to_dict(ra)
    assert d["artifact_id"] == "id1"
    assert d["warnings"] == "warn"

    ac = ArtifactCard("cid", "id1", "model_card", "t", "s", "i", "np", ["l"], ["i"], ["o"], {}, ["l2"], "r", [])
    d2 = artifact_card_to_dict(ac)
    assert d2["card_id"] == "cid"
    assert d2["non_use_policy"] == "np"
