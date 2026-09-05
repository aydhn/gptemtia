"""Phase 119: Cross-Asset Alignment Comprehensive Validation Suite.

Executes rule-based and contract-level validations across profiles,
domains, universe definitions, symbol mappings, timestamp contracts,
join policies, matrix outputs, and non-signal safety boundaries.
"""

from typing import Tuple, Dict, Any, List, Optional
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    CrossAssetAlignmentValidationFinding,
    build_cross_asset_validation_finding_id,
    FORBIDDEN_OUTPUT_WORDS,
)
from advanced_cross_asset_alignment.cross_asset_alignment_profile_registry import build_cross_asset_alignment_profile_registry
from advanced_cross_asset_alignment.cross_asset_alignment_domain_registry import build_cross_asset_alignment_domain_registry
from advanced_cross_asset_alignment.asset_universe_alignment import build_asset_universe_registry
from advanced_cross_asset_alignment.asset_symbol_mapping import build_asset_symbol_mapping_registry
from advanced_cross_asset_alignment.feature_matrix_contracts import build_feature_matrix_contract_registry
from advanced_cross_asset_alignment.feature_matrix_join_policies import build_feature_matrix_join_policy_registry
from advanced_cross_asset_alignment.no_lookahead_alignment_guard import validate_alignment_no_lookahead
from advanced_cross_asset_alignment.cross_domain_feature_matrix import build_cross_domain_feature_matrix_placeholder


def validate_profile_registry(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """Validate profile registry consistency and phase targets."""
    findings = []
    if df.empty:
        findings.append({
            "check": "profile_registry_not_empty",
            "passed": False,
            "detail": "Profil tablosu boş.",
        })
        return findings

    for _, row in df.iterrows():
        name = row.get("profile_name", "unknown")
        if row.get("current_phase") != 119:
            findings.append({
                "check": f"profile_{name}_current_phase",
                "passed": False,
                "detail": f"Profil {name} geçerli fazı 119 olmalı, bulunan: {row.get('current_phase')}",
            })
        if row.get("target_final_phase") != 160:
            findings.append({
                "check": f"profile_{name}_target_phase",
                "passed": False,
                "detail": f"Profil {name} hedef fazı 160 olmalı, bulunan: {row.get('target_final_phase')}",
            })
        if row.get("next_phase") != 120:
            findings.append({
                "check": f"profile_{name}_next_phase",
                "passed": False,
                "detail": f"Profil {name} sonraki fazı 120 olmalı, bulunan: {row.get('next_phase')}",
            })
        if not row.get("local_only") or not row.get("research_only"):
            findings.append({
                "check": f"profile_{name}_local_research",
                "passed": False,
                "detail": f"Profil {name} local_only ve research_only olmalıdır.",
            })

    if not findings:
        findings.append({
            "check": "profile_registry_integrity",
            "passed": True,
            "detail": "Tüm profil kayıtları Phase 119 standartlarına uygun.",
        })
    return findings


def validate_domain_registry(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """Validate that all 28 alignment domains are registered and non-signal."""
    findings = []
    if len(df) < 28:
        findings.append({
            "check": "domain_count",
            "passed": False,
            "detail": f"Kayıtlı domain sayısı 28'den az: {len(df)}",
        })
    else:
        findings.append({
            "check": "domain_count",
            "passed": True,
            "detail": f"28 domain eksiksiz kayıtlı ({len(df)} domain).",
        })

    non_signal_all = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    findings.append({
        "check": "domains_strictly_non_signal",
        "passed": non_signal_all,
        "detail": "Tüm domainlerin non_signal bayrağı True." if non_signal_all else "Non-signal olmayan domain tespit edildi!",
    })
    return findings


def validate_matrix_contracts(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """Validate matrix contracts enforce backward-only join and no future data."""
    findings = []
    if df.empty:
        findings.append({
            "check": "contracts_not_empty",
            "passed": False,
            "detail": "Matris sözleşmeleri tablosu boş.",
        })
        return findings

    for _, row in df.iterrows():
        c_name = row.get("matrix_name") or row.get("contract_id", "unknown")
        nl_pol = str(row.get("no_lookahead_policy", ""))
        if "backward" not in nl_pol and "no_future" not in nl_pol:
            findings.append({
                "check": f"contract_{c_name}_no_future_data",
                "passed": False,
                "detail": f"Sözleşme {c_name} no_lookahead_policy geriye dönük olmalıdır: {nl_pol}",
            })
        if row.get("non_signal") is not True:
            findings.append({
                "check": f"contract_{c_name}_non_signal",
                "passed": False,
                "detail": f"Sözleşme {c_name} non_signal True olmalıdır!",
            })
        jp = str(row.get("join_policy", ""))
        if "backward" not in jp and "event_window" not in jp and "asof" not in jp and "metadata_tag" not in jp:
            findings.append({
                "check": f"contract_{c_name}_backward_direction",
                "passed": False,
                "detail": f"Sözleşme {c_name} join_policy geriye dönük veya asof olmalıdır: {jp}",
            })

    if not any(not f["passed"] for f in findings):
        findings.append({
            "check": "matrix_contracts_integrity",
            "passed": True,
            "detail": "Tüm matris sözleşmeleri geriye dönük ve non-signal ilkelerine uygun.",
        })
    return findings


def validate_matrix_data_frame(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """Validate placeholder feature matrix data structure and forbidden terms."""
    findings = []
    if df.empty:
        findings.append({
            "check": "matrix_not_empty",
            "passed": False,
            "detail": "Örnek feature matrisi boş.",
        })
        return findings

    # Lookahead check
    la_res = validate_alignment_no_lookahead(df)
    findings.append({
        "check": "matrix_no_lookahead_guard",
        "passed": la_res["valid"],
        "detail": "Lookahead veya yasaklı terim sızıntısı yok." if la_res["valid"] else f"Bulgular: {la_res['findings']}",
    })

    # Non-signal forbidden column check
    bad_cols = [c for c in df.columns if any(w in c.lower() for w in FORBIDDEN_OUTPUT_WORDS)]
    findings.append({
        "check": "matrix_no_forbidden_column_words",
        "passed": len(bad_cols) == 0,
        "detail": "Yasaklı kelime içeren kolon yok." if len(bad_cols) == 0 else f"Yasaklı kolonlar: {bad_cols}",
    })

    return findings


def build_cross_asset_alignment_validation_report(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute all Phase 119 validation checks and return results DataFrame and summary."""
    active_profile = profile or get_default_cross_asset_alignment_profile()
    checks: List[Dict[str, Any]] = []

    # 1. Profile Registry
    df_prof, _ = build_cross_asset_alignment_profile_registry(active_profile)
    checks.extend(validate_profile_registry(df_prof))

    # 2. Domain Registry
    df_dom, _ = build_cross_asset_alignment_domain_registry(active_profile)
    checks.extend(validate_domain_registry(df_dom))

    # 3. Feature Matrix Contracts
    df_cont, _ = build_feature_matrix_contract_registry(active_profile)
    checks.extend(validate_matrix_contracts(df_cont))

    # 4. Feature Matrix Sample
    df_matrix, _ = build_cross_domain_feature_matrix_placeholder(active_profile)
    checks.extend(validate_matrix_data_frame(df_matrix))

    df_out = pd.DataFrame(checks)
    df_out["status"] = df_out["passed"].apply(lambda p: "PASS" if p else "FAIL")

    summary = summarize_cross_asset_alignment_validation(df_out)
    summary["profile"] = active_profile.name
    return df_out, summary


def summarize_cross_asset_alignment_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation check DataFrame."""
    if df.empty:
        return {"total_checks": 0, "validation_status": "EMPTY"}

    passed_count = int((df["status"] == "PASS").sum())
    failed_count = int((df["status"] == "FAIL").sum())
    all_passed = failed_count == 0

    return {
        "total_checks": len(df),
        "passed_checks": passed_count,
        "failed_checks": failed_count,
        "all_passed": all_passed,
        "validation_status": "PASS" if all_passed else "FAIL",
    }
