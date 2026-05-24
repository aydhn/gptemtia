path = "commodity_fx_signal_bot/data/storage/data_lake.py"
with open(path, "r") as f:
    content = f.read()

new_init = """    def __init__(self, root_dir):
        if hasattr(root_dir, "lake_dir"):
            self.paths = root_dir
            self.root_dir = root_dir.lake_dir
        else:
            self.root_dir = Path(root_dir)
            from config.paths import ProjectPaths

            self.paths = ProjectPaths()

        self.ohlcv_dir = self.root_dir / "ohlcv"
        self.governance_dir = self.root_dir / "governance"
"""
content = content.replace('    def __init__(self, root_dir):\n        if hasattr(root_dir, "lake_dir"):\n            self.paths = root_dir\n            self.root_dir = root_dir.lake_dir\n        else:\n            self.root_dir = Path(root_dir)\n            from config.paths import ProjectPaths\n\n            self.paths = ProjectPaths()\n\n        self.ohlcv_dir = self.root_dir / "ohlcv"\n', new_init)

with open(path, "w") as f:
    f.write(content)
print("Updated __init__ for DataLake")
