from knowledge_base.kb_labels import (
    list_knowledge_document_type_labels,
    list_memory_card_type_labels,
    validate_knowledge_document_type,
    validate_memory_card_type
)

def test_labels_not_empty():
    assert len(list_knowledge_document_type_labels()) > 0
    assert len(list_memory_card_type_labels()) > 0

def test_validate_labels():
    validate_knowledge_document_type("research_report_document")
    validate_memory_card_type("symbol_memory_card")
