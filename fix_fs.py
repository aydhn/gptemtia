with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

new_methods = """
    # --- Analyst UX Support ---
    def load_command_alias_registry(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_command_alias_registry'):
            return self.data_lake.load_command_alias_registry()
        return pd.DataFrame()

    def load_analyst_intents(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_analyst_intents'):
            return self.data_lake.load_analyst_intents()
        return pd.DataFrame()

    def load_safe_command_suggestions(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_safe_command_suggestions'):
            return self.data_lake.load_safe_command_suggestions()
        return pd.DataFrame()

    def load_prompt_pack_registry(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_prompt_pack_registry'):
            return self.data_lake.load_prompt_pack_registry()
        return pd.DataFrame()

    def load_prompt_pack_manifest(self) -> dict:
        if hasattr(self.data_lake, 'load_prompt_pack_manifest'):
            return self.data_lake.load_prompt_pack_manifest()
        return {}

    def load_workflow_shortcuts(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_workflow_shortcuts'):
            return self.data_lake.load_workflow_shortcuts()
        return pd.DataFrame()

    def load_query_mappings(self, report_name: str) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_query_mappings'):
            return self.data_lake.load_query_mappings(report_name)
        return pd.DataFrame()

    def load_analyst_task_board(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_analyst_task_board'):
            return self.data_lake.load_analyst_task_board()
        return pd.DataFrame()

    def load_productivity_checklist(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_productivity_checklist'):
            return self.data_lake.load_productivity_checklist()
        return pd.DataFrame()

    def load_ux_validation_report(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_ux_validation_report'):
            return self.data_lake.load_ux_validation_report()
        return pd.DataFrame()

    def load_ux_quality(self, profile_name: str | None = None) -> dict:
        if hasattr(self.data_lake, 'load_ux_quality'):
            return self.data_lake.load_ux_quality(profile_name or "balanced_analyst_productivity")
        return {}

    def load_ux_report(self, report_name: str) -> dict:
        if hasattr(self.data_lake, 'load_ux_report'):
            return self.data_lake.load_ux_report(report_name)
        return {}

    def list_available_ux_reports(self) -> dict:
        if hasattr(self.data_lake, 'list_ux_reports'):
            df = self.data_lake.list_ux_reports()
            return {"count": len(df), "files": df["file_name"].tolist() if not df.empty else []}
        return {}
"""

content = content.replace("    # --- Final Review ---", new_methods + "\n    # --- Final Review ---")

with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
    f.write(content)
