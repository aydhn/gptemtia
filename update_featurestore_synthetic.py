with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

new_methods = """
    # Phase 43: Synthetic Indices Data Loading
    def load_synthetic_index_definitions(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_synthetic_index_definitions(timeframe, profile_name)

    def load_synthetic_index_levels(self, index_id: str, timeframe: str) -> pd.DataFrame:
        return self.data_lake.load_synthetic_index_levels(index_id, timeframe)

    def load_relative_strength_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_relative_strength_table(timeframe, profile_name)

    def load_relative_momentum_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_relative_momentum_table(timeframe, profile_name)

    def load_universe_rotation_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_universe_rotation_table(timeframe, profile_name)

    def load_leadership_laggard_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_leadership_laggard_table(timeframe, profile_name)

    def load_synthetic_benchmark_comparison(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_synthetic_benchmark_comparison(timeframe, profile_name)

    def load_synthetic_index_performance(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_synthetic_index_performance(timeframe, profile_name)

    def load_synthetic_index_report(self, timeframe: str, profile_name: str | None = None) -> dict:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_synthetic_index_report(timeframe, profile_name)

    def list_available_synthetic_index_reports(self) -> dict:
        df = self.data_lake.list_synthetic_index_reports()
        if df.empty:
             return {}
        return df.to_dict(orient="records")
"""

lines = content.split('\n')
insert_idx = len(lines) - 1
for i in range(len(lines)-1, -1, -1):
    if lines[i].strip() != "":
         # Find last non-empty line inside class FeatureStore
         if lines[i].startswith("    "):
              insert_idx = i + 1
              break

lines.insert(insert_idx, new_methods)
content = "\n".join(lines)

with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
    f.write(content)
