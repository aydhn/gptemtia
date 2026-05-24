import re
from pathlib import Path

# Update feature_store.py
feature_file = Path("ml/feature_store.py")
content = feature_file.read_text()

if "load_research_planning_signals" not in content:
    append_text = """

    # Phase 48: Research Planning
    def load_research_planning_signals(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_planning_signals(timeframe, profile_name or "balanced_research_planning")

    def load_research_task_registry(self, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_task_registry(profile_name or "balanced_research_planning")

    def load_research_backlog(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_backlog(timeframe, profile_name or "balanced_research_planning")

    def load_research_priority_scores(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_priority_scores(timeframe, profile_name or "balanced_research_planning")

    def load_next_best_experiments(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_next_best_experiments(timeframe, profile_name or "balanced_research_planning")

    def load_research_debt_report(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_debt_report(timeframe, profile_name or "balanced_research_planning")

    def load_research_opportunity_report(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_opportunity_report(timeframe, profile_name or "balanced_research_planning")

    def load_roadmap_health_snapshot(self, timeframe: str, profile_name: str | None = None) -> dict:
        return self.data_lake.load_roadmap_health_snapshot(timeframe, profile_name or "balanced_research_planning")

    def load_task_orchestration_plan(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_task_orchestration_plan(timeframe, profile_name or "balanced_research_planning")

    def load_research_planning_report(self, timeframe: str, profile_name: str | None = None) -> dict:
        return self.data_lake.load_research_planning_report(timeframe, profile_name or "balanced_research_planning")

    def list_available_research_planning_reports(self) -> dict:
        df = self.data_lake.list_research_planning_reports()
        if df.empty:
            return {"reports": []}
        return {"reports": df.to_dict("records")}
"""
    # Insert at the end of FeatureStore class
    match = re.search(r'(class FeatureStore:.*)(def get_feature_info.*?)$', content, re.DOTALL)
    if match:
        content = content[:match.start(2)] + append_text + "\n    " + match.group(2)
        feature_file.write_text(content)
        print("Updated feature_store.py")
    else:
        # Fallback, just append to end of file, assuming class ends at EOF
        content += append_text
        feature_file.write_text(content)
        print("Updated feature_store.py (fallback)")

# Update data_lake.py
lake_file = Path("data/storage/data_lake.py")
content = lake_file.read_text()

if "save_research_planning_signals" not in content:
    append_text = """

    # Phase 48: Research Planning
    def save_research_planning_signals(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_SIGNALS_DIR / f"signals_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_planning_signals(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_SIGNALS_DIR / f"signals_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_task_registry(self, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_TASKS_DIR / f"tasks_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_task_registry(self, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_TASKS_DIR / f"tasks_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_backlog(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_BACKLOG_DIR / f"backlog_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_backlog(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_BACKLOG_DIR / f"backlog_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_priority_scores(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_PRIORITIES_DIR / f"priorities_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_priority_scores(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_PRIORITIES_DIR / f"priorities_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_next_best_experiments(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_NEXT_BEST_DIR / f"next_best_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_next_best_experiments(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_NEXT_BEST_DIR / f"next_best_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_debt_report(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEBT_DIR / f"debt_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_debt_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEBT_DIR / f"debt_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_opportunity_report(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_OPPORTUNITIES_DIR / f"opportunities_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_opportunity_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_OPPORTUNITIES_DIR / f"opportunities_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_roadmap_health_snapshot(self, timeframe: str, profile_name: str, snapshot: dict) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ROADMAP_DIR / f"roadmap_{timeframe}_{profile_name}.json"
        self._save_json(snapshot, filepath)
        return filepath

    def load_roadmap_health_snapshot(self, timeframe: str, profile_name: str) -> dict:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ROADMAP_DIR / f"roadmap_{timeframe}_{profile_name}.json"
        return self._load_json(filepath)

    def save_task_dependency_table(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEPENDENCIES_DIR / f"dependencies_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_task_dependency_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEPENDENCIES_DIR / f"dependencies_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_milestone_tracking_table(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_MILESTONES_DIR / f"milestones_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_milestone_tracking_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_MILESTONES_DIR / f"milestones_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_task_orchestration_plan(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ORCHESTRATION_DIR / f"orchestration_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_task_orchestration_plan(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ORCHESTRATION_DIR / f"orchestration_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_planning_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        self._save_json(quality, filepath)
        return filepath

    def load_research_planning_quality(self, timeframe: str, profile_name: str) -> dict:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        return self._load_json(filepath)

    def save_research_planning_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        filepath = self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR / f"report_{timeframe}_{profile_name}.json"
        self._save_json(report, filepath)
        if markdown:
            md_path = self.paths.REPORTS_RESEARCH_PLANNING_MARKDOWN_DIR / f"report_{timeframe}_{profile_name}.md"
            self._save_text(markdown, md_path)
        return filepath

    def load_research_planning_report(self, timeframe: str, profile_name: str) -> dict:
        filepath = self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR / f"report_{timeframe}_{profile_name}.json"
        return self._load_json(filepath)

    def list_research_planning_reports(self) -> pd.DataFrame:
        files = list(self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR.glob("*.json"))
        data = []
        for f in files:
            parts = f.stem.split("_")
            if len(parts) >= 3:
                data.append({"timeframe": parts[1], "profile": "_".join(parts[2:]), "file": f.name})
        return pd.DataFrame(data)
"""
    # Append to end of class
    content += append_text
    lake_file.write_text(content)
    print("Updated data_lake.py")
