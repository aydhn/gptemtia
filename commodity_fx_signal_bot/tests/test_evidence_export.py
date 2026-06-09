import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_export import (
    build_governance_evidence_export_manifest,
    build_local_evidence_export_index,
    validate_evidence_export_safety
)

def test_evidence_export():
    profile = get_default_evidence_governance_profile()

    art_df = pd.DataFrame([{"artifact_id": "a1", "artifact_label": "safety_evidence"}])
    pack_tables = {"safety": art_df}

    idx_df = build_local_evidence_export_index(art_df, pack_tables, profile)
    assert not idx_df.empty
    assert idx_df.iloc[0]["pack_name"] == "safety"

    manifest = build_governance_evidence_export_manifest(
        pd.DataFrame(), pd.DataFrame(), art_df, pd.DataFrame(), pd.DataFrame(), profile
    )
    assert manifest["export_metadata"]["cloud_upload"] is False
    assert manifest["export_metadata"]["local_only"] is True

    val = validate_evidence_export_safety(manifest, idx_df, profile)
    assert val["passed"] is True
