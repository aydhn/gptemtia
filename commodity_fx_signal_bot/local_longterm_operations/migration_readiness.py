"""Migration readiness."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_migration_readiness_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "check", "warnings": ["Migration readiness gerçek migration approval değildir. Hiçbir dosya değiştirmez."]}])

def build_default_migration_non_goals(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"goal": "no automatic migration", "warnings": ["Migration readiness gerçek migration approval değildir."]},
        {"goal": "no schema rewrite", "warnings": ["Migration readiness gerçek migration approval değildir."]},
        {"goal": "no cloud migration", "warnings": ["Migration readiness gerçek migration approval değildir."]},
        {"goal": "no broker integration migration", "warnings": ["Migration readiness gerçek migration approval değildir."]},
        {"goal": "no production deployment", "warnings": ["Migration readiness gerçek migration approval değildir."]},
        {"goal": "no model deployment", "warnings": ["Migration readiness gerçek migration approval değildir."]},
        {"goal": "no live trading enablement", "warnings": ["Migration readiness gerçek migration approval değildir."]},
        {"goal": "no destructive migration", "warnings": ["Migration readiness gerçek migration approval değildir."]}
    ])

def build_migration_readiness_rehearsal_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_migration_readiness_items(profile)
    return df, summarize_migration_readiness(df, pd.DataFrame())

def build_migration_non_goals_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_migration_non_goals(profile)
    return df, summarize_migration_readiness(pd.DataFrame(), df)

def summarize_migration_readiness(readiness_df: pd.DataFrame, non_goals_df: pd.DataFrame) -> dict:
    return {"readiness_items": len(readiness_df), "non_goals": len(non_goals_df)}
