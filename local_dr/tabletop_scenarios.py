import pandas as pd
from local_dr.dr_config import LocalDRProfile
from local_dr.dr_models import TabletopScenario, build_tabletop_scenario_id, tabletop_scenario_to_dict

def build_tabletop_scenarios_for_domain(domain_label: str, profile: LocalDRProfile) -> list[TabletopScenario]:
    return [
        TabletopScenario(
            scenario_id=build_tabletop_scenario_id("Data Loss", domain_label),
            domain_label=domain_label,
            scenario_name="Data Loss",
            status="defined",
            details="Tabletop scenario for data loss"
        )
    ]

def classify_tabletop_scenario_status(row: pd.Series, profile: LocalDRProfile) -> str:
    return row.get("status", "defined")

def build_dr_tabletop_scenario_registry(domain_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    scenarios = []
    if "domain_label" in domain_df:
        for domain_label in domain_df["domain_label"]:
            scenarios.extend(build_tabletop_scenarios_for_domain(domain_label, profile))
    df = pd.DataFrame([tabletop_scenario_to_dict(s) for s in scenarios])
    summary = summarize_tabletop_scenarios(df)
    return df, summary

def summarize_tabletop_scenarios(scenario_df: pd.DataFrame) -> dict:
    return {
        "total_scenarios": len(scenario_df),
        "tested_scenarios": len(scenario_df[scenario_df.get("status") == "tested"]) if "status" in scenario_df else 0,
    }
