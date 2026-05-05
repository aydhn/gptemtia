import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

insert_str1 = """
    def get_decision_pool_path(self, timeframe: str, profile_name: str) -> Path:
        \"\"\"Get path for decision pool features.\"\"\"
        from config.paths import LAKE_FEATURES_DECISION_POOL_DIR
        filename = f"decision_pool_{timeframe}_{profile_name}.parquet"
        return LAKE_FEATURES_DECISION_POOL_DIR / filename

    def save_decision_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        \"\"\"Save a decision pool DataFrame to the Data Lake.\"\"\"
        if df is None or df.empty:
            return self.get_decision_pool_path(timeframe, profile_name)

        path = self.get_decision_pool_path(timeframe, profile_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            import logging
            logging.getLogger(__name__).debug(f"Saved decision pool to Data Lake: {path}")
        except Exception as e:
            import logging
            logging.getLogger(__name__).error(
                f"Failed to save decision pool ({timeframe}, {profile_name}): {e}"
            )
            raise

        return path

    def load_decision_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        \"\"\"Load a decision pool DataFrame from the Data Lake.\"\"\"
        path = self.get_decision_pool_path(timeframe, profile_name)
        if not path.exists():
            return pd.DataFrame()

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            return df
        except Exception as e:
            import logging
            logging.getLogger(__name__).error(
                f"Failed to load decision pool ({timeframe}, {profile_name}): {e}"
            )
            raise

    def has_decision_pool(self, timeframe: str, profile_name: str) -> bool:
        \"\"\"Check if decision pool exists.\"\"\"
        return self.get_decision_pool_path(timeframe, profile_name).exists()
"""

# append to class
content = content + insert_str1

# Now we need to patch get_feature_path to support decision_candidates
import_patch = """
            LAKE_FEATURES_SIGNAL_POOL_DIR,
            LAKE_FEATURES_DECISION_CANDIDATES_DIR,
        )
"""
content = content.replace("            LAKE_FEATURES_SIGNAL_POOL_DIR,\n        )", import_patch)

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
