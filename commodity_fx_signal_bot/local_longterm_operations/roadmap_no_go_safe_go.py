"""Roadmap no-go safe-go."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_v1x_roadmap_no_go_conditions(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "official release commitment", "warnings": ["official release commitment no-go olur"]},
        {"condition": "live trading enablement", "warnings": ["live trading enablement no-go olur"]},
        {"condition": "broker execution enablement", "warnings": ["broker execution enablement no-go olur"]},
        {"condition": "investment advice automation", "warnings": ["investment advice automation no-go olur"]},
        {"condition": "model deployment approval", "warnings": ["model deployment approval no-go olur"]},
        {"condition": "cloud migration approval", "warnings": ["cloud migration approval no-go olur"]},
        {"condition": "package publish", "warnings": ["package publish no-go olur"]},
        {"condition": "production deployment", "warnings": ["production deployment no-go olur"]},
        {"condition": "legal/compliance approval", "warnings": ["legal/compliance approval no-go olur"]}
    ])

def build_v1x_roadmap_safe_go_conditions(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "offline candidate documented", "warnings": ["safe-go roadmap approval değildir"]},
        {"condition": "manual review required", "warnings": ["safe-go roadmap approval değildir"]},
        {"condition": "no implementation commitment", "warnings": ["safe-go roadmap approval değildir"]},
        {"condition": "no production approval", "warnings": ["safe-go roadmap approval değildir"]},
        {"condition": "no broker/live/advice/deploy expansion", "warnings": ["safe-go roadmap approval değildir"]},
        {"condition": "risk/benefit documented", "warnings": ["safe-go roadmap approval değildir"]}
    ])

def build_v1x_roadmap_no_go_safe_go_summary(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df1 = build_v1x_roadmap_no_go_conditions(profile)
    df2 = build_v1x_roadmap_safe_go_conditions(profile)
    df = pd.concat([df1, df2], ignore_index=True)
    return df, summarize_v1x_roadmap_no_go_safe_go(df)

def summarize_v1x_roadmap_no_go_safe_go(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
