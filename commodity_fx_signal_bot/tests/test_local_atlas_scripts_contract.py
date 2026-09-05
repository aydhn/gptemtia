import pytest
from pathlib import Path

def test_scripts_exist():
    scripts = [
        "run_atlas_domain_registry.py",
        "run_final_meta_index.py",
        "run_universal_navigation_map.py",
        "run_cross_phase_lookup_engine.py",
        "run_offline_semantic_toc.py",
        "run_terminal_project_atlas.py",
        "run_atlas_quality_report.py",
        "run_atlas_status.py"
    ]
    p = Path("scripts")
    for s in scripts:
        assert (p / s).exists()
