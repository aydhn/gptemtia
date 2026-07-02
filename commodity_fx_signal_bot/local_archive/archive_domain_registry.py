import pandas as pd
from typing import Tuple, Dict, List
from .archive_config import LocalArchiveProfile
from .archive_models import ArchiveDomain, build_archive_domain_id, archive_domain_to_dict

def build_default_archive_domains(profile: LocalArchiveProfile) -> List[ArchiveDomain]:
    return [
        ArchiveDomain(
            domain_id=build_archive_domain_id("documentation"),
            domain_name="documentation",
            domain_label="documentation_archive",
            description="Project README, guides, manual and generated docs",
            retention_label="retain_long_term_manual",
            required_artifacts=["README.md", "docs/"],
            warnings=[]
        ),
        ArchiveDomain(
            domain_id=build_archive_domain_id("report"),
            domain_name="report",
            domain_label="report_archive",
            description="Generated reports (PDF, Markdown, CSV)",
            retention_label="retain_long_term_manual",
            required_artifacts=["reports/"],
            warnings=[]
        ),
        ArchiveDomain(
            domain_id=build_archive_domain_id("datalake"),
            domain_name="datalake",
            domain_label="datalake_archive",
            description="Data lake manifests and offline datasets",
            retention_label="retain_long_term_manual",
            required_artifacts=["data/lake/"],
            warnings=["DataLake files can be large, hash may be skipped"]
        ),
        ArchiveDomain(
            domain_id=build_archive_domain_id("config"),
            domain_name="config",
            domain_label="config_archive",
            description="Settings and project configuration",
            retention_label="retain_long_term_manual",
            required_artifacts=["config/", "pyproject.toml"],
            warnings=[]
        ),
        ArchiveDomain(
            domain_id=build_archive_domain_id("script"),
            domain_name="script",
            domain_label="script_archive",
            description="Executable scripts",
            retention_label="retain_long_term_manual",
            required_artifacts=["scripts/"],
            warnings=[]
        ),
        ArchiveDomain(
            domain_id=build_archive_domain_id("test"),
            domain_name="test",
            domain_label="test_archive",
            description="Test suites and fixtures",
            retention_label="retain_long_term_manual",
            required_artifacts=["tests/"],
            warnings=[]
        ),
        ArchiveDomain(
            domain_id=build_archive_domain_id("security"),
            domain_name="security",
            domain_label="security_archive",
            description="Security boundaries, secret reports",
            retention_label="retain_long_term_manual",
            required_artifacts=[],
            warnings=["Must not contain raw secrets"]
        ),
        ArchiveDomain(
            domain_id=build_archive_domain_id("cross_layer"),
            domain_name="cross_layer",
            domain_label="cross_layer_archive",
            description="Evidence, readiness, consistency and metadata",
            retention_label="retain_long_term_manual",
            required_artifacts=[],
            warnings=[]
        )
    ]

def build_archive_domain_registry(profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    domains = build_default_archive_domains(profile)
    df = pd.DataFrame([archive_domain_to_dict(d) for d in domains])
    summary = summarize_archive_domains(df)
    return df, summary

def summarize_archive_domains(domain_df: pd.DataFrame) -> Dict:
    if domain_df.empty:
        return {
            "total_domains": 0,
            "domains_with_warnings": 0,
            "status": "empty"
        }
    return {
        "total_domains": len(domain_df),
        "domains_with_warnings": int((domain_df['warnings'].apply(lambda x: len(x) if isinstance(x, list) else 0) > 0).sum()),
        "status": "generated",
        "notice": "Archive domains are for manual scoping. Not an official retention scope."
    }
