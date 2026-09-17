# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Report Builder."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_profile_registry import (
    build_stress_testing_profile_registry,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_stress_testing_profile_markdown_report,
    build_stress_testing_disclaimer,
)


def test_report_builder():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_testing_profile_registry(prof)
    md = build_stress_testing_profile_markdown_report(summary, df)
    assert "Phase 148" in md
    assert "Profil" in md
    disclaimer = build_stress_testing_disclaimer()
    assert "Phase 148" in disclaimer
