import os
from pathlib import Path

def create_files():
    base_dir = Path("local_distribution_packaging")
    base_dir.mkdir(parents=True, exist_ok=True)

    # __init__.py
    with open(base_dir / "__init__.py", "w", encoding="utf-8") as f:
        f.write('"""Local Distribution Packaging Module for Phase 96"""\n')

    # packaging_config.py
    with open(base_dir / "packaging_config.py", "w", encoding="utf-8") as f:
        f.write('''from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalDistributionPackagingProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_archive_creation: bool = False
    allow_zip_creation: bool = False
    allow_tar_creation: bool = False
    allow_binary_artifact: bool = False
    allow_installer_creation: bool = False
    allow_executable_packaging: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_official_release: bool = False
    allow_official_handover: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_approval: bool = False
    allow_production_approval_claim: bool = False
    allow_official_acceptance_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_web_server: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_telemetry: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_documentation_export_outputs: bool = True
    scan_review_outputs: bool = True
    scan_atlas_outputs: bool = True
    scan_continuity_outputs: bool = True
    scan_preservation_outputs: bool = True
    scan_completion_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 750000
    max_rows: int = 300000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_distribution_packaging": LocalDistributionPackagingProfile(
        name="balanced_local_distribution_packaging",
        description="Genel amacli local/offline distribution bundle rehearsal, portable docs bundle ve packaging governance profili.",
        notes="Genel amacli local/offline distribution bundle rehearsal, portable docs bundle ve packaging governance profili."
    ),
    "portable_docs_focus": LocalDistributionPackagingProfile(
        name="portable_docs_focus",
        description="Portable docs bundle odakli",
        scan_docs=True,
        scan_reports=True,
        scan_generated_docs=True,
        scan_documentation_export_outputs=True,
        scan_review_outputs=True,
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        max_rows=200000,
        notes="Portable docs bundle, reading order, role map ve quickstart packet odakli profil."
    ),
    "release_folder_focus": LocalDistributionPackagingProfile(
        name="release_folder_focus",
        description="Offline release folder manifest odakli",
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_scripts=True,
        scan_tests=True,
        scan_generated_docs=True,
        scan_documentation_export_outputs=False,
        scan_review_outputs=False,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        max_rows=250000,
        notes="Offline release folder manifest, folder tree, inclusion/exclusion matrices ve ZIP-map odakli profil."
    ),
    "strict_packaging_safety": LocalDistributionPackagingProfile(
        name="strict_packaging_safety",
        description="Strict safety",
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Archive/ZIP/release/publish/deploy/binary/installer/live/broker/advice overclaim denetimini sikilastiran profil."
    )
}

def get_local_distribution_packaging_profile(name: str) -> LocalDistributionPackagingProfile:
    if name not in PROFILES:
        raise ConfigError(f"Bilinmeyen profile: {name}")
    return PROFILES[name]

def list_local_distribution_packaging_profiles(enabled_only: bool = True) -> list[LocalDistributionPackagingProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_local_distribution_packaging_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError(f"Profile {p.name}: language bos olmamali.")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError(f"Profile {p.name}: max_items ve max_rows pozitif olmali.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {p.name}: min_readiness_score ve min_quality_score 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {p.name}: dry_run_default True olmali.")
        if any([
            p.allow_real_archive_creation, p.allow_zip_creation, p.allow_tar_creation,
            p.allow_binary_artifact, p.allow_installer_creation, p.allow_package_publish,
            p.allow_docker_build_push, p.allow_git_tag, p.allow_cloud_upload,
            p.allow_deployment, p.allow_official_release, p.allow_official_handover,
            p.allow_legal_signoff, p.allow_compliance_approval, p.allow_production_approval_claim,
            p.allow_broker_readiness_claim, p.allow_live_trading_claim, p.allow_investment_advice,
            p.allow_dashboard_creation, p.allow_external_service, p.allow_vector_db,
            p.allow_file_modification, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite
        ]):
            raise ConfigError(f"Profile {p.name}: tehlikeli allow flagleri True olamaz.")

def get_default_local_distribution_packaging_profile() -> LocalDistributionPackagingProfile:
    return PROFILES["balanced_local_distribution_packaging"]
''')

    # packaging_labels.py
    with open(base_dir / "packaging_labels.py", "w", encoding="utf-8") as f:
        f.write('''class LabelError(Exception):
    pass

DOMAIN_LABELS = [
    "distribution_bundle_domain",
    "portable_docs_domain",
    "release_folder_manifest_domain",
    "handover_zip_map_domain",
    "packaging_governance_domain",
    "packaging_criteria_domain",
    "packaging_evidence_domain",
    "packaging_handoff_domain",
    "packaging_boundary_domain",
    "packaging_quality_domain",
    "quality_validation_domain",
    "unknown_packaging_domain"
]

STATUS_LABELS = [
    "packaging_rehearsal_ready",
    "packaging_rehearsal_ready_with_warnings",
    "packaging_rehearsal_missing",
    "packaging_rehearsal_blocked_by_safety",
    "packaging_rehearsal_needs_manual_review",
    "packaging_rehearsal_unknown"
]

ARTIFACT_LABELS = [
    "artifact_manifest_only",
    "artifact_documentation_only",
    "artifact_csv_registry",
    "artifact_markdown_packet",
    "artifact_txt_packet",
    "artifact_json_report",
    "artifact_html_rehearsal",
    "artifact_zip_map_not_zip",
    "artifact_unknown"
]

ROUTE_LABELS = [
    "package_route_operator",
    "package_route_analyst",
    "package_route_maintainer",
    "package_route_reviewer",
    "package_route_codex_agent",
    "package_route_future_reader",
    "package_route_unknown"
]

RISK_LABELS = [
    "packaging_critical_risk",
    "packaging_high_risk",
    "packaging_medium_risk",
    "packaging_low_risk",
    "packaging_info",
    "packaging_unknown_risk"
]

def list_packaging_domain_labels() -> list[str]:
    return list(DOMAIN_LABELS)

def list_packaging_status_labels() -> list[str]:
    return list(STATUS_LABELS)

def list_packaging_artifact_labels() -> list[str]:
    return list(ARTIFACT_LABELS)

def list_packaging_route_labels() -> list[str]:
    return list(ROUTE_LABELS)

def list_packaging_risk_labels() -> list[str]:
    return list(RISK_LABELS)

def validate_packaging_domain_label(label: str) -> None:
    if label not in DOMAIN_LABELS:
        raise LabelError(f"Invalid domain label: {label}")

def validate_packaging_status(label: str) -> None:
    if label not in STATUS_LABELS:
        raise LabelError(f"Invalid status label: {label}")

def validate_packaging_artifact_label(label: str) -> None:
    if label not in ARTIFACT_LABELS:
        raise LabelError(f"Invalid artifact label: {label}")

def validate_packaging_route(label: str) -> None:
    if label not in ROUTE_LABELS:
        raise LabelError(f"Invalid route label: {label}")

def validate_packaging_risk(label: str) -> None:
    if label not in RISK_LABELS:
        raise LabelError(f"Invalid risk label: {label}")
''')

    # packaging_models.py
    with open(base_dir / "packaging_models.py", "w", encoding="utf-8") as f:
        f.write('''from dataclasses import dataclass, asdict

@dataclass
class PackagingDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class DistributionBundleItem:
    bundle_id: str
    item_name: str
    source_ref: str
    bundle_area: str
    artifact_label: str
    include_rehearsal: bool
    exclusion_reason: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class PortableDocsItem:
    portable_doc_id: str
    doc_title: str
    source_ref: str
    route_label: str
    reading_priority: int
    artifact_label: str
    warnings: list[str]

@dataclass
class ReleaseFolderItem:
    folder_item_id: str
    folder_area: str
    folder_path: str
    intended_contents: list[str]
    artifact_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ZipMapItem:
    zip_map_id: str
    map_area: str
    folder_ref: str
    file_ref: str
    compression_status: str
    boundary_note: str
    warnings: list[str]

@dataclass
class PackagingFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_packaging_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}"

def build_distribution_bundle_item_id(item_name: str, source_ref: str) -> str:
    return f"bnd_{hash(item_name + source_ref)}"

def build_portable_docs_item_id(doc_title: str, source_ref: str) -> str:
    return f"pdoc_{hash(doc_title + source_ref)}"

def build_release_folder_item_id(folder_area: str, folder_path: str) -> str:
    return f"rfld_{hash(folder_area + folder_path)}"

def build_zip_map_item_id(folder_ref: str, file_ref: str) -> str:
    return f"zmap_{hash(folder_ref + file_ref)}"

def build_packaging_finding_id(title: str) -> str:
    return f"fnd_{hash(title)}"

def packaging_domain_to_dict(item: PackagingDomain) -> dict:
    return asdict(item)

def distribution_bundle_item_to_dict(item: DistributionBundleItem) -> dict:
    return asdict(item)

def portable_docs_item_to_dict(item: PortableDocsItem) -> dict:
    return asdict(item)

def release_folder_item_to_dict(item: ReleaseFolderItem) -> dict:
    return asdict(item)

def zip_map_item_to_dict(item: ZipMapItem) -> dict:
    return asdict(item)

def packaging_finding_to_dict(item: PackagingFinding) -> dict:
    return asdict(item)
''')

    # packaging_domain_registry.py
    with open(base_dir / "packaging_domain_registry.py", "w", encoding="utf-8") as f:
        f.write('''import pandas as pd
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
''')

if __name__ == "__main__":
    create_files()
    print("Chunk 1 complete")
