import pandas as pd
from typing import Tuple, List, Dict
from .synthesis_config import LocalSynthesisProfile
from .synthesis_models import PhaseFamily, build_phase_family_id, phase_family_to_dict

def build_default_phase_families(profile: LocalSynthesisProfile) -> List[PhaseFamily]:
    families = [
        PhaseFamily(build_phase_family_id("core_research_family"), "core_research_family", "Core Research", "Phase 1-10", "Core market research", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("data_storage_family"), "data_storage_family", "Data Storage", "Phase 11-20", "Data Lake and feature store", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("reporting_family"), "reporting_family", "Reporting", "Phase 21-30", "Reports", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("safety_governance_family"), "safety_governance_family", "Safety Governance", "Phase 31-40", "Safety", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("metadata_evidence_family"), "metadata_evidence_family", "Metadata Evidence", "Phase 41-50", "Metadata", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("graph_timeline_family"), "graph_timeline_family", "Graph Timeline", "Phase 51-55", "Graph and timeline", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("consistency_readiness_family"), "consistency_readiness_family", "Consistency Readiness", "Phase 56-60", "Consistency", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("maintenance_archive_dr_family"), "maintenance_archive_dr_family", "Maintenance Archive DR", "Phase 61-65", "DR and Archive", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("training_briefing_family"), "training_briefing_family", "Training Briefing", "Phase 66-70", "Training", [], ["Not complete production"]),
        PhaseFamily(build_phase_family_id("synthesis_family"), "synthesis_family", "Synthesis", "Phase 71-75", "Synthesis", [], ["Not complete production"])
    ]
    return families

def build_phase_family_registry(profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    families = build_default_phase_families(profile)
    df = pd.DataFrame([phase_family_to_dict(f) for f in families])
    summary = summarize_phase_families(df)
    return df, summary

def summarize_phase_families(family_df: pd.DataFrame) -> Dict:
    return {"count": len(family_df), "manual_review": "Required"}
