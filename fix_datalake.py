with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

new_methods = """
    # --- Analyst UX ---
    def save_command_alias_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_aliases_dir / "command_alias_registry.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_command_alias_registry(self) -> pd.DataFrame:
        p = self.paths.analyst_ux_aliases_dir / "command_alias_registry.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_analyst_intents(self, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_intents_dir / "analyst_intents.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_analyst_intents(self) -> pd.DataFrame:
        p = self.paths.analyst_ux_intents_dir / "analyst_intents.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_safe_command_suggestions(self, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_suggestions_dir / "safe_command_suggestions.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_safe_command_suggestions(self) -> pd.DataFrame:
        p = self.paths.analyst_ux_suggestions_dir / "safe_command_suggestions.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_prompt_pack_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_prompt_packs_dir / "prompt_pack_registry.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_prompt_pack_registry(self) -> pd.DataFrame:
        p = self.paths.analyst_ux_prompt_packs_dir / "prompt_pack_registry.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_prompt_pack_manifest(self, manifest: dict) -> Path:
        import json
        p = self.paths.analyst_ux_prompt_packs_dir / "prompt_pack_manifest.json"
        with open(p, "w") as f:
            json.dump(manifest, f, indent=4)
        return p

    def load_prompt_pack_manifest(self) -> dict:
        import json
        p = self.paths.analyst_ux_prompt_packs_dir / "prompt_pack_manifest.json"
        if p.exists():
            with open(p, "r") as f:
                return json.load(f)
        return {}

    def save_workflow_shortcuts(self, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_workflow_shortcuts_dir / "workflow_shortcuts.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_workflow_shortcuts(self) -> pd.DataFrame:
        p = self.paths.analyst_ux_workflow_shortcuts_dir / "workflow_shortcuts.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_query_mappings(self, report_name: str, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_query_mappings_dir / f"{report_name}.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_query_mappings(self, report_name: str) -> pd.DataFrame:
        p = self.paths.analyst_ux_query_mappings_dir / f"{report_name}.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_analyst_task_board(self, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_task_board_dir / "analyst_task_board.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_analyst_task_board(self) -> pd.DataFrame:
        p = self.paths.analyst_ux_task_board_dir / "analyst_task_board.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_productivity_checklist(self, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_checklists_dir / "productivity_checklist.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_productivity_checklist(self) -> pd.DataFrame:
        p = self.paths.analyst_ux_checklists_dir / "productivity_checklist.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_ux_validation_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        p = self.paths.analyst_ux_validation_dir / "ux_validation_report.parquet"
        if not df.empty:
            df.to_parquet(p, index=False)
        return p

    def load_ux_validation_report(self) -> pd.DataFrame:
        p = self.paths.analyst_ux_validation_dir / "ux_validation_report.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_ux_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        p = self.paths.analyst_ux_quality_dir / f"ux_quality_{profile_name}.json"
        with open(p, "w") as f:
            json.dump(quality, f, indent=4)
        return p

    def load_ux_quality(self, profile_name: str) -> dict:
        import json
        p = self.paths.analyst_ux_quality_dir / f"ux_quality_{profile_name}.json"
        if p.exists():
            with open(p, "r") as f:
                return json.load(f)
        return {}

    def save_ux_report(self, report_name: str, summary: dict, markdown: str = None) -> Path:
        import json

        md_path = self.paths.reports_analyst_ux_markdown_dir / f"{report_name}.md"
        if markdown:
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)

        json_path = self.paths.reports_analyst_ux_json_dir / f"{report_name}_summary.json"
        with open(json_path, "w") as f:
            json.dump(summary, f, indent=4)

        # also save to txt
        txt_path = self.paths.reports_analyst_ux_txt_dir / f"{report_name}.txt"
        if markdown:
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(markdown)

        return md_path

    def load_ux_report(self, report_name: str) -> dict:
        import json
        p = self.paths.reports_analyst_ux_json_dir / f"{report_name}_summary.json"
        if p.exists():
            with open(p, "r") as f:
                return json.load(f)
        return {}

    def list_ux_reports(self) -> pd.DataFrame:
        import os
        files = []
        if self.paths.reports_analyst_ux_markdown_dir.exists():
            for f in os.listdir(self.paths.reports_analyst_ux_markdown_dir):
                if f.endswith(".md"):
                    files.append({"file_name": f, "report_type": "markdown"})
        return pd.DataFrame(files)
"""

content = content.replace("    # --- Final Review ---", new_methods + "\n    # --- Final Review ---")

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
