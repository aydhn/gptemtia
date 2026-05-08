import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

imports_add = """import json
import logging
import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional
"""

content = content.replace("""import json
import logging
import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional
""", imports_add)


dl_methods = """
    # --- ML DATASET PHASE ---
    def save_ml_feature_matrix(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.ml_features / f"{symbol}_{timeframe}_{profile_name}_features.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_feature_matrix(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_features / f"{symbol}_{timeframe}_{profile_name}_features.parquet"
        return self._load_parquet(path)

    def save_ml_target_frame(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.ml_targets / f"{symbol}_{timeframe}_{profile_name}_targets.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_target_frame(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_targets / f"{symbol}_{timeframe}_{profile_name}_targets.parquet"
        return self._load_parquet(path)

    def save_ml_supervised_dataset(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.ml_datasets / f"{symbol}_{timeframe}_{profile_name}_dataset.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_supervised_dataset(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_datasets / f"{symbol}_{timeframe}_{profile_name}_dataset.parquet"
        return self._load_parquet(path)

    def save_ml_split_manifest(self, symbol: str, timeframe: str, profile_name: str, manifest: dict) -> Path:
        path = self.paths.ml_splits / f"{symbol}_{timeframe}_{profile_name}_split.json"
        self._save_json(manifest, path)
        return path

    def load_ml_split_manifest(self, symbol: str, timeframe: str, profile_name: str) -> dict:
        path = self.paths.ml_splits / f"{symbol}_{timeframe}_{profile_name}_split.json"
        return self._load_json(path) or {}

    def save_ml_dataset_metadata(self, symbol: str, timeframe: str, profile_name: str, metadata: dict) -> Path:
        path = self.paths.ml_metadata / f"{symbol}_{timeframe}_{profile_name}_metadata.json"
        self._save_json(metadata, path)
        return path

    def load_ml_dataset_metadata(self, symbol: str, timeframe: str, profile_name: str) -> dict:
        path = self.paths.ml_metadata / f"{symbol}_{timeframe}_{profile_name}_metadata.json"
        return self._load_json(path) or {}

    def save_ml_dataset_quality(self, symbol: str, timeframe: str, profile_name: str, quality: dict) -> Path:
        path = self.paths.ml_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        self._save_json(quality, path)
        return path

    def load_ml_dataset_quality(self, symbol: str, timeframe: str, profile_name: str) -> dict:
        path = self.paths.ml_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        return self._load_json(path) or {}

    def list_ml_datasets(self) -> pd.DataFrame:
        data = []
        for file_path in self.paths.ml_metadata.glob("*.json"):
            metadata = self._load_json(file_path)
            if metadata:
                data.append(metadata)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)
"""
# find the class definition and insert at end
import sys

# Append methods to class
lines = content.split('\n')
for i in reversed(range(len(lines))):
    if lines[i].strip() != "":
         break

content = "\n".join(lines[:i+1]) + "\n" + dl_methods + "\n"

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
