# -*- coding: utf-8 -*-
"""Tests for Phase 155 Risk Reporting Source Preservation Guards."""

import unittest
import pandas as pd

from advanced_risk_reporting.risk_reporting_source_preservation_guards import (
    build_risk_reporting_source_preservation_guard_registry,
    validate_risk_reporting_source_preservation_action,
)
from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile


class TestRiskReportingSourcePreservationGuards(unittest.TestCase):
    """Test suite for risk reporting source preservation guards."""

    def test_build_risk_reporting_source_preservation_guard_registry_default(self):
        """Test building registry with default profile."""
        df, summary = build_risk_reporting_source_preservation_guard_registry()

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["guard_name"], "source_preservation_guard")
        self.assertEqual(df.iloc[0]["domain"], "preservation_guard")
        self.assertEqual(df.iloc[0]["action_on_violation"], "BLOCK")
        self.assertTrue(df.iloc[0]["is_active"])

        self.assertIsInstance(summary, dict)
        self.assertEqual(summary["guard_count"], 1)
        self.assertTrue(summary["all_active"])

    def test_build_risk_reporting_source_preservation_guard_registry_custom_profile(self):
        """Test building registry with a specific profile."""
        profile = get_default_risk_reporting_profile()
        # We need to replace the entire profile or use dataclasses.replace if it's a frozen dataclass
        from dataclasses import replace
        profile = replace(profile, current_phase=999)
        df, _ = build_risk_reporting_source_preservation_guard_registry(profile=profile)

        self.assertEqual(df.iloc[0]["current_phase"], 999)

    def test_validate_risk_reporting_source_preservation_action_safe(self):
        """Test validation with safe actions."""
        safe_actions = [
            "read_file",
            "load_data",
            "export_report",
            "save_results_to_new_file",
            "analyze_dataset",
        ]

        for action in safe_actions:
            result = validate_risk_reporting_source_preservation_action(action)
            self.assertFalse(result["is_blocked"])
            self.assertTrue(result["is_safe"])
            self.assertEqual(result["action"], "ALLOW")
            self.assertEqual(result["reason"], "No violation")

    def test_validate_risk_reporting_source_preservation_action_blocked(self):
        """Test validation with blocked (destructive) actions."""
        blocked_actions = [
            "overwrite_file",
            "delete_table",
            "DROP_SOURCE_DATA",
            "purge_old_records",
            "destructive_clean_columns",
            "truncate_table_users",
        ]

        for action in blocked_actions:
            result = validate_risk_reporting_source_preservation_action(action)
            self.assertTrue(result["is_blocked"])
            self.assertFalse(result["is_safe"])
            self.assertEqual(result["action"], "BLOCK")
            self.assertEqual(result["reason"], "Destructive source action strictly prohibited")


if __name__ == "__main__":
    unittest.main()
