import os

with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

ml_methods = """
    def load_ml_model_evaluation(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None, model_id: str | None = None) -> dict:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        if not model_id:
             return {}
        return self.data_lake.load_ml_model_evaluation(spec.symbol, timeframe, profile_name, model_id)

    def load_ml_cv_results(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None, model_id: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        if not model_id:
             return pd.DataFrame()
        return self.data_lake.load_ml_cv_results(spec.symbol, timeframe, profile_name, model_id)

    def load_ml_model_quality(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None, model_id: str | None = None) -> dict:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        if not model_id:
             return {}
        return self.data_lake.load_ml_model_quality(spec.symbol, timeframe, profile_name, model_id)

    def list_available_ml_models(self, spec: SymbolSpec | None = None) -> dict:
        df = self.data_lake.list_ml_model_registry()
        if df.empty:
             return {}
        if spec:
             df = df[df['symbol'] == spec.symbol]

        result = {}
        for _, row in df.iterrows():
            sym = row.get("symbol")
            tf = row.get("timeframe")
            if sym not in result:
                result[sym] = {}
            if tf not in result[sym]:
                result[sym][tf] = []
            result[sym][tf].append(row.to_dict())
        return result
"""

if "def load_ml_model_evaluation" not in content:
    content += ml_methods
    with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
        f.write(content)
    print("Added ML model methods to FeatureStore")
