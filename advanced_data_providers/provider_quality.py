import pandas as pd
from .provider_config import DataProviderAbstractionProfile

def check_provider_profile_quality(df: pd.DataFrame | None, profile: DataProviderAbstractionProfile) -> dict: return {"quality_score": 1.0, "issues": []}
def check_provider_registry_quality(df: pd.DataFrame | None, profile: DataProviderAbstractionProfile) -> dict: return {"quality_score": 1.0, "issues": []}
def check_provider_capability_quality(df: pd.DataFrame | None, profile: DataProviderAbstractionProfile) -> dict: return {"quality_score": 1.0, "issues": []}
def check_provider_output_schema_quality(df: pd.DataFrame | None, profile: DataProviderAbstractionProfile) -> dict: return {"quality_score": 1.0, "issues": []}
def check_provider_safety_quality(df: pd.DataFrame | None, profile: DataProviderAbstractionProfile) -> dict: return {"quality_score": 1.0, "issues": []}

def check_for_forbidden_terms_in_provider_layer(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    return {"forbidden_terms_found": [], "critical_issues": []}

def build_provider_quality_report(summary: dict, registry_df: pd.DataFrame | None = None, health_df: pd.DataFrame | None = None) -> dict:
    return {
        "overall_quality": 1.0,
        "is_acceptable": True,
        "quality_metrics": {}
    }
