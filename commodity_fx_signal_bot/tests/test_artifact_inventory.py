from pathlib import Path

from governance.artifact_inventory import ArtifactInventoryBuilder
from governance.governance_config import get_default_governance_profile


def test_classify_artifact_type():
    builder = ArtifactInventoryBuilder(Path("/proj"), Path("/proj/lake"), Path("/proj/reports"))
    assert builder.classify_artifact_type(Path("/proj/lake/features/f.parquet")) == "feature_artifact"
    assert builder.classify_artifact_type(Path("/proj/lake/raw/r.csv")) == "raw_data_artifact"
    assert builder.classify_artifact_type(Path("/proj/lake/unknown/u.txt")) == "unknown_artifact"

def test_scan_artifacts(tmp_path):
    project_root = tmp_path
    lake_root = project_root / "data" / "lake"
    reports_root = project_root / "reports" / "output"

    lake_root.mkdir(parents=True)
    reports_root.mkdir(parents=True)

    feat_dir = lake_root / "features"
    feat_dir.mkdir()
    (feat_dir / "test.txt").write_text("hello")

    builder = ArtifactInventoryBuilder(project_root, lake_root, reports_root)
    profile = get_default_governance_profile()

    df, summary = builder.scan_artifacts(profile)
    assert not df.empty
    assert summary["total_artifacts"] == 1
    assert "test.txt" in df["file_name"].values
