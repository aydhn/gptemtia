from knowledge_base.kb_models import build_document_id, build_chunk_id, build_retrieval_result_id, sanitize_query_text

def test_build_ids():
    assert build_document_id("test/path.md").startswith("doc_")
    assert build_chunk_id("doc_123", 0).startswith("chk_doc_123")
    assert build_retrieval_result_id("q", "d", "c", "m").startswith("ret_")

def test_sanitize_query():
    assert sanitize_query_text("hello! world@") == "hello world"
