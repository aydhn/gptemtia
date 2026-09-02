import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile

def build_maintainability_seed_sections(complexity_df: pd.DataFrame, plan_df: pd.DataFrame, candidate_df: pd.DataFrame) -> list[dict]:
    return [{"title": "Seed", "content": "Future refactor seed."}]

def build_local_maintainability_improvement_seed(complexity_df: pd.DataFrame, plan_df: pd.DataFrame, candidate_df: pd.DataFrame, profile: LocalSimplificationProfile) -> tuple[str, dict]:
    sections = build_maintainability_seed_sections(complexity_df, plan_df, candidate_df)
    text = "# Local Maintainability Improvement Seed\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    return text, summarize_maintainability_seed(text)

def summarize_maintainability_seed(text: str) -> dict:
    return {"length": len(text), "warnings": ["Implementation baslatmaz."]}
