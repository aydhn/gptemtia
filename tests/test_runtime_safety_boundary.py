import pytest
from advanced_runtime.runtime_config import get_default_advanced_runtime_profile, validate_advanced_runtime_profiles
from advanced_runtime.runtime_labels import list_runtime_domain_labels
from advanced_runtime.runtime_models import build_runtime_profile_id
from advanced_runtime.runtime_profile_registry import build_advanced_runtime_profile_registry
from advanced_runtime.runtime_context import build_unified_runtime_context
from advanced_runtime.runtime_capabilities import build_runtime_capability_registry
from advanced_runtime.runtime_module_registry import build_runtime_module_registry
from advanced_runtime.runtime_dependency_graph import build_runtime_dependency_graph
from advanced_runtime.runtime_execution_contract import build_runtime_execution_contract
from advanced_runtime.runtime_command_contract import build_runtime_dry_run_command_contract
from advanced_runtime.runtime_output_contract import build_runtime_output_contract
from advanced_runtime.runtime_datalake_contract import build_runtime_datalake_contract
from advanced_runtime.runtime_featurestore_contract import build_runtime_featurestore_contract
from advanced_runtime.runtime_report_contract import build_runtime_report_contract
from advanced_runtime.runtime_safety_boundary import build_runtime_safety_boundary
from advanced_runtime.runtime_health import build_runtime_health_check
from advanced_runtime.runtime_scoring import calculate_runtime_readiness_score
from advanced_runtime.runtime_quality import build_runtime_quality_report
from advanced_runtime.runtime_pipeline import AdvancedRuntimePipeline

def test_config():
    p = get_default_advanced_runtime_profile()
    assert p.current_phase == 102
    assert p.target_final_phase == 160
    assert p.local_only is True
    assert p.non_production is True
    assert p.research_only is True
    assert p.allow_live_trading is False
    validate_advanced_runtime_profiles()

def test_labels():
    labels = list_runtime_domain_labels()
    assert "runtime_profile_domain" in labels

def test_models():
    assert build_runtime_profile_id("test") == "profile_test"

def test_profile_registry():
    p = get_default_advanced_runtime_profile()
    df, summary = build_advanced_runtime_profile_registry(p)
    assert not df.empty
    assert summary["ready"] > 0

def test_context():
    p = get_default_advanced_runtime_profile()
    txt, summary = build_unified_runtime_context(None, p)
    assert "Phase 102" in txt
    assert summary["length"] > 0

def test_capabilities():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_capability_registry(p)
    assert "future feature engine" in df["capability_name"].values

def test_module_registry():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_module_registry(None, p)
    assert "config/settings.py" in df["module_ref"].values

def test_dependency_graph():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_dependency_graph(p)
    assert not df.empty

def test_execution_contract():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_execution_contract(p)
    assert not df.empty

def test_command_contract():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_dry_run_command_contract(p)
    assert not df.empty

def test_output_contract():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_output_contract(p)
    assert not df.empty

def test_datalake_contract():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_datalake_contract(p)
    assert not df.empty

def test_featurestore_contract():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_featurestore_contract(p)
    assert not df.empty

def test_report_contract():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_report_contract(p)
    assert not df.empty

def test_safety_boundary():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_safety_boundary(p)
    assert not df.empty

def test_health():
    p = get_default_advanced_runtime_profile()
    df, summary = build_runtime_health_check(None, p)
    assert not df.empty

def test_scoring():
    p = get_default_advanced_runtime_profile()
    df, _ = build_runtime_capability_registry(p)
    score = calculate_runtime_readiness_score(df, df, df, df, df, p)
    assert 0 <= score <= 1

def test_quality():
    rep = build_runtime_quality_report({}, None, None)
    assert rep["overall_quality"] > 0

def test_pipeline():
    p = AdvancedRuntimePipeline(None, None, None)
    assert p.profile.current_phase == 102
