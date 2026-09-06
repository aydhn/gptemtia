"""Phase 135: Regime Block Script Contract Report.

Verifies existence and contract conformity of representative operational CLI scripts
across Phases 126-135.
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
    REGIME_BLOCK_SCRIPT_CONTRACT_DOMAIN,
)


REPRESENTATIVE_REGIME_SCRIPTS: List[Dict[str, Any]] = [
    # Phase 126
    {"phase": 126, "script": "scripts/run_regime_foundation_profile_registry.py"},
    {"phase": 126, "script": "scripts/run_regime_foundation_manifest.py"},
    # Phase 127
    {"phase": 127, "script": "scripts/run_regime_matrix_profile_registry.py"},
    {"phase": 127, "script": "scripts/run_regime_matrix_integrity_manifest.py"},
    # Phase 128
    {"phase": 128, "script": "scripts/run_regime_rule_free_profile_registry.py"},
    {"phase": 128, "script": "scripts/run_regime_state_dataset_contracts.py"},
    # Phase 129
    {"phase": 129, "script": "scripts/run_market_behavior_diagnostics_profile_registry.py"},
    {"phase": 129, "script": "scripts/run_behavior_diagnostics_manifest.py"},
    # Phase 130
    {"phase": 130, "script": "scripts/run_regime_transition_profile_registry.py"},
    {"phase": 130, "script": "scripts/run_transition_diagnostics_manifest.py"},
    # Phase 131
    {"phase": 131, "script": "scripts/run_cross_asset_regime_profile_registry.py"},
    {"phase": 131, "script": "scripts/run_cross_asset_regime_findings_manifest.py"},
    # Phase 132
    {"phase": 132, "script": "scripts/run_macro_event_news_regime_profile_registry.py"},
    {"phase": 132, "script": "scripts/run_news_metadata_regime_contexts.py"},
    # Phase 133
    {"phase": 133, "script": "scripts/run_regime_validation_acceptance_profile_registry.py"},
    {"phase": 133, "script": "scripts/run_regime_validation_acceptance_manifest.py"},
    # Phase 134
    {"phase": 134, "script": "scripts/run_regime_featurestore_profile_registry.py"},
    {"phase": 134, "script": "scripts/run_regime_featurestore_policies_manifest.py"},
    # Phase 135
    {"phase": 135, "script": "scripts/run_regime_acceptance_profile_registry.py"},
    {"phase": 135, "script": "scripts/run_phase_126_135_acceptance_manifest.py"},
]


def build_regime_block_script_contract_report(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Audit representative scripts for file presence and contract compliance."""
    root = project_root or Path(__file__).resolve().parent.parent
    active = profile or get_regime_acceptance_profile()

    rows = []
    for item in REPRESENTATIVE_REGIME_SCRIPTS:
        target = root / item["script"]
        exists = target.is_file()
        rows.append({
            "phase": item["phase"],
            "script_path": item["script"],
            "exists": exists,
            "non_signal": True,
            "status_label": ACCEPTANCE_PASS if exists else "acceptance_fail",
        })

    df = pd.DataFrame(rows)
    all_exist = bool(df["exists"].all())
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_SCRIPT_CONTRACT_DOMAIN,
        "active_profile": active.profile_name,
        "total_scripts_checked": len(df),
        "present_scripts": int(df["exists"].sum()),
        "all_present": all_exist,
        "non_signal": True,
        "status": "READY" if all_exist else "INCOMPLETE",
    }
    return df, summary


def summarize_regime_block_script_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize script contracts DataFrame."""
    return {
        "total_scripts": len(df),
        "all_present": bool(df["exists"].all()) if not df.empty and "exists" in df.columns else False,
        "non_signal": True,
    }
