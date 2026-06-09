import pytest
import pandas as pd
from evidence_governance.evidence_report_builder import (
    build_evidence_artifact_inventory_markdown_report,
    build_audit_evidence_binder_markdown_report
)

def test_evidence_report_builder():
    summary = {"total_artifacts": 5}
    art_df = pd.DataFrame([{"artifact_id": "a1", "artifact_label": "lbl", "freshness_label": "fresh", "relative_path": "path"}])

    md1 = build_evidence_artifact_inventory_markdown_report(summary, art_df)
    assert "Evidence Artifact Inventory" in md1
    assert "Total Artifacts:** 5" in md1
    assert "a1" in md1

    md2 = build_audit_evidence_binder_markdown_report({}, "My Binder Content")
    assert "My Binder Content" in md2
    assert "UYARI:** Bu çıktı offline/local governance evidence" in md2
