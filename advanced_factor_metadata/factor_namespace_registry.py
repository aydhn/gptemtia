"""Phase 122 Factor Namespace Registry.

Enforces deterministic lowercase snake_case naming standards for factors
and guarantees absence of prohibited trading/prediction tokens.
Strictly non-signal and research-only.
"""

import re
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_contract_registry import CORE_FACTOR_CONTRACTS
from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY
from advanced_factor_metadata.factor_metadata_models import FORBIDDEN_FACTOR_TOKENS


def build_factor_name(factor_family: str, factor_name: str) -> str:
    """Construct canonical factor name adhering to namespace standards."""
    clean_family = re.sub(r"^factor_family_", "", factor_family.lower())
    clean_name = re.sub(r"^factor_", "", factor_name.lower())
    clean_name = re.sub(r"[^a-z0-9_]+", "_", clean_name).strip("_")

    if clean_name.startswith(f"{clean_family}_"):
        return f"factor_{clean_name}"
    return f"factor_{clean_family}_{clean_name}"


def validate_factor_name(name: str) -> Dict[str, Any]:
    """Validate factor name conforms to lowercase snake_case and non-signal standards."""
    errors: List[str] = []

    if not name:
        return {"factor_name": name, "is_valid": False, "errors": ["Factor name cannot be empty"]}

    if name != name.lower():
        errors.append(f"Factor name '{name}' must be completely lowercase")

    if not re.match(r"^factor_[a-z0-9_]+$", name):
        errors.append(f"Factor name '{name}' must start with 'factor_' and contain only lowercase letters, digits, and underscores")

    for token in FORBIDDEN_FACTOR_TOKENS:
        if token in name.lower():
            errors.append(f"Factor name '{name}' contains forbidden token '{token}'")

    return {
        "factor_name": name,
        "is_valid": len(errors) == 0,
        "errors": errors,
    }


def build_factor_namespace_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Namespace Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records: List[Dict[str, Any]] = []
    for contract in CORE_FACTOR_CONTRACTS:
        fname = contract["factor_name"]
        ffam = contract["factor_family"]
        canonical_name = build_factor_name(ffam, fname)
        val_res = validate_factor_name(canonical_name)

        records.append(
            {
                "factor_name": fname,
                "canonical_factor_name": canonical_name,
                "factor_family": ffam,
                "is_valid": val_res["is_valid"],
                "validation_errors": val_res["errors"],
                "namespace_prefix": "factor_",
                "non_signal": True,
                "status_label": FACTOR_READY if val_res["is_valid"] else "factor_blocked_by_safety",
            }
        )

    df = pd.DataFrame(records)
    all_valid = all(r["is_valid"] for r in records)

    summary = {
        "active_profile": active_profile.name,
        "total_namespaces": len(records),
        "valid_namespaces": sum(1 for r in records if r["is_valid"]),
        "all_valid": all_valid,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY if all_valid else "factor_namespace_validation_failed",
    }
    return df, summary


def summarize_factor_namespace_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor namespace registry DataFrame."""
    return {
        "total_namespaces": len(df),
        "valid_count": int(df["is_valid"].sum()) if "is_valid" in df else 0,
        "status": "VALID" if ("is_valid" in df and df["is_valid"].all()) else "INVALID",
    }
