"""Tests for Phase 121 CLI Scripts Execution Contract."""

import sys
from unittest.mock import patch
import pytest

from scripts.run_feature_validation_profile_registry import main as run_profiles
from scripts.run_feature_validation_rules import main as run_rules
from scripts.run_no_lookahead_validation import main as run_no_lookahead
from scripts.run_feature_matrix_integrity_validation import main as run_matrix_integrity
from scripts.run_domain_feature_output_validation import main as run_domain_outputs
from scripts.run_feature_validation_findings import main as run_findings
from scripts.run_feature_validation_scoring import main as run_scoring
from scripts.run_feature_validation_health_check import main as run_health
from scripts.run_feature_validation_report import main as run_report
from scripts.run_feature_validation_status import main as run_status


def test_all_10_feature_validation_scripts_run_cleanly():
    # 1. Profile registry
    run_profiles()

    # 2. Rules & forbidden columns
    run_rules()

    # 3. No-lookahead validation
    run_no_lookahead()

    # 4. Feature matrix integrity
    run_matrix_integrity()

    # 5. Domain outputs
    run_domain_outputs()

    # 6. Findings & review queue
    run_findings()

    # 7. Scoring
    run_scoring()

    # 8. Health check
    run_health()

    # 9. Report builder
    run_report()

    # 10. Status
    run_status()
