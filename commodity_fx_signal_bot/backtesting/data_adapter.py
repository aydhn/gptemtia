import pandas as pd
from typing import Tuple, Dict
import logging
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

logger = logging.getLogger(__name__)


class BacktestDataAdapter:
    def __init__(self, data_lake: DataLake):
        self.lake = data_lake

    def load_price_frame(
        self, spec: SymbolSpec, timeframe: str
    ) -> tuple[pd.DataFrame, dict]:
        try:
            df = self.lake.load_processed_ohlcv(spec.symbol, timeframe)
            if df.empty:
                return pd.DataFrame(), {"error": "Price dataframe is empty."}
            if not isinstance(df.index, pd.DatetimeIndex):
                return pd.DataFrame(), {
                    "error": "Price dataframe index must be DatetimeIndex."
                }
            required_cols = ["open", "high", "low", "close"]
            for c in required_cols:
                if c not in df.columns:
                    return pd.DataFrame(), {"error": f"Missing required column: {c}"}
            return df, {"status": "success", "rows": len(df)}
        except Exception as e:
            return pd.DataFrame(), {"error": str(e)}

    def load_level_candidates(
        self, spec: SymbolSpec, timeframe: str
    ) -> tuple[pd.DataFrame, dict]:
        try:
            # First try loading sizing candidates as they are the ultimate source
            df = self.lake.load_sizing_candidates(spec.symbol, timeframe)
            if df.empty:
                df = self.lake.load_level_candidates(spec.symbol, timeframe)
            if df.empty:
                return pd.DataFrame(), {"error": "Level candidates dataframe is empty."}
            if not isinstance(df.index, pd.DatetimeIndex):
                try:
                    df.index = pd.to_datetime(df.index)
                except Exception:
                    return pd.DataFrame(), {
                        "error": "Level candidates dataframe index must be DatetimeIndex."
                    }
            return df, {"status": "success", "rows": len(df)}
        except Exception as e:
            return pd.DataFrame(), {"error": str(e)}

    def load_backtest_context_frames(
        self, spec: SymbolSpec, timeframe: str
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        context = {}
        status = {}
        try:
            context["regime"] = self.lake.load_regime_features(spec.symbol, timeframe)
        except:
            context["regime"] = pd.DataFrame()
        return context, status

    def build_backtest_frame(
        self,
        price_df: pd.DataFrame,
        level_df: pd.DataFrame,
    ) -> tuple[pd.DataFrame, dict]:

        if price_df.empty:
            return pd.DataFrame(), {"error": "Empty price_df"}
        if level_df.empty:
            return pd.DataFrame(), {
                "warning": "Empty level_df, backtest will run with no candidates."
            }

        # We don't join them to avoid memory explosion, but we ensure indices are aligned
        # In this implementation we just return price_df, level_df is handled separately
        return price_df, {"status": "success"}
