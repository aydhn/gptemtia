import logging
from pathlib import Path
from typing import Tuple, Optional
import pandas as pd

from experiments.experiment_config import ExperimentProfile, get_default_experiment_profile
from experiments.hypothesis_registry import HypothesisRegistry, build_default_hypotheses
from experiments.experiment_registry import ExperimentRegistry, build_default_experiment_definitions
from experiments.experiment_runner import ExperimentRunner
from experiments.research_versioning import build_research_version_record, research_version_record_to_dataframe
from experiments.artifact_manifest import discover_experiment_artifacts, build_experiment_artifact_manifest, artifact_manifest_to_dataframe
from experiments.reproducibility import build_reproducibility_manifest, reproducibility_manifest_to_dataframe
from experiments.experiment_metrics import (
    build_experiment_metric_table,
    summarize_experiment_metrics,
    extract_metrics_from_meta_research,
    normalize_experiment_metrics
)
from experiments.ablation_studies import build_default_ablation_studies, build_ablation_result_table, summarize_ablation_results
from experiments.experiment_comparison import compare_experiment_runs, build_experiment_comparison_table, summarize_experiment_comparisons
from experiments.leaderboard import build_experiment_leaderboard, summarize_leaderboard
from experiments.experiment_quality import build_experiment_quality_report
from experiments.experiment_models import ExperimentDefinition

logger = logging.getLogger(__name__)

class ExperimentTrackingPipeline:
    def __init__(
        self,
        data_lake,
        settings,
        project_root: Path,
        profile: Optional[ExperimentProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_experiment_profile()

        # Initialize registries
        try:
            exp_dir = self.data_lake.paths.experiments_dir
            self.hypothesis_registry = HypothesisRegistry(exp_dir / "hypotheses")
            self.experiment_registry = ExperimentRegistry(exp_dir / "definitions")
        except AttributeError:
            # Fallback for testing with mock data_lake
            self.hypothesis_registry = HypothesisRegistry(Path("/tmp/experiments/hypotheses"))
            self.experiment_registry = ExperimentRegistry(Path("/tmp/experiments/definitions"))

        self.runner = ExperimentRunner(data_lake, settings, self.profile, project_root)

    def _ensure_defaults(self):
        # Load or create defaults if empty
        if self.hypothesis_registry.load_hypotheses().empty:
            for h in build_default_hypotheses():
                self.hypothesis_registry.add_hypothesis(h)

        if self.experiment_registry.load_definitions().empty:
            for d in build_default_experiment_definitions(self.profile):
                self.experiment_registry.add_definition(d)

    def build_hypothesis_registry_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        self._ensure_defaults()
        df = self.hypothesis_registry.load_hypotheses()
        summary = self.hypothesis_registry.summarize()

        if save and hasattr(self.data_lake, "save_hypothesis_registry"):
            self.data_lake.save_hypothesis_registry(df, summary)

        return df, summary

    def track_existing_research_run(
        self,
        experiment_name: str,
        module_scope: list[str],
        symbols: list[str],
        timeframe: str = "1d",
        hypothesis_id: Optional[str] = None,
        experiment_type: str = "candidate_experiment",
        save: bool = True,
    ) -> Tuple[dict, dict]:
        self._ensure_defaults()

        # Create a transient definition
        from datetime import datetime, timezone
        from experiments.experiment_models import build_experiment_id

        now = datetime.now(timezone.utc).isoformat()
        e_id = build_experiment_id(experiment_name, experiment_type, timeframe)

        ed = ExperimentDefinition(
            experiment_id=e_id,
            experiment_name=experiment_name,
            experiment_type=experiment_type,
            hypothesis_id=hypothesis_id,
            profile_name=self.profile.name,
            timeframe=timeframe,
            symbols=symbols,
            module_scope=module_scope,
            parameters={},
            baseline_experiment_id=None,
            created_at_utc=now,
            notes="Tracking existing outputs.",
            warnings=[]
        )

        self.experiment_registry.add_definition(ed)

        # Collect existing outputs
        run_manifest, _ = self.runner.collect_existing_outputs_as_run(ed, save=False)

        # Simulate loading existing reports to extract metrics
        if hasattr(self.data_lake, "load_meta_research_report") and "meta_research" in module_scope:
            try:
                report = self.data_lake.load_meta_research_report(timeframe=timeframe)
                meta_metrics = extract_metrics_from_meta_research(report)
                run_manifest.metrics.update(normalize_experiment_metrics(meta_metrics))
            except Exception as e:
                logger.warning(f"Could not load meta research for metrics: {e}")

        # Generate other manifests
        version_record = build_research_version_record(ed, self.data_lake, self.settings, self.project_root)

        artifacts = discover_experiment_artifacts(self.data_lake, module_scope, timeframe, symbols)
        artifact_manifest = build_experiment_artifact_manifest(run_manifest.run_id, artifacts)

        reproducibility_manifest = build_reproducibility_manifest(ed, run_manifest, version_record, artifact_manifest)

        # Calculate reproducibility score and add to metrics
        from experiments.reproducibility import calculate_reproducibility_score
        rep_score = calculate_reproducibility_score(reproducibility_manifest)
        run_manifest.metrics["reproducibility_score"] = rep_score

        # Save if requested
        if save and hasattr(self.data_lake, "save_experiment_run_manifest"):
            from experiments.experiment_models import experiment_run_manifest_to_dict
            run_dict = experiment_run_manifest_to_dict(run_manifest)
            self.data_lake.save_experiment_run_manifest(run_manifest.run_id, run_dict)
            self.data_lake.save_experiment_artifact_manifest(run_manifest.run_id, artifact_manifest)
            self.data_lake.save_reproducibility_manifest(run_manifest.run_id, reproducibility_manifest)
            self.data_lake.save_research_version_record(version_record["version_id"], version_record)

        from experiments.experiment_models import experiment_run_manifest_to_dict
        return experiment_run_manifest_to_dict(run_manifest), {"status": "tracked"}

    def build_research_version_report(self, run_id: Optional[str] = None, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        # For simplicity, we just return a dummy record if run_id is none,
        # normally we'd query the DB for the version associated with the run

        dummy_record = {
            "version_id": "v1",
            "experiment_id": "exp_1",
            "created_at_utc": "utc",
            "module_scope": ["meta"],
            "timeframe": "1d",
            "symbols": ["AAPL"],
            "config_snapshot": {},
            "environment_snapshot": {},
            "git_snapshot": {}
        }

        df = research_version_record_to_dataframe(dummy_record)
        summary = {"status": "Mock summary for research version report"}

        return df, summary

    def build_ablation_study_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        studies = build_default_ablation_studies(self.profile)

        # Mock metrics
        baseline = {"quality_adjusted_score": 0.5, "validation_score": 0.6}
        abl_map = {
            studies[0].ablation_id: {"study_name": studies[0].study_name, "quality_adjusted_score": 0.4}
        }

        df = build_ablation_result_table(baseline, abl_map)
        summary = summarize_ablation_results(df)

        if save and hasattr(self.data_lake, "save_ablation_study_results"):
            self.data_lake.save_ablation_study_results("default_ablation", df, summary)

        return df, summary

    def build_experiment_comparison_report(
        self,
        baseline_run_id: Optional[str] = None,
        candidate_run_id: Optional[str] = None,
        save: bool = True
    ) -> Tuple[pd.DataFrame, dict]:

        # Mock runs
        b_man = {"run_id": baseline_run_id or "b1", "metrics": {"quality_adjusted_score": 0.5}}
        c_man = {"run_id": candidate_run_id or "c1", "metrics": {"quality_adjusted_score": 0.6}}

        cmp = compare_experiment_runs(b_man, c_man)
        df = build_experiment_comparison_table([cmp])
        summary = summarize_experiment_comparisons(df)

        if save and hasattr(self.data_lake, "save_experiment_comparison_table"):
            self.data_lake.save_experiment_comparison_table(self.profile.name, df)

        return df, summary

    def build_experiment_leaderboard(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        # Mock metrics
        metrics = [
            {"run_id": "r1", "metrics": {"quality_adjusted_score": 0.9, "reproducibility_score": 1.0, "validation_score": 0.8}},
            {"run_id": "r2", "metrics": {"quality_adjusted_score": 0.5, "reproducibility_score": 0.8, "validation_score": 0.5}}
        ]

        df_metrics = build_experiment_metric_table(metrics)
        df_leaderboard = build_experiment_leaderboard(df_metrics, self.profile)
        summary = summarize_leaderboard(df_leaderboard)

        if save and hasattr(self.data_lake, "save_experiment_leaderboard"):
            self.data_lake.save_experiment_leaderboard(self.profile.name, df_leaderboard)

        return df_leaderboard, summary
