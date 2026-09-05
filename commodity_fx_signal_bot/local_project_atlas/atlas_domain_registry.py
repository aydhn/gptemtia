"""Atlas domain registry module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import AtlasDomain, build_atlas_domain_id, atlas_domain_to_dict

def build_default_atlas_domains(profile: LocalProjectAtlasProfile) -> list[AtlasDomain]:
    domains = []
    labels = [
        "meta_index_domain", "universal_navigation_domain", "cross_phase_lookup_domain",
        "semantic_toc_domain", "terminal_project_atlas_domain", "family_map_domain",
        "phase_map_domain", "route_map_domain", "glossary_domain", "crosswalk_domain",
        "quality_validation_domain"
    ]
    for lbl in labels:
        domains.append(AtlasDomain(
            domain_id=build_atlas_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"{lbl} domain for offline project atlas. Not enterprise search or official index.",
            required_outputs=["none"],
            warnings=["Offline context only."]
        ))
    return domains

def build_atlas_domain_registry(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_atlas_domains(profile)
    df = pd.DataFrame([atlas_domain_to_dict(d) for d in domains])
    summary = summarize_atlas_domains(df)
    return df, summary

def summarize_atlas_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domain_labels": domain_df["domain_label"].unique().tolist() if not domain_df.empty else []
    }
