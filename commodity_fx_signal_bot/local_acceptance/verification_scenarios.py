import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_default_verification_scenarios(profile: LocalAcceptanceProfile) -> pd.DataFrame:
    scenarios = [
        "reviewer asks for project scope",
        "reviewer asks for no-use boundary",
        "reviewer asks for live trading proof",
        "reviewer asks for broker proof",
        "reviewer asks for evidence trail",
        "reviewer asks for test trace",
        "reviewer asks for docs trace",
        "reviewer asks for safety trace",
        "reviewer asks for RC dry-run status",
        "reviewer asks for no-go items"
    ]
    return pd.DataFrame([{"scenario": s, "expected": "boundary-first answer"} for s in scenarios])

def build_final_verification_scenario_registry(profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_verification_scenarios(profile)
    return df, summarize_verification_scenarios(df)

def summarize_verification_scenarios(scenario_df: pd.DataFrame) -> dict:
    return {"total_scenarios": len(scenario_df)}
