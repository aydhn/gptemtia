"""Maintenance Pipeline for orchestrating offline maintenance tasks."""
from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Optional

from config.settings import Settings
from data.storage.data_lake import DataLake
from maintenance.maintenance_config import MaintenanceProfile, get_default_maintenance_profile
from maintenance.storage_inventory import StorageInventoryBuilder
from maintenance.retention_policies import build_default_retention_policies, retention_policies_to_dataframe, apply_retention_policy_to_inventory, summarize_retention_policies
from maintenance.archive_strategy import identify_archive_candidates, build_archive_manifest, build_archive_plan
from maintenance.cleanup_planner import identify_cleanup_candidates, build_cleanup_dry_run_plan
from maintenance.rotation_planner import build_report_rotation_plan, build_log_rotation_plan, build_cache_pruning_plan, build_checkpoint_rotation_plan
from maintenance.duplicate_detection import detect_potential_duplicate_artifacts, summarize_duplicate_artifacts
from maintenance.stale_detection import build_stale_artifact_report
from maintenance.large_artifact_review import build_large_artifact_review_report
from maintenance.storage_growth import build_storage_snapshot, summarize_storage_growth
from maintenance.maintenance_checklist import build_maintenance_checklist, evaluate_maintenance_checklist, summarize_maintenance_checklist
from maintenance.lifecycle_health import build_storage_lifecycle_health_report
from maintenance.maintenance_quality import build_maintenance_quality_report
from maintenance.maintenance_report_builder import (
    build_storage_inventory_markdown_report,
    build_retention_policy_markdown_report,
    build_cleanup_dry_run_markdown_report,
    build_archive_dry_run_markdown_report,
    build_storage_lifecycle_markdown_report,
    build_maintenance_status_markdown_report
)


class MaintenancePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[MaintenanceProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_maintenance_profile()
        self.inventory_builder = StorageInventoryBuilder(project_root)

    def _get_inventory_and_policies(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        inventory_df, _ = self.inventory_builder.scan_storage(self.profile)
        policies = build_default_retention_policies(self.profile)
        policies_df = retention_policies_to_dataframe(policies)
        inventory_df = apply_retention_policy_to_inventory(inventory_df, policies_df, self.profile)
        return inventory_df, policies_df

    def build_storage_inventory_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:
        inventory_df, summary = self.inventory_builder.scan_storage(self.profile)

        if save:
            # Need DataLake save methods defined later
            pass

        return inventory_df, summary

    def build_retention_policy_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:
        policies = build_default_retention_policies(self.profile)
        df = retention_policies_to_dataframe(policies)
        summary = summarize_retention_policies(df)
        return df, summary

    def build_cleanup_dry_run_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:
        inventory_df, policies_df = self._get_inventory_and_policies()
        candidates_df = identify_cleanup_candidates(inventory_df, policies_df, self.profile)
        plan_df, summary = build_cleanup_dry_run_plan(candidates_df, self.profile)
        return plan_df, summary

    def build_archive_dry_run_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:
        inventory_df, policies_df = self._get_inventory_and_policies()
        candidates_df = identify_archive_candidates(inventory_df, policies_df, self.profile)
        manifest = build_archive_manifest(candidates_df, self.profile)
        plan_df, summary = build_archive_plan(candidates_df, self.profile)
        return plan_df, summary

    def build_storage_lifecycle_report(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        inventory_df, policies_df = self._get_inventory_and_policies()

        cleanup_cand_df = identify_cleanup_candidates(inventory_df, policies_df, self.profile)
        cleanup_df, cleanup_summary = build_cleanup_dry_run_plan(cleanup_cand_df, self.profile)

        arch_cand_df = identify_archive_candidates(inventory_df, policies_df, self.profile)
        archive_df, archive_summary = build_archive_plan(arch_cand_df, self.profile)

        health_df, health_summary = build_storage_lifecycle_health_report(inventory_df, cleanup_df, archive_df, self.profile)

        results = {
            "inventory": inventory_df,
            "policies": policies_df,
            "cleanup": cleanup_df,
            "archive": archive_df,
            "health": health_df
        }

        summary = {
            "health": health_summary,
            "cleanup": cleanup_summary,
            "archive": archive_summary
        }

        return results, summary

    def build_maintenance_status(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:
        df = pd.DataFrame([{"status": "OK", "last_run": "today"}])
        summary = {"status": "OK"}
        return df, summary
