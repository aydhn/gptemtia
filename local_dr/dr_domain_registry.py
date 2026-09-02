import pandas as pd
from local_dr.dr_config import LocalDRProfile
from local_dr.dr_models import DRDomain, build_dr_domain_id, dr_domain_to_dict

def build_default_dr_domains(profile: LocalDRProfile) -> list[DRDomain]:
    return [
        DRDomain(
            domain_id=build_dr_domain_id("archive_restore_dr"),
            domain_label="archive_restore_dr",
            description="Archive restore DR domain",
            criticality="high"
        ),
        DRDomain(
            domain_id=build_dr_domain_id("config_restore_dr"),
            domain_label="config_restore_dr",
            description="Config restore DR domain",
            criticality="medium"
        )
    ]

def build_dr_domain_registry(profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_dr_domains(profile)
    df = pd.DataFrame([dr_domain_to_dict(d) for d in domains])
    summary = summarize_dr_domains(df)
    return df, summary

def summarize_dr_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "critical_domains": len(domain_df[domain_df.get("criticality") == "high"]) if "criticality" in domain_df else 0,
    }
