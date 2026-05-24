import pandas as pd

from governance.governance_report_builder import build_artifact_inventory_markdown_report


def test_markdown_builder():
    df = pd.DataFrame([{"artifact_type": "type", "file_name": "f", "size_bytes": 10}])
    sum = {"total_artifacts": 1, "total_size_mb": 0.01}
    md = build_artifact_inventory_markdown_report(sum, df)
    assert "Artifact Inventory Report" in md
    assert "Canlı emir" in md # Disclaimer
