import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

# Add mapping
mapping_add = """            "asset_profiles": paths.LAKE_FEATURES_ASSET_PROFILES_DIR,
            "asset_profile_events": paths.LAKE_FEATURES_ASSET_PROFILE_EVENTS_DIR,
            "group_features": paths.LAKE_FEATURES_GROUP_FEATURES_DIR,
            "sizing_candidates": paths.LAKE_FEATURES_SIZING_CANDIDATES_DIR,
            "sizing_pool": paths.LAKE_FEATURES_SIZING_POOL_DIR,
"""
content = re.sub(r'            "asset_profiles": paths.LAKE_FEATURES_ASSET_PROFILES_DIR,\n            "asset_profile_events": paths.LAKE_FEATURES_ASSET_PROFILE_EVENTS_DIR,\n            "group_features": paths.LAKE_FEATURES_GROUP_FEATURES_DIR,', mapping_add, content)


# Add pool methods
pool_methods = """
    def save_sizing_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        \"\"\"Saves the global universe-level sizing candidate pool.\"\"\"
        if df.empty:
            logger.warning(
                f"Empty sizing pool dataframe for {timeframe} {profile_name}. Skipping save."
            )
            return paths.LAKE_FEATURES_SIZING_POOL_DIR / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        file_path = paths.LAKE_FEATURES_SIZING_POOL_DIR / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        self._write_parquet(df, file_path)
        logger.info(f"Saved sizing pool to {file_path}")
        return file_path

    def load_sizing_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        \"\"\"Loads the global universe-level sizing candidate pool.\"\"\"
        file_path = paths.LAKE_FEATURES_SIZING_POOL_DIR / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        if not file_path.exists():
            raise FileNotFoundError(f"Sizing pool not found: {file_path}")
        return self._read_parquet(file_path)

    def has_sizing_pool(self, timeframe: str, profile_name: str) -> bool:
        \"\"\"Checks if the global universe-level sizing candidate pool exists.\"\"\"
        file_path = paths.LAKE_FEATURES_SIZING_POOL_DIR / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        return file_path.exists()
"""

# Try to insert after has_strategy_rule_pool if it exists, otherwise just end of class
if "def has_strategy_rule_pool" in content:
    content = re.sub(
        r'(    def has_strategy_rule_pool.*?\n        return file_path\.exists\(\)\n)',
        r'\1' + pool_methods,
        content,
        flags=re.DOTALL
    )
elif "def load_decision_pool" in content:
     content = re.sub(
        r'(    def load_decision_pool.*?\n        return self\._read_parquet\(file_path\)\n)',
        r'\1' + pool_methods,
        content,
        flags=re.DOTALL
    )
else:
    # Just append before the last line
    lines = content.split('\n')
    lines.insert(-1, pool_methods)
    content = '\n'.join(lines)


with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
