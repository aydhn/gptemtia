"""Phase 130 Test Runner.

Executes all 39 Phase 130 unit test suites.
"""

import sys
from pathlib import Path
import pytest

TEST_FILES = [
    "tests/test_regime_transition_config.py",
    "tests/test_regime_transition_labels.py",
    "tests/test_regime_transition_models.py",
    "tests/test_regime_transition_profile_registry.py",
    "tests/test_regime_transition_domain_registry.py",
    "tests/test_regime_state_sequence_contracts.py",
    "tests/test_candidate_state_sequence_schema.py",
    "tests/test_pseudo_state_sequence_schema.py",
    "tests/test_regime_transition_metric_registry.py",
    "tests/test_regime_stability_metric_registry.py",
    "tests/test_regime_transition_thresholds.py",
    "tests/test_regime_transition_timestamp_policies.py",
    "tests/test_regime_transition_no_lookahead_guard.py",
    "tests/test_regime_transition_source_phases.py",
    "tests/test_state_persistence_diagnostics.py",
    "tests/test_state_transition_frequency.py",
    "tests/test_state_transition_matrix_placeholders.py",
    "tests/test_state_transition_ambiguity.py",
    "tests/test_state_transition_continuity.py",
    "tests/test_state_transition_stability.py",
    "tests/test_volatility_transition_diagnostics.py",
    "tests/test_trend_transition_diagnostics.py",
    "tests/test_range_transition_diagnostics.py",
    "tests/test_macro_event_transition_context.py",
    "tests/test_news_metadata_transition_context.py",
    "tests/test_cross_asset_transition_prep.py",
    "tests/test_transition_quality_dependencies.py",
    "tests/test_transition_validation_dependencies.py",
    "tests/test_transition_manual_review.py",
    "tests/test_transition_quality_findings.py",
    "tests/test_transition_stability_scoring.py",
    "tests/test_transition_diagnostics_manifest.py",
    "tests/test_regime_transition_report_builder.py",
    "tests/test_regime_transition_pipeline.py",
    "tests/test_regime_transition_health.py",
    "tests/test_regime_transition_validation.py",
    "tests/test_regime_transition_safety_boundary.py",
    "tests/test_phase_131_handoff.py",
    "tests/test_advanced_regime_transition_scripts_contract.py",
]


def main():
    root = Path(__file__).resolve().parent.parent
    args = ["-q"] + [str(root / f) for f in TEST_FILES]
    exit_code = pytest.main(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
