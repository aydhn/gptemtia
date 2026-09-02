
import pandas as pd
from local_dr.dr_config import LocalDRProfile
from local_dr.dr_models import RestoreDrillSimulation
from pathlib import Path

def build_restore_drill_for_domain(domain_label: str, project_root: Path, profile: LocalDRProfile) -> RestoreDrillSimulation:
    return RestoreDrillSimulation(drill_id="drill1", drill_name="drill", domain_label=domain_label, source_manifest=None, expected_artifacts=[], simulated_steps=[], status="restore_drill_simulated", warnings=[])

def simulate_restore_artifact_presence(expected_paths: list[str], project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_restore_drill_simulation_registry(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    drills = [build_restore_drill_for_domain("archive_restore_dr", project_root, profile)]
    df = pd.DataFrame([d.__dict__ for d in drills])
    return df, {"total_drills": len(drills)}

def summarize_restore_drill_simulations(drill_df: pd.DataFrame) -> dict:
    return {"total": len(drill_df)}
