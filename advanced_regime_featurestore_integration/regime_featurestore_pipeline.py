"""Phase 134: Regime FeatureStore Integration Master Pipeline.

Orchestrates the creation, validation, reporting, and DataLake registration
of all FeatureStore contracts, component catalogs, and accepted references.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_profile_registry import (
    build_regime_featurestore_profile_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_domain_registry import (
    build_regime_featurestore_domain_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_contracts import (
    build_regime_featurestore_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_entities import (
    build_regime_featurestore_entity_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_namespace import (
    build_regime_featurestore_namespace_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_schema import (
    build_regime_featurestore_schema_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_version_policies import (
    build_regime_featurestore_version_policy_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_partition_policies import (
    build_regime_featurestore_partition_policy_registry,
)
from advanced_regime_featurestore_integration.regime_taxonomy_store_catalog import (
    build_regime_taxonomy_store_catalog,
)
from advanced_regime_featurestore_integration.regime_matrix_store_catalog import (
    build_regime_matrix_store_catalog,
)
from advanced_regime_featurestore_integration.candidate_state_store_catalog import (
    build_candidate_state_store_catalog,
)
from advanced_regime_featurestore_integration.pseudo_state_store_catalog import (
    build_pseudo_state_store_catalog,
)
from advanced_regime_featurestore_integration.transition_store_catalog import (
    build_transition_store_catalog,
)
from advanced_regime_featurestore_integration.cross_asset_regime_store_catalog import (
    build_cross_asset_regime_store_catalog,
)
from advanced_regime_featurestore_integration.macro_event_news_regime_store_catalog import (
    build_macro_event_news_regime_store_catalog,
)
from advanced_regime_featurestore_integration.regime_validation_acceptance_store_catalog import (
    build_regime_validation_acceptance_store_catalog,
)
from advanced_regime_featurestore_integration.regime_accepted_reference_registries import (
    build_regime_no_lookahead_accepted_reference_registry,
    build_regime_metadata_only_news_accepted_reference_registry,
    build_regime_source_preservation_accepted_reference_registry,
    build_regime_non_signal_accepted_reference_registry,
)
from advanced_regime_featurestore_integration.regime_quality_dependency_store import (
    build_regime_quality_dependency_store_registry,
)
from advanced_regime_featurestore_integration.regime_validation_dependency_store import (
    build_regime_validation_dependency_store_registry,
)
from advanced_regime_featurestore_integration.regime_lineage_references import (
    build_regime_lineage_reference_registry,
)
from advanced_regime_featurestore_integration.regime_manual_review_blocker_store import (
    build_regime_manual_review_blocker_store_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_read_contracts import (
    build_regime_featurestore_read_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_write_contracts import (
    build_regime_featurestore_write_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_query_contracts import (
    build_regime_featurestore_query_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_forbidden_column_policies import (
    build_regime_featurestore_forbidden_column_policy_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_non_signal_policies import (
    build_regime_featurestore_non_signal_policy_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_source_preservation_policies import (
    build_regime_featurestore_source_preservation_policy_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_metadata_manifest import (
    build_regime_featurestore_metadata_manifest,
)
from advanced_regime_featurestore_integration.regime_featurestore_health import (
    build_regime_featurestore_health_check,
)
from advanced_regime_featurestore_integration.regime_featurestore_validation import (
    build_regime_featurestore_validation_report,
)
from advanced_regime_featurestore_integration.regime_featurestore_safety_boundary import (
    build_regime_featurestore_safety_boundary,
)
from advanced_regime_featurestore_integration.phase_135_handoff import (
    build_phase_135_regime_classification_acceptance_handoff_report,
)
from advanced_regime_featurestore_integration.regime_featurestore_report_builder import (
    build_regime_featurestore_profile_markdown_report,
    build_regime_featurestore_contract_markdown_report,
    build_regime_featurestore_manifest_markdown_report,
    build_regime_featurestore_validation_markdown_report,
    build_phase_135_handoff_markdown_report,
)


class RegimeFeatureStorePipeline:
    """Master pipeline orchestrating all Phase 134 FeatureStore integration activities."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[RegimeFeatureStoreProfile] = None,
    ):
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(".")
        self.data_lake = data_lake or DataLake(self.project_root)
        self.profile = profile or get_regime_featurestore_profile()

    def build_profiles_domains_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Construct profile, domain, and contract registries."""
        p_df, p_sum = build_regime_featurestore_profile_registry(self.profile)
        d_df, d_sum = build_regime_featurestore_domain_registry(self.profile)
        c_df, c_sum = build_regime_featurestore_contract_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_featurestore_profile_registry"):
            self.data_lake.save_regime_featurestore_profile_registry(p_df, p_sum)
            self.data_lake.save_regime_featurestore_domain_registry(d_df, d_sum)
            self.data_lake.save_regime_featurestore_contract_registry(c_df, c_sum)

        tables = {"profiles": p_df, "domains": d_df, "contracts": c_df}
        summary = {"profiles": p_sum, "domains": d_sum, "contracts": c_sum}
        return tables, summary

    def build_entities_namespace_schema(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Construct entities, namespaces, schemas, version, and partition policies."""
        e_df, e_sum = build_regime_featurestore_entity_registry(self.profile)
        n_df, n_sum = build_regime_featurestore_namespace_registry(self.profile)
        s_df, s_sum = build_regime_featurestore_schema_registry(self.profile)
        v_df, v_sum = build_regime_featurestore_version_policy_registry(self.profile)
        pt_df, pt_sum = build_regime_featurestore_partition_policy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_featurestore_entity_registry"):
            self.data_lake.save_regime_featurestore_entity_registry(e_df, e_sum)
            self.data_lake.save_regime_featurestore_namespace_registry(n_df, n_sum)
            self.data_lake.save_regime_featurestore_schema_registry(s_df, s_sum)
            self.data_lake.save_regime_featurestore_version_policy_registry(v_df, v_sum)
            self.data_lake.save_regime_featurestore_partition_policy_registry(pt_df, pt_sum)

        tables = {"entities": e_df, "namespaces": n_df, "schema": s_df, "version_policies": v_df, "partition_policies": pt_df}
        summary = {"entities": e_sum, "namespaces": n_sum, "schema": s_sum, "version_policies": v_sum, "partition_policies": pt_sum}
        return tables, summary

    def build_component_store_catalogs(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Construct all 8 component store catalogs."""
        tax_df, tax_sum = build_regime_taxonomy_store_catalog(self.profile)
        mat_df, mat_sum = build_regime_matrix_store_catalog(self.profile)
        cand_df, cand_sum = build_candidate_state_store_catalog(self.profile)
        ps_df, ps_sum = build_pseudo_state_store_catalog(self.profile)
        tr_df, tr_sum = build_transition_store_catalog(self.profile)
        ca_df, ca_sum = build_cross_asset_regime_store_catalog(self.profile)
        mne_df, mne_sum = build_macro_event_news_regime_store_catalog(self.profile)
        va_df, va_sum = build_regime_validation_acceptance_store_catalog(self.profile)

        if save and hasattr(self.data_lake, "save_regime_taxonomy_store_catalog"):
            self.data_lake.save_regime_taxonomy_store_catalog(tax_df, tax_sum)
            self.data_lake.save_regime_matrix_store_catalog(mat_df, mat_sum)
            self.data_lake.save_candidate_state_store_catalog(cand_df, cand_sum)
            self.data_lake.save_pseudo_state_store_catalog(ps_df, ps_sum)
            self.data_lake.save_transition_store_catalog(tr_df, tr_sum)
            self.data_lake.save_cross_asset_regime_store_catalog(ca_df, ca_sum)
            self.data_lake.save_macro_event_news_regime_store_catalog(mne_df, mne_sum)
            self.data_lake.save_regime_validation_acceptance_store_catalog(va_df, va_sum)

        catalogs = {
            "taxonomy_catalog": tax_df,
            "matrix_catalog": mat_df,
            "candidate_state_catalog": cand_df,
            "pseudo_state_catalog": ps_df,
            "transition_catalog": tr_df,
            "cross_asset_catalog": ca_df,
            "macro_event_news_catalog": mne_df,
            "validation_acceptance_catalog": va_df,
        }
        summary = {
            "taxonomy": tax_sum,
            "matrix": mat_sum,
            "candidate_state": cand_sum,
            "pseudo_state": ps_sum,
            "transition": tr_sum,
            "cross_asset": ca_sum,
            "macro_event_news": mne_sum,
            "validation_acceptance": va_sum,
        }
        return catalogs, summary

    def build_accepted_references_dependencies_lineage(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Construct accepted references, dependencies, lineage, and blocker registries."""
        nl_df, nl_sum = build_regime_no_lookahead_accepted_reference_registry(self.profile)
        mo_df, mo_sum = build_regime_metadata_only_news_accepted_reference_registry(self.profile)
        sp_df, sp_sum = build_regime_source_preservation_accepted_reference_registry(self.profile)
        ns_df, ns_sum = build_regime_non_signal_accepted_reference_registry(self.profile)
        qd_df, qd_sum = build_regime_quality_dependency_store_registry(self.profile)
        vd_df, vd_sum = build_regime_validation_dependency_store_registry(self.profile)
        lin_df, lin_sum = build_regime_lineage_reference_registry(self.profile)
        blk_df, blk_sum = build_regime_manual_review_blocker_store_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_no_lookahead_accepted_reference_registry"):
            self.data_lake.save_regime_no_lookahead_accepted_reference_registry(nl_df, nl_sum)
            self.data_lake.save_regime_metadata_only_news_accepted_reference_registry(mo_df, mo_sum)
            self.data_lake.save_regime_source_preservation_accepted_reference_registry(sp_df, sp_sum)
            self.data_lake.save_regime_non_signal_accepted_reference_registry(ns_df, ns_sum)
            self.data_lake.save_regime_quality_dependency_store_registry(qd_df, qd_sum)
            self.data_lake.save_regime_validation_dependency_store_registry(vd_df, vd_sum)
            self.data_lake.save_regime_lineage_reference_registry(lin_df, lin_sum)
            self.data_lake.save_regime_manual_review_blocker_store_registry(blk_df, blk_sum)

        tables = {
            "no_lookahead_accepted": nl_df,
            "metadata_only_news_accepted": mo_df,
            "source_preservation_accepted": sp_df,
            "non_signal_accepted": ns_df,
            "quality_dependencies": qd_df,
            "validation_dependencies": vd_df,
            "lineage": lin_df,
            "blockers": blk_df,
        }
        summary = {
            "no_lookahead": nl_sum,
            "metadata_only_news": mo_sum,
            "source_preservation": sp_sum,
            "non_signal": ns_sum,
            "quality_dependencies": qd_sum,
            "validation_dependencies": vd_sum,
            "lineage": lin_sum,
            "blockers": blk_sum,
        }
        return tables, summary

    def build_read_write_query_policies_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Construct read/write/query contracts, governance policies, and metadata manifest."""
        rc_df, rc_sum = build_regime_featurestore_read_contract_registry(self.profile)
        wc_df, wc_sum = build_regime_featurestore_write_contract_registry(self.profile)
        qc_df, qc_sum = build_regime_featurestore_query_contract_registry(self.profile)
        fc_df, fc_sum = build_regime_featurestore_forbidden_column_policy_registry(self.profile)
        nsp_df, nsp_sum = build_regime_featurestore_non_signal_policy_registry(self.profile)
        spp_df, spp_sum = build_regime_featurestore_source_preservation_policy_registry(self.profile)
        man_df, man_sum = build_regime_featurestore_metadata_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_regime_featurestore_read_contract_registry"):
            self.data_lake.save_regime_featurestore_read_contract_registry(rc_df, rc_sum)
            self.data_lake.save_regime_featurestore_write_contract_registry(wc_df, wc_sum)
            self.data_lake.save_regime_featurestore_query_contract_registry(qc_df, qc_sum)
            self.data_lake.save_regime_featurestore_forbidden_column_policy_registry(fc_df, fc_sum)
            self.data_lake.save_regime_featurestore_non_signal_policy_registry(nsp_df, nsp_sum)
            self.data_lake.save_regime_featurestore_source_preservation_policy_registry(spp_df, spp_sum)
            self.data_lake.save_regime_featurestore_metadata_manifest(man_df, man_sum)

        tables = {
            "read_contracts": rc_df,
            "write_contracts": wc_df,
            "query_contracts": qc_df,
            "forbidden_columns": fc_df,
            "non_signal_policies": nsp_df,
            "source_preservation_policies": spp_df,
            "manifest": man_df,
        }
        summary = {
            "read_contracts": rc_sum,
            "write_contracts": wc_sum,
            "query_contracts": qc_sum,
            "forbidden_columns": fc_sum,
            "non_signal_policies": nsp_sum,
            "source_preservation_policies": spp_sum,
            "manifest": man_sum,
        }
        return tables, summary

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Construct health, validation, safety boundary, and Phase 135 handoff reports."""
        h_df, h_sum = build_regime_featurestore_health_check(self.project_root, self.profile)
        s_df, s_sum = build_regime_featurestore_safety_boundary(self.profile)
        ho_df, ho_sum = build_phase_135_regime_classification_acceptance_handoff_report(self.profile)

        v_input_tables = {
            "profiles": build_regime_featurestore_profile_registry(self.profile)[0],
            "contracts": build_regime_featurestore_contract_registry(self.profile)[0],
            "schema": build_regime_featurestore_schema_registry(self.profile)[0],
            "catalogs": self.build_component_store_catalogs(save=False)[0],
            "manifest": build_regime_featurestore_metadata_manifest(self.profile)[0],
        }
        v_df, v_sum = build_regime_featurestore_validation_report(v_input_tables, self.profile)

        if save and hasattr(self.data_lake, "save_regime_featurestore_health_check"):
            self.data_lake.save_regime_featurestore_health_check(h_df, h_sum)
            self.data_lake.save_regime_featurestore_safety_boundary(s_df, s_sum)
            self.data_lake.save_regime_featurestore_validation_report(v_df, v_sum)
            self.data_lake.save_phase_135_regime_classification_acceptance_handoff_report(ho_df, ho_sum)

        tables = {"health": h_df, "safety": s_df, "validation": v_df, "handoff": ho_df}
        summary = {"health": h_sum, "safety": s_sum, "validation": v_sum, "handoff": ho_sum}
        return tables, summary

    def build_regime_featurestore_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Execute full end-to-end status synthesis across all Phase 134 outputs."""
        t1, s1 = self.build_profiles_domains_contracts(save=save)
        t2, s2 = self.build_entities_namespace_schema(save=save)
        t3, s3 = self.build_component_store_catalogs(save=save)
        t4, s4 = self.build_accepted_references_dependencies_lineage(save=save)
        t5, s5 = self.build_read_write_query_policies_manifest(save=save)
        t6, s6 = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"module": "profiles", "count": len(t1["profiles"]), "status": s1["profiles"]["status"], "non_signal": True},
            {"module": "domains", "count": len(t1["domains"]), "status": s1["domains"]["status"], "non_signal": True},
            {"module": "contracts", "count": len(t1["contracts"]), "status": s1["contracts"]["status"], "non_signal": True},
            {"module": "entities", "count": len(t2["entities"]), "status": s2["entities"]["status"], "non_signal": True},
            {"module": "schema", "count": len(t2["schema"]), "status": s2["schema"]["status"], "non_signal": True},
            {"module": "catalogs", "count": len(t3), "status": "regime_store_ready", "non_signal": True},
            {"module": "accepted_references", "count": len(t4["no_lookahead_accepted"]) + len(t4["metadata_only_news_accepted"]) + len(t4["source_preservation_accepted"]) + len(t4["non_signal_accepted"]), "status": "regime_store_ready", "non_signal": True},
            {"module": "manifest", "count": len(t5["manifest"]), "status": s5["manifest"]["status"], "non_signal": True},
            {"module": "health", "count": len(t6["health"]), "status": s6["health"]["status"], "non_signal": True},
            {"module": "validation", "count": len(t6["validation"]), "status": s6["validation"]["status"], "non_signal": True},
            {"module": "safety", "count": len(t6["safety"]), "status": s6["safety"]["status"], "non_signal": True},
            {"module": "handoff", "count": len(t6["handoff"]), "status": s6["handoff"]["status"], "non_signal": True},
        ]
        status_df = pd.DataFrame(status_rows)

        full_summary = {
            "current_phase": 134,
            "target_final_phase": 160,
            "next_phase": 135,
            "active_profile": self.profile.profile_name,
            "total_modules": len(status_rows),
            "all_healthy": s6["health"]["all_healthy"],
            "all_validation_passed": s6["validation"]["all_passed"],
            "all_handoff_ready": s6["handoff"]["all_satisfied"],
            "overall_status": "regime_store_ready",
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        }

        if save and hasattr(self.data_lake, "save_regime_featurestore_report"):
            profile_md = build_regime_featurestore_profile_markdown_report(s1["profiles"], t1["profiles"])
            contract_md = build_regime_featurestore_contract_markdown_report(s1["contracts"], t1["contracts"])
            manifest_md = build_regime_featurestore_manifest_markdown_report(s5["manifest"], t5["manifest"])
            val_md = build_regime_featurestore_validation_markdown_report(s6["validation"], t6["validation"])
            handoff_md = build_phase_135_handoff_markdown_report(s6["handoff"], t6["handoff"])

            combined_md = f"{profile_md}\n---\n{contract_md}\n---\n{manifest_md}\n---\n{val_md}\n---\n{handoff_md}"
            self.data_lake.save_regime_featurestore_report(self.profile.profile_name, full_summary, combined_md)

        return status_df, full_summary
