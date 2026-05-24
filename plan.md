1. **Settings Update**: Add `knowledge_base_enabled` and related settings to `config/settings.py` and `.env.example`.
2. **Paths Update**: Add knowledge base paths to `config/paths.py`. Update `ensure_project_directories()` in `config/paths.py` (or where appropriate) to create these paths.
3. **KB Config Module**: Create `knowledge_base/kb_config.py` with `KnowledgeBaseProfile` and default profiles.
4. **KB Labels Module**: Create `knowledge_base/kb_labels.py` with controlled label sets.
5. **KB Models Module**: Create `knowledge_base/kb_models.py` with `KnowledgeDocument`, `KnowledgeChunk`, `RetrievalResult`, `ResearchMemoryCard`, `DecisionJournalEntry` dataclasses.
6. **Document Discovery Module**: Create `knowledge_base/document_discovery.py`.
7. **Text Extraction Module**: Create `knowledge_base/text_extraction.py`.
8. **Chunking Module**: Create `knowledge_base/chunking.py`.
9. **Indexing Module**: Create `knowledge_base/indexing.py`.
10. **TF-IDF Retrieval Module**: Create `knowledge_base/tfidf_retrieval.py`.
11. **Fuzzy Retrieval Module**: Create `knowledge_base/fuzzy_retrieval.py`.
12. **Hybrid Retrieval Module**: Create `knowledge_base/hybrid_retrieval.py`.
13. **Memory Cards Module**: Create `knowledge_base/memory_cards.py`.
14. **Decision Journal Module**: Create `knowledge_base/decision_journal.py`.
15. **Analyst Notes Module**: Create `knowledge_base/analyst_notes.py`.
16. **Query Engine Module**: Create `knowledge_base/query_engine.py`.
17. **Findings Digest Module**: Create `knowledge_base/findings_digest.py`.
18. **Workspace Summary Module**: Create `knowledge_base/workspace_summary.py`.
19. **KB Quality Module**: Create `knowledge_base/kb_quality.py`.
20. **KB Report Builder Module**: Create `knowledge_base/kb_report_builder.py`.
21. **KB Pipeline Module**: Create `knowledge_base/kb_pipeline.py`.
22. **Data Lake Support**: Update `data/storage/data_lake.py` to support knowledge base outputs.
23. **Feature Store Support**: Update `ml/feature_store.py` to support loading knowledge base outputs.
24. **Scripts**: Create `scripts/run_knowledge_index_report.py`, `scripts/run_research_query.py`, `scripts/run_symbol_memory_report.py`, `scripts/run_decision_journal_report.py`, `scripts/run_recent_findings_digest.py`, `scripts/run_analyst_workspace_status.py`.
25. **Report Builder**: Update `reports/report_builder.py` with KB specific text formatting.
26. **README & Docs**: Update `README.md`, `docs/ARCHITECTURE.md`, `docs/PHASE_LOG.md`.
27. **Tests**: Add tests for all new KB modules.
28. **Pre-commit**: Complete pre commit steps.
