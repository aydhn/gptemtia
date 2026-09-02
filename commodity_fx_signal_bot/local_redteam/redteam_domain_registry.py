import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile
from local_redteam.redteam_models import RedTeamDomain, build_redteam_domain_id, redteam_domain_to_dict

def build_default_redteam_domains(profile: LocalRedTeamProfile) -> list[RedTeamDomain]:
    labels = [
        "redteam_rehearsal_domain", "misuse_scenario_domain", "abuse_case_simulation_domain",
        "adversarial_prompt_safety_domain", "prompt_injection_risk_domain", "unsafe_output_domain",
        "forbidden_capability_domain", "boundary_violation_domain", "safety_response_domain",
        "manual_escalation_domain", "safety_assurance_domain", "safety_coverage_domain",
        "quality_validation_domain"
    ]
    domains = []
    for label in labels:
        domains.append(RedTeamDomain(
            domain_id=build_redteam_domain_id(label),
            domain_label=label,
            domain_name=label.replace("_", " ").title(),
            description=f"Offline/local {label.replace('_', ' ')} logic.",
            required_outputs=[f"{label}_output_1", f"{label}_output_2"],
            warnings=["Bu domain offline/local dokümantasyon içindir, gerçek attack/exploit içermez."]
        ))
    return domains

def build_redteam_domain_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_redteam_domains(profile)
    df = pd.DataFrame([redteam_domain_to_dict(d) for d in domains])
    summary = summarize_redteam_domains(df)
    return df, summary

def summarize_redteam_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domains_listed": domain_df["domain_label"].tolist() if not domain_df.empty else [],
        "note": "Domain registry is for offline/local rehearsal only."
    }
