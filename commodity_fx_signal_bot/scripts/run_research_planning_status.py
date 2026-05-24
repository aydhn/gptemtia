import argparse
from pathlib import Path
from config.paths import ProjectPaths

def main():
    parser = argparse.ArgumentParser(description="Generate Research Planning Status Report")
    args = parser.parse_args()

    project_root = Path(__file__).parent.parent
    paths = ProjectPaths(project_root)

    planning_dir = paths.LAKE_RESEARCH_PLANNING_DIR
    if not planning_dir.exists():
        print(f"Research Planning directory does not exist: {planning_dir}")
        return

    files = list(planning_dir.rglob("*.*"))
    print(f"Found {len(files)} files in {planning_dir}")
    print("WARNING: Output files represent offline planning tasks, NOT live system statuses.")

if __name__ == "__main__":
    main()
