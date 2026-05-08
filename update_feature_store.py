import re

with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

fs_methods = """
    # --- ML Dataset Methods ---
    def load_ml_feature_matrix(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        return self.data_lake.load_ml_feature_matrix(spec.symbol, timeframe, profile_name)

    def load_ml_target_frame(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        return self.data_lake.load_ml_target_frame(spec.symbol, timeframe, profile_name)

    def load_ml_supervised_dataset(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        return self.data_lake.load_ml_supervised_dataset(spec.symbol, timeframe, profile_name)

    def load_ml_dataset_metadata(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> dict:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        return self.data_lake.load_ml_dataset_metadata(spec.symbol, timeframe, profile_name)

    def list_available_ml_datasets(self, spec: SymbolSpec | None = None) -> dict:
        df = self.data_lake.list_ml_datasets()
        if df.empty:
             return {}
        if spec:
             df = df[df['symbol'] == spec.symbol]

        result = {}
        for _, row in df.iterrows():
             sym = row['symbol']
             tf = row['timeframe']
             prof = row['profile']
             key = f"{sym}_{tf}_{prof}"
             result[key] = row.to_dict()
        return result
"""

lines = content.split('\n')
for i in reversed(range(len(lines))):
    if lines[i].strip() != "":
         break

content = "\n".join(lines[:i+1]) + "\n" + fs_methods + "\n"

with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
    f.write(content)
