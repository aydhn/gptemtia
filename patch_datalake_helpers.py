import os
from pathlib import Path

def patch_data_lake():
    p = Path("commodity_fx_signal_bot/data/storage/data_lake.py")
    content = p.read_text(encoding="utf-8")
    
    helpers = """
    def _save_df(self, df, directory, filename, summary=None):
        import pandas as pd
        if df is None: return Path(directory) / f"{filename}.csv"
        Path(directory).mkdir(parents=True, exist_ok=True)
        out_path = Path(directory) / f"{filename}.csv"
        df.to_csv(out_path, index=False)
        return out_path

    def _load_df(self, directory, filename):
        import pandas as pd
        out_path = Path(directory) / f"{filename}.csv"
        if not out_path.exists(): return pd.DataFrame()
        return pd.read_csv(out_path)

    def _save_text(self, text, directory, filename, summary=None):
        if text is None: return Path(directory) / f"{filename}.md"
        Path(directory).mkdir(parents=True, exist_ok=True)
        out_path = Path(directory) / f"{filename}.md"
        out_path.write_text(text, encoding="utf-8")
        return out_path

    def _load_text(self, directory, filename):
        out_path = Path(directory) / f"{filename}.md"
        if not out_path.exists(): return ""
        return out_path.read_text(encoding="utf-8")

    def _save_json(self, data, directory, filename):
        import json
        Path(directory).mkdir(parents=True, exist_ok=True)
        out_path = Path(directory) / f"{filename}.json"
        out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return out_path

    def _load_json(self, directory, filename):
        import json
        out_path = Path(directory) / f"{filename}.json"
        if not out_path.exists(): return {}
        return json.loads(out_path.read_text(encoding="utf-8"))

"""
    if "def _save_df" not in content:
        content = content.replace("class DataLake:", "class DataLake:\n" + helpers)
        p.write_text(content, encoding="utf-8")
        print("Patched DataLake with helpers.")
    else:
        print("DataLake already has helpers.")

if __name__ == "__main__":
    patch_data_lake()
