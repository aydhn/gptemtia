import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from documentation.documentation_models import (
    DocumentationRecord,
    build_doc_id,
    build_coverage_id,
    build_link_check_id,
    documentation_record_to_dict,
    estimate_word_count,
    count_markdown_headings
)

def test_build_doc_id_deterministic():
    id1 = build_doc_id("docs/USER_GUIDE.md")
    id2 = build_doc_id("docs/USER_GUIDE.md")
    assert id1 == id2
    assert id1.startswith("doc_")

def test_build_coverage_id_deterministic():
    id1 = build_coverage_id("data", "docs/MODULE_DATA.md")
    id2 = build_coverage_id("data", "docs/MODULE_DATA.md")
    assert id1 == id2
    assert id1.startswith("cov_")

def test_build_link_check_id_deterministic():
    id1 = build_link_check_id("USER_GUIDE.md", "OPERATOR_MANUAL.md")
    id2 = build_link_check_id("USER_GUIDE.md", "OPERATOR_MANUAL.md")
    assert id1 == id2
    assert id1.startswith("lnk_")

def test_documentation_record_to_dict():
    record = DocumentationRecord(
        doc_id="doc_test",
        title="Test",
        document_type="unknown",
        audience="unknown",
        path="/tmp/test",
        relative_path="test",
        status="doc_complete",
        word_count=10,
        heading_count=1,
        has_disclaimer=True,
        safety_label="safety_language_ok",
        warnings=[]
    )
    d = documentation_record_to_dict(record)
    assert d["doc_id"] == "doc_test"
    assert d["has_disclaimer"] is True

def test_word_and_heading_count():
    text = "# Title\n\nSome words here."
    assert estimate_word_count(text) == 5
    assert count_markdown_headings(text) == 1
