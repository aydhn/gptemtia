import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

def build_known_limitations_register(project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_limitations(profile)
    return df, summarize_known_limitations(df)

def collect_limitations_from_docs_and_reports(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def build_default_limitations(profile: LocalReadinessProfile) -> pd.DataFrame:
    limitations = [
        "offline/local only", "no live trading", "no broker execution",
        "no investment advice", "no model deployment", "no production scheduler",
        "no dashboard", "no external LLM/API", "no scraping",
        "no official compliance certification", "synthetic/demo/test limitations",
        "backtest limitations", "data freshness limitations", "manual review required"
    ]
    return pd.DataFrame({"limitation": limitations})

def summarize_known_limitations(limitations_df: pd.DataFrame) -> dict:
    return {"total_limitations": len(limitations_df)}
