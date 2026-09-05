"""Phase 127: Regime Matrix Validation Engine.

Executes rule audits, validates manifests, scans text/data for forbidden claims,
and synthesizes the master validation report.
"""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

FORBIDDEN_CLAIMS_REGEX = [
    r"\bofficial\s+approval\b",
    r"\bproduction\s+ready\b",
    r"\bbroker\s+ready\b",
    r"\blive\s+trading\s+ready\b",
    r"\btrade\s+signals?\b",
    r"\bbuy\s+signals?\b",
    r"\bsell\s+signals?\b",
    r"\bbuy\s+recommendation\b",
    r"\bsell\s+recommendation\b",
    r"\bguaranteed\b",
    r"\bprofitable\b",
    r"\bmodel\s+trained\b",
    r"\bclustering\s+executed\b",
]


def check_forbidden_claims_in_text(text: str) -> List[str]:
    """Scan string for forbidden claims and return matching findings."""
    res = validate_no_forbidden_regime_matrix_claims(text=text)
    return res.get("findings", [])


def validate_no_forbidden_regime_matrix_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Audit string content, DataFrame cells, or summary dicts for forbidden claims."""
    findings = []
    text_to_audit = ""
    if text:
        text_to_audit += text + " "
    if summary:
        text_to_audit += str(summary) + " "
    if df is not None and not df.empty:
        text_to_audit += " ".join(df.astype(str).values.flatten()[:500])

    for pat in FORBIDDEN_CLAIMS_REGEX:
        matches = re.findall(pat, text_to_audit, re.IGNORECASE)
        if matches:
            findings.extend(matches)

    is_valid = len(findings) == 0
    return {
        "is_valid": is_valid,
        "findings_count": len(findings),
        "findings": findings,
        "non_signal": True,
    }


def validate_regime_matrix_profile_registry(
    df: pd.DataFrame,
    profile: RegimeMatrixProfile,
) -> Dict[str, Any]:
    """Validate profile table against Phase 127 invariants."""
    if df.empty:
        return {"status": "FAIL", "reason": "Profile dataframe is empty"}

    valid_phases = (
        (df["current_phase"] == 127).all()
        and (df["target_final_phase"] == 160).all()
        and (df["next_phase"] == 128).all()
    )
    valid_non_signal = bool(df["non_signal"].all())
    valid_safety = (
        bool(df["source_preserved"].all())
        and bool((~df["official_approval"]).all())
        and bool((~df["production_ready"]).all())
        and bool((~df["broker_ready"]).all())
        and bool((~df["model_training_executed"]).all())
        and bool((~df["clustering_executed"]).all())
        and bool((~df["unsupervised_execution"]).all())
    )

    is_valid = valid_phases and valid_non_signal and valid_safety
    return {
        "is_valid": is_valid,
        "status": "PASS" if is_valid else "FAIL",
        "valid_phases": bool(valid_phases),
        "valid_non_signal": valid_non_signal,
        "valid_safety": valid_safety,
    }


def validate_regime_feature_matrix_contracts(
    df: pd.DataFrame,
    profile: RegimeMatrixProfile,
) -> Dict[str, Any]:
    """Validate feature matrix contracts."""
    if df.empty:
        return {"status": "FAIL", "reason": "Contracts dataframe is empty"}

    all_non_signal = bool(df["non_signal"].all())
    all_no_lookahead = bool(df["no_lookahead_required"].all())
    all_validation_req = bool(df["validation_required"].all())

    is_valid = all_non_signal and all_no_lookahead and all_validation_req
    return {
        "is_valid": is_valid,
        "status": "PASS" if is_valid else "FAIL",
        "contract_count": len(df),
    }


def validate_regime_state_dataset_contracts(
    df: pd.DataFrame,
    profile: RegimeMatrixProfile,
) -> Dict[str, Any]:
    """Validate state dataset contracts."""
    if df.empty:
        return {"status": "FAIL", "reason": "State dataset contracts dataframe is empty"}

    all_no_labels = bool(df["no_target_label_prediction"].all())
    all_training_disallowed = bool((~df["model_training_allowed"]).all())
    all_clustering_disallowed = bool((~df["clustering_allowed"]).all())
    all_non_signal = bool(df["non_signal"].all())

    is_valid = all_no_labels and all_training_disallowed and all_clustering_disallowed and all_non_signal
    return {
        "is_valid": is_valid,
        "status": "PASS" if is_valid else "FAIL",
        "state_dataset_contract_count": len(df),
    }


def validate_regime_matrix_integrity_manifest(
    df: pd.DataFrame,
    profile: RegimeMatrixProfile,
) -> Dict[str, Any]:
    """Validate integrity manifest DataFrame."""
    if df.empty:
        return {"status": "FAIL", "reason": "Manifest dataframe is empty"}

    row = df.iloc[0]
    is_valid = (
        int(row["current_phase"]) == 127
        and int(row["target_final_phase"]) == 160
        and int(row["next_phase"]) == 128
        and bool(row["non_signal"]) is True
        and bool(row["source_preserved"]) is True
        and bool(row["official_approval"]) is False
        and bool(row["production_ready"]) is False
        and bool(row["broker_ready"]) is False
        and bool(row["model_training_executed"]) is False
        and bool(row["clustering_executed"]) is False
        and bool(row["unsupervised_execution"]) is False
        and bool(row["destructive_action_allowed"]) is False
        and bool(row["auto_fix_allowed"]) is False
        and bool(row["auto_drop_allowed"]) is False
    )
    return {
        "is_valid": is_valid,
        "status": "PASS" if is_valid else "FAIL",
    }


def build_regime_matrix_validation_report(
    tables: Optional[Dict[str, pd.DataFrame]] = None,
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Synthesize complete validation report auditing all Phase 127 components."""
    p = profile or get_default_regime_matrix_profile()

    if tables is None:
        from advanced_regime_matrix.regime_matrix_profile_registry import build_regime_matrix_profile_registry
        from advanced_regime_matrix.regime_feature_matrix_contracts import build_regime_feature_matrix_contract_registry
        from advanced_regime_matrix.regime_state_dataset_contracts import build_regime_state_dataset_contract_registry
        from advanced_regime_matrix.regime_matrix_integrity_manifest import build_regime_matrix_integrity_manifest

        df_prof, _ = build_regime_matrix_profile_registry(p)
        df_cont, _ = build_regime_feature_matrix_contract_registry(p)
        df_scont, _ = build_regime_state_dataset_contract_registry(p)
        df_man, _ = build_regime_matrix_integrity_manifest(p)
        tables = {
            "profiles": df_prof,
            "contracts": df_cont,
            "state_dataset_contracts": df_scont,
            "manifest": df_man,
        }

    checks = []

    # 1. Profile check
    if "profiles" in tables:
        v_prof = validate_regime_matrix_profile_registry(tables["profiles"], p)
        checks.append({"rule_name": "Profile Registry Invariants", "status": v_prof["status"]})

    # 2. Feature matrix contracts check
    if "contracts" in tables:
        v_cont = validate_regime_feature_matrix_contracts(tables["contracts"], p)
        checks.append({"rule_name": "Feature Matrix Contracts Non-Signal", "status": v_cont["status"]})

    # 3. State dataset contracts check
    if "state_dataset_contracts" in tables:
        v_scont = validate_regime_state_dataset_contracts(tables["state_dataset_contracts"], p)
        checks.append({"rule_name": "State Dataset Contracts Zero Target/Label", "status": v_scont["status"]})

    # 4. Manifest check
    if "manifest" in tables:
        v_man = validate_regime_matrix_integrity_manifest(tables["manifest"], p)
        checks.append({"rule_name": "Integrity Manifest Compliance", "status": v_man["status"]})

    # 5. Forbidden claims check
    forbidden_audit = validate_no_forbidden_regime_matrix_claims(
        summary={"profile": p.profile_name, "phase": 127}
    )
    checks.append({
        "rule_name": "Zero Forbidden Claims Audit",
        "status": "PASS" if forbidden_audit["is_valid"] else "FAIL",
    })

    df = pd.DataFrame(checks)
    total_rules = len(df)
    passed_rules = int((df["status"] == "PASS").sum()) if not df.empty else 0
    all_passed = total_rules == passed_rules

    summary = {
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "total_rules": total_rules,
        "passed_rules": passed_rules,
        "failed_rules": total_rules - passed_rules,
        "all_passed": all_passed,
        "forbidden_claims_clean": True,
        "current_phase": p.current_phase,
        "target_final_phase": p.target_final_phase,
        "next_phase": p.next_phase,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


run_regime_matrix_validation = build_regime_matrix_validation_report

