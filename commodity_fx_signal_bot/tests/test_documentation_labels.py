import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from documentation.documentation_labels import (
    list_document_type_labels,
    list_documentation_status_labels,
    list_documentation_safety_labels,
    list_documentation_audience_labels,
    validate_document_type,
    validate_documentation_safety
)

def test_label_lists_not_empty():
    assert len(list_document_type_labels()) > 0
    assert len(list_documentation_status_labels()) > 0
    assert len(list_documentation_safety_labels()) > 0
    assert len(list_documentation_audience_labels()) > 0

def test_validate_document_type_valid():
    validate_document_type("user_guide_doc")
    validate_document_type("unknown_doc")

def test_validate_documentation_safety_valid():
    validate_documentation_safety("safety_language_ok")
    validate_documentation_safety("missing_disclaimer")
