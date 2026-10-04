import unittest
from unittest.mock import MagicMock

import pandas as pd

from advanced_risk_reporting.risk_reporting_portfolio_adjustment_guards import (
    build_risk_reporting_portfolio_adjustment_guard_registry,
    validate_portfolio_adjustment_request,
)


class TestRiskReportingPortfolioAdjustmentGuards(unittest.TestCase):
    def test_build_registry_default_profile(self):
        """Test building registry with default profile."""
        df, summary = build_risk_reporting_portfolio_adjustment_guard_registry()

        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(summary, dict)
        self.assertFalse(df.empty)

        # Check guard item properties
        self.assertEqual(df.iloc[0]["guard_name"], "portfolio_adjustment_guard")
        self.assertEqual(df.iloc[0]["domain"], "claim_guard")
        self.assertTrue(df.iloc[0]["is_active"])
        self.assertEqual(df.iloc[0]["action_on_violation"], "BLOCK")

        # Check summary properties
        self.assertEqual(summary["guard_count"], 1)
        self.assertTrue(summary["all_active"])

    def test_build_registry_custom_profile(self):
        """Test building registry with a provided profile."""
        # Using a mock instead since RiskReportingProfile is a frozen dataclass
        mock_profile = MagicMock()
        mock_profile.current_phase = 999
        mock_profile.target_final_phase = 1000
        mock_profile.next_phase = 9999

        df, _summary = build_risk_reporting_portfolio_adjustment_guard_registry(
            profile=mock_profile
        )

        self.assertEqual(df.iloc[0]["current_phase"], 999)
        self.assertEqual(df.iloc[0]["target_final_phase"], 1000)
        self.assertEqual(df.iloc[0]["next_phase"], 9999)

    def test_validate_safe_request(self):
        """Test validation of safe requests that shouldn't be blocked."""
        safe_requests = [
            "generate risk report",
            "calculate exposure limits",
            {"action": "show_metrics"},
            "view portfolio status",
            "None",
        ]

        for req in safe_requests:
            with self.subTest(request=req):
                result = validate_portfolio_adjustment_request(req)
                self.assertFalse(result["is_blocked"])
                self.assertTrue(result["is_safe"])
                self.assertEqual(result["action"], "ALLOW")
                self.assertEqual(result["reason"], "No violation")

    def test_validate_blocked_request(self):
        """Test validation blocks prohibited portfolio adjustment requests."""
        prohibited_requests = [
            "adjust_portfolio weights",
            "rebalance now",
            "hedge the position",
            "de_risk immediately",
            "reduce_position by half",
            "reallocate assets",
            "modify_weights",
            {"command": "REBALANCE"},
        ]

        for req in prohibited_requests:
            with self.subTest(request=req):
                result = validate_portfolio_adjustment_request(req)
                self.assertTrue(result["is_blocked"])
                self.assertFalse(result["is_safe"])
                self.assertEqual(result["action"], "BLOCK")
                self.assertIn("prohibited", result["reason"])


if __name__ == "__main__":
    unittest.main()
