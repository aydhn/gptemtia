import os
from pathlib import Path

def main():
    base_dir = Path("commodity_fx_signal_bot")
    tests_dir = base_dir / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)
    
    with open(tests_dir / "test_simplification_config.py", "w", encoding="utf-8") as f:
        f.write("""import pytest
from local_simplification.simplification_config import (
    validate_local_simplification_profiles,
    get_default_local_simplification_profile,
    get_local_simplification_profile,
    ConfigError
)

def test_validate_local_simplification_profiles_passes():
    validate_local_simplification_profiles()

def test_get_default_local_simplification_profile():
    p = get_default_local_simplification_profile()
    assert p.name == "balanced_local_simplification"
    assert p.language == "tr"
    assert p.max_items > 0
    assert p.max_candidate_items > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default is True
    assert p.allow_auto_refactor is False

def test_get_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_local_simplification_profile("unknown_profile_name")
""")

    with open(tests_dir / "test_simplification_labels.py", "w", encoding="utf-8") as f:
        f.write("""import pytest
from local_simplification.simplification_labels import (
    list_simplification_domain_labels,
    list_simplification_candidate_labels,
    list_simplification_status_labels,
    list_complexity_level_labels,
    list_simplification_risk_labels,
    validate_simplification_domain_label,
    validate_simplification_candidate_label
)

def test_lists_not_empty():
    assert len(list_simplification_domain_labels()) > 0
    assert len(list_simplification_candidate_labels()) > 0
    assert len(list_simplification_status_labels()) > 0
    assert len(list_complexity_level_labels()) > 0
    assert len(list_simplification_risk_labels()) > 0

def test_validate_domain_label_passes():
    validate_simplification_domain_label(list_simplification_domain_labels()[0])

def test_validate_candidate_label_passes():
    validate_simplification_candidate_label(list_simplification_candidate_labels()[0])
""")

    with open(tests_dir / "test_simplification_models.py", "w", encoding="utf-8") as f:
        f.write("""from local_simplification.simplification_models import (
    build_simplification_domain_id,
    build_complexity_item_id,
    build_simplification_candidate_id,
    build_slimming_plan_item_id,
    SlimmingPlanItem,
    slimming_plan_item_to_dict
)

def test_build_ids():
    assert build_simplification_domain_id("test") == "domain_test"
    assert build_complexity_item_id("a", "b") == "comp_a_b"
    assert build_simplification_candidate_id("a", "b") == "cand_a_b"
    assert build_slimming_plan_item_id("a", "b") == "plan_b_a"

def test_slimming_plan_item_not_real_cleanup():
    item = SlimmingPlanItem("1", "title", "cat", "hint", "action", True, [], ["Not real cleanup"])
    d = slimming_plan_item_to_dict(item)
    assert d["dry_run_only"] is True
""")

    with open(tests_dir / "test_simplification_domain_registry.py", "w", encoding="utf-8") as f:
        f.write("""from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.simplification_domain_registry import build_simplification_domain_registry

def test_build_simplification_domain_registry():
    p = get_default_local_simplification_profile()
    df, summary = build_simplification_domain_registry(p)
    assert not df.empty
    assert "required_reports" in df.columns
    assert "Bu registry official architecture simplification scope degildir." in summary["warnings"]
""")

    with open(tests_dir / "test_complexity_map.py", "w", encoding="utf-8") as f:
        f.write("""from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.complexity_map import build_final_modular_complexity_map, classify_complexity_level

def test_classify_complexity_level():
    assert classify_complexity_level(10, "folder_depth") == "complexity_very_high"

def test_build_final_modular_complexity_map():
    p = get_default_local_simplification_profile()
    df, summary = build_final_modular_complexity_map(Path("."), p)
    assert df is not None
    assert "Bu rapor official architecture assessment degildir." in summary["warnings"]
""")

    print("Created phase 82 tests 1")

if __name__ == "__main__":
    main()
