import os
from pathlib import Path
import re

def fix_paths():
    paths_path = Path("config/paths.py")
    with open(paths_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace DATA_LAKE_DIR with LAKE_DIR in LOCAL_REUSE section
    content = content.replace('LOCAL_REUSE_DIR = DATA_LAKE_DIR / "local_reuse"', 'LOCAL_REUSE_DIR = LAKE_DIR / "local_reuse"')
    
    with open(paths_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed LAKE_DIR reference in paths.py")

if __name__ == "__main__":
    fix_paths()
