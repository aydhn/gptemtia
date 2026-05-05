with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

insert_str = """
    def get_strategy_pool_path(self, timeframe: str, profile_name: str) -> Path:
        \"\"\"Get path for strategy pool features.\"\"\"
        from config.paths import LAKE_FEATURES_STRATEGY_POOL_DIR

        filename = f"strategy_pool_{timeframe}_{profile_name}.parquet"
        return LAKE_FEATURES_STRATEGY_POOL_DIR / filename

    def save_strategy_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        \"\"\"Save a strategy pool DataFrame to the Data Lake.\"\"\"
        if df is None or df.empty:
            return self.get_strategy_pool_path(timeframe, profile_name)

        path = self.get_strategy_pool_path(timeframe, profile_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            import logging

            logging.getLogger(__name__).debug(
                f"Saved strategy pool to Data Lake: {path}"
            )
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to save strategy pool ({timeframe}, {profile_name}): {e}"
            )
            raise

        return path

    def load_strategy_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        \"\"\"Load a strategy pool DataFrame from the Data Lake.\"\"\"
        path = self.get_strategy_pool_path(timeframe, profile_name)
        if not path.exists():
            return pd.DataFrame()

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            return df
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to load strategy pool ({timeframe}, {profile_name}): {e}"
            )
            raise

    def has_strategy_pool(self, timeframe: str, profile_name: str) -> bool:
        \"\"\"Check if strategy pool exists.\"\"\"
        return self.get_strategy_pool_path(timeframe, profile_name).exists()
"""

if "get_strategy_pool_path" not in content:
    content += insert_str

    # Also update get_feature_path map if needed, but wait it seems get_feature_path is dynamically building or uses a map

    with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
        f.write(content)
