import pytest
from pathlib import Path
import pandas as pd
from unittest.mock import Mock

from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_pipeline import EvidenceGovernancePipeline
from config.settings import Settings

def test_evidence_pipeline():
    settings = Settings()
    profile = get_default_evidence_governance_profile()

    # Mock DataLake
    mock_dl = Mock()
    mock_dl.load_evidence_artifact_inventory.return_value = pd.DataFrame([{"artifact_id": "a1", "artifact_label": "report_evidence", "freshness_label": "evidence_fresh"}])
    mock_dl.load_policy_registry.return_value = pd.DataFrame([{"policy_id": "p1", "controls": ["c_dom"]}])
    mock_dl.load_control_registry.return_value = pd.DataFrame([{"control_id": "c1", "control_domain": "c_dom", "required_evidence_labels": ["report_evidence"]}])
    mock_dl.load_evidence_traceability_matrix.return_value = pd.DataFrame([{"artifact_id": "a1"}])

    pipeline = EvidenceGovernancePipeline(
        data_lake=mock_dl,
        settings=settings,
        project_root=Path("."),
        profile=profile
    )

    df, sum = pipeline.build_evidence_artifact_inventory(save=False)
    assert isinstance(df, pd.DataFrame)

    res, sum = pipeline.build_policy_control_mapping(save=False)
    assert "control_to_evidence_mapping" in res

    text, sum = pipeline.build_audit_evidence_binder(save=False)
    assert "Audit Evidence Binder" in text

    df, sum = pipeline.build_evidence_traceability_matrix(save=False)
    assert isinstance(df, pd.DataFrame)

    res, sum = pipeline.build_governance_evidence_export(save=False)
    assert "export_manifest" in res
