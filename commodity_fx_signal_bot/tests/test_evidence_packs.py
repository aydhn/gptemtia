import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_packs import (
    build_safety_evidence_pack,
    build_secrets_hygiene_evidence_pack
)

def test_evidence_packs():
    profile = get_default_evidence_governance_profile()

    art_df = pd.DataFrame([
        {"artifact_id": "a1", "artifact_label": "safety_evidence"},
        {"artifact_id": "a2", "artifact_label": "secrets_hygiene_evidence"},
        {"artifact_id": "a3", "artifact_label": "other_evidence"}
    ])

    map_df = pd.DataFrame()

    sf_df, sum = build_safety_evidence_pack(art_df, map_df, profile)
    assert len(sf_df) == 1
    assert sum["pack_size"] == 1

    sec_df, _ = build_secrets_hygiene_evidence_pack(art_df, map_df, profile)
    assert len(sec_df) == 1
