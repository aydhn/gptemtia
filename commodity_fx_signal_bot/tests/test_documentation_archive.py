import pytest
from pathlib import Path
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.documentation_archive import build_documentation_archive_index

def test_documentation_archive_index(tmp_path):
    profile = get_default_local_archive_profile()

    (tmp_path / "README.md").write_text("Hello")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "OPERATOR_MANUAL.md").write_text("Manual")

    df, summary = build_documentation_archive_index(tmp_path, profile)

    assert not df.empty
    roles = df["doc_role"].tolist()
    assert "project_root" in roles
    assert "operator_guide" in roles
