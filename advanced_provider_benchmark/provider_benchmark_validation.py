from typing import Tuple, Dict, Any, Optional
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile

FORBIDDEN_TERMS = [
    "official approval",
    "production ready",
    "live trading ready",
    "broker ready",
    "buy signal",
    "sell signal",
    "trade signal",
    "investment advice",
    "execute order",
    "web scraping",
    "full text article",
    "source overwrite",
    "destructive clean",
]


def validate_no_forbidden_benchmark_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    found_terms = []
    if text:
        lower_t = text.lower()
        for term in FORBIDDEN_TERMS:
            # Allow disclaimers containing forbidden phrases negated (e.g. "not an official approval")
            if term in lower_t:
                # check if negated
                negations = [f"not {term}", f"no {term}", f"zero {term}", f"not an {term}", f"değildir"]
                if not any(n in lower_t for n in negations):
                    found_terms.append(term)
    if summary:
        if summary.get("official_approval_guarantee", False):
            found_terms.append("official_approval_guarantee is True")
        if summary.get("production_ready_guarantee", False):
            found_terms.append("production_ready_guarantee is True")
        if summary.get("broker_ready_guarantee", False):
            found_terms.append("broker_ready_guarantee is True")

    if df is not None and not df.empty:
        if "official_approval" in df.columns and bool(df["official_approval"].any()):
            found_terms.append("official_approval column has True")
        if "production_ready" in df.columns and bool(df["production_ready"].any()):
            found_terms.append("production_ready column has True")
        if "broker_ready" in df.columns and bool(df["broker_ready"].any()):
            found_terms.append("broker_ready column has True")
        if "destructive_action_allowed" in df.columns and bool(df["destructive_action_allowed"].any()):
            found_terms.append("destructive_action_allowed column has True")

    return {
        "valid": len(found_terms) == 0,
        "forbidden_terms_found": found_terms,
    }


def validate_provider_benchmark_profile_registry(
    df: pd.DataFrame, profile: ProviderBenchmarkProfile
) -> Dict[str, Any]:
    valid = True
    issues = []
    if df.empty:
        return {"valid": False, "issues": ["Profile registry is empty"]}
    if "current_phase" in df.columns and not (df["current_phase"] == 115).all():
        valid = False
        issues.append("Profile registry contains invalid current_phase (!= 115)")
    if "target_final_phase" in df.columns and not (df["target_final_phase"] == 160).all():
        valid = False
        issues.append("Profile registry contains invalid target_final_phase (!= 160)")
    if "local_only" in df.columns and not df["local_only"].all():
        valid = False
        issues.append("Profile registry contains local_only=False")
    return {"valid": valid, "issues": issues}


def validate_provider_benchmark_metric_registry(
    df: pd.DataFrame, profile: ProviderBenchmarkProfile
) -> Dict[str, Any]:
    valid = True
    issues = []
    if df.empty:
        return {"valid": False, "issues": ["Metric registry is empty"]}
    expected = [
        "metric_coverage",
        "metric_capability",
        "metric_quality",
        "metric_normalization",
        "metric_traceability",
        "metric_license_provenance",
        "metric_no_scraping_compliance",
        "metric_metadata_only_compliance",
        "metric_manual_review_load",
        "metric_cross_domain_consistency",
    ]
    actual = df["metric_label"].tolist() if "metric_label" in df.columns else []
    for exp in expected:
        if exp not in actual:
            valid = False
            issues.append(f"Missing expected metric: {exp}")
    return {"valid": valid, "issues": issues}


def validate_provider_benchmark_scores(
    df: pd.DataFrame, profile: ProviderBenchmarkProfile
) -> Dict[str, Any]:
    valid = True
    issues = []
    if df.empty:
        return {"valid": False, "issues": ["Scores dataframe is empty"]}
    if "total_score" in df.columns:
        if (df["total_score"] < 0.0).any() or (df["total_score"] > 1.0).any():
            valid = False
            issues.append("total_score values must be strictly in range [0.0, 1.0]")
    if "official_approval" in df.columns and df["official_approval"].any():
        valid = False
        issues.append("official_approval must be False for all providers")
    if "production_ready" in df.columns and df["production_ready"].any():
        valid = False
        issues.append("production_ready must be False for all providers")
    if "broker_ready" in df.columns and df["broker_ready"].any():
        valid = False
        issues.append("broker_ready must be False for all providers")
    return {"valid": valid, "issues": issues}


def validate_provider_ranking_research(
    df: pd.DataFrame, profile: ProviderBenchmarkProfile
) -> Dict[str, Any]:
    valid = True
    issues = []
    if df.empty:
        return {"valid": False, "issues": ["Ranking dataframe is empty"]}
    if "official_approval" in df.columns and df["official_approval"].any():
        valid = False
        issues.append("Ranking cannot grant official approval")
    return {"valid": valid, "issues": issues}


def validate_provider_benchmark_findings(
    df: pd.DataFrame, profile: ProviderBenchmarkProfile
) -> Dict[str, Any]:
    valid = True
    issues = []
    if df.empty:
        return {"valid": False, "issues": ["Findings dataframe is empty"]}
    return {"valid": valid, "issues": issues}


def validate_provider_benchmark_manual_review_queue(
    df: pd.DataFrame, profile: ProviderBenchmarkProfile
) -> Dict[str, Any]:
    valid = True
    issues = []
    if "destructive_action_allowed" in df.columns and df["destructive_action_allowed"].any():
        valid = False
        issues.append("destructive_action_allowed must be False for all review items")
    return {"valid": valid, "issues": issues}


def build_provider_benchmark_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    checks = []

    # Check 1: Profile registry
    prof_res = validate_provider_benchmark_profile_registry(tables.get("profiles", pd.DataFrame()), profile)
    checks.append({
        "validation_area": "profile_registry",
        "status": "VALID" if prof_res["valid"] else "INVALID",
        "issues": "; ".join(prof_res["issues"]) if prof_res["issues"] else "None",
    })

    # Check 2: Metric registry
    metric_res = validate_provider_benchmark_metric_registry(tables.get("metrics", pd.DataFrame()), profile)
    checks.append({
        "validation_area": "metric_registry",
        "status": "VALID" if metric_res["valid"] else "INVALID",
        "issues": "; ".join(metric_res["issues"]) if metric_res["issues"] else "None",
    })

    # Check 3: Scores
    score_res = validate_provider_benchmark_scores(tables.get("scores", pd.DataFrame()), profile)
    checks.append({
        "validation_area": "benchmark_scores",
        "status": "VALID" if score_res["valid"] else "INVALID",
        "issues": "; ".join(score_res["issues"]) if score_res["issues"] else "None",
    })

    # Check 4: Ranking
    rank_res = validate_provider_ranking_research(tables.get("ranking", pd.DataFrame()), profile)
    checks.append({
        "validation_area": "ranking_research",
        "status": "VALID" if rank_res["valid"] else "INVALID",
        "issues": "; ".join(rank_res["issues"]) if rank_res["issues"] else "None",
    })

    # Check 5: Manual review queue
    rev_res = validate_provider_benchmark_manual_review_queue(tables.get("manual_review", pd.DataFrame()), profile)
    checks.append({
        "validation_area": "manual_review_queue",
        "status": "VALID" if rev_res["valid"] else "INVALID",
        "issues": "; ".join(rev_res["issues"]) if rev_res["issues"] else "None",
    })

    # Check 6: Forbidden claims across tables
    claim_issues = []
    for t_name, t_df in tables.items():
        c_res = validate_no_forbidden_benchmark_claims(df=t_df)
        if not c_res["valid"]:
            claim_issues.append(f"{t_name}: {c_res['forbidden_terms_found']}")
    checks.append({
        "validation_area": "forbidden_claims_enforcement",
        "status": "VALID" if len(claim_issues) == 0 else "INVALID",
        "issues": "; ".join(claim_issues) if claim_issues else "None",
    })

    df = pd.DataFrame.from_records(checks)
    all_valid = bool((df["status"] == "VALID").all()) if not df.empty and "status" in df.columns else False
    summary = {
        "validation_status": "VALID" if all_valid else "INVALID",
        "total_checks": len(df),
        "forbidden_claims_found": not all_valid,
        "scores_valid": score_res["valid"],
        "current_phase": 115,
        "target_final_phase": 160,
    }
    return df, summary
