from pathlib import Path
from config.settings import Settings
from config.paths import DATA_DIR
from data.storage.data_lake import DataLake
from backup_recovery.backup_pipeline import BackupRecoveryPipeline

def test_backup_pipeline():
    settings = Settings.from_env()
    dl = DataLake(DATA_DIR / "lake")
    pipe = BackupRecoveryPipeline(dl, settings, Path("."))
    df, sum = pipe.build_project_state_inventory_report(save=False)
    assert sum["status"] == "empty"
