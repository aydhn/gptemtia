"""Phase 135: Regime Block Test Contract Report.

Verifies existence and coverage of test contracts for each phase across the 126-135 regime block.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    REGIME_BLOCK_TEST_CONTRACT_DOMAIN,
)


REPRESENTATIVE_REGIME_TESTS: List[Dict[str, Any]] = [
    {"phase": 126, "test_file": "tests/test_regime_foundation_manifest.py"},
    {"phase": 127, "test_file": "tests/test_regime_matrix_integrity_manifest.py"},
    {"phase": 128, "test_file": "tests/test_regime_candidate_state_integrity_manifest.py"},
    {"phase": 129, "test_file": "tests/test_behavior_diagnostics_manifest.py"},
    {"phase": 130, "test_file": "tests/test_transition_diagnostics_manifest.py"},
    {"phase": 131, "test_file": "tests/test_cross_asset_regime_context_manifest.py"},
    {"phase": 132, "test_file": "tests/test_macro_event_news_regime_context_manifest.py"},
    {"phase": 133, "test_file": "tests/test_regime_validation_acceptance_manifest.py"},
    {"phase": 134, "test_file": "tests/test_regime_featurestore_metadata_manifest.py"},
    {"phase": 135, "test_file": "tests/test_phase_126_135_acceptance_manifest.py"},
]


def build_regime_block_test_contract_report(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Audit representative test files across the 10-phase regime block."""
    root = project_root or Path(__file__).resolve().parent.parent
    active = profile or get_regime_acceptance_profile()

    rows = []
    for item in REPRESENTATIVE_REGIME_TESTS:
        target = root / item["test_file"]
        exists = target.is_file()
        rows.append({
            "phase": item["phase"],
            "test_file": item["test_file"],
            "exists": exists,
            "non_signal": True,
            "status_label": ACCEPTANCE_PASS if exists else "acceptance_fail",
        })

    df = pd.DataFrame(rows)
    all_exist = bool(df["exists"].all())
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_TEST_CONTRACT_DOMAIN,
        "active_profile": active.profile_name,
        "total_test_suites_checked": len(df),
        "present_test_suites": int(df["exists"].sum()),
        "all_present": all_exist,
        "non_signal": True,
        "status": "READY" if all_exist else "INCOMPLETE",
    }
    return df, summary


def summarize_regime_block_test_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize test contracts DataFrame."""
    return {
        "total_test_suites": len(df),
        "all_present": bool(df["exists"].all()) if not df.empty and "exists" in df.columns else False,
        "non_signal": True,
    }
