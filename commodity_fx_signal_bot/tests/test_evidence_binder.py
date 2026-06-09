import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_binder import (
    build_audit_evidence_binder,
    build_binder_index
)

def test_build_audit_evidence_binder():
    profile = get_default_evidence_governance_profile()

    pol_df = pd.DataFrame([{"policy_id": "p1"}])
    ctrl_df = pd.DataFrame([{"control_id": "c1"}])
    art_df = pd.DataFrame([{"artifact_id": "a1", "artifact_label": "test_ev", "freshness_label": "fresh"}])
    map_df = pd.DataFrame([{"artifact_id": "a1", "control_id": "c1"}])

    text, summary = build_audit_evidence_binder(pol_df, ctrl_df, map_df, art_df, profile)

    assert "Audit Evidence Binder" in text
    assert "policy_id" in text
    assert summary["binder_length_chars"] > 0
    assert summary["total_indexed_artifacts"] == 1

def test_build_binder_index():
    art_df = pd.DataFrame([{"artifact_id": "a1", "artifact_label": "test_ev"}])
    map_df = pd.DataFrame([{"artifact_id": "a1", "control_id": "c1"}])

    idx = build_binder_index(art_df, map_df)
    assert len(idx) == 1
    assert idx.iloc[0]["mapped_controls"] == 1
