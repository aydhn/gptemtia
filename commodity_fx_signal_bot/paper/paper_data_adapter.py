import pandas as pd
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

class PaperDataAdapter:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_price_frame(self, spec: SymbolSpec, timeframe: str) -> tuple[pd.DataFrame, dict]:
        try:
            df = self.data_lake.load_processed_ohlcv(spec.symbol, timeframe)
            if df.empty:
                return pd.DataFrame(), {"error": "Price frame empty."}
            return df, {}
        except Exception as e:
            return pd.DataFrame(), {"error": str(e)}

    def load_level_candidates(self, spec: SymbolSpec, timeframe: str) -> tuple[pd.DataFrame, dict]:
        try:
            df = self.data_lake.load_level_candidates(spec.symbol, timeframe)
            if df.empty:
                return pd.DataFrame(), {"warning": "Level candidates empty."}
            return df, {}
        except Exception as e:
            return pd.DataFrame(), {"warning": str(e)}

    def load_sizing_candidates(self, spec: SymbolSpec, timeframe: str) -> tuple[pd.DataFrame, dict]:
        try:
            df = self.data_lake.load_sizing_candidates(spec.symbol, timeframe)
            if df.empty:
                return pd.DataFrame(), {"warning": "Sizing candidates empty."}
            return df, {}
        except Exception as e:
            return pd.DataFrame(), {"warning": str(e)}

    def load_risk_candidates(self, spec: SymbolSpec, timeframe: str) -> tuple[pd.DataFrame, dict]:
        try:
            df = self.data_lake.load_risk_candidates(spec.symbol, timeframe)
            if df.empty:
                return pd.DataFrame(), {"warning": "Risk candidates empty."}
            return df, {}
        except Exception as e:
            return pd.DataFrame(), {"warning": str(e)}

    def load_ml_context(self, spec: SymbolSpec, timeframe: str) -> tuple[pd.DataFrame, dict]:
        try:
            df = self.data_lake.load_ml_integration_features(spec.symbol, timeframe)
            if df.empty:
                return pd.DataFrame(), {"warning": "ML context empty."}
            return df, {}
        except Exception as e:
            return pd.DataFrame(), {"warning": str(e)}

    def load_paper_context_frames(self, spec: SymbolSpec, timeframe: str) -> tuple[dict[str, pd.DataFrame], dict]:
        warnings = {}

        frames = {}
        level_df, w1 = self.load_level_candidates(spec, timeframe)
        if w1: warnings.update(w1)
        frames["level_candidates"] = level_df

        sizing_df, w2 = self.load_sizing_candidates(spec, timeframe)
        if w2: warnings.update(w2)
        frames["sizing_candidates"] = sizing_df

        risk_df, w3 = self.load_risk_candidates(spec, timeframe)
        if w3: warnings.update(w3)
        frames["risk_candidates"] = risk_df

        ml_df, w4 = self.load_ml_context(spec, timeframe)
        if w4: warnings.update(w4)
        frames["ml_integration_context"] = ml_df

        return frames, warnings
