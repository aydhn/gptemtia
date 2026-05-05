import re

with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

insert_str = """
    def load_decision_candidates(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "decision_candidates"):
            return self.data_lake.load_features(spec, timeframe, "decision_candidates")
        return pd.DataFrame()

    def load_decision_pool(
        self, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        prof = profile_name or "balanced_directional_decision"
        if self.data_lake.has_decision_pool(timeframe, prof):
            return self.data_lake.load_decision_pool(timeframe, prof)
        return pd.DataFrame()

    def list_available_decision_candidates(self, spec: SymbolSpec) -> dict:
        return {
            "decision_candidates": self.data_lake.list_feature_timeframes(
                spec, "decision_candidates"
            )
        }

    def list_available_decision_pools(self) -> dict:
        return {"decision_pool": ["1d"]}
"""

content = content + insert_str

with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
    f.write(content)
