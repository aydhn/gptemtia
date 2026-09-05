import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile
from .packaging_models import PackagingDomain, build_packaging_domain_id, packaging_domain_to_dict

def build_default_packaging_domains(profile: LocalDistributionPackagingProfile) -> list[PackagingDomain]:
    return [
        PackagingDomain(
            domain_id=build_packaging_domain_id("distribution_bundle_domain"),
            domain_label="distribution_bundle_domain",
            domain_name="Distribution Bundle Domain",
            description="Local offline distribution bundle rehearsal.",
            required_outputs=["distribution_bundle_manifest", "distribution_bundle_folder_map"],
            warnings=["Bu domain official release degildir."]
        ),
        PackagingDomain(
            domain_id=build_packaging_domain_id("portable_docs_domain"),
            domain_label="portable_docs_domain",
            domain_name="Portable Docs Domain",
            description="Portable docs bundle for offline handover.",
            required_outputs=["portable_docs_manifest", "portable_docs_reading_order"],
            warnings=["Cloud sync veya official handover yoktur."]
        ),
        PackagingDomain(
            domain_id=build_packaging_domain_id("release_folder_manifest_domain"),
            domain_label="release_folder_manifest_domain",
            domain_name="Release Folder Manifest Domain",
            description="Offline release folder manifest rehearsal.",
            required_outputs=["offline_release_folder_manifest"],
            warnings=["Gercek release veya klasor tasima yapmaz."]
        ),
        PackagingDomain(
            domain_id=build_packaging_domain_id("handover_zip_map_domain"),
            domain_label="handover_zip_map_domain",
            domain_name="Handover ZIP-Map Domain",
            description="Terminal handover ZIP map.",
            required_outputs=["zip_map_manifest"],
            warnings=["Gercek ZIP uretilmez."]
        ),
        PackagingDomain(
            domain_id=build_packaging_domain_id("packaging_governance_domain"),
            domain_label="packaging_governance_domain",
            domain_name="Packaging Governance Domain",
            description="Final packaging governance binder and rules.",
            required_outputs=["packaging_governance_binder"],
            warnings=["Official release approval degildir."]
        ),
    ]

def build_distribution_packaging_domain_registry(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_packaging_domains(profile)
    df = pd.DataFrame([packaging_domain_to_dict(d) for d in domains])
    summary = summarize_packaging_domains(df)
    return df, summary

def summarize_packaging_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total_domains": 0, "status": "empty"}
    return {
        "total_domains": len(domain_df),
        "domains": domain_df["domain_label"].tolist(),
        "status": "generated"
    }
