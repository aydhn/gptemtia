import pandas as pd
from typing import Tuple, Dict, Optional
from pathlib import Path

from config.settings import Settings
from data.storage.data_lake import DataLake
from knowledge_base.kb_config import KnowledgeBaseProfile, get_default_knowledge_base_profile
from knowledge_base.document_discovery import KnowledgeDocumentDiscovery
from knowledge_base.chunking import build_chunks_for_document, chunks_to_dataframe
from knowledge_base.indexing import build_knowledge_index, save_knowledge_index
from knowledge_base.query_engine import ResearchQueryEngine
from knowledge_base.memory_cards import build_symbol_memory_card, memory_cards_to_dataframe, summarize_memory_cards
from knowledge_base.decision_journal import build_default_decision_journal_entries, decision_entries_to_dataframe
from knowledge_base.analyst_notes import build_default_analyst_notes, analyst_note_to_dict
from knowledge_base.findings_digest import extract_recent_findings, build_recent_findings_digest, summarize_findings_digest
from knowledge_base.workspace_summary import build_workspace_status_table, summarize_workspace_health, build_workspace_summary
from knowledge_base.kb_quality import build_kb_quality_report
from core.logger import get_logger

logger = get_logger(__name__)

class KnowledgeBasePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[KnowledgeBaseProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_knowledge_base_profile()
        self.discovery = KnowledgeDocumentDiscovery(project_root)

    def _build_core_dataframes(self) -> Tuple[pd.DataFrame, pd.DataFrame, Dict]:
        # 1. Discover
        docs_df, disc_summary = self.discovery.discover_documents(self.profile)

        if docs_df.empty:
            return pd.DataFrame(), pd.DataFrame(), {"discovery": disc_summary}

        # 2. Text Extraction & 3. Chunking (combining these here for simplicity as we iterate)
        from knowledge_base.kb_models import KnowledgeDocument
        from knowledge_base.text_extraction import extract_text_from_document

        all_chunks = []
        for idx, row in docs_df.iterrows():
            doc = KnowledgeDocument(**row)
            path = Path(doc.path)

            if not path.exists():
                continue

            text, meta = extract_text_from_document(path)

            # Update hash and metadata
            import hashlib
            doc.text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
            doc.metadata.update(meta)

            chunks = build_chunks_for_document(doc, text, self.profile)
            all_chunks.extend(chunks)

            # Update DataFrame row if we want to keep hash in docs_df
            docs_df.at[idx, 'text_hash'] = doc.text_hash

        chunks_df = chunks_to_dataframe(all_chunks)
        return docs_df, chunks_df, {"discovery": disc_summary, "chunks_generated": len(chunks_df)}

    def build_knowledge_index_report(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        docs_df, chunks_df, run_summary = self._build_core_dataframes()

        # 4. Knowledge Index
        index = build_knowledge_index([], []) # Not used directly here since we have DFs
        index.documents_df = docs_df
        index.chunks_df = chunks_df
        index_summary = index.summarize()
        run_summary["index"] = index_summary

        # 11. KB Quality
        quality_report = build_kb_quality_report(index_summary, docs_df, chunks_df)
        run_summary["quality"] = quality_report

        if save:
            if hasattr(self.data_lake, 'save_knowledge_documents'):
                self.data_lake.save_knowledge_documents(docs_df, run_summary)
                self.data_lake.save_knowledge_chunks(chunks_df, run_summary)
                self.data_lake.save_knowledge_index_summary(index_summary)
                self.data_lake.save_kb_quality(self.profile.name, quality_report)

            from knowledge_base.kb_report_builder import build_knowledge_index_markdown_report
            md = build_knowledge_index_markdown_report(index_summary, docs_df, chunks_df)
            if hasattr(self.data_lake, 'save_knowledge_base_report'):
                self.data_lake.save_knowledge_base_report("knowledge_index_report", index_summary, md)

        return {"documents": docs_df, "chunks": chunks_df}, run_summary

    def run_research_query(
        self,
        query_text: str,
        symbol: Optional[str] = None,
        module_name: Optional[str] = None,
        document_type: Optional[str] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:

        # In a real scenario, we'd load these from DataLake
        # For pipeline simplicity, we build on the fly if not loaded
        docs_df, chunks_df, _ = self._build_core_dataframes()

        engine = ResearchQueryEngine(docs_df, chunks_df, self.profile)
        results_df, summary = engine.query(query_text, top_k=None, symbol=symbol, module_name=module_name, document_type=document_type)

        if save and hasattr(self.data_lake, 'save_retrieval_results'):
            import hashlib
            q_id = hashlib.md5(query_text.encode('utf-8')).hexdigest()[:8]
            self.data_lake.save_retrieval_results(q_id, results_df, summary)

            from knowledge_base.kb_report_builder import build_research_query_markdown_report
            md = build_research_query_markdown_report(query_text, summary, results_df)
            self.data_lake.save_knowledge_base_report(f"research_query_{q_id}", summary, md)

        return results_df, summary

    def build_symbol_memory_report(self, symbol: str, save: bool = True) -> Tuple[dict, Dict]:
        docs_df, chunks_df, _ = self._build_core_dataframes()
        card = build_symbol_memory_card(symbol, docs_df, chunks_df)

        summary = {"symbol": symbol, "card_id": card.card_id}

        if save and hasattr(self.data_lake, 'save_symbol_memory_card'):
            from knowledge_base.kb_models import research_memory_card_to_dict
            self.data_lake.save_symbol_memory_card(symbol, research_memory_card_to_dict(card))

            from knowledge_base.kb_report_builder import build_symbol_memory_markdown_report
            md = build_symbol_memory_markdown_report(symbol, summary, card)
            self.data_lake.save_knowledge_base_report(f"symbol_memory_{symbol}", summary, md)

        return vars(card), summary

    def build_decision_journal_report(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        entries = build_default_decision_journal_entries()
        df = decision_entries_to_dataframe(entries)

        summary = {"total_entries": len(df)}

        if save and hasattr(self.data_lake, 'save_decision_journal'):
            self.data_lake.save_decision_journal(df, summary)

            from knowledge_base.kb_report_builder import build_decision_journal_markdown_report
            md = build_decision_journal_markdown_report(summary, df)
            self.data_lake.save_knowledge_base_report("decision_journal_report", summary, md)

        return df, summary

    def build_recent_findings_digest(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        docs_df, chunks_df, _ = self._build_core_dataframes()

        findings_df = extract_recent_findings(docs_df, chunks_df)
        summary = summarize_findings_digest(findings_df)

        if save and hasattr(self.data_lake, 'save_recent_findings_digest'):
            self.data_lake.save_recent_findings_digest(findings_df, summary)

            from knowledge_base.kb_report_builder import build_recent_findings_markdown_report
            md = build_recent_findings_markdown_report(summary, findings_df)
            self.data_lake.save_knowledge_base_report("recent_findings_digest", summary, md)

        return findings_df, summary

    def build_analyst_workspace_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        docs_df, chunks_df, _ = self._build_core_dataframes()

        summary = build_workspace_summary(docs_df, chunks_df)
        health = summarize_workspace_health(summary)
        summary.update(health)

        status_df = build_workspace_status_table(docs_df, chunks_df)

        if save and hasattr(self.data_lake, 'save_workspace_summary'):
            self.data_lake.save_workspace_summary(summary)

            from knowledge_base.kb_report_builder import build_analyst_workspace_status_markdown_report
            md = build_analyst_workspace_status_markdown_report(summary, status_df)
            self.data_lake.save_knowledge_base_report("analyst_workspace_status", summary, md)

        return status_df, summary
