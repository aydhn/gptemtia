import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def detect_missing_redteam_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_domain"}])

def detect_missing_misuse_scenarios(scenario_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_scenario"}])

def detect_missing_safety_coverage(coverage_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_coverage"}])

def detect_unreviewed_blindspots(blindspot_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "unreviewed_blindspot"}])

def build_redteam_gap_register(domain_df: pd.DataFrame, scenario_df: pd.DataFrame, coverage_df: pd.DataFrame, blindspot_df: pd.DataFrame, profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    d1 = detect_missing_redteam_domains(domain_df)
    d2 = detect_missing_misuse_scenarios(scenario_df)
    d3 = detect_missing_safety_coverage(coverage_df)
    d4 = detect_unreviewed_blindspots(blindspot_df)
    df = pd.concat([d1, d2, d3, d4], ignore_index=True) if not all(x.empty for x in [d1, d2, d3, d4]) else pd.DataFrame()
    return df, summarize_redteam_gaps(df)

def summarize_redteam_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total": len(gap_df)}
