import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pytest
from pathlib import Path
from documentation.doc_inventory import (
    classify_document_type,
    infer_document_audience,
    build_documentation_record
)

def test_classify_document_type():
    assert classify_document_type(Path("docs/USER_GUIDE.md")) == "user_guide_doc"
    assert classify_document_type(Path("docs/operator_manual.md")) == "operator_manual_doc"
    assert classify_document_type(Path("docs/some_file.md")) == "unknown_doc"

def test_infer_document_audience():
    assert infer_document_audience(Path("docs/USER_GUIDE.md")) == "user_audience"
    assert infer_document_audience(Path("docs/operator_manual.md")) == "operator_audience"

def test_build_documentation_record(tmp_path):
    project_root = tmp_path
    docs_dir = project_root / "docs"
    docs_dir.mkdir()

    ug_path = docs_dir / "USER_GUIDE.md"
    ug_path.write_text("# User Guide\n\nBu doküman offline/local araştırma platformunu açıklar.", encoding="utf-8")

    record = build_documentation_record(ug_path, project_root)
    assert record.title == "User Guide"
    assert record.document_type == "user_guide_doc"
    assert record.audience == "user_audience"
    assert record.has_disclaimer is True
    assert record.safety_label == "safety_language_ok"
