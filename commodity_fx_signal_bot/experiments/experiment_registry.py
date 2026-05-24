import json
import logging
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
from typing import Optional

from experiments.experiment_models import (
    ExperimentDefinition,
    build_experiment_id,
    experiment_definition_to_dict
)
from experiments.experiment_config import ExperimentProfile

logger = logging.getLogger(__name__)

class ExperimentRegistry:
    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        self.file_path = self.registry_dir / "experiment_registry.jsonl"
        self._cache = {}
        self._load()

    def _load(self):
        if not self.file_path.exists():
            return
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    ed = ExperimentDefinition(**data)
                    self._cache[ed.experiment_id] = ed
        except Exception as e:
            logger.error(f"Failed to load experiment registry: {e}")

    def _save(self):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                for ed in self._cache.values():
                    f.write(json.dumps(experiment_definition_to_dict(ed)) + "\n")
        except Exception as e:
            logger.error(f"Failed to save experiment registry: {e}")

    def add_definition(self, definition: ExperimentDefinition) -> Path:
        self._cache[definition.experiment_id] = definition
        self._save()
        return self.file_path

    def load_definitions(self) -> pd.DataFrame:
        if not self._cache:
            return pd.DataFrame()
        data = [experiment_definition_to_dict(ed) for ed in self._cache.values()]
        return pd.DataFrame(data)

    def get_definition(self, experiment_id: str) -> Optional[dict]:
        ed = self._cache.get(experiment_id)
        if ed:
            return experiment_definition_to_dict(ed)
        return None

    def list_by_type(self, experiment_type: str) -> pd.DataFrame:
        df = self.load_definitions()
        if df.empty:
            return df
        return df[df["experiment_type"] == experiment_type]

    def list_by_hypothesis(self, hypothesis_id: str) -> pd.DataFrame:
        df = self.load_definitions()
        if df.empty:
            return df
        return df[df["hypothesis_id"] == hypothesis_id]

    def summarize(self) -> dict:
        df = self.load_definitions()
        if df.empty:
            return {
                "total_definitions": 0,
                "by_type": {},
                "by_profile": {}
            }

        return {
            "total_definitions": len(df),
            "by_type": df["experiment_type"].value_counts().to_dict(),
            "by_profile": df["profile_name"].value_counts().to_dict()
        }

def build_default_experiment_definitions(profile: ExperimentProfile) -> list[ExperimentDefinition]:
    now = datetime.now(timezone.utc).isoformat()
    defaults = [
        {
            "name": "baseline_meta_research_experiment",
            "type": "baseline_experiment",
            "module_scope": ["meta_research"]
        },
        {
            "name": "factor_ablation_without_macro_sensitivity",
            "type": "ablation_experiment",
            "module_scope": ["factor_research"]
        },
        {
            "name": "meta_research_without_ml_evidence",
            "type": "ablation_experiment",
            "module_scope": ["meta_research"]
        },
        {
            "name": "meta_research_without_factor_evidence",
            "type": "ablation_experiment",
            "module_scope": ["meta_research"]
        },
        {
            "name": "portfolio_regime_stress_ablation",
            "type": "ablation_experiment",
            "module_scope": ["portfolio_regime"]
        },
        {
            "name": "synthetic_index_rotation_ablation",
            "type": "ablation_experiment",
            "module_scope": ["synthetic_indices"]
        },
        {
            "name": "factor_neutralization_ablation",
            "type": "ablation_experiment",
            "module_scope": ["factor_research"]
        }
    ]

    definitions = []
    for d in defaults:
        e_id = build_experiment_id(d["name"], d["type"], "1d")
        ed = ExperimentDefinition(
            experiment_id=e_id,
            experiment_name=d["name"],
            experiment_type=d["type"],
            hypothesis_id=None,
            profile_name=profile.name,
            timeframe="1d",
            symbols=["*"],
            module_scope=d["module_scope"],
            parameters={},
            baseline_experiment_id=None,
            created_at_utc=now,
            notes="",
            warnings=[]
        )
        definitions.append(ed)

    return definitions
