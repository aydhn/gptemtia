from typing import Tuple, Dict, Any, List, Optional
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


COPYRIGHT_BOUNDARY_SPECS = [
    ("fx_data_copyright_check", "dataset_fx_quote", False, False, False, False, True, "Strict no full text / raw market quotes only", "lineage_complete"),
    ("commodity_data_copyright_check", "dataset_commodity_spot", False, False, False, False, True, "Strict no full text / spot & futures quotes only", "lineage_complete"),
    ("macro_data_copyright_check", "dataset_macro_timeseries", False, False, False, False, True, "Strict no full text / numerical indicators only", "lineage_complete"),
    ("calendar_data_copyright_check", "dataset_calendar_event", False, False, False, False, True, "Strict no full text / event release timestamps only", "lineage_complete"),
    ("news_metadata_copyright_check", "dataset_news_metadata", False, False, False, False, True, "Metadata only: zero article body, zero scraped HTML", "lineage_complete"),
    ("provider_metadata_copyright_check", "dataset_provider_metadata", False, False, False, False, True, "Capability identifiers only: zero proprietary text", "lineage_complete"),
]


def build_copyright_boundary_provenance_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for check_id, ds_type, has_ft, has_body, has_html, has_copy, meta_only, policy, status in COPYRIGHT_BOUNDARY_SPECS:
        records.append({
            "check_id": check_id,
            "dataset_type": ds_type,
            "contains_full_text": has_ft,
            "contains_article_body": has_body,
            "contains_scraped_html": has_html,
            "copyrighted_article_copy": has_copy,
            "metadata_only": meta_only,
            "no_full_text_policy": policy,
            "status_label": status,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_copyright_boundary_provenance(df)
    return df, summary


def check_copyright_boundary_provenance(df: Optional[pd.DataFrame] = None) -> Dict[str, Any]:
    if df is None:
        p = DataLineageProfile(name="temp", description="temp")
        df, _ = build_copyright_boundary_provenance_registry(p)

    has_forbidden = False
    violations = []

    for idx, row in df.iterrows():
        if row.get("contains_full_text", False):
            has_forbidden = True
            violations.append(f"Row {idx}: contains_full_text is True")
        if row.get("contains_article_body", False):
            has_forbidden = True
            violations.append(f"Row {idx}: contains_article_body is True")
        if row.get("contains_scraped_html", False):
            has_forbidden = True
            violations.append(f"Row {idx}: contains_scraped_html is True")
        if row.get("copyrighted_article_copy", False):
            has_forbidden = True
            violations.append(f"Row {idx}: copyrighted_article_copy is True")
        if not row.get("metadata_only", True):
            has_forbidden = True
            violations.append(f"Row {idx}: metadata_only is False")

    return {
        "passed": not has_forbidden,
        "violations": violations,
        "total_checks": len(df),
        "zero_full_text": not has_forbidden,
    }


def summarize_copyright_boundary_provenance(df: pd.DataFrame) -> Dict[str, Any]:
    check_result = check_copyright_boundary_provenance(df)
    return {
        "total_checks": len(df),
        "all_passed": check_result["passed"],
        "violations_count": len(check_result["violations"]),
        "zero_full_text": check_result["zero_full_text"],
        "current_phase": 114,
        "target_final_phase": 160,
    }
