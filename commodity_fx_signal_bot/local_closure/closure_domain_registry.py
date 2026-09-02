
import pandas as pd
from local_closure.closure_config import LocalClosureProfile
from local_closure.closure_models import ClosureDomain, build_closure_domain_id, closure_domain_to_dict

def build_default_closure_domains(profile: LocalClosureProfile) -> list[ClosureDomain]:
    domains = [
        ClosureDomain(
            domain_id=build_closure_domain_id("meta_review_domain"),
            domain_label="meta_review_domain",
            domain_name="Final Meta Review",
            description="Overall project review in local/offline context.",
            required_outputs=["final_meta_review_report"],
            warnings=["Not an official closure."]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("lessons_learned_domain"),
            domain_label="lessons_learned_domain",
            domain_name="Lessons Learned",
            description="Collected insights and observations.",
            required_outputs=["lessons_learned_compendium"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("roadmap_domain"),
            domain_label="roadmap_domain",
            domain_name="Future Roadmap",
            description="Future work items backlog.",
            required_outputs=["future_roadmap_backlog"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("governance_rehearsal_domain"),
            domain_label="governance_rehearsal_domain",
            domain_name="Governance Rehearsal",
            description="Post-project governance rehearsal.",
            required_outputs=["post_project_governance_rehearsal_guide"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("closure_dossier_domain"),
            domain_label="closure_dossier_domain",
            domain_name="Closure Dossier",
            description="Final local closure dossier.",
            required_outputs=["v1_local_closure_dossier"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("recap_domain"),
            domain_label="recap_domain",
            domain_name="Closure Recaps",
            description="Executive and technical summaries.",
            required_outputs=["closure_executive_recap", "closure_technical_recap"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("unresolved_items_domain"),
            domain_label="unresolved_items_domain",
            domain_name="Unresolved Items",
            description="Tracking items not resolved in V1.",
            required_outputs=["closure_unresolved_items_register"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("maintenance_aftercare_domain"),
            domain_label="maintenance_aftercare_domain",
            domain_name="Maintenance and Aftercare",
            description="Post-project maintenance instructions.",
            required_outputs=["closure_maintenance_calendar_rehearsal", "closure_handoff_aftercare_guide"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("quality_validation_domain"),
            domain_label="quality_validation_domain",
            domain_name="Quality Validation",
            description="Final validation checks.",
            required_outputs=["closure_validation_report", "closure_quality_report"],
            warnings=[]
        )
    ]
    return domains

def build_closure_domain_registry(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_closure_domains(profile)
    df = pd.DataFrame([closure_domain_to_dict(d) for d in domains])
    summary = summarize_closure_domains(df)
    return df, summary

def summarize_closure_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df.empty:
        return {"total_domains": 0, "status": "empty"}
    return {
        "total_domains": len(domain_df),
        "domains": domain_df["domain_label"].tolist(),
        "status": "generated"
    }
