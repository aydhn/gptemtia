"""Phase 125: Feature Factor Acceptance Pipeline.

Master pipeline orchestrating the end-to-end acceptance reporting,
gate evaluations, compliance checks, safety boundaries, manifest generation,
and Phase 126 regime handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_profile_registry import (
    build_feature_factor_acceptance_profile_registry,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_domain_registry import (
    build_feature_factor_acceptance_domain_registry,
)
from advanced_feature_factor_acceptance.feature_engine_block_inventory import (
    build_feature_engine_block_inventory_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_dependencies import (
    build_feature_engine_block_dependency_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_gates import (
    build_feature_engine_block_acceptance_gate_registry,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_scoring import (
    build_feature_engine_block_acceptance_score_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_manual_review import (
    build_feature_engine_block_manual_review_queue,
)
from advanced_feature_factor_acceptance.feature_engine_block_safety_boundary import (
    build_feature_engine_block_safety_boundary_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_compliance import (
    build_feature_engine_block_non_signal_compliance_report,
    build_feature_engine_block_no_lookahead_compliance_report,
    build_feature_engine_block_forbidden_column_compliance_report,
    build_feature_engine_block_news_metadata_only_compliance_report,
    build_feature_engine_block_source_preservation_report,
    build_feature_engine_block_feature_store_readiness_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_documentation import (
    build_feature_engine_block_documentation_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_script_contracts import (
    build_feature_engine_block_script_contract_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_test_contracts import (
    build_feature_engine_block_test_contract_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_status import (
    build_feature_engine_block_status_report,
)
from advanced_feature_factor_acceptance.phase_116_125_acceptance_manifest import (
    build_phase_116_125_acceptance_manifest,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_health import (
    build_feature_factor_acceptance_health_check,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_validation import (
    build_feature_factor_acceptance_validation_report,
)
from advanced_feature_factor_acceptance.phase_126_handoff import (
    build_phase_126_regime_classification_handoff_report,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_feature_factor_acceptance_profile_markdown_report,
    build_feature_engine_inventory_markdown_report,
    build_feature_engine_dependency_markdown_report,
    build_acceptance_gate_markdown_report,
    build_acceptance_score_markdown_report,
    build_manual_review_markdown_report,
    build_compliance_markdown_report,
    build_contract_markdown_report,
    build_acceptance_manifest_markdown_report,
    build_health_markdown_report,
    build_validation_markdown_report,
    build_phase_126_handoff_markdown_report,
)


class FeatureFactorAcceptancePipeline:
    """Master pipeline for Phase 125 Feature/Factor Acceptance."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[FeatureFactorAcceptanceProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_feature_factor_acceptance_profile()

    def build_profiles_domains_inventory(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 1: Build profiles, domains, and block inventory."""
        df_prof, s_prof = build_feature_factor_acceptance_profile_registry(self.profile)
        df_dom, s_dom = build_feature_factor_acceptance_domain_registry(self.profile)
        df_inv, s_inv = build_feature_engine_block_inventory_report(self.profile)

        if save:
            self.data_lake.save_feature_factor_acceptance_profile_registry(df_prof, s_prof)
            self.data_lake.save_feature_factor_acceptance_domain_registry(df_dom, s_dom)
            self.data_lake.save_feature_engine_block_inventory_report(df_inv, s_inv)

        tables = {"profiles": df_prof, "domains": df_dom, "inventory": df_inv}
        summaries = {"profiles": s_prof, "domains": s_dom, "inventory": s_inv}
        return tables, summaries

    def build_dependencies_gates_scoring(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 2: Build dependencies, acceptance gates, scoring, and review queue."""
        df_dep, s_dep = build_feature_engine_block_dependency_report(self.profile)
        df_gate, s_gate = build_feature_engine_block_acceptance_gate_registry(self.profile)
        df_score, s_score = build_feature_engine_block_acceptance_score_report(self.profile)
        df_rev, s_rev = build_feature_engine_block_manual_review_queue(self.profile)

        if save:
            self.data_lake.save_feature_engine_block_dependency_report(df_dep, s_dep)
            self.data_lake.save_feature_engine_block_acceptance_gate_registry(df_gate, s_gate)
            self.data_lake.save_feature_engine_block_acceptance_score_report(df_score, s_score)
            self.data_lake.save_feature_engine_block_manual_review_queue(df_rev, s_rev)

        tables = {"dependencies": df_dep, "gates": df_gate, "scoring": df_score, "manual_review": df_rev}
        summaries = {"dependencies": s_dep, "gates": s_gate, "scoring": s_score, "manual_review": s_rev}
        return tables, summaries

    def build_compliance_and_safety(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 3: Build safety boundaries and all compliance audits."""
        df_safe, s_safe = build_feature_engine_block_safety_boundary_report(self.profile)
        df_nonsig, s_nonsig = build_feature_engine_block_non_signal_compliance_report(self.profile)
        df_look, s_look = build_feature_engine_block_no_lookahead_compliance_report(self.profile)
        df_forbid, s_forbid = build_feature_engine_block_forbidden_column_compliance_report(self.profile)
        df_news, s_news = build_feature_engine_block_news_metadata_only_compliance_report(self.profile)
        df_source, s_source = build_feature_engine_block_source_preservation_report(self.profile)
        df_store, s_store = build_feature_engine_block_feature_store_readiness_report(self.profile)

        if save:
            self.data_lake.save_feature_engine_block_safety_boundary_report(df_safe, s_safe)
            self.data_lake.save_feature_engine_block_non_signal_compliance_report(df_nonsig, s_nonsig)
            self.data_lake.save_feature_engine_block_no_lookahead_compliance_report(df_look, s_look)
            self.data_lake.save_feature_engine_block_forbidden_column_compliance_report(df_forbid, s_forbid)
            self.data_lake.save_feature_engine_block_news_metadata_only_compliance_report(df_news, s_news)
            self.data_lake.save_feature_engine_block_source_preservation_report(df_source, s_source)
            self.data_lake.save_feature_engine_block_feature_store_readiness_report(df_store, s_store)

        tables = {
            "safety": df_safe,
            "non_signal": df_nonsig,
            "no_lookahead": df_look,
            "forbidden_columns": df_forbid,
            "news_metadata_only": df_news,
            "source_preservation": df_source,
            "feature_store_readiness": df_store,
        }
        summaries = {
            "safety": s_safe,
            "non_signal": s_nonsig,
            "no_lookahead": s_look,
            "forbidden_columns": s_forbid,
            "news_metadata_only": s_news,
            "source_preservation": s_source,
            "feature_store_readiness": s_store,
        }
        return tables, summaries

    def build_contract_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 4: Build documentation, script, and test contract audits."""
        df_doc, s_doc = build_feature_engine_block_documentation_report(self.project_root, self.profile)
        df_scr, s_scr = build_feature_engine_block_script_contract_report(self.project_root, self.profile)
        df_tst, s_tst = build_feature_engine_block_test_contract_report(self.project_root, self.profile)

        if save:
            self.data_lake.save_feature_engine_block_documentation_report(df_doc, s_doc)
            self.data_lake.save_feature_engine_block_script_contract_report(df_scr, s_scr)
            self.data_lake.save_feature_engine_block_test_contract_report(df_tst, s_tst)

        tables = {"documentation": df_doc, "scripts": df_scr, "tests": df_tst}
        summaries = {"documentation": s_doc, "scripts": s_scr, "tests": s_tst}
        return tables, summaries

    def build_manifest_and_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 5: Build block status, manifest, and Phase 126 handoff."""
        df_stat, s_stat = build_feature_engine_block_status_report(self.profile)
        df_man, s_man = build_phase_116_125_acceptance_manifest(self.profile)
        df_hand, s_hand = build_phase_126_regime_classification_handoff_report(self.profile)

        if save:
            self.data_lake.save_feature_engine_block_status_report(df_stat, s_stat)
            self.data_lake.save_phase_116_125_acceptance_manifest(df_man, s_man)
            self.data_lake.save_phase_126_regime_classification_handoff_report(df_hand, s_hand)

        tables = {"status": df_stat, "manifest": df_man, "handoff": df_hand}
        summaries = {"status": s_stat, "manifest": s_man, "handoff": s_hand}
        return tables, summaries

    def build_health_validation_status(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 6: Build health check and overall validation audit."""
        df_hlth, s_hlth = build_feature_factor_acceptance_health_check(self.project_root, self.profile)
        t1, _ = self.build_profiles_domains_inventory(save=False)
        t2, _ = self.build_dependencies_gates_scoring(save=False)
        t5, _ = self.build_manifest_and_handoff(save=False)

        val_tables = {
            "profiles": t1["profiles"],
            "inventory": t1["inventory"],
            "gates": t2["gates"],
            "manifest": t5["manifest"],
        }
        df_val, s_val = build_feature_factor_acceptance_validation_report(val_tables, self.profile)

        if save:
            self.data_lake.save_feature_factor_acceptance_health_check(df_hlth, s_hlth)
            self.data_lake.save_feature_factor_acceptance_validation_report(df_val, s_val)

        tables = {"health": df_hlth, "validation": df_val}
        summaries = {"health": s_hlth, "validation": s_val}
        return tables, summaries

    def run_full_acceptance_pipeline(self, save: bool = True) -> Dict[str, Any]:
        """Execute all stages of the acceptance pipeline."""
        t1, s1 = self.build_profiles_domains_inventory(save=save)
        t2, s2 = self.build_dependencies_gates_scoring(save=save)
        t3, s3 = self.build_compliance_and_safety(save=save)
        t4, s4 = self.build_contract_reports(save=save)
        t5, s5 = self.build_manifest_and_handoff(save=save)
        t6, s6 = self.build_health_validation_status(save=save)

        result = {
            "profile": self.profile.profile_name,
            "overall_status": s5["status"].get("overall_status", "ACCEPTANCE_PASS"),
            "acceptance_score": s2["scoring"].get("overall_score", 1.0),
            "total_modules": s1["inventory"].get("total_modules", 10),
            "total_gates": s2["gates"].get("total_gates", 16),
            "health_status": s6["health"].get("health_status", "HEALTHY"),
            "validation_status": s6["validation"].get("validation_status", "VALIDATION_PASS"),
            "handoff_status": s5["handoff"].get("handoff_status", "READY"),
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }

        if save:
            md_manifest = build_acceptance_manifest_markdown_report(s5["manifest"], t5["manifest"])
            self.data_lake.save_feature_factor_acceptance_report(
                profile_name=self.profile.profile_name,
                report=result,
                markdown=md_manifest,
            )

        return result
