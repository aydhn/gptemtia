from pathlib import Path

def fix():
    p = Path("commodity_fx_signal_bot/data/storage/data_lake.py")
    c = p.read_text()

    # In DataLake patch we used self.project_paths, but it should be self.paths
    c = c.replace("self.project_paths", "self.paths")

    p.write_text(c)
    print("Fixed data_lake project_paths.")

fix()
