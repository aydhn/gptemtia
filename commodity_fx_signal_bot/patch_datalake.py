import re
from pathlib import Path

def patch_datalake():
    path = Path("data/storage/data_lake.py")
    content = path.read_text()

    if "save_knowledge_documents" in content:
        print("Data Lake already patched.")
        return

    addition = """
    # Phase 49 Knowledge Base Methods
    def save_knowledge_documents(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "documents.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.project_paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_knowledge_documents(self) -> pd.DataFrame:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "documents.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_knowledge_chunks(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "chunks.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.project_paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_knowledge_chunks(self) -> pd.DataFrame:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "chunks.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_knowledge_index_summary(self, summary: dict) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_INDEXES_DIR / "index_summary.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        return p

    def load_knowledge_index_summary(self) -> dict:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_INDEXES_DIR / "index_summary.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_retrieval_results(self, query_id: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"results_{query_id}.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.project_paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"summary_{query_id}.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_retrieval_results(self, query_id: str) -> pd.DataFrame:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"results_{query_id}.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_memory_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "memory_cards.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.project_paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_memory_cards(self) -> pd.DataFrame:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "memory_cards.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_symbol_memory_card(self, symbol: str, card: dict) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / f"card_{symbol}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(card, f, indent=2)
        return p

    def load_symbol_memory_card(self, symbol: str) -> dict:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / f"card_{symbol}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_decision_journal(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "decision_journal.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.project_paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_decision_journal(self) -> pd.DataFrame:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "decision_journal.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_analyst_notes(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "analyst_notes.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.project_paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_analyst_notes(self) -> pd.DataFrame:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "analyst_notes.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_recent_findings_digest(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "recent_findings.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.project_paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_recent_findings_digest(self) -> pd.DataFrame:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "recent_findings.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_workspace_summary(self, summary: dict) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_WORKSPACE_DIR / "workspace_summary.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        return p

    def load_workspace_summary(self) -> dict:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_WORKSPACE_DIR / "workspace_summary.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_kb_quality(self, profile_name: str, quality: dict) -> Path:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_QUALITY_DIR / f"quality_{profile_name}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(quality, f, indent=2)
        return p

    def load_kb_quality(self, profile_name: str) -> dict:
        p = self.project_paths.LAKE_KNOWLEDGE_BASE_QUALITY_DIR / f"quality_{profile_name}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_knowledge_base_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        p = self.project_paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR / f"report_{profile_name}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_p = self.project_paths.REPORTS_KNOWLEDGE_BASE_MARKDOWN_DIR / f"report_{profile_name}.md"
            with open(md_p, 'w', encoding='utf-8') as f:
                f.write(markdown)

            txt_p = self.project_paths.REPORTS_KNOWLEDGE_BASE_TXT_DIR / f"report_{profile_name}.txt"
            with open(txt_p, 'w', encoding='utf-8') as f:
                f.write(markdown) # Use markdown as text for now

        return p

    def load_knowledge_base_report(self, profile_name: str) -> dict:
        p = self.project_paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR / f"report_{profile_name}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def list_knowledge_base_reports(self) -> pd.DataFrame:
        d = self.project_paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR
        reports = []
        if d.exists():
            for p in d.glob("report_*.json"):
                profile_name = p.stem.replace("report_", "")
                with open(p, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        reports.append({
                            "profile_name": profile_name,
                            "file": p.name
                        })
                    except Exception:
                        pass
        return pd.DataFrame(reports)

"""

    # Let's insert at the end of the class.
    # We find the last method and insert before the end of the file.

    # Or simple string replace if we know a good anchor. Let's just append if it's the class.
    # Since it's a python file, we can just append, but it needs to be indented properly.

    # Let's read lines and insert before the first class definition end.

    # Easier way: Just append to the file since DataLake is the only class.
    path.write_text(content + "\n" + addition)
    print("Data Lake patched successfully.")

if __name__ == "__main__":
    patch_datalake()
