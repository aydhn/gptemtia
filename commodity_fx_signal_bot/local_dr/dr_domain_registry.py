
import pandas as pd
from local_dr.dr_config import LocalDRProfile
from local_dr.dr_models import DRDomain

def build_default_dr_domains(profile: LocalDRProfile) -> list[DRDomain]:
    return [DRDomain(domain_id="archive_restore_dr", domain_name="Archive Restore", domain_label="archive_restore_dr", description="", required_artifacts=[], warnings=[])]

def build_dr_domain_registry(profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_dr_domains(profile)
    df = pd.DataFrame([d.__dict__ for d in domains])
    return df, {"total_domains": len(domains)}

def summarize_dr_domains(domain_df: pd.DataFrame) -> dict:
    return {"total": len(domain_df)}
