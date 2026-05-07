with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

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

# Append just before the end of the class
# The class is `DataLake`. I'll just append it to the end of the file assuming no other top-level things.
with open("commodity_fx_signal_bot/data/storage/data_lake.py", "a") as f:
    f.write("\n" + pool_methods)
