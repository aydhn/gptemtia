import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from documentation.doc_report_builder import (
    build_documentation_pack_markdown_report,
    build_documentation_quality_markdown_report,
    build_safe_usage_docs_markdown_report,
    build_script_reference_markdown_report,
    build_output_reference_markdown_report,
    build_documentation_status_markdown_report,
    build_documentation_disclaimer
)
import pandas as pd

def test_build_documentation_disclaimer():
    assert "Canlı emir" in build_documentation_disclaimer()

def test_build_reports():
    summary = {"profile": "test", "quality_score": 0.8}
    df = pd.DataFrame()

    assert "Documentation Pack" in build_documentation_pack_markdown_report(summary, df)
    assert "Documentation Quality" in build_documentation_quality_markdown_report(summary, {})
    assert "Safe Usage Docs" in build_safe_usage_docs_markdown_report(summary, df)
    assert "Script Reference" in build_script_reference_markdown_report(summary, df)
    assert "Output Reference" in build_output_reference_markdown_report(summary, df)
    assert "Documentation Status" in build_documentation_status_markdown_report(summary, df)
