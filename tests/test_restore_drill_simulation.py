import pandas as pd
from pathlib import Path
from local_dr.dr_config import get_default_local_dr_profile
from local_dr.restore_drill_simulation import build_restore_drill_simulation_registry, build_restore_drill_for_domain, simulate_restore_artifact_presence, summarize_restore_drill_simulations

def test_restore_drill_simulation(tmp_path):
    profile = get_default_local_dr_profile()
    
    drill = build_restore_drill_for_domain("archive_restore_dr", tmp_path, profile)
    assert drill.drill_name == "Basic Drill"
    
    (tmp_path / "test_file.txt").touch()
    
    df, summary = simulate_restore_artifact_presence(["test_file.txt", "non_existent.txt"], tmp_path, profile)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert summary["total_paths"] == 2
    assert summary["paths_found"] == 1
    
    reg_df, reg_summary = build_restore_drill_simulation_registry(tmp_path, profile)
    assert isinstance(reg_df, pd.DataFrame)
    assert len(reg_df) == 1
    assert reg_summary["total_drills"] == 1
    assert reg_summary["passed_drills"] == 0
