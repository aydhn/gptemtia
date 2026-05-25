import pandas as pd
from typing import Tuple, Dict, Optional

from .performance_config import PerformanceProfile

def build_runtime_optimization_recommendations(bottleneck_df: pd.DataFrame) -> pd.DataFrame:
    recs = []

    runtime_bn = bottleneck_df[bottleneck_df["bottleneck_type"] == "runtime_bottleneck"]

    for _, row in runtime_bn.iterrows():
        sev = row["severity"]
        mod = row["module_name"]

        if sev == "high":
            recs.append({
                "module_name": mod,
                "recommendation": "Long-running scriptleri status/report ve heavy report olarak ayır. Batch size düşür.",
                "risk_level": "medium_risk_optimization_candidate",
                "action": "manual_review_required"
            })
        elif sev == "medium":
            recs.append({
                "module_name": mod,
                "recommendation": "Repeated report scans için cache kullan.",
                "risk_level": "low_risk_optimization_candidate",
                "action": "offline_suggestion"
            })

    return pd.DataFrame(recs)

def build_memory_optimization_recommendations(bottleneck_df: pd.DataFrame) -> pd.DataFrame:
    recs = []

    mem_bn = bottleneck_df[bottleneck_df["bottleneck_type"] == "memory_bottleneck"]

    for _, row in mem_bn.iterrows():
        sev = row["severity"]
        mod = row["module_name"]

        if sev == "high":
            recs.append({
                "module_name": mod,
                "recommendation": "Büyük DataFrame'leri erken filtrele. Gereksiz kolonları düşür. Büyük raporlarda streaming write veya chunked read kullan.",
                "risk_level": "high_risk_manual_review_required",
                "action": "manual_review_required"
            })
        elif sev == "medium":
            recs.append({
                "module_name": mod,
                "recommendation": "Batch size düşür. Parquet opsiyonel kullan.",
                "risk_level": "low_risk_optimization_candidate",
                "action": "offline_suggestion"
            })

    return pd.DataFrame(recs)

def build_cache_optimization_recommendations(
    cache_df: Optional[pd.DataFrame],
    bottleneck_df: Optional[pd.DataFrame]
) -> pd.DataFrame:

    recs = []

    if bottleneck_df is not None and not bottleneck_df.empty:
        cache_bn = bottleneck_df[bottleneck_df["bottleneck_type"].isin(["cache_bottleneck", "io_bottleneck"])]

        for _, row in cache_bn.iterrows():
            if row["bottleneck_type"] == "cache_bottleneck":
                recs.append({
                    "module_name": row["module_name"],
                    "recommendation": "Knowledge index chunk sayısını profile göre sınırla. Cache TTL uzatılabilir.",
                    "risk_level": "low_risk_optimization_candidate",
                    "action": "offline_suggestion"
                })
            elif row["bottleneck_type"] == "io_bottleneck":
                recs.append({
                    "module_name": row["module_name"],
                    "recommendation": "CSV yerine parquet opsiyonel kullan; pyarrow yoksa CSV fallback. Tek worker güvenli default kalsın.",
                    "risk_level": "medium_risk_optimization_candidate",
                    "action": "manual_review_required"
                })

    return pd.DataFrame(recs)

def build_safe_optimization_recommendation_report(
    bottleneck_df: pd.DataFrame,
    profile: PerformanceProfile
) -> Tuple[pd.DataFrame, Dict]:

    dfs = []

    dfs.append(build_runtime_optimization_recommendations(bottleneck_df))
    dfs.append(build_memory_optimization_recommendations(bottleneck_df))
    dfs.append(build_cache_optimization_recommendations(None, bottleneck_df))

    valid_dfs = [df for df in dfs if not df.empty]

    if not valid_dfs:
        df = pd.DataFrame(columns=["module_name", "recommendation", "risk_level", "action"])
    else:
        df = pd.concat(valid_dfs, ignore_index=True)

    summary = {
        "total_recommendations": len(df),
        "high_risk": len(df[df["risk_level"] == "high_risk_manual_review_required"]) if not df.empty else 0,
        "medium_risk": len(df[df["risk_level"] == "medium_risk_optimization_candidate"]) if not df.empty else 0,
        "low_risk": len(df[df["risk_level"] == "low_risk_optimization_candidate"]) if not df.empty else 0
    }

    return df, summary

def summarize_optimization_recommendations(recommendation_df: pd.DataFrame) -> dict:
    if recommendation_df.empty:
        return {"total_recommendations": 0}

    return {
        "total_recommendations": len(recommendation_df),
        "manual_review_required": len(recommendation_df[recommendation_df["action"] == "manual_review_required"]) if "action" in recommendation_df.columns else 0
    }
