# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Full System Integration Report Builder."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_full_system_integration_disclaimer,
    build_full_system_integration_profile_markdown_report,
    build_system_component_markdown_report,
    build_full_system_integration_full_markdown_report,
)


def test_disclaimer():
    disclaimer = build_full_system_integration_disclaimer()
    assert "UYARI VE KAPSAM SINIRI" in disclaimer
    assert "Phase 158" in disclaimer
    assert "Canlı emir" in disclaimer


def test_markdown_reports():
    profile = get_default_full_system_integration_profile()
    summary = {"active_profile": profile.profile_name, "total_profiles": 3, "status": "ready"}
    df = pd.DataFrame([{"profile_name": profile.profile_name}])

    md_prof = build_full_system_integration_profile_markdown_report(summary, df)
    assert "# Phase 158: Full-System Integration Profiles" in md_prof
    assert profile.profile_name in md_prof

    md_comp = build_system_component_markdown_report(summary, df)
    assert "# Phase 158: System Component Registry" in md_comp


def test_full_markdown_report():
    profile = get_default_full_system_integration_profile()
    tables = {
        "components": pd.DataFrame([{"component_id": "CMP-01", "name": "data"}]),
        "manifest": pd.DataFrame([{"manifest_id": "MNF-01"}]),
    }
    summary = {
        "active_profile": profile.profile_name,
        "readiness_score": 1.0,
        "classification": "full_system_integration_contract_ready_non_production",
        "meets_threshold": True,
        "handoff_ready": True,
    }
    md_full = build_full_system_integration_full_markdown_report(tables, summary)
    assert "# Phase 158: Consolidated Full-System Integration & Advanced Acceptance Rehearsal Report" in md_full
    assert "Executive Governance Summary" in md_full
    assert "Registered System Components" in md_full
