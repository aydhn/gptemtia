from pathlib import Path

def patch_featurestore():
    path = Path("ml/feature_store.py")
    content = path.read_text()

    if "load_knowledge_documents" in content:
        print("Feature Store already patched.")
        return

    addition = """
    # Phase 49 Knowledge Base Methods
    def load_knowledge_documents(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_knowledge_documents'):
            return self.data_lake.load_knowledge_documents()
        return pd.DataFrame()

    def load_knowledge_chunks(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_knowledge_chunks'):
            return self.data_lake.load_knowledge_chunks()
        return pd.DataFrame()

    def load_knowledge_index_summary(self) -> dict:
        if hasattr(self.data_lake, 'load_knowledge_index_summary'):
            return self.data_lake.load_knowledge_index_summary()
        return {}

    def load_retrieval_results(self, query_id: str) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_retrieval_results'):
            return self.data_lake.load_retrieval_results(query_id)
        return pd.DataFrame()

    def load_memory_cards(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_memory_cards'):
            return self.data_lake.load_memory_cards()
        return pd.DataFrame()

    def load_symbol_memory_card(self, symbol: str) -> dict:
        if hasattr(self.data_lake, 'load_symbol_memory_card'):
            return self.data_lake.load_symbol_memory_card(symbol)
        return {}

    def load_decision_journal(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_decision_journal'):
            return self.data_lake.load_decision_journal()
        return pd.DataFrame()

    def load_analyst_notes(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_analyst_notes'):
            return self.data_lake.load_analyst_notes()
        return pd.DataFrame()

    def load_recent_findings_digest(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_recent_findings_digest'):
            return self.data_lake.load_recent_findings_digest()
        return pd.DataFrame()

    def load_workspace_summary(self) -> dict:
        if hasattr(self.data_lake, 'load_workspace_summary'):
            return self.data_lake.load_workspace_summary()
        return {}

    def load_kb_quality(self, profile_name: str | None = None) -> dict:
        if hasattr(self.data_lake, 'load_kb_quality'):
            return self.data_lake.load_kb_quality(profile_name or "balanced_local_knowledge_base")
        return {}

    def load_knowledge_base_report(self, profile_name: str | None = None) -> dict:
        if hasattr(self.data_lake, 'load_knowledge_base_report'):
            return self.data_lake.load_knowledge_base_report(profile_name or "knowledge_index_report")
        return {}

    def list_available_knowledge_base_reports(self) -> dict:
        if hasattr(self.data_lake, 'list_knowledge_base_reports'):
            df = self.data_lake.list_knowledge_base_reports()
            if not df.empty:
                return df.to_dict(orient='records')
        return {}
"""

    path.write_text(content + "\n" + addition)
    print("Feature Store patched successfully.")

if __name__ == "__main__":
    patch_featurestore()
