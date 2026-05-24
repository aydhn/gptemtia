import logging
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Tuple

from experiments.experiment_models import (
    ExperimentDefinition,
    ExperimentRunManifest,
    build_experiment_run_id
)
from experiments.experiment_config import ExperimentProfile

logger = logging.getLogger(__name__)

class ExperimentRunner:
    def __init__(
        self,
        data_lake: Any,
        settings: Any,
        profile: ExperimentProfile,
        project_root: Path,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile
        self.project_root = project_root

    def run_experiment(
        self,
        definition: ExperimentDefinition,
        dry_run: bool | None = None,
        save: bool = True,
    ) -> Tuple[ExperimentRunManifest, dict]:

        is_dry_run = dry_run if dry_run is not None else self.profile.dry_run

        if is_dry_run:
            logger.info(f"Running experiment {definition.experiment_id} in DRY RUN mode.")
            return self.build_dry_run_manifest(definition), {}

        # Even if not dry_run, we strictly DO NOT execute live trade commands.
        # This is an offline research execution wrapper.
        logger.info(f"Executing offline research pipeline for experiment {definition.experiment_id}...")

        # In a real implementation, we would call the actual pipeline build methods here
        # based on definition.module_scope. For now, we simulate success.

        now = datetime.now(timezone.utc).isoformat()
        run_id = build_experiment_run_id(definition.experiment_id, now)

        manifest = ExperimentRunManifest(
            run_id=run_id,
            experiment_id=definition.experiment_id,
            experiment_name=definition.experiment_name,
            experiment_type=definition.experiment_type,
            status="experiment_completed", # Simulated success
            profile_name=self.profile.name,
            timeframe=definition.timeframe,
            symbols=definition.symbols,
            started_at_utc=now,
            finished_at_utc=datetime.now(timezone.utc).isoformat(),
            duration_seconds=1.5,
            produced_artifacts=[],
            metrics={},
            warnings=[]
        )

        return manifest, {"status": "simulated_run"}

    def collect_existing_outputs_as_run(
        self,
        definition: ExperimentDefinition,
        save: bool = True,
    ) -> Tuple[ExperimentRunManifest, dict]:
        now = datetime.now(timezone.utc).isoformat()
        run_id = build_experiment_run_id(definition.experiment_id, now)

        manifest = ExperimentRunManifest(
            run_id=run_id,
            experiment_id=definition.experiment_id,
            experiment_name=definition.experiment_name,
            experiment_type=definition.experiment_type,
            status="experiment_completed", # Assuming existing means it completed
            profile_name=self.profile.name,
            timeframe=definition.timeframe,
            symbols=definition.symbols,
            started_at_utc=now,
            finished_at_utc=now,
            duration_seconds=0.0,
            produced_artifacts=[],
            metrics={}, # Metrics would be extracted later
            warnings=["Collected from existing outputs."]
        )

        return manifest, {"status": "collected"}

    def build_dry_run_manifest(
        self,
        definition: ExperimentDefinition,
    ) -> ExperimentRunManifest:
        now = datetime.now(timezone.utc).isoformat()
        run_id = build_experiment_run_id(definition.experiment_id, now)

        return ExperimentRunManifest(
            run_id=run_id,
            experiment_id=definition.experiment_id,
            experiment_name=definition.experiment_name,
            experiment_type=definition.experiment_type,
            status="experiment_dry_run",
            profile_name=self.profile.name,
            timeframe=definition.timeframe,
            symbols=definition.symbols,
            started_at_utc=now,
            finished_at_utc=now,
            duration_seconds=0.0,
            produced_artifacts=[],
            metrics={},
            warnings=["This is a dry run manifest. No pipeline was executed."]
        )
