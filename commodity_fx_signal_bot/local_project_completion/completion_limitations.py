import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def build_default_completion_known_limitations(profile: LocalProjectCompletionProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"limitation": "no live trading"},
        {"limitation": "no broker integration"},
        {"limitation": "no investment advice"},
        {"limitation": "no production deployment"},
        {"limitation": "no package publish"},
        {"limitation": "no cloud dependency"},
        {"limitation": "no external LLM/API"},
        {"limitation": "no official acceptance"},
        {"limitation": "manual review required"},
        {"limitation": "offline/local outputs only"}
    ])

def build_project_completion_known_limitations_register(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_completion_known_limitations(profile)
    return df, summarize_completion_known_limitations(df)

def summarize_completion_known_limitations(df: pd.DataFrame) -> dict:
    return {"limitations": len(df), "note": "Not a production limitation disclosure."}
