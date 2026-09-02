
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile
from .hardening_models import HardeningDomain, build_hardening_domain_id

def build_default_hardening_domains(profile: LocalHardeningProfile) -> list[HardeningDomain]:
    return [
        HardeningDomain(domain_id=build_hardening_domain_id("source_hardening"), domain_label="source_hardening", domain_name="Source", description="Source code hardening", required_checks=[], warnings=[])
    ]

def build_hardening_domain_registry(profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_hardening_domains(profile)
    df = pd.DataFrame([d.__dict__ for d in domains]) if domains else pd.DataFrame()
    return df, summarize_hardening_domains(df)

def summarize_hardening_domains(domain_df: pd.DataFrame) -> dict:
    return {"total": len(domain_df)}
