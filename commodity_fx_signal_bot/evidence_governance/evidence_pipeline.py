import logging
from pathlib import Path
import pandas as pd

from config.settings import Settings
from evidence_governance.evidence_config import EvidenceGovernanceProfile, get_default_evidence_governance_profile
from evidence_governance.artifact_inventory import discover_evidence_artifacts
from evidence_governance.policy_registry import build_default_policy_registry, policy_registry_to_dataframe
from evidence_governance.control_registry import build_default_control_registry, control_registry_to_dataframe
from evidence_governance.control_mapping import build_policy_to_control_mapping, map_controls_to_evidence, build_control_status_table, summarize_control_mapping
from evidence_governance.evidence_binder import build_audit_evidence_binder
from evidence_governance.traceability_matrix import build_evidence_traceability_matrix, summarize_traceability_matrix
from evidence_governance.evidence_export import build_governance_evidence_export_manifest, build_local_evidence_export_index
from evidence_governance.evidence_quality import build_evidence_quality_report
from evidence_governance.evidence_scoring import build_evidence_completeness_report, build_evidence_freshness_report, summarize_evidence_scoring
from evidence_governance.evidence_gaps import detect_evidence_gaps, evidence_gaps_to_dataframe
from evidence_governance.evidence_packs import build_safety_evidence_pack, build_secrets_hygiene_evidence_pack, build_backup_recovery_evidence_pack, build_portable_packaging_evidence_pack, build_quality_gate_evidence_pack, build_scenario_regression_evidence_pack, build_final_review_evidence_pack, build_documentation_evidence_pack, build_master_orchestration_evidence_pack

logger = logging.getLogger(__name__)

class EvidenceGovernancePipeline:
    def __init__(
        self,
        data_lake, # Using duck typing to avoid circular import if data_lake imports this
        settings: Settings,
        project_root: Path,
        profile: EvidenceGovernanceProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_evidence_governance_profile()

    def build_evidence_artifact_inventory(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        try:
            df, summary = discover_evidence_artifacts(self.project_root, self.profile)

            if save and hasattr(self.data_lake, "save_evidence_artifact_inventory"):
                self.data_lake.save_evidence_artifact_inventory(df, summary)

            return df, summary
        except Exception as e:
            logger.error(f"Error building evidence artifact inventory: {e}")
            return pd.DataFrame(), {"error": str(e)}

    def build_policy_control_mapping(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        try:
            # Re-load artifacts
            if hasattr(self.data_lake, "load_evidence_artifact_inventory"):
                art_df = self.data_lake.load_evidence_artifact_inventory()
            else:
                art_df = pd.DataFrame()

            pol_list = build_default_policy_registry(self.profile)
            pol_df = policy_registry_to_dataframe(pol_list)

            ctrl_list = build_default_control_registry(self.profile)
            ctrl_df = control_registry_to_dataframe(ctrl_list)

            pol_ctrl_df = build_policy_to_control_mapping(pol_df, ctrl_df)
            ctrl_ev_df, _ = map_controls_to_evidence(ctrl_df, art_df, self.profile)
            status_df = build_control_status_table(ctrl_df, ctrl_ev_df, art_df)

            summary = summarize_control_mapping(ctrl_ev_df, status_df)

            res = {
                "policy_registry": pol_df,
                "control_registry": ctrl_df,
                "policy_to_control_mapping": pol_ctrl_df,
                "control_to_evidence_mapping": ctrl_ev_df,
                "control_status_table": status_df
            }

            if save:
                if hasattr(self.data_lake, "save_policy_registry"):
                    self.data_lake.save_policy_registry(pol_df)
                if hasattr(self.data_lake, "save_control_registry"):
                    self.data_lake.save_control_registry(ctrl_df)
                if hasattr(self.data_lake, "save_policy_to_control_mapping"):
                    self.data_lake.save_policy_to_control_mapping(pol_ctrl_df)
                if hasattr(self.data_lake, "save_control_to_evidence_mapping"):
                    self.data_lake.save_control_to_evidence_mapping(ctrl_ev_df)

            return res, summary
        except Exception as e:
            logger.error(f"Error building policy control mapping: {e}")
            return {}, {"error": str(e)}

    def build_audit_evidence_binder(
        self,
        save: bool = True,
    ) -> tuple[str, dict]:
        try:
            # Need to load mappings and artifacts
            art_df = self.data_lake.load_evidence_artifact_inventory() if hasattr(self.data_lake, "load_evidence_artifact_inventory") else pd.DataFrame()
            pol_df = self.data_lake.load_policy_registry() if hasattr(self.data_lake, "load_policy_registry") else pd.DataFrame()
            ctrl_df = self.data_lake.load_control_registry() if hasattr(self.data_lake, "load_control_registry") else pd.DataFrame()
            map_df = self.data_lake.load_control_to_evidence_mapping() if hasattr(self.data_lake, "load_control_to_evidence_mapping") else pd.DataFrame()

            binder_text, summary = build_audit_evidence_binder(pol_df, ctrl_df, map_df, art_df, self.profile)

            if save and hasattr(self.data_lake, "save_audit_evidence_binder"):
                self.data_lake.save_audit_evidence_binder(binder_text, summary)

            return binder_text, summary
        except Exception as e:
            logger.error(f"Error building audit evidence binder: {e}")
            return "", {"error": str(e)}

    def build_evidence_traceability_matrix(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        try:
            art_df = self.data_lake.load_evidence_artifact_inventory() if hasattr(self.data_lake, "load_evidence_artifact_inventory") else pd.DataFrame()
            pol_df = self.data_lake.load_policy_registry() if hasattr(self.data_lake, "load_policy_registry") else pd.DataFrame()
            ctrl_df = self.data_lake.load_control_registry() if hasattr(self.data_lake, "load_control_registry") else pd.DataFrame()
            map_df = self.data_lake.load_control_to_evidence_mapping() if hasattr(self.data_lake, "load_control_to_evidence_mapping") else pd.DataFrame()

            trace_df = build_evidence_traceability_matrix(pol_df, ctrl_df, map_df, art_df)
            summary = summarize_traceability_matrix(trace_df)

            if save and hasattr(self.data_lake, "save_evidence_traceability_matrix"):
                self.data_lake.save_evidence_traceability_matrix(trace_df, summary)

            return trace_df, summary
        except Exception as e:
            logger.error(f"Error building evidence traceability matrix: {e}")
            return pd.DataFrame(), {"error": str(e)}

    def build_governance_evidence_export(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        try:
            art_df = self.data_lake.load_evidence_artifact_inventory() if hasattr(self.data_lake, "load_evidence_artifact_inventory") else pd.DataFrame()
            pol_df = self.data_lake.load_policy_registry() if hasattr(self.data_lake, "load_policy_registry") else pd.DataFrame()
            ctrl_df = self.data_lake.load_control_registry() if hasattr(self.data_lake, "load_control_registry") else pd.DataFrame()
            trace_df = self.data_lake.load_evidence_traceability_matrix() if hasattr(self.data_lake, "load_evidence_traceability_matrix") else pd.DataFrame()

            # Recreate mapping to find gaps
            ctrl_ev_df, _ = map_controls_to_evidence(ctrl_df, art_df, self.profile)
            status_df = build_control_status_table(ctrl_df, ctrl_ev_df, art_df)
            gap_list = detect_evidence_gaps(status_df, trace_df, self.profile)
            gap_df = evidence_gaps_to_dataframe(gap_list)

            manifest = build_governance_evidence_export_manifest(pol_df, ctrl_df, art_df, trace_df, gap_df, self.profile)

            pack_tables = {
                "safety": build_safety_evidence_pack(art_df, ctrl_ev_df, self.profile)[0],
                "secrets_hygiene": build_secrets_hygiene_evidence_pack(art_df, ctrl_ev_df, self.profile)[0],
                "backup_recovery": build_backup_recovery_evidence_pack(art_df, ctrl_ev_df, self.profile)[0],
                "packaging": build_portable_packaging_evidence_pack(art_df, ctrl_ev_df, self.profile)[0],
                "quality": build_quality_gate_evidence_pack(art_df, ctrl_ev_df, self.profile)[0],
                "scenario_regression": build_scenario_regression_evidence_pack(art_df, ctrl_ev_df, self.profile)[0],
                "final_review": build_final_review_evidence_pack(art_df, ctrl_ev_df, self.profile)[0],
                "documentation": build_documentation_evidence_pack(art_df, ctrl_ev_df, self.profile)[0],
                "master_orchestration": build_master_orchestration_evidence_pack(art_df, ctrl_ev_df, self.profile)[0]
            }

            index_df = build_local_evidence_export_index(art_df, pack_tables, self.profile)

            res = {
                "export_manifest": pd.DataFrame([manifest]), # Wrapped for compatibility with return type if needed, but normally manifest is dict. We will return index_df and packs
                "export_index": index_df,
                **pack_tables
            }

            if save:
                if hasattr(self.data_lake, "save_governance_evidence_export"):
                    self.data_lake.save_governance_evidence_export(manifest)
                for k, v in pack_tables.items():
                    if hasattr(self.data_lake, "save_evidence_pack"):
                        self.data_lake.save_evidence_pack(k, v)

            return res, {"manifest": manifest}
        except Exception as e:
            logger.error(f"Error building governance evidence export: {e}")
            return {}, {"error": str(e)}

    def build_evidence_quality_report(
        self,
        save: bool = True,
    ) -> tuple[dict, dict]:
        try:
            art_df = self.data_lake.load_evidence_artifact_inventory() if hasattr(self.data_lake, "load_evidence_artifact_inventory") else pd.DataFrame()
            trace_df = self.data_lake.load_evidence_traceability_matrix() if hasattr(self.data_lake, "load_evidence_traceability_matrix") else pd.DataFrame()

            report = build_evidence_quality_report({"dummy": "summary"}, art_df, trace_df, pd.DataFrame())

            if save and hasattr(self.data_lake, "save_evidence_quality"):
                self.data_lake.save_evidence_quality(self.profile.name, report)

            return report, {"quality": report.get("passed", False)}
        except Exception as e:
            logger.error(f"Error building evidence quality report: {e}")
            return {}, {"error": str(e)}

    def build_evidence_status(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        # Return a mock status for now
        status = [
            {"component": "artifacts", "status": "ok"},
            {"component": "policies", "status": "ok"}
        ]
        return pd.DataFrame(status), {"status": "ok"}
