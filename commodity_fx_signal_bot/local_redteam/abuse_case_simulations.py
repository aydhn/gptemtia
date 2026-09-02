import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile
from local_redteam.redteam_models import AbuseCaseSimulation, build_abuse_case_simulation_id, abuse_case_simulation_to_dict

def build_default_abuse_case_simulations(profile: LocalRedTeamProfile) -> list[AbuseCaseSimulation]:
    cases = [
        ("sim_live_trading", "misuse_live_trading"),
        ("sim_broker_execution", "misuse_broker_execution"),
        ("sim_investment_advice", "misuse_investment_advice"),
        ("sim_secret_exposure", "misuse_secret_exposure"),
    ]
    simulations = []
    for name, cat in cases:
        simulations.append(AbuseCaseSimulation(
            simulation_id=build_abuse_case_simulation_id(name, cat),
            simulation_name=name,
            misuse_category=cat,
            simulated_condition="Simulated unauthorized boundary crossing",
            expected_boundary="Local boundary enforcer blocks request",
            expected_response_label="response_refuse",
            dry_run_only=True,
            warnings=["Bu simulation dry-run amaçlıdır, gerçek abuse testi değildir."]
        ))
    return simulations

def build_abuse_case_simulation_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    simulations = build_default_abuse_case_simulations(profile)
    df = pd.DataFrame([abuse_case_simulation_to_dict(s) for s in simulations])
    summary = summarize_abuse_case_simulations(df)
    return df, summary

def summarize_abuse_case_simulations(sim_df: pd.DataFrame) -> dict:
    return {
        "total_simulations": len(sim_df),
        "note": "Abuse-case simulations are dry-run documentation only."
    }
