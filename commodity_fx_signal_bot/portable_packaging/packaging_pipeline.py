from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any, Optional
import json

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from portable_packaging.packaging_config import PortablePackagingProfile, get_default_portable_packaging_profile
from portable_packaging.environment_snapshot import build_environment_snapshot
from portable_packaging.dependency_inventory import build_dependency_inventory
from portable_packaging.requirements_export import build_requirements_minimal_export, build_requirements_frozen_export, build_optional_dependencies_note, save_requirements_exports
from portable_packaging.install_verification import build_install_verification_report
from portable_packaging.import_verification import verify_core_module_imports
from portable_packaging.script_verification import build_script_availability_verification
from portable_packaging.config_verification import build_config_template_verification
from portable_packaging.source_policy import build_source_inclusion_policy, build_source_exclusion_policy
from portable_packaging.bundle_manifest import scan_bundle_artifacts, build_portable_bundle_manifest, build_portable_bundle_manifest_json, save_portable_bundle_manifest
from portable_packaging.archive_manifest import build_archive_plan_from_bundle_manifest, build_archive_manifest_json, save_archive_manifest_json
from portable_packaging.reproducible_setup import build_reproducible_setup_guide, save_reproducible_setup_guide
from portable_packaging.environment_drift import build_environment_drift_report
from portable_packaging.packaging_safety import build_packaging_safety_report
from portable_packaging.packaging_quality import build_packaging_quality_report
from portable_packaging.packaging_report_builder import (
    build_environment_snapshot_markdown_report,
    build_dependency_inventory_markdown_report,
    build_requirements_export_markdown_report,
    build_install_verification_markdown_report,
    build_portable_bundle_manifest_markdown_report,
    build_packaging_quality_markdown_report,
    build_packaging_status_markdown_report
)

class PortablePackagingPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[PortablePackagingProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_portable_packaging_profile()

    def build_environment_snapshot_report(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        snapshot, packages_df, summary = build_environment_snapshot()

        md_report = build_environment_snapshot_markdown_report(summary, packages_df)

        if save:
            self.data_lake.save_environment_snapshot(
                snapshot.__dict__, packages_df, summary
            )
            # Dummy saving to output dirs for scripts

        return {"packages": packages_df}, summary

    def build_dependency_inventory_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        _, packages_df, _ = build_environment_snapshot()
        df, summary = build_dependency_inventory(self.project_root, packages_df)

        if save:
            self.data_lake.save_dependency_inventory(df, summary)

        return df, summary

    def build_requirements_export_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        _, packages_df, _ = build_environment_snapshot()
        dep_df, _ = build_dependency_inventory(self.project_root, packages_df)

        min_txt, _ = build_requirements_minimal_export(dep_df)
        frozen_txt, _ = build_requirements_frozen_export(packages_df)
        notes_txt = build_optional_dependencies_note(dep_df)

        exports = {
            "requirements_minimal.txt": min_txt,
            "requirements_frozen_local.txt": frozen_txt,
            "requirements_notes.md": notes_txt
        }

        paths = ProjectPaths()
        df, summary = save_requirements_exports(paths.PORTABLE_BUNDLE_SETUP_DIR, exports)

        if save:
            self.data_lake.save_requirements_export_report(df, summary)

        return df, summary

    def build_install_verification_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        df, summary = build_install_verification_report(self.project_root)

        if save:
            self.data_lake.save_install_verification_report(df, summary)

        return df, summary

    def build_portable_bundle_manifest_report(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        artifact_df, summary = scan_bundle_artifacts(self.project_root, self.profile)
        manifest = build_portable_bundle_manifest(self.profile, artifact_df, None)
        manifest_json = build_portable_bundle_manifest_json(manifest, artifact_df)

        paths = ProjectPaths()
        if save:
            out = paths.PORTABLE_BUNDLE_MANIFESTS_DIR / "portable_bundle_manifest.json"
            save_portable_bundle_manifest(manifest_json, out)
            self.data_lake.save_portable_bundle_manifest(manifest_json)
            self.data_lake.save_bundle_artifact_inventory(artifact_df, summary)

        return {"artifacts": artifact_df}, summary

    def build_reproducible_setup_guide(
        self,
        save: bool = True,
    ) -> Tuple[str, Dict[str, Any]]:
        _, packages_df, _ = build_environment_snapshot()
        dep_df, _ = build_dependency_inventory(self.project_root, packages_df)
        inst_df, _ = build_install_verification_report(self.project_root)

        md, summary = build_reproducible_setup_guide(None, dep_df, inst_df, self.profile)

        paths = ProjectPaths()
        if save:
            out = paths.DOCS_PORTABLE_PACKAGING_DIR / "REPRODUCIBLE_SETUP_GUIDE.md"
            save_reproducible_setup_guide(md, out)
            self.data_lake.save_reproducible_setup_guide(md, summary)

        return md, summary

    def build_packaging_status(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        df = pd.DataFrame([{"status": "ok"}])
        summary = {"status": "ok"}
        return df, summary
