from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import (
    ProviderBenchmarkProfile,
    list_provider_benchmark_profiles,
)
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkProfileItem,
    build_provider_benchmark_profile_id,
)


def build_default_provider_benchmark_profile_records(
    active_profile: ProviderBenchmarkProfile,
) -> List[ProviderBenchmarkProfileItem]:
    profiles = list_provider_benchmark_profiles(enabled_only=False)
    records: List[ProviderBenchmarkProfileItem] = []
    for p in profiles:
        prof_id = build_provider_benchmark_profile_id(p.name)
        status = "benchmark_pass" if p.enabled else "benchmark_placeholder_only"
        warnings: List[str] = []
        if p.min_benchmark_score > 0.6:
            warnings.append("High minimum benchmark score threshold configured")
        records.append(
            ProviderBenchmarkProfileItem(
                profile_id=prof_id,
                profile_name=p.name,
                current_phase=p.current_phase,
                target_final_phase=p.target_final_phase,
                next_phase=p.next_phase,
                local_only=p.local_only,
                non_production=p.non_production,
                research_only=p.research_only,
                dry_run=p.dry_run_default,
                status_label=status,
                warnings=warnings,
            )
        )
    return records


def build_provider_benchmark_profile_registry(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = build_default_provider_benchmark_profile_records(profile)
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_benchmark_profile_registry(df)
    return df, summary


def summarize_provider_benchmark_profile_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_profiles": len(df),
        "profile_names": df["profile_name"].tolist() if "profile_name" in df.columns else [],
        "all_local_only": bool(df["local_only"].all()) if "local_only" in df.columns else True,
        "all_non_production": bool(df["non_production"].all()) if "non_production" in df.columns else True,
        "current_phase": 115,
        "target_final_phase": 160,
    }
