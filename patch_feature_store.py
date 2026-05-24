with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

new_methods = """
    # Phase 46: Experiment Tracking Loaders
    def load_hypothesis_registry(self) -> pd.DataFrame:
        return self.data_lake.load_hypothesis_registry()

    def load_experiment_definitions(self) -> pd.DataFrame:
        return self.data_lake.load_experiment_definitions()

    def load_experiment_run_manifest(self, run_id: str) -> dict:
        return self.data_lake.load_experiment_run_manifest(run_id)

    def load_experiment_artifact_manifest(self, run_id: str) -> dict:
        return self.data_lake.load_experiment_artifact_manifest(run_id)

    def load_reproducibility_manifest(self, run_id: str) -> dict:
        return self.data_lake.load_reproducibility_manifest(run_id)

    def load_experiment_comparison_table(self, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_experiment_comparison_table(profile_name or "default")

    def load_experiment_leaderboard(self, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_experiment_leaderboard(profile_name or "default")

    def load_experiment_quality(self, run_id_or_profile: str) -> dict:
        return self.data_lake.load_experiment_quality(run_id_or_profile)

    def list_available_experiment_reports(self) -> dict:
        return {"reports": self.data_lake.list_experiment_reports().to_dict('records') if hasattr(self.data_lake, 'list_experiment_reports') else []}

"""

content = content.replace("    def save_portfolio_regime_stress_tests(self,", new_methods + "    def save_portfolio_regime_stress_tests(self,")

with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
    f.write(content)
