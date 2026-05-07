with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

new_methods = """
    # --- Risk Candidates (Phase 23 fix if missing) ---
    def load_risk_candidates(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if not self.data_lake.has_features(spec, timeframe, "risk_candidates"):
            return pd.DataFrame()
        return self.data_lake.load_features(spec, timeframe, "risk_candidates")

    def load_risk_pool(
        self, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        p_name = profile_name or self.settings.default_risk_profile
        try:
            # Assuming data_lake has load_risk_pool, fallback if not
            if hasattr(self.data_lake, "load_risk_pool"):
                return self.data_lake.load_risk_pool(timeframe, p_name)
            return pd.DataFrame()
        except FileNotFoundError:
            return pd.DataFrame()

    # --- Sizing Candidates (Phase 24) ---
    def load_sizing_candidates(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if not self.data_lake.has_features(spec, timeframe, "sizing_candidates"):
            return pd.DataFrame()
        return self.data_lake.load_features(spec, timeframe, "sizing_candidates")

    def load_sizing_pool(
        self, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        p_name = profile_name or self.settings.default_sizing_profile
        try:
            return self.data_lake.load_sizing_pool(timeframe, p_name)
        except FileNotFoundError:
            return pd.DataFrame()

    def list_available_sizing_candidates(self, spec: SymbolSpec) -> list[str]:
        return self.data_lake.list_feature_timeframes(spec, "sizing_candidates")

    def list_available_sizing_pools(self) -> dict:
        # Simplistic implementation matching others if exists
        return {}
"""

with open("commodity_fx_signal_bot/ml/feature_store.py", "a") as f:
    f.write("\n" + new_methods)
