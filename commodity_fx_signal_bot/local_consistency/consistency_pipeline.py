from pathlib import Path

import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_consistency.consistency_config import (
    LocalConsistencyProfile,
    get_default_local_consistency_profile,
)


class LocalConsistencyPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: LocalConsistencyProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_consistency_profile()

    def build_consistency_check_registry(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        from local_consistency.check_registry import build_consistency_check_registry
        df, summary = build_consistency_check_registry(self.profile)
        if save:
            self.data_lake.save_consistency_check_registry(df, summary)
        return {"check_registry": df}, summary

    def build_cross_layer_consistency_matrix(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        from local_consistency.check_registry import build_cross_layer_consistency_matrix
        df, summary = build_cross_layer_consistency_matrix(pd.DataFrame())
        if save:
            self.data_lake.save_cross_layer_consistency_matrix(df, summary)
        return df, summary

    def build_contradiction_detection_report(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        from local_consistency.contradiction_detector import build_contradiction_detection_report
        df, summary = build_contradiction_detection_report(self.project_root, self.profile)
        if save:
            self.data_lake.save_contradiction_detection_report(df, summary)
        return df, summary

    def build_stale_reconciliation_plan(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        from local_consistency.stale_reconciliation import build_stale_artifact_reconciliation_plan
        df, summary = build_stale_artifact_reconciliation_plan(self.project_root, self.profile)
        if save:
            self.data_lake.save_stale_artifact_reconciliation_plan(df, summary)
        return df, summary

    def build_system_coherence_report(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        from local_consistency.coherence_scoring import build_cross_layer_coherence_score_report
        df, summary = build_cross_layer_coherence_score_report(pd.DataFrame(), pd.DataFrame(), self.profile)
        if save:
            self.data_lake.save_system_coherence_report(summary)
        return {"score": df}, summary

    def build_consistency_quality_report(
        self,
        save: bool = True,
    ) -> tuple[dict, dict]:
        from local_consistency.consistency_quality import build_consistency_quality_report
        report = build_consistency_quality_report({})
        if save:
            self.data_lake.save_consistency_quality(self.profile.name, report)
        return report, {}

    def build_consistency_status(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        return pd.DataFrame(), {}
