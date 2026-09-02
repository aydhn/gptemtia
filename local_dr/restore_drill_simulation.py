import pandas as pd
from pathlib import Path
from local_dr.dr_config import LocalDRProfile
from local_dr.dr_models import RestoreDrillSimulation, build_restore_drill_id, restore_drill_simulation_to_dict

def build_restore_drill_for_domain(domain_label: str, project_root: Path, profile: LocalDRProfile) -> RestoreDrillSimulation:
    return RestoreDrillSimulation(
        drill_id=build_restore_drill_id("Basic Drill", domain_label),
        domain_label=domain_label,
        drill_name="Basic Drill",
        status="pending",
        paths_checked=[]
    )

def simulate_restore_artifact_presence(expected_paths: list[str], project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    results = []
    for path in expected_paths:
        full_path = project_root / path
        results.append({
            "path": path,
            "present": full_path.exists()
        })
    df = pd.DataFrame(results)
    summary = {
        "total_paths": len(results),
        "paths_found": sum(1 for r in results if r["present"])
    }
    return df, summary

def build_restore_drill_simulation_registry(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    drills = [
        build_restore_drill_for_domain("archive_restore_dr", project_root, profile)
    ]
    df = pd.DataFrame([restore_drill_simulation_to_dict(d) for d in drills])
    summary = summarize_restore_drill_simulations(df)
    return df, summary

def summarize_restore_drill_simulations(drill_df: pd.DataFrame) -> dict:
    return {
        "total_drills": len(drill_df),
        "passed_drills": len(drill_df[drill_df.get("status") == "passed"]) if "status" in drill_df else 0,
    }
