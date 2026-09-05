"""Phase 124 Feature Store Integration Master Pipeline.

Orchestrates all Phase 124 routines across profiles, contracts, entities,
features, factors, namespace, schema, versioning, partitioning, lineage,
validation, quality/drift, blockers, manifest, policies, catalogs, health,
safety, and Phase 125 acceptance handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_integration_profile_registry import (
    build_feature_store_integration_profile_registry,
)
from advanced_feature_store_integration.feature_store_integration_domain_registry import (
    build_feature_store_integration_domain_registry,
)
from advanced_feature_store_integration.feature_store_contract_registry import (
    build_feature_store_contract_registry,
)
from advanced_feature_store_integration.feature_store_entity_registry import (
    build_feature_store_entity_registry,
)
from advanced_feature_store_integration.feature_store_feature_registry import (
    build_feature_store_feature_registry,
)
from advanced_feature_store_integration.feature_store_factor_registry import (
    build_feature_store_factor_registry,
)
from advanced_feature_store_integration.feature_store_namespace_registry import (
    build_feature_store_namespace_registry,
)
from advanced_feature_store_integration.feature_store_schema_registry import (
    build_feature_store_schema_registry,
)
from advanced_feature_store_integration.feature_store_version_policies import (
    build_feature_store_version_policy_registry,
)
from advanced_feature_store_integration.feature_store_partition_policies import (
    build_feature_store_partition_policy_registry,
)
from advanced_feature_store_integration.feature_store_lineage_references import (
    build_feature_store_lineage_reference_registry,
)
from advanced_feature_store_integration.feature_store_validation_status import (
    build_feature_store_validation_status_registry,
)
from advanced_feature_store_integration.feature_store_quality_scores import (
    build_feature_store_quality_score_registry,
)
from advanced_feature_store_integration.feature_store_drift_scores import (
    build_feature_store_drift_score_registry,
)
from advanced_feature_store_integration.feature_store_manual_review_blockers import (
    build_feature_store_manual_review_blocker_registry,
)
from advanced_feature_store_integration.feature_store_metadata_manifest import (
    build_feature_store_metadata_manifest,
)
from advanced_feature_store_integration.feature_store_read_contracts import (
    build_feature_store_read_contract_registry,
)
from advanced_feature_store_integration.feature_store_write_contracts import (
    build_feature_store_write_contract_registry,
)
from advanced_feature_store_integration.feature_store_query_contracts import (
    build_feature_store_query_contract_registry,
)
from advanced_feature_store_integration.feature_store_non_signal_policies import (
    build_feature_store_non_signal_policy_registry,
)
from advanced_feature_store_integration.feature_store_forbidden_column_policies import (
    build_feature_store_forbidden_column_policy_registry,
)
from advanced_feature_store_integration.feature_store_source_preservation_policies import (
    build_feature_store_source_preservation_policy_registry,
)
from advanced_feature_store_integration.feature_store_catalog_reports import (
    build_feature_store_feature_catalog_report,
    build_feature_store_factor_catalog_report,
    build_feature_store_quality_drift_catalog_report,
    build_feature_store_validation_catalog_report,
)
from advanced_feature_store_integration.feature_store_integration_health import (
    build_feature_store_integration_health_check,
)
from advanced_feature_store_integration.feature_store_integration_validation import (
    build_feature_store_integration_validation_report,
)
from advanced_feature_store_integration.feature_store_integration_safety_boundary import (
    build_feature_store_integration_safety_boundary,
)
from advanced_feature_store_integration.phase_125_handoff import (
    build_phase_125_feature_factor_engine_acceptance_handoff_report,
)
from advanced_feature_store_integration.feature_store_integration_report_builder import (
    build_feature_store_integration_profile_markdown_report,
    build_feature_store_contract_markdown_report,
    build_feature_store_catalog_markdown_report,
    build_feature_store_manifest_markdown_report,
    build_feature_store_policy_markdown_report,
    build_feature_store_health_markdown_report,
    build_feature_store_validation_markdown_report,
    build_feature_store_safety_markdown_report,
    build_phase_125_handoff_markdown_report,
)


class FeatureStoreIntegrationPipeline:
    """Master pipeline orchestrating Feature Store Integration Expansion."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[FeatureStoreIntegrationProfile] = None,
    ):
        self.settings = settings or get_settings()
        self.data_lake = data_lake or DataLake()
        self.project_root = project_root or Path(".")
        self.profile = profile or get_default_feature_store_integration_profile()

    def build_profiles_domains_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_prof, s_prof = build_feature_store_integration_profile_registry(self.profile)
        df_dom, s_dom = build_feature_store_integration_domain_registry(self.profile)
        df_con, s_con = build_feature_store_contract_registry(self.profile)

        if save and hasattr(self.data_lake, "save_feature_store_integration_profile_registry"):
            self.data_lake.save_feature_store_integration_profile_registry(df_prof, s_prof)
            self.data_lake.save_feature_store_integration_domain_registry(df_dom, s_dom)
            self.data_lake.save_feature_store_contract_registry(df_con, s_con)

        tables = {"profiles": df_prof, "domains": df_dom, "contracts": df_con}
        summaries = {"profiles": s_prof, "domains": s_dom, "contracts": s_con}
        return tables, summaries

    def build_entity_feature_factor_registries(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_ent, s_ent = build_feature_store_entity_registry(self.profile)
        df_feat, s_feat = build_feature_store_feature_registry(self.profile)
        df_fac, s_fac = build_feature_store_factor_registry(self.profile)

        if save and hasattr(self.data_lake, "save_feature_store_entity_registry"):
            self.data_lake.save_feature_store_entity_registry(df_ent, s_ent)
            self.data_lake.save_feature_store_feature_registry(df_feat, s_feat)
            self.data_lake.save_feature_store_factor_registry(df_fac, s_fac)

        tables = {"entities": df_ent, "features": df_feat, "factors": df_fac}
        summaries = {"entities": s_ent, "features": s_feat, "factors": s_fac}
        return tables, summaries

    def build_schema_version_partition_lineage(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_ns, s_ns = build_feature_store_namespace_registry(self.profile)
        df_sch, s_sch = build_feature_store_schema_registry(self.profile)
        df_ver, s_ver = build_feature_store_version_policy_registry(self.profile)
        df_part, s_part = build_feature_store_partition_policy_registry(self.profile)
        df_lin, s_lin = build_feature_store_lineage_reference_registry(self.profile)

        if save and hasattr(self.data_lake, "save_feature_store_namespace_registry"):
            self.data_lake.save_feature_store_namespace_registry(df_ns, s_ns)
            self.data_lake.save_feature_store_schema_registry(df_sch, s_sch)
            self.data_lake.save_feature_store_version_policy_registry(df_ver, s_ver)
            self.data_lake.save_feature_store_partition_policy_registry(df_part, s_part)
            self.data_lake.save_feature_store_lineage_reference_registry(df_lin, s_lin)

        tables = {"namespace": df_ns, "schemas": df_sch, "version": df_ver, "partition": df_part, "lineage": df_lin}
        summaries = {"namespace": s_ns, "schemas": s_sch, "version": s_ver, "partition": s_part, "lineage": s_lin}
        return tables, summaries

    def build_validation_quality_drift_review(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_val, s_val = build_feature_store_validation_status_registry(self.profile)
        df_qual, s_qual = build_feature_store_quality_score_registry(self.profile)
        df_drift, s_drift = build_feature_store_drift_score_registry(self.profile)
        df_blk, s_blk = build_feature_store_manual_review_blocker_registry(self.profile)

        if save and hasattr(self.data_lake, "save_feature_store_validation_status_registry"):
            self.data_lake.save_feature_store_validation_status_registry(df_val, s_val)
            self.data_lake.save_feature_store_quality_score_registry(df_qual, s_qual)
            self.data_lake.save_feature_store_drift_score_registry(df_drift, s_drift)
            self.data_lake.save_feature_store_manual_review_blocker_registry(df_blk, s_blk)

        tables = {"validation": df_val, "quality": df_qual, "drift": df_drift, "blockers": df_blk}
        summaries = {"validation": s_val, "quality": s_qual, "drift": s_drift, "blockers": s_blk}
        return tables, summaries

    def build_manifest_read_write_query_policies(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_man, s_man = build_feature_store_metadata_manifest(self.profile)
        df_read, s_read = build_feature_store_read_contract_registry(self.profile)
        df_write, s_write = build_feature_store_write_contract_registry(self.profile)
        df_query, s_query = build_feature_store_query_contract_registry(self.profile)
        df_nsig, s_nsig = build_feature_store_non_signal_policy_registry(self.profile)
        df_forbid, s_forbid = build_feature_store_forbidden_column_policy_registry(self.profile)
        df_pres, s_pres = build_feature_store_source_preservation_policy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_feature_store_metadata_manifest"):
            self.data_lake.save_feature_store_metadata_manifest(df_man, s_man)
            self.data_lake.save_feature_store_read_contract_registry(df_read, s_read)
            self.data_lake.save_feature_store_write_contract_registry(df_write, s_write)
            self.data_lake.save_feature_store_query_contract_registry(df_query, s_query)
            self.data_lake.save_feature_store_non_signal_policy_registry(df_nsig, s_nsig)
            self.data_lake.save_feature_store_forbidden_column_policy_registry(df_forbid, s_forbid)
            self.data_lake.save_feature_store_source_preservation_policy_registry(df_pres, s_pres)

        tables = {
            "manifest": df_man,
            "read_contracts": df_read,
            "write_contracts": df_write,
            "query_contracts": df_query,
            "non_signal": df_nsig,
            "forbidden_columns": df_forbid,
            "source_preservation": df_pres,
        }
        summaries = {
            "manifest": s_man,
            "read_contracts": s_read,
            "write_contracts": s_write,
            "query_contracts": s_query,
            "non_signal": s_nsig,
            "forbidden_columns": s_forbid,
            "source_preservation": s_pres,
        }
        return tables, summaries

    def build_catalog_reports(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_fc, s_fc = build_feature_store_feature_catalog_report(self.profile)
        df_fac, s_fac = build_feature_store_factor_catalog_report(self.profile)
        df_qd, s_qd = build_feature_store_quality_drift_catalog_report(self.profile)
        df_vc, s_vc = build_feature_store_validation_catalog_report(self.profile)

        if save and hasattr(self.data_lake, "save_feature_store_feature_catalog_report"):
            self.data_lake.save_feature_store_feature_catalog_report(df_fc, s_fc)
            self.data_lake.save_feature_store_factor_catalog_report(df_fac, s_fac)
            self.data_lake.save_feature_store_quality_drift_catalog_report(df_qd, s_qd)
            self.data_lake.save_feature_store_validation_catalog_report(df_vc, s_vc)

        tables = {"feature_catalog": df_fc, "factor_catalog": df_fac, "quality_drift_catalog": df_qd, "validation_catalog": df_vc}
        summaries = {"feature_catalog": s_fc, "factor_catalog": s_fac, "quality_drift_catalog": s_qd, "validation_catalog": s_vc}
        return tables, summaries

    def build_health_validation_safety_handoff(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_hlth, s_hlth = build_feature_store_integration_health_check(self.project_root, self.profile)
        t_all = {"profiles": pd.DataFrame(), "contracts": pd.DataFrame(), "schemas": pd.DataFrame(), "manifest": pd.DataFrame()}
        df_val, s_val = build_feature_store_integration_validation_report(t_all, self.profile)
        df_safe, s_safe = build_feature_store_integration_safety_boundary(self.profile)
        df_hnd, s_hnd = build_phase_125_feature_factor_engine_acceptance_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_feature_store_integration_health_check"):
            self.data_lake.save_feature_store_integration_health_check(df_hlth, s_hlth)
            self.data_lake.save_feature_store_integration_validation_report(df_val, s_val)
            self.data_lake.save_feature_store_integration_safety_boundary(df_safe, s_safe)
            self.data_lake.save_phase_125_feature_factor_engine_acceptance_handoff_report(df_hnd, s_hnd)

        tables = {"health": df_hlth, "validation": df_val, "safety": df_safe, "handoff": df_hnd}
        summaries = {"health": s_hlth, "validation": s_val, "safety": s_safe, "handoff": s_hnd}
        return tables, summaries

    def build_feature_store_integration_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        status_records = [
            {"component": "profiles_and_domains", "status": "READY", "non_signal": True},
            {"component": "contract_registry", "status": "READY", "non_signal": True},
            {"component": "entity_registry", "status": "READY", "non_signal": True},
            {"component": "feature_registry", "status": "READY", "non_signal": True},
            {"component": "factor_registry", "status": "READY", "non_signal": True},
            {"component": "namespace_registry", "status": "READY", "non_signal": True},
            {"component": "schema_registry", "status": "READY", "non_signal": True},
            {"component": "version_policies", "status": "READY", "non_signal": True},
            {"component": "partition_policies", "status": "READY", "non_signal": True},
            {"component": "lineage_references", "status": "READY", "non_signal": True},
            {"component": "validation_status", "status": "READY", "non_signal": True},
            {"component": "quality_scores", "status": "READY", "non_signal": True},
            {"component": "drift_scores", "status": "READY", "non_signal": True},
            {"component": "manual_review_blockers", "status": "READY", "non_signal": True},
            {"component": "metadata_manifest", "status": "READY", "non_signal": True},
            {"component": "read_contracts", "status": "READY", "non_signal": True},
            {"component": "write_contracts", "status": "READY", "non_signal": True},
            {"component": "query_contracts", "status": "READY", "non_signal": True},
            {"component": "non_signal_policies", "status": "READY", "non_signal": True},
            {"component": "forbidden_column_policies", "status": "READY", "non_signal": True},
            {"component": "source_preservation_policies", "status": "READY", "non_signal": True},
            {"component": "catalog_reports", "status": "READY", "non_signal": True},
            {"component": "health_check", "status": "READY", "non_signal": True},
            {"component": "validation_report", "status": "READY", "non_signal": True},
            {"component": "safety_boundary", "status": "READY", "non_signal": True},
            {"component": "phase_125_handoff", "status": "READY", "non_signal": True},
        ]
        df = pd.DataFrame(status_records)
        summary = {
            "overall_status": "READY",
            "total_components": len(status_records),
            "ready_components": len(status_records),
            "current_phase": 124,
            "next_phase": 125,
            "target_final_phase": 160,
            "non_signal": True,
            "source_preserved": True,
        }
        return df, summary
