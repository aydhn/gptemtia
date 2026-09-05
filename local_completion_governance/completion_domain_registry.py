import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile
from local_completion_governance.completion_models import CompletionDomain, build_completion_domain_id, completion_domain_to_dict

def build_default_completion_domains(profile: LocalCompletionGovernanceProfile) -> list[CompletionDomain]:
    return [
        CompletionDomain(
            domain_id=build_completion_domain_id("closure_synthesis_domain"),
            domain_label="closure_synthesis_domain",
            domain_name="Closure Synthesis",
            description="Local/offline project closure synthesis rehearsal.",
            required_outputs=["final_local_closure_synthesis.md"],
            warnings=["Not official project closure."]
        ),
        CompletionDomain(
            domain_id=build_completion_domain_id("end_state_certification_domain"),
            domain_label="end_state_certification_domain",
            domain_name="End-State Certification Rehearsal",
            description="Local/offline end-state certification documentation rehearsal.",
            required_outputs=["end_state_certification_rehearsal.md"],
            warnings=["Not a real certification."]
        ),
        CompletionDomain(
            domain_id=build_completion_domain_id("project_freeze_domain"),
            domain_label="project_freeze_domain",
            domain_name="Terminal Project Freeze Summary",
            description="Local/offline project freeze snapshot summary.",
            required_outputs=["terminal_project_freeze_summary.md"],
            warnings=["Not an official project freeze."]
        ),
        CompletionDomain(
            domain_id=build_completion_domain_id("acceptance_evidence_domain"),
            domain_label="acceptance_evidence_domain",
            domain_name="Offline Acceptance Evidence Pack",
            description="Local/offline acceptance evidence documentation.",
            required_outputs=["offline_acceptance_evidence_pack.md"],
            warnings=["Not official acceptance or legal proof."]
        )
    ]

def build_completion_governance_domain_registry(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_completion_domains(profile)
    df = pd.DataFrame([completion_domain_to_dict(d) for d in domains])
    return df, summarize_completion_domains(df)

def summarize_completion_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domains": domain_df["domain_name"].tolist() if not domain_df.empty else []
    }
