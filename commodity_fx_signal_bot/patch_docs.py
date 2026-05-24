from pathlib import Path

def patch_docs():
    # 1. README.md
    readme_path = Path("README.md")
    readme_content = readme_path.read_text()

    if "Knowledge Base, Research Memory and Analyst Workspace" not in readme_content:
        addition = """

## Knowledge Base, Research Memory and Analyst Workspace

The project includes an offline knowledge base and analyst workspace:
- Knowledge base local/offline çalışır.
- Ücretli embedding/API kullanmaz.
- Raporlar, docs, experiment, governance, planning ve meta-research çıktıları indexlenir.
- Retrieval result yatırım tavsiyesi değildir.
- Symbol memory card AL/SAT üretmez.
- Decision journal trade journal değildir.
- Findings digest trade fırsatı listesi değildir.
- Çıktılar `data/lake/knowledge_base` ve `reports/output/knowledge_base` altında oluşur.

### Komutlar:
```bash
python -m scripts.run_knowledge_index_report
python -m scripts.run_research_query --query "GC=F hakkında ne biliyoruz?"
python -m scripts.run_symbol_memory_report --symbol GC=F
python -m scripts.run_decision_journal_report
python -m scripts.run_recent_findings_digest
python -m scripts.run_analyst_workspace_status
```
"""
        readme_path.write_text(readme_content + addition)

    # 2. ARCHITECTURE.md
    arch_path = Path("docs/ARCHITECTURE.md")
    if arch_path.exists():
        arch_content = arch_path.read_text()
        if "DocumentDiscovery" not in arch_content:
            arch_addition = """
## Phase 49: Knowledge Base & Analyst Workspace

Docs / Reports Output / DataLake Research Artifacts / Experiments / Governance / Planning / Meta
→ `DocumentDiscovery`
→ `TextExtraction`
→ `Chunking`
→ `KnowledgeIndex`
→ `TFIDFRetrieval`
→ `FuzzyRetrieval`
→ `HybridRetrieval`
→ `MemoryCards`
→ `DecisionJournal`
→ `AnalystNotes`
→ `FindingsDigest`
→ `WorkspaceSummary`
→ `KBQuality`
→ Analyst Workspace Reports
"""
            arch_path.write_text(arch_content + "\n" + arch_addition)

    # 3. PHASE_LOG.md
    phase_path = Path("docs/PHASE_LOG.md")
    if phase_path.exists():
        phase_content = phase_path.read_text()
        if "Phase 49" not in phase_content:
            phase_addition = """
### Phase 49: Knowledge Base, Research Memory and Analyst Workspace
- Knowledge base profile sistemi eklendi.
- KB label registry eklendi.
- KnowledgeDocument, KnowledgeChunk, RetrievalResult, ResearchMemoryCard ve DecisionJournalEntry modelleri eklendi.
- Document discovery eklendi.
- Text extraction ve sensitive masking eklendi.
- Chunking eklendi.
- Local knowledge index eklendi.
- TF-IDF retrieval eklendi.
- Fuzzy retrieval eklendi.
- Hybrid retrieval eklendi.
- Memory cards eklendi.
- Decision journal eklendi.
- Analyst notes eklendi.
- Research query engine eklendi.
- Recent findings digest eklendi.
- Workspace summary eklendi.
- KB quality report eklendi.
- KnowledgeBasePipeline eklendi.
- DataLake knowledge base kayıt desteği aldı.
- Knowledge base scriptleri eklendi.
- Testler genişletildi.
"""
            phase_path.write_text(phase_content + "\n" + phase_addition)

if __name__ == "__main__":
    patch_docs()
