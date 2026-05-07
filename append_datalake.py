import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

# Add level_pool related methods to DataLake
level_pool_methods = """
    def save_level_pool(self, timeframe: str, df: pd.DataFrame, profile_name: str) -> Path:
        \"\"\"Save a universe-level pool dataframe.\"\"\"
        from config.paths import LAKE_FEATURES_LEVEL_POOL_DIR
        LAKE_FEATURES_LEVEL_POOL_DIR.mkdir(parents=True, exist_ok=True)
        file_path = LAKE_FEATURES_LEVEL_POOL_DIR / f"level_pool_{timeframe}_{profile_name}.parquet"
        df.to_parquet(file_path, engine="pyarrow", index=True)
        return file_path

    def load_level_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        \"\"\"Load a universe-level pool dataframe.\"\"\"
        from config.paths import LAKE_FEATURES_LEVEL_POOL_DIR
        file_path = LAKE_FEATURES_LEVEL_POOL_DIR / f"level_pool_{timeframe}_{profile_name}.parquet"
        if file_path.exists():
            return pd.read_parquet(file_path, engine="pyarrow")
        return pd.DataFrame()

    def has_level_pool(self, timeframe: str, profile_name: str) -> bool:
        from config.paths import LAKE_FEATURES_LEVEL_POOL_DIR
        file_path = LAKE_FEATURES_LEVEL_POOL_DIR / f"level_pool_{timeframe}_{profile_name}.parquet"
        return file_path.exists()
"""

# Insert before the end of the class
content = content.replace("    # --- Additional DataLake utilities can be added here ---", level_pool_methods + "\n    # --- Additional DataLake utilities can be added here ---")

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
