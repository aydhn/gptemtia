import re

file_path = "commodity_fx_signal_bot/ml/feature_store.py"
with open(file_path, "r") as f:
    content = f.read()

new_methods = """
    def load_regime_features(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "regime"):
            return self.data_lake.load_features(spec, timeframe, "regime")
        return pd.DataFrame()

    def load_regime_events(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "regime_events"):
            return self.data_lake.load_features(spec, timeframe, "regime_events")
        return pd.DataFrame()

    def list_available_regime_features(self, spec: SymbolSpec) -> dict:
        return {
            "regime": self.data_lake.list_feature_timeframes(spec, "regime"),
            "regime_events": self.data_lake.list_feature_timeframes(spec, "regime_events"),
        }
"""

if "load_regime_features" not in content:
    content += new_methods

with open(file_path, "w") as f:
    f.write(content)
