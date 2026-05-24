cd commodity_fx_signal_bot
source venv/bin/activate
pytest tests/test_kb*.py tests/test_knowledge_base*.py tests/test_document_discovery.py tests/test_text_extraction.py tests/test_chunking.py tests/test_indexing.py tests/test_tfidf_retrieval.py tests/test_fuzzy_retrieval.py tests/test_hybrid_retrieval.py tests/test_memory_cards.py tests/test_decision_journal.py tests/test_analyst_notes.py tests/test_query_engine.py tests/test_findings_digest.py tests/test_workspace_summary.py
