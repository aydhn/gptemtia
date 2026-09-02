import os
from pathlib import Path

def generate_tests():
    base_dir = Path("commodity_fx_signal_bot/tests")
    
    # test_performance_config.py
    (base_dir / "test_performance_config.py").write_text("""import pytest
from local_performance.performance_config import validate_local_performance_profiles, get_default_local_performance_profile, get_local_performance_profile, ConfigError

def test_validate_local_performance_profiles():
    validate_local_performance_profiles()

def test_get_default_local_performance_profile():
    p = get_default_local_performance_profile()
    assert p.name == "balanced_local_performance"
    assert p.language != ""
    assert p.default_memory_budget_mb > 0
    assert p.default_disk_budget_mb > 0
    assert p.default_runtime_budget_minutes > 0
    assert p.max_items > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default is True
    assert p.allow_real_benchmark is False
    assert p.allow_production_capacity_claim is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_performance_profile("unknown")
""", encoding="utf-8")

    # test_performance_labels.py
    (base_dir / "test_performance_labels.py").write_text("""import pytest
from local_performance.performance_labels import list_performance_domain_labels, list_performance_estimate_labels, list_performance_status_labels, list_efficiency_candidate_labels, list_performance_risk_labels, validate_performance_domain_label, validate_performance_estimate_label, validate_performance_status, validate_efficiency_candidate_label, validate_performance_risk, ConfigError

def test_label_lists():
    assert len(list_performance_domain_labels()) > 0
    assert len(list_performance_estimate_labels()) > 0
    assert len(list_performance_status_labels()) > 0
    assert len(list_efficiency_candidate_labels()) > 0
    assert len(list_performance_risk_labels()) > 0

def test_validators():
    validate_performance_domain_label("performance_budget_domain")
    validate_performance_estimate_label("cpu_estimate_low")
    validate_performance_status("performance_ready_for_rehearsal")
    assert "production capacity approval" not in "performance_ready_for_rehearsal"
""", encoding="utf-8")

    # test_performance_models.py
    (base_dir / "test_performance_models.py").write_text("""from local_performance.performance_models import build_performance_domain_id, build_resource_estimate_id, build_runtime_estimate_id, build_efficiency_candidate_id, PerformanceDomain, performance_domain_to_dict

def test_builders():
    assert build_performance_domain_id("test") == build_performance_domain_id("test")
    assert build_resource_estimate_id("a", "b") == build_resource_estimate_id("a", "b")
    assert build_runtime_estimate_id("a", "b") == build_runtime_estimate_id("a", "b")
    assert build_efficiency_candidate_id("a", "b") == build_efficiency_candidate_id("a", "b")

def test_dataclasses():
    d = PerformanceDomain("1", "lbl", "name", "desc", [], [])
    dct = performance_domain_to_dict(d)
    assert "domain_id" in dct
""", encoding="utf-8")

    # test_performance_domain_registry.py
    (base_dir / "test_performance_domain_registry.py").write_text("""from local_performance.performance_domain_registry import build_performance_domain_registry, build_default_performance_domains
from local_performance.performance_config import get_default_local_performance_profile

def test_domain_registry():
    p = get_default_local_performance_profile()
    df, s = build_performance_domain_registry(p)
    assert not df.empty
    domains = build_default_performance_domains(p)
    assert len(domains) > 0
""", encoding="utf-8")

    # test_performance_budget.py
    (base_dir / "test_performance_budget.py").write_text("""from local_performance.performance_budget import build_final_local_performance_budget, build_default_performance_budget_items, classify_budget_pressure
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_performance_budget():
    p = get_default_local_performance_profile()
    df, s = build_final_local_performance_budget(Path("."), p)
    assert not df.empty
    items = build_default_performance_budget_items(p)
    assert not items.empty
    assert classify_budget_pressure(None, p) == "normal"
""", encoding="utf-8")

    # test_runtime_profile.py
    (base_dir / "test_runtime_profile.py").write_text("""from local_performance.runtime_profile import build_lightweight_runtime_profile, build_runtime_profile_items, classify_runtime_mode
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_runtime_profile():
    p = get_default_local_performance_profile()
    df, s = build_lightweight_runtime_profile(Path("."), p)
    assert not df.empty
    items = build_runtime_profile_items(p)
    assert not items.empty
    assert classify_runtime_mode(pd.Series({"mode_name": "test"}), p) == "test"
""", encoding="utf-8")

    # test_resource_footprint.py
    (base_dir / "test_resource_footprint.py").write_text("""from local_performance.resource_footprint import build_resource_footprint_rehearsal_report, discover_resource_footprint_items
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_resource_footprint():
    p = get_default_local_performance_profile()
    df, s = build_resource_footprint_rehearsal_report(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_cpu_estimates.py
    (base_dir / "test_cpu_estimates.py").write_text("""from local_performance.cpu_estimates import build_cpu_usage_estimate_registry, estimate_cpu_pressure_for_file
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_cpu_estimates():
    p = get_default_local_performance_profile()
    df, s = build_cpu_usage_estimate_registry(Path("."), p)
    assert not df.empty
    est = estimate_cpu_pressure_for_file(Path("."), Path("."), p)
    assert isinstance(est, dict)
""", encoding="utf-8")

    # test_memory_estimates.py
    (base_dir / "test_memory_estimates.py").write_text("""from local_performance.memory_estimates import build_memory_usage_estimate_registry, estimate_memory_pressure_for_layer
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_memory_estimates():
    p = get_default_local_performance_profile()
    df, s = build_memory_usage_estimate_registry(Path("."), p)
    assert not df.empty
    est = estimate_memory_pressure_for_layer("l", 1, p)
    assert isinstance(est, dict)
""", encoding="utf-8")

    # test_disk_estimates.py
    (base_dir / "test_disk_estimates.py").write_text("""from local_performance.disk_estimates import build_disk_usage_estimate_registry, estimate_disk_usage_by_layer
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_disk_estimates():
    p = get_default_local_performance_profile()
    df, s = build_disk_usage_estimate_registry(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_growth_estimates.py
    (base_dir / "test_growth_estimates.py").write_text("""from local_performance.growth_estimates import build_report_output_growth_estimate, build_datalake_growth_estimate, build_generated_docs_growth_estimate
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_growth_estimates():
    p = get_default_local_performance_profile()
    df1, _ = build_report_output_growth_estimate(Path("."), p)
    df2, _ = build_datalake_growth_estimate(Path("."), p)
    df3, _ = build_generated_docs_growth_estimate(Path("."), p)
    assert not df1.empty and not df2.empty and not df3.empty
""", encoding="utf-8")

    # test_script_runtime_estimates.py
    (base_dir / "test_script_runtime_estimates.py").write_text("""from local_performance.script_runtime_estimates import build_script_runtime_estimate_registry, estimate_script_runtime_from_static_features
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_script_runtime_estimates():
    p = get_default_local_performance_profile()
    df, s = build_script_runtime_estimate_registry(Path("."), p)
    assert not df.empty
    est = estimate_script_runtime_from_static_features(Path("."), Path("."), p)
    assert isinstance(est, dict)
""", encoding="utf-8")

    # test_test_runtime_estimates.py
    (base_dir / "test_test_runtime_estimates.py").write_text("""from local_performance.test_runtime_estimates import build_test_runtime_estimate_registry, estimate_test_runtime_from_static_features
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_test_runtime_estimates():
    p = get_default_local_performance_profile()
    df, s = build_test_runtime_estimate_registry(Path("."), p)
    assert not df.empty
    est = estimate_test_runtime_from_static_features(Path("."), Path("."), p)
    assert isinstance(est, dict)
""", encoding="utf-8")

    # test_pipeline_runtime_estimates.py
    (base_dir / "test_pipeline_runtime_estimates.py").write_text("""from local_performance.pipeline_runtime_estimates import build_pipeline_runtime_estimate_registry, build_known_pipeline_runtime_estimates
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_pipeline_runtime_estimates():
    p = get_default_local_performance_profile()
    df, s = build_pipeline_runtime_estimate_registry(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_maintenance_cost.py
    (base_dir / "test_maintenance_cost.py").write_text("""from local_performance.maintenance_cost import build_maintenance_cost_estimate
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_maintenance_cost():
    p = get_default_local_performance_profile()
    df, s = build_maintenance_cost_estimate(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_maintenance_effort.py
    (base_dir / "test_maintenance_effort.py").write_text("""from local_performance.maintenance_effort import build_maintenance_effort_matrix, classify_maintenance_effort
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_maintenance_effort():
    p = get_default_local_performance_profile()
    df, s = build_maintenance_effort_matrix(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_operator_time_budget.py
    (base_dir / "test_operator_time_budget.py").write_text("""from local_performance.operator_time_budget import build_operator_time_budget_report
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_operator_time_budget():
    p = get_default_local_performance_profile()
    df, s = build_operator_time_budget_report(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_machine_suitability.py
    (base_dir / "test_machine_suitability.py").write_text("""from local_performance.machine_suitability import build_local_machine_suitability_checklist
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_machine_suitability():
    p = get_default_local_performance_profile()
    df, s = build_local_machine_suitability_checklist(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_efficiency_planning.py
    (base_dir / "test_efficiency_planning.py").write_text("""from local_performance.efficiency_planning import build_offline_efficiency_planning_guide
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_efficiency_planning():
    p = get_default_local_performance_profile()
    text, s = build_offline_efficiency_planning_guide(Path("."), p)
    assert isinstance(text, str)
    assert len(text) > 0
""", encoding="utf-8")

    # test_efficiency_candidates.py
    (base_dir / "test_efficiency_candidates.py").write_text("""from local_performance.efficiency_candidates import build_efficiency_candidate_registry
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_efficiency_candidates():
    p = get_default_local_performance_profile()
    df, s = build_efficiency_candidate_registry(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_lightweight_mode.py
    (base_dir / "test_lightweight_mode.py").write_text("""from local_performance.lightweight_mode import build_lightweight_mode_recommendation_registry
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_lightweight_mode():
    p = get_default_local_performance_profile()
    df, s = build_lightweight_mode_recommendation_registry(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_heavy_output_warnings.py
    (base_dir / "test_heavy_output_warnings.py").write_text("""from local_performance.heavy_output_warnings import build_heavy_output_warning_registry
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_heavy_output_warnings():
    p = get_default_local_performance_profile()
    df, s = build_heavy_output_warning_registry(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_storage_retention.py
    (base_dir / "test_storage_retention.py").write_text("""from local_performance.storage_retention import build_storage_retention_rehearsal_plan
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_storage_retention():
    p = get_default_local_performance_profile()
    df, s = build_storage_retention_rehearsal_plan(Path("."), p)
    assert not df.empty
""", encoding="utf-8")

    # test_report_rotation.py
    (base_dir / "test_report_rotation.py").write_text("""from local_performance.report_rotation import build_report_rotation_rehearsal_guide
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_report_rotation():
    p = get_default_local_performance_profile()
    text, s = build_report_rotation_rehearsal_guide(Path("."), p)
    assert isinstance(text, str)
""", encoding="utf-8")

    # test_datalake_retention.py
    (base_dir / "test_datalake_retention.py").write_text("""from local_performance.datalake_retention import build_datalake_retention_rehearsal_guide
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_datalake_retention():
    p = get_default_local_performance_profile()
    text, s = build_datalake_retention_rehearsal_guide(Path("."), p)
    assert isinstance(text, str)
""", encoding="utf-8")

    # test_performance_no_go_safe_go.py
    (base_dir / "test_performance_no_go_safe_go.py").write_text("""from local_performance.performance_no_go_safe_go import build_performance_no_go_safe_go_summary
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_performance_no_go_safe_go():
    p = get_default_local_performance_profile()
    df, s = build_performance_no_go_safe_go_summary(p)
    assert not df.empty
""", encoding="utf-8")

    # test_performance_exceptions.py
    (base_dir / "test_performance_exceptions.py").write_text("""from local_performance.performance_exceptions import build_performance_exception_register
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_performance_exceptions():
    p = get_default_local_performance_profile()
    df, s = build_performance_exception_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
""", encoding="utf-8")

    # test_performance_gaps.py
    (base_dir / "test_performance_gaps.py").write_text("""from local_performance.performance_gaps import build_performance_gap_register
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_performance_gaps():
    p = get_default_local_performance_profile()
    df, s = build_performance_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
""", encoding="utf-8")

    # test_performance_risks.py
    (base_dir / "test_performance_risks.py").write_text("""from local_performance.performance_risks import build_performance_risk_summary
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_performance_risks():
    p = get_default_local_performance_profile()
    df, s = build_performance_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
""", encoding="utf-8")

    # test_performance_scoring.py
    (base_dir / "test_performance_scoring.py").write_text("""from local_performance.performance_scoring import build_performance_readiness_score_report
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_performance_scoring():
    p = get_default_local_performance_profile()
    df, s = build_performance_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
""", encoding="utf-8")

    # test_performance_validation.py
    (base_dir / "test_performance_validation.py").write_text("""from local_performance.performance_validation import validate_performance_domains
from local_performance.performance_config import get_default_local_performance_profile
import pandas as pd

def test_performance_validation():
    p = get_default_local_performance_profile()
    v = validate_performance_domains(pd.DataFrame(), p)
    assert v["valid"]
""", encoding="utf-8")

    # test_performance_quality.py
    (base_dir / "test_performance_quality.py").write_text("""from local_performance.performance_quality import check_for_forbidden_terms_in_performance
from local_performance.performance_config import get_default_local_performance_profile

def test_performance_quality():
    res = check_for_forbidden_terms_in_performance("benchmark completed")
    assert not res["valid"]
    res2 = check_for_forbidden_terms_in_performance("gercek benchmark degildir")
    assert res2["valid"]
""", encoding="utf-8")

    # test_performance_report_builder.py
    (base_dir / "test_performance_report_builder.py").write_text("""from local_performance.performance_report_builder import build_performance_domain_registry_markdown_report

def test_performance_report_builder():
    txt = build_performance_domain_registry_markdown_report({})
    assert "benchmark" in txt
""", encoding="utf-8")

    # test_performance_pipeline.py
    (base_dir / "test_performance_pipeline.py").write_text("""from local_performance.performance_pipeline import LocalPerformancePipeline
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
from config.settings import Settings

class MockDataLake:
    pass

def test_performance_pipeline():
    p = get_default_local_performance_profile()
    dl = MockDataLake()
    s = Settings()
    pipe = LocalPerformancePipeline(dl, s, Path("."), p)
    res, summ = pipe.build_performance_domain_registry(save=False)
    assert "performance_domain_registry" in res
""", encoding="utf-8")

    # test_local_performance_scripts_contract.py
    (base_dir / "test_local_performance_scripts_contract.py").write_text("""def test_scripts_contract():
    import scripts.run_performance_domain_registry
    import scripts.run_final_local_performance_budget
    import scripts.run_resource_footprint_rehearsal
    import scripts.run_maintenance_cost_estimate
    import scripts.run_offline_efficiency_plan
    import scripts.run_performance_quality_report
    import scripts.run_performance_status
    assert True
""", encoding="utf-8")

if __name__ == "__main__":
    generate_tests()
    print("Tests generated")
