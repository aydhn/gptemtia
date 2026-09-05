def test_scripts_exist():
    import os
    assert os.path.exists("scripts/run_advanced_config_profile_registry.py")
    assert os.path.exists("scripts/run_research_mode_presets.py")
    assert os.path.exists("scripts/run_profile_composition.py")
    assert os.path.exists("scripts/run_profile_compatibility_matrix.py")
    assert os.path.exists("scripts/run_advanced_config_quality_report.py")
    assert os.path.exists("scripts/run_advanced_config_status.py")
