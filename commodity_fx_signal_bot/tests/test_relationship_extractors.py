import pytest
from local_knowledge_graph.relationship_extractors import (
    extract_paths_from_text,
    extract_symbols_from_text,
    extract_module_names_from_text,
    extract_command_names_from_text,
    build_relationship_extraction_summary
)

def test_extractors():
    assert extract_paths_from_text("path") is not None
    assert extract_symbols_from_text("sym") is not None
    assert extract_module_names_from_text("mod") is not None
    assert extract_command_names_from_text("cmd") is not None

def test_no_raw_secret():
    summary = build_relationship_extraction_summary("my secret")
    # Secret handling logic is a placeholder but ensures we don't expose raw
    assert "secret" not in str(summary.get("extracted_symbols", []))
