import pytest
import pandas as pd
from command_center.command_quality import (
    check_for_forbidden_command_terms_in_command_center,
    check_command_registry_quality,
    check_workflow_quality,
    check_runbook_quality,
    check_dry_run_plan_quality,
    build_command_center_quality_report
)
from command_center.command_config import get_default_command_center_profile

def test_check_for_forbidden_command_terms():
    res1 = check_for_forbidden_command_terms_in_command_center(text="this is a live order test")
    assert res1["forbidden_terms_found"] is True

    df = pd.DataFrame([{"cmd": "deploy server"}], dtype=object)
    res2 = check_for_forbidden_command_terms_in_command_center(df=df)
    assert res2["forbidden_terms_found"] is True

def test_check_registries_quality():
    profile = get_default_command_center_profile()
    df_safe = pd.DataFrame([{"cmd": "python run_status.py"}], dtype=object)

    res = check_command_registry_quality(df_safe, profile)
    assert res["valid"] is True

    df_unsafe = pd.DataFrame([{"cmd": "live execution broker"}], dtype=object)
    res2 = check_command_registry_quality(df_unsafe, profile)
    assert res2["valid"] is False

def test_build_quality_report():
    summary = {"profile": get_default_command_center_profile()}
    df_safe = pd.DataFrame([{"cmd": "python run_status.py"}], dtype=object)

    rep = build_command_center_quality_report(summary, commands_df=df_safe)
    assert rep["passed"] is True
    assert rep["warning_count"] == 0
