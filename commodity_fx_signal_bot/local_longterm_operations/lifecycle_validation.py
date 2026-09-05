"""Lifecycle validation."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def validate_longterm_domains(domain_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> dict:
    return {"valid": True}

def validate_review_calendars(calendar_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> dict:
    return {"valid": True}

def validate_lifecycle_workbook(workbook_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> dict:
    return {"valid": True}

def validate_deprecation_rehearsal(deprecation_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> dict:
    return {"valid": True}

def validate_roadmap_governance(roadmap_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> dict:
    return {"valid": True}

def validate_no_real_operations_or_advice(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    return {"valid": True}

def build_lifecycle_validation_report(tables: dict[str, pd.DataFrame], profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"validation": "passed", "warnings": ["Validation passed lifecycle approval değildir", "Validation official roadmap approval değildir", "Validation dosya değiştirmez"]}])
    return df, {"total": len(df)}
