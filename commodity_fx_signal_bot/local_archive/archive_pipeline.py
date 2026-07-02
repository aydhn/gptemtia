from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Optional
from config.settings import Settings
from data.storage.data_lake import DataLake
from .archive_config import LocalArchiveProfile, get_default_local_archive_profile
from .archive_domain_registry import build_archive_domain_registry
from .archive_item_registry import build_archive_item_registry
from .archive_candidate_inventory import build_archive_candidate_inventory
from .archive_exclusion_registry import build_archive_exclusion_registry
from .snapshot_catalog import build_project_snapshot_catalog
from .cold_storage_manifest import build_cold_storage_manifest, build_cold_storage_manifest_index
from .retention_policy import build_retention_policy_registry
from .retention_review import build_retention_review_checklist
from .hash_manifest import build_archive_hash_manifest
from .integrity_verification import build_archive_integrity_verification_plan
from .restore_readiness import build_archive_restore_readiness_checklist
from .provenance_registry import build_archive_provenance_registry
from .dependency_snapshot import build_archive_dependency_snapshot_summary
from .documentation_archive import build_documentation_archive_index
from .report_archive import build_report_archive_index
from .datalake_archive import build_datalake_archive_index
from .cross_layer_archive import build_cross_layer_archive_index
from .security_archive_boundary import build_security_sensitive_archive_boundary_report
from .secret_exclusion_verification import build_secret_exclusion_verification_report
from .archive_gaps import build_archive_gap_register
from .archive_risks import build_archive_risk_summary
from .preservation_binder import build_long_horizon_preservation_binder
from .archive_validation import build_archive_validation_report
from .archive_quality import build_archive_quality_report

class LocalArchivePipeline:
    def __init__(self, data_lake: DataLake, settings: Settings, project_root: Path, profile: Optional[LocalArchiveProfile] = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_archive_profile()
        self.domain_df = pd.DataFrame()
        self.item_df = pd.DataFrame()
        self.candidate_df = pd.DataFrame()
        self.exclusion_df = pd.DataFrame()
        self.snapshot_df = pd.DataFrame()
        self.manifest = {}
        self.manifest_index_df = pd.DataFrame()
        self.gap_df = pd.DataFrame()
        self.boundary_df = pd.DataFrame()
        self.verification_df = pd.DataFrame()
        self.risk_df = pd.DataFrame()

    def _ensure_base_data(self):
        if self.domain_df.empty: self.domain_df, _ = build_archive_domain_registry(self.profile)
        if self.item_df.empty: self.item_df, _ = build_archive_item_registry(self.project_root, self.domain_df, self.profile)

    def build_archive_domain_registry(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        self._ensure_base_data()
        self.candidate_df, _ = build_archive_candidate_inventory(self.project_root, self.profile)
        self.exclusion_df, _ = build_archive_exclusion_registry(self.project_root, self.profile)
        dfs = {"domain": self.domain_df, "item": self.item_df, "candidate": self.candidate_df, "exclusion": self.exclusion_df}
        if save:
            if hasattr(self.data_lake, 'save_archive_domain_registry'): self.data_lake.save_archive_domain_registry(self.domain_df)
            if hasattr(self.data_lake, 'save_archive_item_registry'): self.data_lake.save_archive_item_registry(self.item_df)
            if hasattr(self.data_lake, 'save_archive_candidate_inventory'): self.data_lake.save_archive_candidate_inventory(self.candidate_df)
            if hasattr(self.data_lake, 'save_archive_exclusion_registry'): self.data_lake.save_archive_exclusion_registry(self.exclusion_df)
        return dfs, {"status": "success"}

    def build_project_snapshot_catalog(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        self._ensure_base_data()
        self.snapshot_df, _ = build_project_snapshot_catalog(self.item_df, self.profile)
        doc_idx, _ = build_documentation_archive_index(self.project_root, self.profile)
        rep_idx, _ = build_report_archive_index(self.project_root, self.profile)
        lake_idx, _ = build_datalake_archive_index(self.project_root, self.profile)
        cross_idx, _ = build_cross_layer_archive_index(self.project_root, self.profile)
        dfs = {"snapshot": self.snapshot_df, "doc_idx": doc_idx, "rep_idx": rep_idx, "lake_idx": lake_idx, "cross_idx": cross_idx}
        if save:
            if hasattr(self.data_lake, 'save_project_snapshot_catalog'): self.data_lake.save_project_snapshot_catalog(self.snapshot_df)
            if hasattr(self.data_lake, 'save_documentation_archive_index'): self.data_lake.save_documentation_archive_index(doc_idx)
            if hasattr(self.data_lake, 'save_report_archive_index'): self.data_lake.save_report_archive_index(rep_idx)
            if hasattr(self.data_lake, 'save_datalake_archive_index'): self.data_lake.save_datalake_archive_index(lake_idx)
            if hasattr(self.data_lake, 'save_cross_layer_archive_index'): self.data_lake.save_cross_layer_archive_index(cross_idx)
        return dfs, {"status": "success"}

    def build_cold_storage_manifest(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        self._ensure_base_data()
        if self.snapshot_df.empty: self.snapshot_df, _ = build_project_snapshot_catalog(self.item_df, self.profile)
        self.manifest, _ = build_cold_storage_manifest(self.item_df, self.snapshot_df, self.profile)
        self.manifest_index_df, _ = build_cold_storage_manifest_index(self.item_df, self.profile)
        ret_pol, _ = build_retention_policy_registry(self.domain_df, self.profile)
        ret_rev, _ = build_retention_review_checklist(ret_pol, self.item_df, self.profile)
        dfs = {"manifest_index": self.manifest_index_df, "retention_policy": ret_pol, "retention_review": ret_rev}
        if save:
            if hasattr(self.data_lake, 'save_cold_storage_manifest'): self.data_lake.save_cold_storage_manifest(self.manifest)
            if hasattr(self.data_lake, 'save_cold_storage_manifest_index'): self.data_lake.save_cold_storage_manifest_index(self.manifest_index_df)
            if hasattr(self.data_lake, 'save_retention_policy_registry'): self.data_lake.save_retention_policy_registry(ret_pol)
            if hasattr(self.data_lake, 'save_retention_review_checklist'): self.data_lake.save_retention_review_checklist(ret_rev)
        return dfs, {"status": "success"}

    def build_archive_integrity_plan(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        self._ensure_base_data()
        if self.exclusion_df.empty: self.exclusion_df, _ = build_archive_exclusion_registry(self.project_root, self.profile)
        hash_df, _ = build_archive_hash_manifest(self.item_df, self.project_root, self.profile)
        plan_df, _ = build_archive_integrity_verification_plan(self.item_df, self.profile)
        readiness_df, _ = build_archive_restore_readiness_checklist(self.item_df, self.manifest, self.profile)
        prov_df, _ = build_archive_provenance_registry(self.item_df, self.profile)
        dep_df, _ = build_archive_dependency_snapshot_summary(self.project_root, self.profile)
        self.boundary_df, _ = build_security_sensitive_archive_boundary_report(self.project_root, self.profile)
        self.verification_df, _ = build_secret_exclusion_verification_report(self.exclusion_df, self.item_df, self.profile)
        dfs = {"hash": hash_df, "plan": plan_df, "readiness": readiness_df, "provenance": prov_df, "dependency": dep_df, "boundary": self.boundary_df, "verification": self.verification_df}
        if save:
            if hasattr(self.data_lake, 'save_archive_hash_manifest'): self.data_lake.save_archive_hash_manifest(hash_df)
            if hasattr(self.data_lake, 'save_archive_integrity_verification_plan'): self.data_lake.save_archive_integrity_verification_plan(plan_df)
            if hasattr(self.data_lake, 'save_archive_restore_readiness_checklist'): self.data_lake.save_archive_restore_readiness_checklist(readiness_df)
            if hasattr(self.data_lake, 'save_archive_provenance_registry'): self.data_lake.save_archive_provenance_registry(prov_df)
            if hasattr(self.data_lake, 'save_archive_dependency_snapshot_summary'): self.data_lake.save_archive_dependency_snapshot_summary(dep_df)
            if hasattr(self.data_lake, 'save_security_sensitive_archive_boundary_report'): self.data_lake.save_security_sensitive_archive_boundary_report(self.boundary_df)
            if hasattr(self.data_lake, 'save_secret_exclusion_verification_report'): self.data_lake.save_secret_exclusion_verification_report(self.verification_df)
        return dfs, {"status": "success"}

    def build_preservation_binder(self, save: bool = True) -> Tuple[str, Dict]:
        self._ensure_base_data()
        if self.snapshot_df.empty: self.snapshot_df, _ = build_project_snapshot_catalog(self.item_df, self.profile)
        if self.manifest_index_df.empty: self.manifest_index_df, _ = build_cold_storage_manifest_index(self.item_df, self.profile)
        if self.exclusion_df.empty: self.exclusion_df, _ = build_archive_exclusion_registry(self.project_root, self.profile)
        self.gap_df, _ = build_archive_gap_register(self.item_df, self.snapshot_df, self.manifest_index_df, self.exclusion_df, self.profile)
        if self.boundary_df.empty: self.boundary_df, _ = build_security_sensitive_archive_boundary_report(self.project_root, self.profile)
        if self.verification_df.empty: self.verification_df, _ = build_secret_exclusion_verification_report(self.exclusion_df, self.item_df, self.profile)
        self.risk_df, _ = build_archive_risk_summary(self.gap_df, self.boundary_df, self.verification_df, self.profile)
        binder_text, summary = build_long_horizon_preservation_binder(self.domain_df, self.item_df, self.snapshot_df, self.manifest, self.risk_df, self.profile)
        if save:
            if hasattr(self.data_lake, 'save_archive_gap_register'): self.data_lake.save_archive_gap_register(self.gap_df)
            if hasattr(self.data_lake, 'save_archive_risk_summary'): self.data_lake.save_archive_risk_summary(self.risk_df)
            if hasattr(self.data_lake, 'save_long_horizon_preservation_binder'): self.data_lake.save_long_horizon_preservation_binder(binder_text)
        return binder_text, summary

    def build_archive_quality_report(self, save: bool = True) -> Tuple[Dict, Dict]:
        val_df, val_summary = build_archive_validation_report({"domain_df": self.domain_df, "item_df": self.item_df}, self.profile)
        qual_report = build_archive_quality_report(summary={"validation": val_summary}, domain_df=self.domain_df, item_df=self.item_df, risk_df=self.risk_df)
        if save:
            if hasattr(self.data_lake, 'save_archive_validation_report'): self.data_lake.save_archive_validation_report(val_df)
            if hasattr(self.data_lake, 'save_archive_quality'): self.data_lake.save_archive_quality(self.profile.name, qual_report)
        return qual_report, {"status": "success"}

    def build_archive_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        status = []
        status.append({"component": "archive_domains", "status": "generated" if not self.domain_df.empty else "missing"})
        status.append({"component": "archive_items", "status": "generated" if not self.item_df.empty else "missing"})
        status.append({"component": "cold_storage_manifest", "status": "generated" if self.manifest else "missing"})
        df = pd.DataFrame(status)
        return df, {"status": "success"}
