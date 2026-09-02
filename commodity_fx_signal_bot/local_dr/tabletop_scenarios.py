
import pandas as pd
from local_dr.dr_config import LocalDRProfile
from local_dr.dr_models import TabletopScenario

def build_tabletop_scenarios_for_domain(domain_label: str, profile: LocalDRProfile) -> list[TabletopScenario]:
    return [TabletopScenario(scenario_id="sc1", scenario_name="generated report missing", domain_label=domain_label, description="", failure_mode="missing", expected_manual_response="", status="scenario_ready_for_tabletop", warnings=[])]

def classify_tabletop_scenario_status(row: pd.Series, profile: LocalDRProfile) -> str:
    return "scenario_ready_for_tabletop"

def build_dr_tabletop_scenario_registry(domain_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    scenarios = []
    for _, row in domain_df.iterrows():
        scenarios.extend(build_tabletop_scenarios_for_domain(row["domain_label"], profile))
    df = pd.DataFrame([s.__dict__ for s in scenarios])
    return df, {"total_scenarios": len(scenarios)}

def summarize_tabletop_scenarios(scenario_df: pd.DataFrame) -> dict:
    return {"total": len(scenario_df)}
