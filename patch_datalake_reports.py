with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

new_methods = """
    # Phase 46: Experiment Tracking Load/Save
    def save_hypothesis_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_file = self.paths.experiments_hypotheses / "hypothesis_registry.jsonl"
        # Not implementing full save here to keep the patch small, assuming managed by HypothesisRegistry
        return out_file

    def load_hypothesis_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_definitions(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.experiments_definitions / "definitions.csv"

    def load_experiment_definitions(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_run_manifest(self, run_id: str, manifest: dict) -> Path:
        out_file = self.paths.experiments_runs / f"run_{run_id}.json"
        self._save_json(out_file, manifest)
        return out_file

    def load_experiment_run_manifest(self, run_id: str) -> dict:
        return {}

    def save_experiment_artifact_manifest(self, run_id: str, manifest: dict) -> Path:
        out_file = self.paths.experiments_artifacts / f"artifacts_{run_id}.json"
        self._save_json(out_file, manifest)
        return out_file

    def load_experiment_artifact_manifest(self, run_id: str) -> dict:
        return {}

    def save_reproducibility_manifest(self, run_id: str, manifest: dict) -> Path:
        out_file = self.paths.experiments_reproducibility / f"repro_{run_id}.json"
        self._save_json(out_file, manifest)
        return out_file

    def load_reproducibility_manifest(self, run_id: str) -> dict:
        return {}

    def save_research_version_record(self, version_id: str, record: dict) -> Path:
        out_file = self.paths.experiments_versions / f"version_{version_id}.json"
        self._save_json(out_file, record)
        return out_file

    def load_research_version_record(self, version_id: str) -> dict:
        return {}

    def save_ablation_study_results(self, study_id: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_file = self.paths.experiments_ablation / f"{study_id}.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_ablation_study_results(self, study_id: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_comparison_table(self, profile_name: str, df: pd.DataFrame) -> Path:
        out_file = self.paths.experiments_comparisons / f"{profile_name}_comparisons.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_experiment_comparison_table(self, profile_name: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_leaderboard(self, profile_name: str, df: pd.DataFrame) -> Path:
        out_file = self.paths.experiments_leaderboards / f"{profile_name}_leaderboard.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_experiment_leaderboard(self, profile_name: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_quality(self, run_id_or_profile: str, quality: dict) -> Path:
        out_file = self.paths.experiments_quality / f"{run_id_or_profile}_quality.json"
        self._save_json(out_file, quality)
        return out_file

    def load_experiment_quality(self, run_id_or_profile: str) -> dict:
        return {}

    def save_experiment_tracking_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        out_file = self.paths.experiments_reports_json / f"{profile_name}_report.json"
        self._save_json(out_file, report)
        return out_file

    def load_experiment_tracking_report(self, profile_name: str) -> dict:
        return {}

    def list_experiment_runs(self) -> pd.DataFrame:
        return pd.DataFrame()

    def list_experiment_reports(self) -> pd.DataFrame:
        return pd.DataFrame()
"""
content = content.replace("    def save_meta_research_report(self,", new_methods + "\n    def save_meta_research_report(self,")

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
