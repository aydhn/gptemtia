import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.control_mapping import (
    build_policy_to_control_mapping,
    map_controls_to_evidence,
    build_control_status_table
)

def test_control_mapping():
    profile = get_default_evidence_governance_profile()

    # Mocks
    pol_df = pd.DataFrame([{"policy_id": "p1", "controls": ["c_dom"], "policy_domain": "c_dom"}])
    ctrl_df = pd.DataFrame([{"control_id": "c1", "control_domain": "c_dom", "required_evidence_labels": ["test_ev"]}])
    art_df = pd.DataFrame([{"artifact_id": "a1", "artifact_label": "test_ev", "freshness_label": "evidence_fresh"}])

    # Test policy to control
    p2c = build_policy_to_control_mapping(pol_df, ctrl_df)
    assert not p2c.empty

    # Test control to evidence
    c2e, sum = map_controls_to_evidence(ctrl_df, art_df, profile)
    assert not c2e.empty
    assert c2e.iloc[0]["mapping_strength"] == "direct_evidence"

    # Test status
    status_df = build_control_status_table(ctrl_df, c2e, art_df)
    assert not status_df.empty
    assert status_df.iloc[0]["status"] == "control_evidenced"
