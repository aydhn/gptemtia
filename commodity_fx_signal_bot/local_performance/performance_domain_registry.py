import pandas as pd
from .performance_config import LocalPerformanceProfile
from .performance_models import PerformanceDomain, build_performance_domain_id, performance_domain_to_dict
from .performance_labels import list_performance_domain_labels

def build_default_performance_domains(profile: LocalPerformanceProfile) -> list[PerformanceDomain]:
    domains = []
    for lbl in list_performance_domain_labels():
        if lbl == "unknown_performance_domain": continue
        domains.append(PerformanceDomain(
            domain_id=build_performance_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"{lbl} domain for offline planning",
            required_reports=[],
            warnings=["Bu domain official capacity scope degildir."]
        ))
    return domains

def build_performance_domain_registry(profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_performance_domains(profile)
    df = pd.DataFrame([performance_domain_to_dict(d) for d in domains])
    summary = summarize_performance_domains(df)
    return df, summary

def summarize_performance_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total": 0, "status": "empty"}
    return {"total": len(domain_df), "domains": domain_df["domain_label"].tolist()}
