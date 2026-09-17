# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Validation.

Validates the full set of final delivery registries, contracts, evidence,
boundaries, manifests, and claims against strict Phase 160 safety invariants.
"""

from typing import Dict, Optional, Tuple, Union
import re
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_VALIDATION_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def validate_final_delivery_profile_registry(
    df: pd.DataFrame,
    profile: FinalDeliveryProfile | None = None,
) -> dict:
    """Validate profile registry DataFrame."""
    active_profile = profile or get_default_final_delivery_profile()
    errors = []
    if df.empty:
        errors.append("Profile registry is empty")
    if "current_phase" in df.columns and not (df["current_phase"] == 160).all():
        errors.append("All profiles must have current_phase == 160")
    if "target_final_phase" in df.columns and not (df["target_final_phase"] == 160).all():
        errors.append("All profiles must have target_final_phase == 160")
    if "next_phase" in df.columns and not df["next_phase"].isna().all():
        errors.append("All profiles must have next_phase == None")
    if "allow_live_trading" in df.columns and df["allow_live_trading"].any():
        errors.append("allow_live_trading must be False across all profiles")

    passed = len(errors) == 0
    return {"check": "profile_registry_validation", "passed": passed, "errors": errors}


def validate_final_delivery_package_contracts(
    df: pd.DataFrame,
    profile: FinalDeliveryProfile | None = None,
) -> dict:
    """Validate package contracts DataFrame."""
    errors = []
    if df.empty:
        errors.append("Package contract registry is empty")
    if "system_execution_allowed" in df.columns and df["system_execution_allowed"].any():
        errors.append("system_execution_allowed must be False")
    if "live_trading_allowed" in df.columns and df["live_trading_allowed"].any():
        errors.append("live_trading_allowed must be False")
    if "broker_execution_allowed" in df.columns and df["broker_execution_allowed"].any():
        errors.append("broker_execution_allowed must be False")
    if "manual_review_required" in df.columns and not df["manual_review_required"].all():
        errors.append("manual_review_required must be True for all contracts")

    passed = len(errors) == 0
    return {"check": "package_contracts_validation", "passed": passed, "errors": errors}


def validate_final_delivery_evidence(
    df_map: Dict[str, pd.DataFrame],
    profile: FinalDeliveryProfile | None = None,
) -> dict:
    """Validate that evidence registries exist and are non-empty."""
    errors = []
    for k, df in df_map.items():
        if df is None or df.empty:
            errors.append(f"Evidence table '{k}' is empty or missing")

    passed = len(errors) == 0
    return {"check": "evidence_validation", "passed": passed, "errors": errors}


def validate_final_delivery_boundaries(
    df_map: Dict[str, pd.DataFrame],
    profile: FinalDeliveryProfile | None = None,
) -> dict:
    """Validate boundary registries enforce strict prohibitions."""
    errors = []
    no_go_df = df_map.get("no_go")
    if no_go_df is None or no_go_df.empty:
        errors.append("No-go boundary registry is empty")
    elif "strictly_prohibited" in no_go_df.columns and not no_go_df["strictly_prohibited"].all():
        errors.append("All no-go rules must be strictly prohibited")

    passed = len(errors) == 0
    return {"check": "boundary_validation", "passed": passed, "errors": errors}


def validate_final_delivery_manifest(
    df: pd.DataFrame,
    profile: FinalDeliveryProfile | None = None,
) -> dict:
    """Validate master manifest DataFrame satisfies Phase 160 completion rules."""
    errors = []
    if df.empty:
        errors.append("Manifest DataFrame is empty")
        return {"check": "manifest_validation", "passed": False, "errors": errors}

    row = df.iloc[0]
    if row.get("current_phase") != 160:
        errors.append("current_phase must be 160")
    if row.get("target_final_phase") != 160:
        errors.append("target_final_phase must be 160")
    if row.get("next_phase") is not None and not pd.isna(row.get("next_phase")):
        errors.append("next_phase must be None")
    if not row.get("phase_160_completed", False):
        errors.append("phase_160_completed must be True")
    if not row.get("final_plan_closed", False):
        errors.append("final_plan_closed must be True")
    if not row.get("full_advanced_bot_final_delivery_completed", False):
        errors.append("full_advanced_bot_final_delivery_completed must be True")
    if not row.get("final_delivery_contract_ready", False):
        errors.append("final_delivery_contract_ready must be True")
    if row.get("production_ready", True):
        errors.append("production_ready must be False")
    if row.get("broker_ready", True):
        errors.append("broker_ready must be False")
    if row.get("live_trading_ready", True):
        errors.append("live_trading_ready must be False")
    if row.get("official_approval", True):
        errors.append("official_approval must be False")
    if row.get("system_executed", True):
        errors.append("system_executed must be False")
    if row.get("end_to_end_run_executed", True):
        errors.append("end_to_end_run_executed must be False")
    if row.get("release_deployed", True):
        errors.append("release_deployed must be False")
    if row.get("production_deployed", True):
        errors.append("production_deployed must be False")
    if row.get("broker_execution_executed", True):
        errors.append("broker_execution_executed must be False")
    if row.get("signal_generation_executed", True):
        errors.append("signal_generation_executed must be False")
    if row.get("model_training_executed", True):
        errors.append("model_training_executed must be False")
    if row.get("prediction_generated", True):
        errors.append("prediction_generated must be False")
    if row.get("artifact_persisted", True):
        errors.append("artifact_persisted must be False")
    if row.get("model_registry_written", True):
        errors.append("model_registry_written must be False")

    passed = len(errors) == 0
    return {"check": "manifest_validation", "passed": passed, "errors": errors}


def validate_no_forbidden_final_delivery_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[dict] = None,
) -> dict:
    """Validate that text, dataframe, or summary contains zero forbidden claims."""
    forbidden_terms = [
        r"\blive[_\s-]?trading[_\s-]?ready\b",
        r"\bproduction[_\s-]?ready[_\s-]?approved\b",
        r"\bbroker[_\s-]?ready[_\s-]?approved\b",
        r"\bofficial[_\s-]?approval[_\s-]?granted\b",
        r"\btrading[_\s-]?signal[_\s-]?active\b",
        r"\bbuy[_\s-]?recommendation\b",
        r"\bsell[_\s-]?recommendation\b",
    ]

    target_content = ""
    if text:
        target_content += text + " "
    if df is not None:
        target_content += " ".join(df.astype(str).values.flatten()) + " "
    if summary:
        target_content += " ".join(str(v) for v in summary.values()) + " "

    target_lower = target_content.lower()
    matches = []
    for pat in forbidden_terms:
        if re.search(pat, target_lower):
            matches.append(pat)

    passed = len(matches) == 0
    return {
        "check": "forbidden_claims_validation",
        "passed": passed,
        "matches": matches,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if passed else "FORBIDDEN_CLAIMS_DETECTED",
    }


def build_final_delivery_validation_report(
    tables: Optional[dict] = None,
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build consolidated validation report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()
    tbls = tables or {}

    checks = []
    if "profiles" in tbls:
        checks.append(validate_final_delivery_profile_registry(tbls["profiles"], active_profile))
    if "package_contracts" in tbls:
        checks.append(validate_final_delivery_package_contracts(tbls["package_contracts"], active_profile))
    if "evidence" in tbls:
        checks.append(validate_final_delivery_evidence(tbls["evidence"], active_profile))
    if "boundaries" in tbls:
        checks.append(validate_final_delivery_boundaries(tbls["boundaries"], active_profile))
    if "manifest" in tbls:
        checks.append(validate_final_delivery_manifest(tbls["manifest"], active_profile))

    # General forbidden claims check across provided tables
    checks.append(validate_no_forbidden_final_delivery_claims(summary=tbls.get("summary")))

    rows = []
    for c in checks:
        rows.append({
            "check_name": c["check"],
            "passed": c["passed"],
            "errors": ", ".join(c.get("errors", [])) if not c["passed"] else "None",
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_VALIDATION_DOMAIN,
            "status": "PASS" if c["passed"] else "FAIL",
        })

    df = pd.DataFrame(rows)
    all_passed = bool(df["passed"].all())
    summary = {
        "active_profile": active_profile.profile_name,
        "total_checks": len(rows),
        "passed_checks": int(df["passed"].sum()),
        "failed_checks": int((~df["passed"]).sum()),
        "all_passed": all_passed,
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if all_passed else "VALIDATION_FAILED",
    }
    return df, summary
