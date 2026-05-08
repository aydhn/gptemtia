import os

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

ml_methods = """
    def save_ml_model_evaluation(self, symbol: str, timeframe: str, profile_name: str, model_id: str, evaluation: dict) -> Path:
        path = self.paths.ml_model_evaluations / f"{model_id}_evaluation.json"
        self._save_json(evaluation, path)
        return path

    def load_ml_model_evaluation(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> dict:
        path = self.paths.ml_model_evaluations / f"{model_id}_evaluation.json"
        return self._load_json(path) or {}

    def save_ml_cv_results(self, symbol: str, timeframe: str, profile_name: str, model_id: str, df: pd.DataFrame) -> Path:
        path = self.paths.ml_model_cv / f"{model_id}_cv.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_cv_results(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> pd.DataFrame:
        path = self.paths.ml_model_cv / f"{model_id}_cv.parquet"
        return self._load_parquet(path)

    def save_ml_model_quality(self, symbol: str, timeframe: str, profile_name: str, model_id: str, quality: dict) -> Path:
        path = self.paths.ml_model_quality / f"{model_id}_quality.json"
        self._save_json(quality, path)
        return path

    def load_ml_model_quality(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> dict:
        path = self.paths.ml_model_quality / f"{model_id}_quality.json"
        return self._load_json(path) or {}

    def save_ml_registry_entry(self, entry: dict) -> Path:
        model_id = entry.get("model_id", "unknown")
        path = self.paths.ml_model_registry / f"{model_id}_registry.json"
        self._save_json(entry, path)
        return path

    def list_ml_model_registry(self) -> pd.DataFrame:
        data = []
        for file_path in self.paths.ml_model_registry.glob("*.json"):
            metadata = self._load_json(file_path)
            if metadata:
                data.append(metadata)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)
"""

if "def save_ml_model_evaluation" not in content:
    content += ml_methods
    with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
        f.write(content)
    print("Added ML methods to DataLake")
