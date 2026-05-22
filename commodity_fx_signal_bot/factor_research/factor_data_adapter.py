import pandas as pd
import numpy as np
from data.storage.data_lake import DataLake
from config.symbols import SymbolSpec
import logging

logger = logging.getLogger(__name__)

class FactorDataAdapter:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_close_prices(self, specs: list[SymbolSpec], timeframe: str) -> tuple[pd.DataFrame, dict]:
        summary = {"loaded_symbols": 0, "missing_symbols": [], "warnings": []}
        close_series = {}
        for spec in specs:
            df = self.data_lake.load_ohlcv(spec.symbol, timeframe)
            if not df.empty and "close" in df.columns:
                close_series[spec.symbol] = df["close"]
                summary["loaded_symbols"] += 1
            else:
                summary["missing_symbols"].append(spec.symbol)

        if not close_series:
            summary["warnings"].append("No close prices loaded.")
            return pd.DataFrame(), summary

        close_df = pd.DataFrame(close_series)
        close_df.index = pd.to_datetime(close_df.index)
        return close_df.sort_index(), summary

    def build_returns_matrix(self, close_df: pd.DataFrame, method: str = "log") -> tuple[pd.DataFrame, dict]:
        summary = {"method": method, "warnings": []}
        if close_df.empty:
             summary["warnings"].append("Empty close_df provided.")
             return pd.DataFrame(), summary

        if method == "log":
            returns_df = np.log(close_df / close_df.shift(1))
        else:
            returns_df = close_df.pct_change()

        returns_df = returns_df.dropna(how="all")
        return returns_df, summary

    def load_research_ranking(self, timeframe: str, profile_name: str | None = None) -> tuple[pd.DataFrame, dict]:
        # Phase 39 integration
        try:
             df = self.data_lake.load_research_ranking_table(timeframe, profile_name)
             return df, {"status": "loaded"}
        except AttributeError:
             return pd.DataFrame(), {"warnings": ["Method load_research_ranking_table not found in DataLake."]}

    def load_synthetic_indices(self, timeframe: str, profile_name: str | None = None) -> tuple[dict[str, pd.DataFrame], dict]:
         # Phase 43 integration
         try:
              if profile_name is None:
                  from config.settings import settings
                  profile_name = settings.default_synthetic_index_profile
              df = self.data_lake.load_synthetic_index_levels_all(timeframe, profile_name) if hasattr(self.data_lake, 'load_synthetic_index_levels_all') else pd.DataFrame()
              if df.empty:
                   return {}, {"warnings": ["No synthetic indices found."]}

              indices = {}
              for col in df.columns:
                  indices[col] = df[[col]]
              return indices, {"status": "loaded"}
         except Exception as e:
              return {}, {"warnings": [f"Error loading synthetic indices: {str(e)}"]}

    def load_portfolio_regime_context(self, timeframe: str, profile_name: str | None = None) -> tuple[dict[str, pd.DataFrame], dict]:
        # Phase 42 integration
         try:
              if profile_name is None:
                  from config.settings import settings
                  profile_name = settings.default_portfolio_regime_profile
              df = self.data_lake.load_portfolio_regime_history(timeframe, profile_name) if hasattr(self.data_lake, 'load_portfolio_regime_history') else pd.DataFrame()
              if df.empty:
                   return {}, {"warnings": ["No portfolio regime history found."]}

              return {"regimes": df}, {"status": "loaded"}
         except Exception as e:
              return {}, {"warnings": [f"Error loading portfolio regime context: {str(e)}"]}

    def load_macro_proxy_context(self, timeframe: str) -> tuple[dict[str, pd.DataFrame], dict]:
         summary = {"warnings": []}
         proxies = {}

         # Attempt to load known macro proxies
         for symbol, key in [("USDTRY=X", "usdtry"), ("GC=F", "gold"), ("CL=F", "oil")]:
             df = self.data_lake.load_ohlcv(symbol, timeframe)
             if not df.empty and "close" in df.columns:
                  proxies[key] = df[["close"]]
             else:
                  summary["warnings"].append(f"Missing macro proxy data for {symbol}.")

         return proxies, summary
