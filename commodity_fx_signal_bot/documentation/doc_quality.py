import pandas as pd
from documentation.documentation_config import DocumentationProfile

def check_documentation_inventory_quality(docs_df: pd.DataFrame | None, profile: DocumentationProfile) -> dict:
    if docs_df is None or docs_df.empty:
        return {"passed": False, "warnings": ["Documentation inventory is empty."]}

    missing_disclaimers = len(docs_df[docs_df["has_disclaimer"] == False])
    if profile.require_disclaimers and missing_disclaimers > 0:
        return {"passed": False, "warnings": [f"{missing_disclaimers} dokümanda disclaimer eksik."]}

    return {"passed": True, "warnings": []}

def check_documentation_coverage_quality(coverage_df: pd.DataFrame | None, profile: DocumentationProfile) -> dict:
    if coverage_df is None or coverage_df.empty:
        return {"passed": False, "warnings": ["Coverage matrix is empty."]}

    missing = len(coverage_df[coverage_df["status"] != "covered"])
    return {"passed": missing == 0, "warnings": [f"{missing} modül için dokümantasyon eksik."] if missing > 0 else []}

def check_documentation_link_quality(link_df: pd.DataFrame | None) -> dict:
    if link_df is None or link_df.empty:
        return {"passed": True, "warnings": []}

    broken = len(link_df[link_df["status"] == "broken"])
    return {"passed": broken == 0, "warnings": [f"{broken} kırık link bulundu."] if broken > 0 else []}

def check_documentation_safety_quality(safety_df: pd.DataFrame | None, profile: DocumentationProfile) -> dict:
    if safety_df is None or safety_df.empty:
        return {"passed": True, "warnings": []}

    unsafe = len(safety_df[safety_df["is_safe"] == False])
    if profile.require_no_live_trading_language and unsafe > 0:
        return {"passed": False, "warnings": [f"{unsafe} dokümanda riskli canlı işlem dili bulundu."]}

    return {"passed": True, "warnings": []}

def check_documentation_consistency_quality(consistency_df: pd.DataFrame | None) -> dict:
    if consistency_df is None or consistency_df.empty:
        return {"passed": True, "warnings": []}

    failed = len(consistency_df[consistency_df["passed"] == False])
    return {"passed": failed == 0, "warnings": [f"{failed} tutarsızlık bulundu."] if failed > 0 else []}

def build_documentation_quality_report(
    summary: dict,
    docs_df: pd.DataFrame | None = None,
    coverage_df: pd.DataFrame | None = None,
    safety_df: pd.DataFrame | None = None,
    link_df: pd.DataFrame | None = None,
    consistency_df: pd.DataFrame | None = None,
    profile: DocumentationProfile | None = None
) -> dict:

    if profile is None:
        from documentation.documentation_config import get_default_documentation_profile
        profile = get_default_documentation_profile()

    inv_q = check_documentation_inventory_quality(docs_df, profile)
    cov_q = check_documentation_coverage_quality(coverage_df, profile)
    lnk_q = check_documentation_link_quality(link_df)
    saf_q = check_documentation_safety_quality(safety_df, profile)
    con_q = check_documentation_consistency_quality(consistency_df)

    all_warnings = inv_q["warnings"] + cov_q["warnings"] + lnk_q["warnings"] + saf_q["warnings"] + con_q["warnings"]

    passed = inv_q["passed"] and cov_q["passed"] and lnk_q["passed"] and saf_q["passed"] and con_q["passed"]

    return {
        "inventory_valid": inv_q["passed"],
        "coverage_valid": cov_q["passed"],
        "links_valid": lnk_q["passed"],
        "safety_valid": saf_q["passed"],
        "consistency_valid": con_q["passed"],
        "disclaimers_present": inv_q["passed"],
        "unsafe_language_found": not saf_q["passed"],
        "missing_required_docs": not cov_q["passed"],
        "warning_count": len(all_warnings),
        "passed": passed,
        "warnings": all_warnings
    }
