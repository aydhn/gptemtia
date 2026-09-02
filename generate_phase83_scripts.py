import os
from pathlib import Path

def generate_scripts():
    base_dir = Path("commodity_fx_signal_bot/scripts")
    
    # run_performance_domain_registry.py
    (base_dir / "run_performance_domain_registry.py").write_text("""import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_performance.performance_config import get_local_performance_profile, get_default_local_performance_profile
from local_performance.performance_pipeline import LocalPerformancePipeline

def main():
    parser = argparse.ArgumentParser(description="Run Performance Domain Registry")
    parser.add_argument("--profile", type=str, default="balanced_local_performance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    ProjectPaths.ensure_project_directories()
    data_lake = DataLake(ProjectPaths.DATA_LAKE_DIR)
    
    try:
        profile = get_local_performance_profile(args.profile)
    except Exception:
        profile = get_default_local_performance_profile()

    pipeline = LocalPerformancePipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    pipeline.build_performance_domain_registry(save=args.save)
    print("Performance domain registry generated.")

if __name__ == "__main__":
    main()
""", encoding="utf-8")

    # run_final_local_performance_budget.py
    (base_dir / "run_final_local_performance_budget.py").write_text("""import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_performance.performance_config import get_local_performance_profile, get_default_local_performance_profile
from local_performance.performance_pipeline import LocalPerformancePipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_performance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    ProjectPaths.ensure_project_directories()
    data_lake = DataLake(ProjectPaths.DATA_LAKE_DIR)
    try:
        profile = get_local_performance_profile(args.profile)
    except:
        profile = get_default_local_performance_profile()

    pipeline = LocalPerformancePipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    pipeline.build_final_local_performance_budget(save=args.save)
    print("Final local performance budget generated.")

if __name__ == "__main__":
    main()
""", encoding="utf-8")

    # run_resource_footprint_rehearsal.py
    (base_dir / "run_resource_footprint_rehearsal.py").write_text("""import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_performance.performance_config import get_local_performance_profile, get_default_local_performance_profile
from local_performance.performance_pipeline import LocalPerformancePipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_performance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    ProjectPaths.ensure_project_directories()
    data_lake = DataLake(ProjectPaths.DATA_LAKE_DIR)
    try:
        profile = get_local_performance_profile(args.profile)
    except:
        profile = get_default_local_performance_profile()

    pipeline = LocalPerformancePipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    pipeline.build_resource_footprint_rehearsal(save=args.save)
    print("Resource footprint rehearsal generated.")

if __name__ == "__main__":
    main()
""", encoding="utf-8")

    # run_maintenance_cost_estimate.py
    (base_dir / "run_maintenance_cost_estimate.py").write_text("""import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_performance.performance_config import get_local_performance_profile, get_default_local_performance_profile
from local_performance.performance_pipeline import LocalPerformancePipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_performance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    ProjectPaths.ensure_project_directories()
    data_lake = DataLake(ProjectPaths.DATA_LAKE_DIR)
    try:
        profile = get_local_performance_profile(args.profile)
    except:
        profile = get_default_local_performance_profile()

    pipeline = LocalPerformancePipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    pipeline.build_maintenance_cost_estimate(save=args.save)
    print("Maintenance cost estimate generated.")

if __name__ == "__main__":
    main()
""", encoding="utf-8")

    # run_offline_efficiency_plan.py
    (base_dir / "run_offline_efficiency_plan.py").write_text("""import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_performance.performance_config import get_local_performance_profile, get_default_local_performance_profile
from local_performance.performance_pipeline import LocalPerformancePipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_performance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    ProjectPaths.ensure_project_directories()
    data_lake = DataLake(ProjectPaths.DATA_LAKE_DIR)
    try:
        profile = get_local_performance_profile(args.profile)
    except:
        profile = get_default_local_performance_profile()

    pipeline = LocalPerformancePipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    pipeline.build_offline_efficiency_plan(save=args.save)
    print("Offline efficiency plan generated.")

if __name__ == "__main__":
    main()
""", encoding="utf-8")

    # run_performance_quality_report.py
    (base_dir / "run_performance_quality_report.py").write_text("""import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_performance.performance_config import get_local_performance_profile, get_default_local_performance_profile
from local_performance.performance_pipeline import LocalPerformancePipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_performance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    ProjectPaths.ensure_project_directories()
    data_lake = DataLake(ProjectPaths.DATA_LAKE_DIR)
    try:
        profile = get_local_performance_profile(args.profile)
    except:
        profile = get_default_local_performance_profile()

    pipeline = LocalPerformancePipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    pipeline.build_performance_quality_report(save=args.save)
    print("Performance quality report generated.")

if __name__ == "__main__":
    main()
""", encoding="utf-8")

    # run_performance_status.py
    (base_dir / "run_performance_status.py").write_text("""import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_performance.performance_config import get_local_performance_profile, get_default_local_performance_profile
from local_performance.performance_pipeline import LocalPerformancePipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_performance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    ProjectPaths.ensure_project_directories()
    data_lake = DataLake(ProjectPaths.DATA_LAKE_DIR)
    try:
        profile = get_local_performance_profile(args.profile)
    except:
        profile = get_default_local_performance_profile()

    pipeline = LocalPerformancePipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    pipeline.build_performance_status(save=args.save)
    print("Performance status generated.")

if __name__ == "__main__":
    main()
""", encoding="utf-8")

if __name__ == "__main__":
    generate_scripts()
    print("Scripts generated")
