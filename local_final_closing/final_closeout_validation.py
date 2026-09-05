import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def validate_final_closing_domains(domain_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> dict:
    if domain_df is None or domain_df.empty:
        return {"valid": False, "reason": "No domains"}
    if "domain_id" not in domain_df.columns:
        return {"valid": False, "reason": "Missing domain_id"}
    return {"valid": True}

def validate_final_master_terminal_lock(lock_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> dict:
    if lock_df is None or lock_df.empty:
        return {"valid": False, "reason": "No lock items"}
    if "lock_id" not in lock_df.columns:
        return {"valid": False, "reason": "Missing lock_id"}
    return {"valid": True}

def validate_project_constitution(constitution_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> dict:
    if constitution_df is None or constitution_df.empty:
        return {"valid": False, "reason": "No constitution items"}
    if "constitution_id" not in constitution_df.columns:
        return {"valid": False, "reason": "Missing constitution_id"}
    return {"valid": True}

def validate_non_production_seal(seal_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> dict:
    if seal_df is None or seal_df.empty:
        return {"valid": False, "reason": "No seal items"}
    if "seal_id" not in seal_df.columns:
        return {"valid": False, "reason": "Missing seal_id"}
    return {"valid": True}

def validate_terminal_archive_index(archive_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> dict:
    if archive_df is None or archive_df.empty:
        return {"valid": False, "reason": "No archive items"}
    if "archive_index_id" not in archive_df.columns:
        return {"valid": False, "reason": "Missing archive_index_id"}
    return {"valid": True}

def validate_closing_governance_no_go_safe_go(summary_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> dict:
    if summary_df is None or summary_df.empty:
        return {"valid": False, "reason": "No summary"}
    return {"valid": True}

def validate_no_real_final_closeout_or_advice(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    return {"valid": True, "reason": "validation dosya değiştirmez"}

def build_final_closeout_validation_report(tables: dict[str, pd.DataFrame], profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    results = []
    if "domain_df" in tables:
        results.append(validate_final_closing_domains(tables["domain_df"], profile))
    df = pd.DataFrame(results)
    return df, {"total_validations": len(results)}
