"""Domain registry."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile
from .export_models import DocumentationExportDomain, build_documentation_export_domain_id

def build_default_documentation_export_domains(profile: LocalDocumentationExportProfile) -> list[DocumentationExportDomain]:
    return [
        DocumentationExportDomain(
            domain_id=build_documentation_export_domain_id("static_site_export_domain"),
            domain_label="static_site_export_domain",
            domain_name="Static Site Export Domain",
            description="Local, offline static site rehearsal domain.",
            required_outputs=["static_site_export_manifest.csv"],
            warnings=["Bu domain official documentation release degildir."]
        ),
        DocumentationExportDomain(
            domain_id=build_documentation_export_domain_id("offline_html_pack_domain"),
            domain_label="offline_html_pack_domain",
            domain_name="Offline HTML Pack",
            description="Offline readable HTML pack without web server.",
            required_outputs=["offline_html_page_registry.csv"],
            warnings=["Gercek dashboard degildir."]
        )
    ]

def build_documentation_export_domain_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_documentation_export_domains(profile)
    df = pd.DataFrame([d.__dict__ for d in domains])
    return df, summarize_documentation_export_domains(df)

def summarize_documentation_export_domains(domain_df: pd.DataFrame) -> dict:
    return {"domain_count": len(domain_df)}
