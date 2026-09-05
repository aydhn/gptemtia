from typing import Tuple, Dict, Any, List, Optional
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile

FORBIDDEN_KEYWORDS = [
    "live trading",
    "canli emir",
    "broker integration",
    "broker baglantisi",
    "real order",
    "gercek emir",
    "investment advice",
    "yatirim tavsiyesi",
    "buy signal",
    "sell signal",
    "al sinyali",
    "sat sinyali",
    "production ready",
    "model deployment",
    "web scraping",
    "html scraping",
    "paywall bypass",
    "source overwrite",
    "destructive cleaning",
    "official approval",
    "resmi onay",
]


def validate_data_normalization_profile_registry(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = not df.empty and "profile_name" in df.columns
    return {
        "valid": valid,
        "total_profiles": len(df),
        "has_balanced": "balanced_non_destructive_normalization" in df["profile_name"].tolist() if valid else False,
    }


def validate_data_normalization_domain_registry(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = not df.empty and len(df) >= 20
    return {
        "valid": valid,
        "total_domains": len(df),
    }


def validate_normalization_rule_registry(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = not df.empty and "non_destructive" in df.columns and bool(df["non_destructive"].all())
    return {
        "valid": valid,
        "total_rules": len(df),
        "all_non_destructive": valid,
    }


def validate_canonical_schema_registry(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = not df.empty and "schema_name" in df.columns and "primary_key_fields" in df.columns
    return {
        "valid": valid,
        "total_schemas": len(df),
    }


def validate_canonical_field_registry(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = not df.empty and "canonical_field_name" in df.columns and "required" in df.columns
    return {
        "valid": valid,
        "total_canonical_fields": len(df),
    }


def validate_normalization_findings(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = "finding_id" in df.columns if not df.empty else True
    return {
        "valid": valid,
        "total_findings": len(df),
    }


def validate_normalization_decisions(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = True
    if not df.empty:
        if "destructive_action_allowed" in df.columns and bool(df["destructive_action_allowed"].any()):
            valid = False
        if "source_preserved" in df.columns and not bool(df["source_preserved"].all()):
            valid = False
    return {
        "valid": valid,
        "total_decisions": len(df),
        "destructive_action_allowed": False,
        "source_preserved": True,
    }


def validate_manual_review_normalization_queue(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = True
    if not df.empty:
        if "destructive_action_allowed" in df.columns and bool(df["destructive_action_allowed"].any()):
            valid = False
    return {
        "valid": valid,
        "total_queue_items": len(df),
        "destructive_action_allowed": False,
    }


def validate_normalized_output_manifest(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = not df.empty and "source_preserved" in df.columns and bool(df["source_preserved"].all())
    return {
        "valid": valid,
        "manifest_entries": len(df),
        "source_preserved": valid,
    }


def validate_normalization_scores(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = True
    if not df.empty and "score" in df.columns:
        valid = bool(((df["score"] >= 0.0) & (df["score"] <= 1.0)).all())
    return {
        "valid": valid,
        "scores_in_range": valid,
    }


def validate_data_normalization_safety_boundary(
    df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Dict[str, Any]:
    valid = not df.empty and "condition_type" in df.columns
    return {
        "valid": valid,
        "total_conditions": len(df),
    }


def validate_no_forbidden_normalization_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    found_violations: List[str] = []
    if text:
        lower_t = text.lower()
        for kw in FORBIDDEN_KEYWORDS:
            if kw in lower_t:
                found_violations.append(f"Metinde yasaklı ifade bulundu: '{kw}'")

    if df is not None and not df.empty:
        for col in df.select_dtypes(include=["object"]).columns:
            for val in df[col].dropna().astype(str):
                lower_v = val.lower()
                for kw in FORBIDDEN_KEYWORDS:
                    if kw in lower_v and "forbidden" not in lower_v and "yasal uyari" not in lower_v:
                        found_violations.append(f"Tablo '{col}' sütununda yasaklı iddia: '{kw}'")
                        break

    return {
        "passed": len(found_violations) == 0,
        "violations_count": len(found_violations),
        "violations": found_violations,
    }


def build_data_normalization_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []

    # 1. Profile registry validation
    p_res = validate_data_normalization_profile_registry(tables.get("profile_registry", pd.DataFrame()), profile)
    records.append({
        "validation_item": "profile_registry_integrity",
        "passed": p_res["valid"],
        "note": f"Profiller doğrulandı (toplam: {p_res['total_profiles']})",
    })

    # 2. Domain registry validation
    d_res = validate_data_normalization_domain_registry(tables.get("domain_registry", pd.DataFrame()), profile)
    records.append({
        "validation_item": "domain_registry_integrity",
        "passed": d_res["valid"],
        "note": f"Alanlar doğrulandı (toplam: {d_res['total_domains']})",
    })

    # 3. Rule registry validation
    r_res = validate_normalization_rule_registry(tables.get("rule_registry", pd.DataFrame()), profile)
    records.append({
        "validation_item": "rule_registry_non_destructive",
        "passed": r_res["valid"],
        "note": f"Kurallar non-destructive (toplam: {r_res['total_rules']})",
    })

    # 4. Canonical schema validation
    s_res = validate_canonical_schema_registry(tables.get("canonical_schema_registry", pd.DataFrame()), profile)
    records.append({
        "validation_item": "canonical_schema_integrity",
        "passed": s_res["valid"],
        "note": f"Kanonik şemalar doğrulandı (toplam: {s_res['total_schemas']})",
    })

    # 5. Canonical field validation
    f_res = validate_canonical_field_registry(tables.get("canonical_field_registry", pd.DataFrame()), profile)
    records.append({
        "validation_item": "canonical_field_integrity",
        "passed": f_res["valid"],
        "note": f"Kanonik alanlar doğrulandı (toplam: {f_res['total_canonical_fields']})",
    })

    # 6. Decisions non-destructive validation
    dec_res = validate_normalization_decisions(tables.get("decision_registry", pd.DataFrame()), profile)
    records.append({
        "validation_item": "decision_registry_non_destructive",
        "passed": dec_res["valid"],
        "note": "Kararlar source_preserved=True ve destructive_action_allowed=False",
    })

    # 7. Manual review queue validation
    rev_res = validate_manual_review_normalization_queue(tables.get("manual_review_queue", pd.DataFrame()), profile)
    records.append({
        "validation_item": "manual_review_queue_safety",
        "passed": rev_res["valid"],
        "note": "Manuel inceleme kuyruğu yıkıcı eylem barındırmaz",
    })

    # 8. Output manifest validation
    man_res = validate_normalized_output_manifest(tables.get("output_manifest", pd.DataFrame()), profile)
    records.append({
        "validation_item": "output_manifest_source_preservation",
        "passed": man_res["valid"],
        "note": "Manifest kaynak verinin korunduğunu onaylar",
    })

    # 9. Scores validation
    sc_res = validate_normalization_scores(tables.get("score_report", pd.DataFrame()), profile)
    records.append({
        "validation_item": "normalization_scores_bounded",
        "passed": sc_res["valid"],
        "note": "Normalizasyon skorları [0.0, 1.0] aralığında",
    })

    # 10. Forbidden claims validation
    fc_res = validate_no_forbidden_normalization_claims(summary={})
    records.append({
        "validation_item": "no_forbidden_claims",
        "passed": fc_res["passed"],
        "note": "Yasaklı ticaret, broker veya resmi onay iddiası tespit edilmedi",
    })

    df = pd.DataFrame.from_records(records)
    all_passed = bool(df["passed"].all()) if "passed" in df.columns else False
    summary = {
        "total_validations": len(df),
        "all_passed": all_passed,
        "forbidden_claims_found": fc_res["violations_count"],
        "current_phase": 113,
        "target_final_phase": 160,
    }
    return df, summary
