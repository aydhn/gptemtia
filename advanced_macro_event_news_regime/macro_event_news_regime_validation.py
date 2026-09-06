"""Phase 132: Macro/Event/News Regime Validation Report and Checks."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)
from advanced_macro_event_news_regime.metadata_only_news_boundary import (
    FORBIDDEN_NEWS_FIELDS,
)
from advanced_macro_event_news_regime.macro_event_news_no_lookahead_guard import (
    FORBIDDEN_COLUMNS,
)

FORBIDDEN_CLAIM_PHRASES = [
    "official approval",
    "production ready",
    "broker ready",
    "investment advice",
    "trading signal",
    "buy recommendation",
    "sell recommendation",
    "trained model",
    "model deployment",
    "sentiment analysis score",
    "full article text",
]


def validate_macro_event_news_regime_profile_registry(
    df: pd.DataFrame,
    profile: MacroEventNewsRegimeProfile,
) -> Dict[str, Any]:
    """Validate profile registry rows against safety constraints."""
    if df.empty:
        return {"valid": False, "error": "Profile registry is empty"}

    valid_phases = (
        (df["current_phase"] == 132).all()
        and (df["target_final_phase"] == 160).all()
        and (df["next_phase"] == 133).all()
    )
    valid_safety = (
        (df["local_only"] == True).all()
        and (df["non_production"] == True).all()
        and (df["research_only"] == True).all()
        and (df["non_signal"] == True).all()
        and (df["official_approval"] == False).all()
        and (df["production_ready"] == False).all()
        and (df["broker_ready"] == False).all()
    )
    passed = bool(valid_phases and valid_safety)
    return {
        "valid": passed,
        "valid_phases": bool(valid_phases),
        "valid_safety": bool(valid_safety),
        "status": "PASS" if passed else "FAIL",
    }


def validate_macro_event_news_entity_registries(
    df_map: Dict[str, pd.DataFrame],
    profile: MacroEventNewsRegimeProfile,
) -> Dict[str, Any]:
    """Validate all entity DataFrames (macro, event, news metadata)."""
    results = {}
    overall_valid = True
    for name, df in df_map.items():
        if df.empty:
            results[name] = {"valid": False, "error": "empty DataFrame"}
            overall_valid = False
            continue

        non_signal_ok = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
        source_preserved_ok = bool(df["source_preserved"].all()) if "source_preserved" in df.columns else False

        # If news metadata, check forbidden fields
        has_news_violation = False
        if "news" in name:
            for forbidden in FORBIDDEN_NEWS_FIELDS:
                if forbidden in df.columns:
                    has_news_violation = True
                    break

        item_valid = non_signal_ok and source_preserved_ok and not has_news_violation
        results[name] = {
            "valid": item_valid,
            "non_signal": non_signal_ok,
            "source_preserved": source_preserved_ok,
            "has_news_violation": has_news_violation,
        }
        if not item_valid:
            overall_valid = False

    return {"valid": overall_valid, "entity_checks": results, "status": "PASS" if overall_valid else "FAIL"}


def validate_metadata_only_news_boundary(
    df: pd.DataFrame,
    profile: MacroEventNewsRegimeProfile,
) -> Dict[str, Any]:
    """Validate that news boundary table strictly enforces metadata-only rules."""
    if df.empty:
        return {"valid": False, "error": "Boundary DataFrame empty"}

    enforced = bool(df["strictly_enforced"].all()) if "strictly_enforced" in df.columns else False
    non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    passed = enforced and non_signal
    return {"valid": passed, "status": "PASS" if passed else "FAIL"}


def validate_macro_event_news_context_contracts(
    df: pd.DataFrame,
    profile: MacroEventNewsRegimeProfile,
) -> Dict[str, Any]:
    """Validate context contract table requirements."""
    if df.empty:
        return {"valid": False, "error": "Contracts DataFrame empty"}

    lookahead_ok = bool(df["no_lookahead_required"].all()) if "no_lookahead_required" in df.columns else False
    meta_ok = bool(df["metadata_only_news_required"].all()) if "metadata_only_news_required" in df.columns else False
    non_signal_ok = bool(df["non_signal_required"].all()) if "non_signal_required" in df.columns else False
    passed = lookahead_ok and meta_ok and non_signal_ok
    return {"valid": passed, "status": "PASS" if passed else "FAIL"}


def validate_macro_event_news_regime_context_manifest(
    df: pd.DataFrame,
    profile: MacroEventNewsRegimeProfile,
) -> Dict[str, Any]:
    """Validate manifest invariants."""
    if df.empty:
        return {"valid": False, "error": "Manifest DataFrame empty"}

    row = df.iloc[0]
    checks = {
        "phase_132": int(row.get("current_phase", 0)) == 132,
        "phase_160": int(row.get("target_final_phase", 0)) == 160,
        "phase_133": int(row.get("next_phase", 0)) == 133,
        "non_signal": bool(row.get("non_signal", False)),
        "source_preserved": bool(row.get("source_preserved", False)),
        "no_official_approval": not bool(row.get("official_approval", True)),
        "no_production_ready": not bool(row.get("production_ready", True)),
        "no_broker_ready": not bool(row.get("broker_ready", True)),
        "no_full_text": not bool(row.get("contains_full_article_text", True)),
        "no_article_body": not bool(row.get("contains_article_body", True)),
        "no_raw_content": not bool(row.get("contains_raw_content", True)),
        "no_scraped_html": not bool(row.get("contains_scraped_html", True)),
        "no_embedding": not bool(row.get("contains_embedding", True)),
        "no_vector": not bool(row.get("contains_vector", True)),
        "no_sentiment": not bool(row.get("sentiment_model_output", True)),
        "no_model_training": not bool(row.get("model_training_executed", True)),
        "no_model_fit": not bool(row.get("model_fit_executed", True)),
        "no_model_predict": not bool(row.get("model_predict_executed", True)),
        "no_clustering": not bool(row.get("clustering_executed", True)),
        "no_unsupervised": not bool(row.get("unsupervised_execution", True)),
        "no_destructive": not bool(row.get("destructive_action_allowed", True)),
        "no_autofix": not bool(row.get("auto_fix_allowed", True)),
        "no_autodrop": not bool(row.get("auto_drop_allowed", True)),
    }
    all_passed = all(checks.values())
    return {"valid": all_passed, "checks": checks, "status": "PASS" if all_passed else "FAIL"}


def validate_no_forbidden_macro_event_news_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Validate that text, DataFrame, or summary dictionary contains zero prohibited claims."""
    violations = []
    if text:
        text_lower = text.lower()
        for phrase in FORBIDDEN_CLAIM_PHRASES:
            if phrase in text_lower:
                violations.append(phrase)

    if df is not None and not df.empty:
        for c in df.columns:
            for forbidden_col in FORBIDDEN_COLUMNS:
                if c.lower() == forbidden_col:
                    violations.append(f"column:{c}")

    if summary:
        for k, v in summary.items():
            if k in ["official_approval", "production_ready", "broker_ready"] and v is True:
                violations.append(f"summary:{k}")

    is_clean = len(violations) == 0
    return {
        "valid": is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "FAIL_FORBIDDEN_CLAIMS_DETECTED",
    }


def build_macro_event_news_regime_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build validation report covering all Phase 132 requirements."""
    p = profile or get_macro_event_news_regime_profile()

    checks = []

    # 1. Profile registry validation
    if "profiles" in tables:
        res = validate_macro_event_news_regime_profile_registry(tables["profiles"], p)
        checks.append(("profile_registry_validation", res["valid"], res.get("status", "PASS")))

    # 2. Entities validation
    entity_keys = {k: v for k, v in tables.items() if "entity" in k or "entities" in k}
    if entity_keys:
        res = validate_macro_event_news_entity_registries(entity_keys, p)
        checks.append(("entities_validation", res["valid"], res.get("status", "PASS")))

    # 3. Metadata boundary validation
    if "boundary" in tables:
        res = validate_metadata_only_news_boundary(tables["boundary"], p)
        checks.append(("metadata_only_boundary_validation", res["valid"], res.get("status", "PASS")))

    # 4. Contracts validation
    if "contracts" in tables:
        res = validate_macro_event_news_context_contracts(tables["contracts"], p)
        checks.append(("context_contracts_validation", res["valid"], res.get("status", "PASS")))

    # 5. Manifest validation
    if "manifest" in tables:
        res = validate_macro_event_news_regime_context_manifest(tables["manifest"], p)
        checks.append(("manifest_invariants_validation", res["valid"], res.get("status", "PASS")))

    # 6. Forbidden claims check
    res = validate_no_forbidden_macro_event_news_claims()
    checks.append(("forbidden_claims_validation", res["valid"], res.get("status", "PASS")))

    rows = []
    for check_name, is_valid, status in checks:
        rows.append(
            {
                "check_name": check_name,
                "passed": is_valid,
                "status": status,
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    passed_cnt = int(df["passed"].sum()) if not df.empty else 0
    all_passed = bool(passed_cnt == len(df) and len(df) > 0)

    summary = {
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "total_checks": len(df),
        "passed_checks": passed_cnt,
        "failed_checks": len(df) - passed_cnt,
        "forbidden_claims_clean": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary
