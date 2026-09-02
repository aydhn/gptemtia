"""
Archival Domain Registry.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archival_models import ArchivalDomain, build_archival_domain_id, archival_domain_to_dict

def build_default_archival_domains(profile: LocalArchivalProfile) -> list[ArchivalDomain]:
    return [
        ArchivalDomain(
            domain_id=build_archival_domain_id("seal_rehearsal_domain"),
            domain_label="seal_rehearsal_domain",
            domain_name="Seal Rehearsal Domain",
            description="Local/offline archival seal rehearsal context.",
            required_artifacts=["final_archival_seal_rehearsal_manifest"],
            warnings=["Not an official archival scope."]
        ),
        ArchivalDomain(
            domain_id=build_archival_domain_id("provenance_lockfile_domain"),
            domain_label="provenance_lockfile_domain",
            domain_name="Provenance Lockfile Domain",
            description="Local provenance lockfile domain.",
            required_artifacts=["local_provenance_lockfile"],
            warnings=["Not a legal lockfile."]
        )
    ]

def build_archival_domain_registry(profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_archival_domains(profile)
    df = pd.DataFrame([archival_domain_to_dict(d) for d in domains])
    summary = summarize_archival_domains(df)
    return df, summary

def summarize_archival_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df) if domain_df is not None else 0,
        "note": "This is a local/offline dry-run registry."
    }
