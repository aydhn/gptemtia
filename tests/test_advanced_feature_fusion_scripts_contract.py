"""Tests for Phase 120 CLI Scripts Execution Contract."""

import sys
from unittest.mock import patch
import pytest

from scripts.run_fusion_feature_profile_registry import main as run_profiles
from scripts.run_fusion_feature_contracts import main as run_contracts
from scripts.run_macro_calendar_policy_registries import main as run_policies
from scripts.run_news_metadata_fusion_policies import main as run_news_policies
from scripts.run_macro_calendar_news_fusion_registries import main as run_cross_registries
from scripts.run_fusion_feature_matrix import main as run_matrix
from scripts.run_fusion_feature_metadata_registry import main as run_meta_registry
from scripts.run_fusion_feature_health_check import main as run_health
from scripts.run_fusion_feature_validation_report import main as run_val_report
from scripts.run_fusion_feature_status import main as run_status


def test_all_10_scripts_run_cleanly():
    # 1. Profile registry
    run_profiles()

    # 2. Contracts
    run_contracts()

    # 3. Macro & calendar policies
    run_policies()

    # 4. News policies
    run_news_policies()

    # 5. Cross fusion registries
    run_cross_registries()

    # 6. Feature matrix
    run_matrix()

    # 7. Metadata registry
    run_meta_registry()

    # 8. Health check
    run_health()

    # 9. Validation report
    run_val_report()

    # 10. Status
    run_status()
