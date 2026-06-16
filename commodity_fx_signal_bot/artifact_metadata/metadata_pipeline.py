"""
Artifact Metadata Pipeline.
"""

from pathlib import Path
import pandas as pd
import logging

from .metadata_config import ArtifactMetadataProfile, get_default_artifact_metadata_profile
from .artifact_inventory import discover_research_artifacts, summarize_research_artifacts
from .model_cards import build_model_card_registry, summarize_model_cards
from .dataset_cards import build_dataset_card_registry, summarize_dataset_cards
from .experiment_cards import build_experiment_card_registry, summarize_experiment_cards
from .reproducibility_cards import build_reproducibility_card_registry, build_reproducibility_checklist, summarize_reproducibility_cards
from .backtest_cards import build_backtest_card_registry, summarize_backtest_cards
from .scenario_cards import build_scenario_card_registry, summarize_scenario_cards
from .regression_cards import build_regression_card_registry, summarize_regression_cards
from .feature_set_cards import build_feature_set_card_registry, summarize_feature_set_cards
from .synthetic_data_cards import build_synthetic_data_card_registry, summarize_synthetic_data_cards
from .research_report_cards import build_research_report_card_registry, summarize_research_report_cards
from .lineage_cards import build_artifact_lineage_cards, summarize_lineage_cards
from .limitation_cards import build_artifact_limitation_cards, build_risk_limitation_summary_cards
from .intended_use_cards import build_intended_use_cards, summarize_intended_use_cards
from .non_use_policy_cards import build_non_use_policy_cards, summarize_non_use_policy_cards
from .metadata_scoring import build_metadata_completeness_report, build_metadata_freshness_report, summarize_metadata_scoring
from .metadata_validation import build_card_validation_report
from .metadata_quality import build_metadata_quality_report
from .metadata_export import build_research_artifact_metadata_export, build_metadata_export_index, summarize_metadata_export

logger = logging.getLogger(__name__)

class ArtifactMetadataPipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: ArtifactMetadataProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_artifact_metadata_profile()

    def build_research_artifact_inventory(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, raw_summary = discover_research_artifacts(self.project_root, self.profile)
        summary = summarize_research_artifacts(df)

        if save:
             try:
                 # In a real impl, this would call data_lake.save_research_artifact_inventory
                 pass
             except Exception as e:
                 logger.error(f"Save failed: {e}")

        return df, summary

    def build_model_dataset_cards(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, _ = discover_research_artifacts(self.project_root, self.profile)

        mc_df, mc_sum = build_model_card_registry(df, self.profile)
        dc_df, dc_sum = build_dataset_card_registry(df, self.profile)
        fc_df, fc_sum = build_feature_set_card_registry(df, self.profile)
        sc_df, sc_sum = build_synthetic_data_card_registry(df, self.profile)

        tables = {
            "model_cards": mc_df,
            "dataset_cards": dc_df,
            "feature_set_cards": fc_df,
            "synthetic_data_cards": sc_df
        }

        summary = {
            "total_model_cards": mc_sum.get("total_model_cards", 0),
            "total_dataset_cards": dc_sum.get("total_dataset_cards", 0),
            "total_feature_set_cards": fc_sum.get("total_feature_set_cards", 0),
            "total_synthetic_data_cards": sc_sum.get("total_synthetic_data_cards", 0)
        }

        return tables, summary

    def build_experiment_reproducibility_cards(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, _ = discover_research_artifacts(self.project_root, self.profile)

        ec_df, ec_sum = build_experiment_card_registry(df, self.profile)
        bc_df, bc_sum = build_backtest_card_registry(df, self.profile)
        rc_df, rc_sum = build_reproducibility_card_registry(df, self.profile)
        cl_df, cl_sum = build_reproducibility_checklist(df, self.profile)

        tables = {
            "experiment_cards": ec_df,
            "backtest_cards": bc_df,
            "reproducibility_cards": rc_df,
            "reproducibility_checklist": cl_df
        }

        summary = {
            "total_experiment_cards": ec_sum.get("total_experiment_cards", 0),
            "total_backtest_cards": bc_sum.get("total_backtest_cards", 0),
            "total_reproducibility_cards": rc_sum.get("total_reproducibility_cards", 0),
            "total_checks": cl_sum.get("total_checks", 0)
        }

        return tables, summary

    def build_scenario_regression_cards(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, _ = discover_research_artifacts(self.project_root, self.profile)

        sc_df, sc_sum = build_scenario_card_registry(df, self.profile)
        rc_df, rc_sum = build_regression_card_registry(df, self.profile)

        tables = {
            "scenario_cards": sc_df,
            "regression_cards": rc_df
        }

        summary = {
            "total_scenario_cards": sc_sum.get("total_scenario_cards", 0),
            "total_regression_cards": rc_sum.get("total_regression_cards", 0)
        }

        return tables, summary

    def build_research_metadata_export(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, _ = discover_research_artifacts(self.project_root, self.profile)

        rr_df, _ = build_research_report_card_registry(df, self.profile)
        lc_df, _ = build_artifact_lineage_cards(df, self.profile)
        lim_df, _ = build_artifact_limitation_cards(df, self.profile)
        iu_df, _ = build_intended_use_cards(df, self.profile)
        nu_df, _ = build_non_use_policy_cards(df, self.profile)

        tables = {
            "research_report_cards": rr_df,
            "lineage_cards": lc_df,
            "limitation_cards": lim_df,
            "intended_use_cards": iu_df,
            "non_use_policy_cards": nu_df
        }

        manifest = build_research_artifact_metadata_export(df, tables, self.profile)
        index_df = build_metadata_export_index(df, tables, self.profile)

        tables["export_index"] = index_df
        summary = summarize_metadata_export(manifest, index_df)

        return tables, summary

    def build_metadata_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        df, _ = discover_research_artifacts(self.project_root, self.profile)
        tables, _ = self.build_model_dataset_cards(save=False)
        tables2, _ = self.build_experiment_reproducibility_cards(save=False)
        tables.update(tables2)

        q_report = build_metadata_quality_report(summary={}, artifact_df=df, card_tables=tables)

        return q_report, {"passed": q_report.get("passed", False)}

    def build_metadata_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return pd.DataFrame(), {"status": "ok"}
