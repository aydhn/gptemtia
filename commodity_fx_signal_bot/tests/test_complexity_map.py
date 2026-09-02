from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.complexity_map import build_final_modular_complexity_map, classify_complexity_level

def test_classify_complexity_level():
    assert classify_complexity_level(10, "folder_depth") == "complexity_very_high"

def test_build_final_modular_complexity_map():
    p = get_default_local_simplification_profile()
    df, summary = build_final_modular_complexity_map(Path("."), p)
    assert df is not None
    assert "Bu rapor official architecture assessment degildir." in summary["warnings"]
