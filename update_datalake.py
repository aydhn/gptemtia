import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

portfolio_regime_methods = """

    # Phase 42: Portfolio Regime Research
    def save_portfolio_regimes(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_regimes / f"regimes_{timeframe}_{profile_name}.parquet")

    def load_portfolio_regimes(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_regimes / f"regimes_{timeframe}_{profile_name}.parquet")

    def save_regime_conditioned_returns(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_conditioned_returns / f"conditioned_returns_{timeframe}_{profile_name}.parquet")

    def load_regime_conditioned_returns(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_conditioned_returns / f"conditioned_returns_{timeframe}_{profile_name}.parquet")

    def save_regime_correlation_summary(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_correlation / f"correlation_{timeframe}_{profile_name}.parquet")

    def load_regime_correlation_summary(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_correlation / f"correlation_{timeframe}_{profile_name}.parquet")

    def save_macro_scenario_sensitivity(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_scenarios / f"scenario_sensitivity_{timeframe}_{profile_name}.parquet")

    def load_macro_scenario_sensitivity(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_scenarios / f"scenario_sensitivity_{timeframe}_{profile_name}.parquet")

    def save_basket_stress_test_results(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_stress_tests / f"stress_test_{timeframe}_{profile_name}.parquet")

    def load_basket_stress_test_results(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_stress_tests / f"stress_test_{timeframe}_{profile_name}.parquet")

    def save_drawdown_clusters(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_drawdowns / f"drawdown_clusters_{timeframe}_{profile_name}.parquet")

    def load_drawdown_clusters(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_drawdowns / f"drawdown_clusters_{timeframe}_{profile_name}.parquet")

    def save_recovery_analysis(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_recovery / f"recovery_analysis_{timeframe}_{profile_name}.parquet")

    def load_recovery_analysis(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_recovery / f"recovery_analysis_{timeframe}_{profile_name}.parquet")

    def save_tail_risk_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_tail_risk / f"tail_risk_{timeframe}_{profile_name}.parquet")

    def load_tail_risk_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_tail_risk / f"tail_risk_{timeframe}_{profile_name}.parquet")

    def save_risk_regime_exposure(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        return self._save_df(df, self.paths.portfolio_regime_exposure / f"exposure_{timeframe}_{profile_name}.parquet")

    def load_risk_regime_exposure(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_exposure / f"exposure_{timeframe}_{profile_name}.parquet")

    def save_portfolio_regime_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        if markdown:
            md_path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)
        return path

    def load_portfolio_regime_report(self, timeframe: str, profile_name: str) -> dict:
        import json
        path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_portfolio_regime_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path:
        import json
        path = self.paths.portfolio_regime_quality / f"quality_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_portfolio_regime_quality(self, timeframe: str, profile_name: str) -> dict:
        import json
        path = self.paths.portfolio_regime_quality / f"quality_{timeframe}_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_portfolio_regime_reports(self) -> pd.DataFrame:
        return pd.DataFrame()
"""

# Append just before the end of the class, or just append to end of file and trust indentation
with open("commodity_fx_signal_bot/data/storage/data_lake.py", "a") as f:
    f.write(portfolio_regime_methods)
