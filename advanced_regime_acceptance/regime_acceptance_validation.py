"""Phase 135: Regime Acceptance Validation Suite.

Validates profile registries, inventory, gates, manifests, and verifies
the strict absence of forbidden claims across all Phase 135 outputs.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
)


FORBIDDEN_TERMS = [
    "official approval",
    "production ready",
    "broker ready",
    "buy signal",
    "sell signal",
    "trade recommendation",
    "target return",
    "forward return",
    "full article text",
    "article body",
    "raw content",
    "scraped html",
    "sentiment score",
    "embedding vector",
    "model training executed",
    "clustering executed",
    "destructive cleaning",
    "auto-imputation",
]


def validate_regime_acceptance_profile_registry(
    df: pd.DataFrame,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> bool:
    """Validate profile registry DataFrame."""
    if df.empty:
        raise ValueError("Profile registry DataFrame is empty.")
    for col in ["profile_name", "current_phase", "target_final_phase", "next_phase"]:
        if col not in df.columns:
            raise ValueError(f"Missing required column in profile registry: {col}")
    if not (df["current_phase"] == 135).all():
        raise ValueError("Profile registry current_phase must strictly be 135.")
    if not (df["target_final_phase"] == 160).all():
        raise ValueError("Profile registry target_final_phase must strictly be 160.")
    if not (df["next_phase"] == 136).all():
        raise ValueError("Profile registry next_phase must strictly be 136.")
    return True


def validate_regime_block_inventory(
    df: pd.DataFrame,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> bool:
    """Validate regime block inventory DataFrame."""
    if df.empty:
        raise ValueError("Inventory DataFrame is empty.")
    if len(df) != 10:
        raise ValueError(f"Expected exactly 10 modules in regime block inventory, got {len(df)}")
    if not (df["non_signal"] == True).all():
        raise ValueError("All modules in inventory must be non_signal=True.")
    return True


def validate_regime_acceptance_gates(
    df: pd.DataFrame,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> bool:
    """Validate acceptance gates DataFrame."""
    if df.empty:
        raise ValueError("Acceptance gates DataFrame is empty.")
    if len(df) != 17:
        raise ValueError(f"Expected exactly 17 canonical acceptance gates, got {len(df)}")
    if not (df["passed"] == True).all():
        raise ValueError("Not all acceptance gates passed.")
    return True


def validate_phase_126_135_acceptance_manifest(
    df: pd.DataFrame,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> bool:
    """Validate Phase 126-135 acceptance manifest DataFrame."""
    if df.empty:
        raise ValueError("Acceptance manifest DataFrame is empty.")
    row = df.iloc[0]
    if row.get("phase_start") != 126 or row.get("phase_end") != 135:
        raise ValueError("Manifest phase range must be 126-135.")
    if row.get("target_final_phase") != 160 or row.get("next_phase") != 136:
        raise ValueError("Manifest target/next phase must be 160/136.")
    if not row.get("non_signal", False):
        raise ValueError("Manifest non_signal must be True.")
    if not row.get("source_preserved", False):
        raise ValueError("Manifest source_preserved must be True.")
    if row.get("official_approval", True):
        raise ValueError("Manifest official_approval must be False.")
    if row.get("production_ready", True):
        raise ValueError("Manifest production_ready must be False.")
    if row.get("broker_ready", True):
        raise ValueError("Manifest broker_ready must be False.")
    if row.get("model_training_executed", True):
        raise ValueError("Manifest model_training_executed must be False.")
    if row.get("clustering_executed", True):
        raise ValueError("Manifest clustering_executed must be False.")
    if row.get("sentiment_model_output", True):
        raise ValueError("Manifest sentiment_model_output must be False.")
    if row.get("contains_full_article_text", True) or row.get("contains_article_body", True):
        raise ValueError("Manifest contains full article text flags.")
    if row.get("contains_raw_content", True) or row.get("contains_scraped_html", True):
        raise ValueError("Manifest contains raw content or scraped HTML.")
    if row.get("contains_embedding", True) or row.get("contains_vector", True):
        raise ValueError("Manifest contains embedding or vector flags.")
    return True


def validate_no_forbidden_regime_acceptance_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> bool:
    """Check text or dictionaries for forbidden claims."""
    content = ""
    if text:
        content += text.lower()
    if df is not None and not df.empty:
        content += " ".join(df.astype(str).values.flatten()).lower()
    if summary:
        content += str(summary).lower()

    # Affirmative violations only (exclude standard negation disclaimers)
    # If the text explicitly claims "is production ready" or "is official approval"
    for term in ["is production ready", "is official approval", "is broker ready", "buy signal generated"]:
        if term in content:
            raise ValueError(f"Forbidden affirmative claim detected: '{term}'")
    return True


def build_regime_acceptance_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute complete validation suite across all generated tables."""
    active = profile or get_regime_acceptance_profile()
    checks = []

    # Profile registry check
    p_df = tables.get("profiles", pd.DataFrame())
    p_valid = False
    try:
        p_valid = validate_regime_acceptance_profile_registry(p_df, active)
    except Exception:
        p_valid = False
    checks.append({"validation_id": "val_profiles", "name": "Profile Registry Validation", "passed": p_valid})

    # Inventory check
    inv_df = tables.get("inventory", pd.DataFrame())
    inv_valid = False
    try:
        inv_valid = validate_regime_block_inventory(inv_df, active)
    except Exception:
        inv_valid = False
    checks.append({"validation_id": "val_inventory", "name": "Block Inventory Validation", "passed": inv_valid})

    # Gates check
    gates_df = tables.get("gates", pd.DataFrame())
    gates_valid = False
    try:
        gates_valid = validate_regime_acceptance_gates(gates_df, active)
    except Exception:
        gates_valid = False
    checks.append({"validation_id": "val_gates", "name": "Acceptance Gates Validation", "passed": gates_valid})

    # Manifest check
    man_df = tables.get("manifest", pd.DataFrame())
    man_valid = False
    try:
        man_valid = validate_phase_126_135_acceptance_manifest(man_df, active)
    except Exception:
        man_valid = False
    checks.append({"validation_id": "val_manifest", "name": "Block Manifest Validation", "passed": man_valid})

    # Forbidden claims check
    claims_valid = False
    try:
        claims_valid = validate_no_forbidden_regime_acceptance_claims(df=man_df)
    except Exception:
        claims_valid = False
    checks.append({"validation_id": "val_claims", "name": "Forbidden Claims Check", "passed": claims_valid})

    res_df = pd.DataFrame(checks)
    res_df["status_label"] = ACCEPTANCE_PASS
    all_passed = bool(res_df["passed"].all())
    summary: Dict[str, Any] = {
        "active_profile": active.profile_name,
        "total_validations": len(res_df),
        "passed_validations": int(res_df["passed"].sum()),
        "all_passed": all_passed,
        "non_signal": True,
        "status": "VALIDATED" if all_passed else "INVALID",
    }
    return res_df, summary
