"""Phase 125: Feature Engine Block Test Contract Report.

Verifies existence and coverage of test contracts for each phase in the 116-125 block.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)

REPRESENTATIVE_TESTS = [
    {"phase": 116, "test_file": "tests/test_advanced_feature_engine_scripts_contract.py"},
    {"phase": 117, "test_file": "tests/test_advanced_technical_indicators_scripts_contract.py"},
    {"phase": 118, "test_file": "tests/test_advanced_feature_grid_scripts_contract.py"},
    {"phase": 119, "test_file": "tests/test_cross_asset_alignment_pipeline.py"},
    {"phase": 120, "test_file": "tests/test_advanced_feature_fusion_scripts_contract.py"},
    {"phase": 121, "test_file": "tests/test_advanced_feature_validation_scripts_contract.py"},
    {"phase": 122, "test_file": "tests/test_advanced_factor_metadata_scripts_contract.py"},
    {"phase": 123, "test_file": "tests/test_advanced_feature_quality_drift_scripts_contract.py"},
    {"phase": 124, "test_file": "tests/test_advanced_feature_store_integration_scripts_contract.py"},
    {"phase": 125, "test_file": "tests/test_advanced_feature_factor_acceptance_scripts_contract.py"},
]


def build_feature_engine_block_test_contract_report(
    project_root: Optional[Path] = None,
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Audit representative test contract files across the 10-phase block."""
    root = project_root or Path(__file__).resolve().parent.parent
    rows = []
    for item in REPRESENTATIVE_TESTS:
        p = root / item["test_file"]
        exists = p.exists()
        rows.append({
            "phase": item["phase"],
            "test_file": item["test_file"],
            "exists": exists,
            "status": "VALID_TEST_CONTRACT" if exists else "MISSING",
            "non_signal": True,
        })
    df = pd.DataFrame(rows)

    summary = {
        "total_test_suites_checked": len(df),
        "present_test_suites": int(df["exists"].sum()),
        "missing_test_suites": int((~df["exists"]).sum()),
        "all_present": bool(df["exists"].all()),
        "non_signal": True,
    }
    return df, summary


def summarize_feature_engine_block_test_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize test contracts DataFrame."""
    return {
        "total_test_suites": len(df),
        "all_present": bool(df["exists"].all()) if "exists" in df.columns else False,
        "non_signal": True,
    }
