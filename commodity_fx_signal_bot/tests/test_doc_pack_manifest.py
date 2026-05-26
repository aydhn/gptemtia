import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd
from documentation.documentation_config import get_default_documentation_profile
from documentation.doc_pack_manifest import (
    build_documentation_pack_manifest,
    build_documentation_pack_manifest_json,
    summarize_documentation_pack_manifest
)

def test_build_documentation_pack_manifest():
    profile = get_default_documentation_profile()
    docs_df = pd.DataFrame([{"relative_path": "USER_GUIDE.md"}])
    cov_df = pd.DataFrame()
    saf_df = pd.DataFrame()

    manifest = build_documentation_pack_manifest(profile, docs_df, cov_df, saf_df)
    assert manifest.profile_name == "balanced_documentation_pack"
    assert manifest.document_count == 1
    assert "OPERATOR_MANUAL.md" in manifest.missing_documents

def test_manifest_json_and_summary():
    profile = get_default_documentation_profile()
    docs_df = pd.DataFrame()
    manifest = build_documentation_pack_manifest(profile, docs_df, pd.DataFrame(), pd.DataFrame())

    m_json = build_documentation_pack_manifest_json(manifest, docs_df)
    assert "disclaimer" in m_json

    summary = summarize_documentation_pack_manifest(m_json)
    assert summary["profile"] == "balanced_documentation_pack"
