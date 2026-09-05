from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.no_lookahead_alignment_guard import (
    validate_no_forbidden_alignment_columns,
    FORBIDDEN_COLUMNS,
)
from advanced_cross_asset_alignment.cross_domain_feature_namespace import validate_namespaced_feature_name


VALIDATION_RULES_CONFIG: List[Dict[str, Any]] = [
    {
        "rule_id": "rule_forbidden_columns",
        "rule_name": "Forbidden Column Name Rule",
        "description": "Matriste signal, buy, sell, long, short, target, label, prediction gibi kelimelerin bulunmasını yasaklar.",
        "severity": "CRITICAL",
        "is_active": True,
    },
    {
        "rule_id": "rule_timestamp_order",
        "rule_name": "Timestamp Monotonic Order Rule",
        "description": "Zaman damgasının kronolojik artan sırada olmasını ve geleceğe sıçrama içermemesini denetler.",
        "severity": "CRITICAL",
        "is_active": True,
    },
    {
        "rule_id": "rule_namespace_conformance",
        "rule_name": "Cross-Domain Namespace Conformance Rule",
        "description": "Hizalanmış feature sütunlarının domain ön eki ve geçerli slug kurallarına uymasını denetler.",
        "severity": "HIGH",
        "is_active": True,
    },
    {
        "rule_id": "rule_no_future_leakage",
        "rule_name": "No Future Leakage Rule",
        "description": "Asof veya join işleminde sağ taraf verisinin sol taraf barından sonraki tarihe ait olmamasını sağlar.",
        "severity": "CRITICAL",
        "is_active": True,
    },
    {
        "rule_id": "rule_metadata_only_news",
        "rule_name": "Metadata-Only News Boundary Rule",
        "description": "Haber verilerinde metin, özet veya telifli içerik bulunmadığını, yalnızca etiket/sayı olduğunu doğrular.",
        "severity": "CRITICAL",
        "is_active": True,
        "enforced": True,
    },
    {
        "rule_id": "rule_backward_only_asof",
        "rule_name": "Backward-Only Asof Join Rule",
        "description": "Zaman serisi asof birleştirmelerinde yalnızca backward yönüne izin verir; forward veya nearest yasaktır.",
        "severity": "CRITICAL",
        "is_active": True,
        "enforced": True,
    },
    {
        "rule_id": "rule_non_mutation_guarantee",
        "rule_name": "DataFrame Non-Mutation Guarantee Rule",
        "description": "Hizalama operasyonlarının girdi verilerini mutasyona uğratmadan df.copy() ile çalışmasını sağlar.",
        "severity": "CRITICAL",
        "is_active": True,
        "enforced": True,
    },
    {
        "rule_id": "rule_dry_run_local_safety",
        "rule_name": "Dry-Run Local Offline Boundary Rule",
        "description": "Canlı emir, ağ aramaları ve üretim dağıtımı engellerini denetler.",
        "severity": "CRITICAL",
        "is_active": True,
        "enforced": True,
    },
]

VALIDATION_RULES = VALIDATION_RULES_CONFIG



def validate_cross_asset_forbidden_columns(df: pd.DataFrame) -> Dict[str, Any]:
    return validate_no_forbidden_alignment_columns(df)


def validate_cross_asset_timestamp_order(df: pd.DataFrame, base_ts: str, context_ts: str) -> Dict[str, Any]:
    issues = []
    if base_ts not in df.columns:
        issues.append(f"base_ts sütunu '{base_ts}' bulunamadı.")
    if context_ts not in df.columns:
        issues.append(f"context_ts sütunu '{context_ts}' bulunamadı.")

    if issues:
        return {"is_valid": False, "issues": issues}

    base_series = pd.to_datetime(df[base_ts], utc=True)
    ctx_series = pd.to_datetime(df[context_ts], utc=True)

    # In backward join context_ts must be <= base_ts for all non-null values
    diff = ctx_series - base_series
    future_rows = (diff > pd.Timedelta(0)).sum()
    if future_rows > 0:
        issues.append(f"{future_rows} satırda context_ts > base_ts tespit edildi (geleceğe bakış sızıntısı!).")

    return {
        "is_valid": len(issues) == 0,
        "future_rows_count": int(future_rows),
        "issues": issues,
    }


def validate_cross_asset_namespace(df: pd.DataFrame, feature_columns: List[str]) -> Dict[str, Any]:
    invalid_cols = []
    for col in feature_columns:
        if col in df.columns:
            res = validate_namespaced_feature_name(col)
            if not res["is_valid"]:
                invalid_cols.append({"column": col, "issues": res["issues"]})

    return {
        "is_valid": len(invalid_cols) == 0,
        "invalid_columns": invalid_cols,
    }


def validate_cross_asset_alignment_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    issues = []
    # 1. Check forbidden columns
    forbidden_res = validate_cross_asset_forbidden_columns(df)
    if not forbidden_res["is_valid"]:
        issues.extend(forbidden_res["issues"])

    # 2. Check timestamps if present
    if "normalized_timestamp" in df.columns:
        ts_series = pd.to_datetime(df["normalized_timestamp"], utc=True)
        if not ts_series.is_monotonic_increasing:
            issues.append("normalized_timestamp sütunu kronolojik artan sırada değil.")

    return {
        "is_valid": len(issues) == 0,
        "issues": issues,
        "row_count": len(df),
        "column_count": len(df.columns),
    }


def build_cross_asset_alignment_validation_rule_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(VALIDATION_RULES_CONFIG)
    summary = summarize_cross_asset_alignment_validation_rules(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_cross_asset_alignment_validation_rules(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_rules": 0, "status": "EMPTY"}

    all_active = bool(df["is_active"].all()) if "is_active" in df.columns else False
    return {
        "total_rules": len(df),
        "rule_ids": list(df["rule_id"]) if "rule_id" in df.columns else [],
        "all_rules_active": all_active,
        "all_enforced": all_active,
        "non_signal": True,
        "status": "READY" if all_active else "INCOMPLETE",
    }

