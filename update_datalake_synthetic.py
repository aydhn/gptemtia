with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

new_methods = """
    # Phase 43: Synthetic Indices
    def save_synthetic_index_definitions(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_definitions / f"definitions_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_definitions(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_definitions / f"definitions_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_levels(self, index_id: str, timeframe: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_levels / f"{index_id}_{timeframe}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_levels(self, index_id: str, timeframe: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_levels / f"{index_id}_{timeframe}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_returns(self, index_id: str, timeframe: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_returns / f"{index_id}_{timeframe}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_returns(self, index_id: str, timeframe: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_returns / f"{index_id}_{timeframe}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_relative_strength_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_relative_strength / f"relative_strength_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_relative_strength_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_relative_strength / f"relative_strength_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_relative_momentum_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_relative_momentum / f"relative_momentum_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_relative_momentum_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_relative_momentum / f"relative_momentum_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_universe_rotation_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_rotation / f"universe_rotation_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_universe_rotation_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_rotation / f"universe_rotation_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_leadership_laggard_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_leadership / f"leadership_laggard_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_leadership_laggard_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_leadership / f"leadership_laggard_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_benchmark_comparison(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_comparisons / f"benchmark_comparison_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_benchmark_comparison(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_comparisons / f"benchmark_comparison_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_performance(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        path = self.paths.synthetic_indices_performance / f"index_performance_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_performance(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_performance / f"index_performance_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path:
        path = self.paths.synthetic_indices_quality / f"quality_{timeframe}_{profile_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_synthetic_index_quality(self, timeframe: str, profile_name: str) -> dict:
        path = self.paths.synthetic_indices_quality / f"quality_{timeframe}_{profile_name}.json"
        if path.exists():
            import json
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def save_synthetic_index_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = self.paths.synthetic_indices_reports / f"report_{timeframe}_{profile_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        if markdown:
             md_path = self.paths.synthetic_indices_reports_markdown / f"report_{timeframe}_{profile_name}.md"
             with open(md_path, "w") as f:
                 f.write(markdown)

        return path

    def load_synthetic_index_report(self, timeframe: str, profile_name: str) -> dict:
        path = self.paths.synthetic_indices_reports / f"report_{timeframe}_{profile_name}.json"
        if path.exists():
            import json
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def list_synthetic_index_reports(self) -> pd.DataFrame:
        records = []
        if self.paths.synthetic_indices_reports.exists():
            import json
            for path in self.paths.synthetic_indices_reports.glob("*.json"):
                try:
                    with open(path, "r") as f:
                        data = json.load(f)
                        records.append({
                            "file": path.name,
                            "timeframe": data.get("timeframe"),
                            "profile": data.get("profile"),
                            "timestamp": data.get("timestamp")
                        })
                except Exception:
                    pass
        return pd.DataFrame(records)
"""

# Insert before the last method (typically a helper or just before end of class)
# Looking for a good insertion point.

# Let's insert it before the class ends, but ensuring indentation.
lines = content.split('\n')
insert_idx = len(lines) - 1
for i in range(len(lines)-1, -1, -1):
    if lines[i].strip() != "":
         # Find last non-empty line
         if lines[i].startswith("    "): # Inside class
              insert_idx = i + 1
              break

lines.insert(insert_idx, new_methods)
content = "\n".join(lines)

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
