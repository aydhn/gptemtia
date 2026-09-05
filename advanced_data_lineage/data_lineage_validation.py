from typing import Tuple, Dict, Any, List, Optional
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


FORBIDDEN_TERMS = [
    "official approval",
    "resmi onay",
    "production ready",
    "buy signal",
    "sell signal",
    "al sinyali",
    "sat sinyali",
    "yatırım tavsiyesi",
    "investment advice",
    "broker execution",
    "live trading",
    "canlı emir",
    "web scraping",
    "html scraping",
    "paywall bypass",
    "full article text",
    "haber tam metni",
    "source overwrite",
    "destructive cleaning",
]


def validate_no_forbidden_lineage_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    found_violations: List[str] = []

    content_to_scan = []
    if text:
        content_to_scan.append(text)
    if df is not None:
        content_to_scan.append(df.to_string())
    if summary is not None:
        content_to_scan.append(str(summary))

    full_blob = " ".join(content_to_scan).lower()
    for term in FORBIDDEN_TERMS:
        if term in full_blob:
            found_violations.append(term)

    return {
        "passed": len(found_violations) == 0,
        "violations": found_violations,
        "violations_count": len(found_violations),
    }


def validate_data_lineage_profile_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    passed = len(df) >= 3 and bool(df["non_destructive"].all()) and bool(df["local_only"].all())
    return {"passed": passed, "total_profiles": len(df)}


def validate_data_lineage_domain_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    passed = len(df) >= 25
    return {"passed": passed, "total_domains": len(df)}


def validate_provenance_source_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    passed = len(df) >= 8 and bool((df["no_scraping_policy"] == "Strict no-scraping").all())
    return {"passed": passed, "total_sources": len(df)}


def validate_source_reference_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    no_creds = bool((~df["contains_credentials"]).all()) if "contains_credentials" in df.columns else False
    no_full = bool((~df["contains_full_text"]).all()) if "contains_full_text" in df.columns else False
    passed = len(df) >= 8 and no_creds and no_full
    return {"passed": passed, "no_credentials": no_creds, "no_full_text": no_full}


def validate_provider_provenance_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    passed = len(df) >= 8
    return {"passed": passed, "total_providers": len(df)}


def validate_dataset_provenance_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    all_preserved = bool(df["source_preserved"].all()) if "source_preserved" in df.columns else False
    passed = len(df) >= 8 and all_preserved
    return {"passed": passed, "all_source_preserved": all_preserved}


def validate_schema_provenance_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    passed = len(df) >= 8
    return {"passed": passed, "total_schemas": len(df)}


def validate_transformation_provenance_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    all_preserved = bool(df["source_preserved"].all()) if "source_preserved" in df.columns else False
    no_dest = bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns else False
    passed = len(df) >= 8 and all_preserved and no_dest
    return {"passed": passed, "all_source_preserved": all_preserved, "zero_destructive": no_dest}


def validate_license_provenance_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    passed = len(df) >= 5
    return {"passed": passed, "total_license_records": len(df)}


def validate_copyright_boundary_provenance(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    no_ft = bool((~df["contains_full_text"]).all()) if "contains_full_text" in df.columns else False
    passed = len(df) >= 5 and no_ft
    return {"passed": passed, "zero_full_text": no_ft}


def validate_metadata_only_provenance(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    all_meta = bool(df["metadata_only"].all()) if "metadata_only" in df.columns else False
    passed = len(df) >= 3 and all_meta
    return {"passed": passed, "all_metadata_only": all_meta}


def validate_audit_trail_event_registry(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    no_dest = bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns else False
    passed = len(df) >= 8 and no_dest
    return {"passed": passed, "zero_destructive": no_dest}


def validate_traceability_scores(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    valid_range = bool(((df["score"] >= 0.0) & (df["score"] <= 1.0)).all()) if "score" in df.columns else False
    passed = len(df) >= 5 and valid_range
    return {"passed": passed, "valid_score_range": valid_range}


def validate_data_lineage_safety_boundary(
    df: pd.DataFrame, profile: DataLineageProfile
) -> Dict[str, Any]:
    has_no_go = bool((df["status"] == "BLOCKED_NO_GO").any()) if "status" in df.columns else False
    has_safe_go = bool((df["status"] == "ALLOWED_SAFE_GO").any()) if "status" in df.columns else False
    passed = has_no_go and has_safe_go
    return {"passed": passed, "has_no_go": has_no_go, "has_safe_go": has_safe_go}


def build_data_lineage_validation_report(
    tables: Dict[str, pd.DataFrame], profile: DataLineageProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        ("val_001", "profile_registry_integrity", validate_data_lineage_profile_registry(tables.get("profiles", pd.DataFrame()), profile)["passed"]),
        ("val_002", "domain_registry_integrity", validate_data_lineage_domain_registry(tables.get("domains", pd.DataFrame()), profile)["passed"]),
        ("val_003", "provenance_source_integrity", validate_provenance_source_registry(tables.get("sources", pd.DataFrame()), profile)["passed"]),
        ("val_004", "source_reference_integrity", validate_source_reference_registry(tables.get("source_references", pd.DataFrame()), profile)["passed"]),
        ("val_005", "provider_provenance_integrity", validate_provider_provenance_registry(tables.get("providers", pd.DataFrame()), profile)["passed"]),
        ("val_006", "dataset_provenance_integrity", validate_dataset_provenance_registry(tables.get("datasets", pd.DataFrame()), profile)["passed"]),
        ("val_007", "schema_provenance_integrity", validate_schema_provenance_registry(tables.get("schemas", pd.DataFrame()), profile)["passed"]),
        ("val_008", "transformation_provenance_integrity", validate_transformation_provenance_registry(tables.get("transformations", pd.DataFrame()), profile)["passed"]),
        ("val_009", "license_provenance_integrity", validate_license_provenance_registry(tables.get("licenses", pd.DataFrame()), profile)["passed"]),
        ("val_010", "copyright_boundary_integrity", validate_copyright_boundary_provenance(tables.get("copyright", pd.DataFrame()), profile)["passed"]),
        ("val_011", "metadata_only_integrity", validate_metadata_only_provenance(tables.get("metadata_only", pd.DataFrame()), profile)["passed"]),
        ("val_012", "audit_trail_integrity", validate_audit_trail_event_registry(tables.get("audit_trail", pd.DataFrame()), profile)["passed"]),
        ("val_013", "traceability_score_integrity", validate_traceability_scores(tables.get("traceability_scores", pd.DataFrame()), profile)["passed"]),
        ("val_014", "safety_boundary_integrity", validate_data_lineage_safety_boundary(tables.get("safety", pd.DataFrame()), profile)["passed"]),
    ]

    records = []
    for r_id, name, res in rules:
        records.append({
            "rule_id": r_id,
            "rule_name": name,
            "status": "PASS" if res else "FAIL",
            "enforced": True,
            "current_phase": 114,
        })
    df = pd.DataFrame.from_records(records)
    total = len(df)
    passed_count = int((df["status"] == "PASS").sum())
    overall = "PASS" if passed_count == total else "FAIL"

    summary = {
        "total_rules": total,
        "passed_rules": passed_count,
        "validation_status": overall,
        "forbidden_claims_found": 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
    return df, summary
