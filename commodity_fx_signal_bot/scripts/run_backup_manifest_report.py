"""
Script to run the backup manifest report.
"""
import argparse
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import Settings
from config.paths import DATA_DIR
from data.storage.data_lake import DataLake
from backup_recovery.backup_pipeline import BackupRecoveryPipeline

def main():
    parser = argparse.ArgumentParser(description="Run backup manifest report.")
    parser.add_argument("--profile", type=str, default="balanced_local_backup_recovery", help="Backup recovery profile name.")
    parser.add_argument("--no-save", action="store_true", help="Do not save the output.")
    args = parser.parse_args()

    settings = Settings.from_env()
    data_lake = DataLake(DATA_DIR / "lake")

    from backup_recovery.backup_config import get_backup_recovery_profile
    profile = get_backup_recovery_profile(args.profile)

    pipeline = BackupRecoveryPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=PROJECT_ROOT,
        profile=profile,
    )

    print(f"Running backup manifest report with profile {args.profile}...")
    data, summary = pipeline.build_backup_manifest_report(save=not args.no_save)
    print("Done. Summary:")
    print(summary)

if __name__ == "__main__":
    main()
