import pandas as pd
import hashlib
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any

from experiments.experiment_config import ExperimentProfile

@dataclass
class AblationStudyDefinition:
    ablation_id: str
    study_name: str
    baseline_experiment_id: str
    removed_components: list[str]
    modified_parameters: dict
    target_metrics: list[str]
    created_at_utc: str
    notes: str
    warnings: list[str]

def build_ablation_id(study_name: str, removed_components: list[str]) -> str:
    comps = "_".join(sorted(removed_components))
    raw = f"{study_name}_{comps}"
    h = hashlib.md5(raw.encode()).hexdigest()[:8]
    return f"abl_{h}"

def ablation_study_definition_to_dict(study: AblationStudyDefinition) -> dict:
    return asdict(study)

def build_default_ablation_studies(profile: ExperimentProfile) -> list[AblationStudyDefinition]:
    now = datetime.now(timezone.utc).isoformat()
    baseline_id = "exp_baseline_meta_rese_8b6883ba" # A hypothetical baseline ID

    defaults = [
        {"name": "remove_ml_evidence", "comps": ["ml"]},
        {"name": "remove_factor_evidence", "comps": ["factor"]},
        {"name": "remove_regime_evidence", "comps": ["regime"]},
        {"name": "remove_synthetic_index_evidence", "comps": ["synthetic_index"]},
        {"name": "remove_validation_penalty", "comps": ["validation_penalty"]},
        {"name": "remove_uncertainty_penalty", "comps": ["uncertainty_penalty"]},
        {"name": "remove_quality_penalty", "comps": ["quality_penalty"]},
        {"name": "remove_asset_class_neutralization", "comps": ["neutralization"]},
    ]

    studies = []
    for d in defaults:
        a_id = build_ablation_id(d["name"], d["comps"])
        study = AblationStudyDefinition(
            ablation_id=a_id,
            study_name=d["name"],
            baseline_experiment_id=baseline_id,
            removed_components=d["comps"],
            modified_parameters={},
            target_metrics=["quality_adjusted_score", "validation_score", "reproducibility_score"],
            created_at_utc=now,
            notes="",
            warnings=[]
        )
        studies.append(study)

    return studies

def build_ablation_result_table(baseline_metrics: dict, ablation_metrics_map: dict[str, dict]) -> pd.DataFrame:
    rows = []

    # Add baseline row
    b_row = {"ablation_id": "baseline", "study_name": "BASELINE"}
    for k, v in baseline_metrics.items():
        if isinstance(v, (int, float)):
            b_row[k] = v
    rows.append(b_row)

    # Add ablation rows
    for study_id, metrics in ablation_metrics_map.items():
        a_row = {"ablation_id": study_id, "study_name": metrics.get("study_name", study_id)}
        for k, v in metrics.items():
            if k == "study_name":
                continue
            if isinstance(v, (int, float)):
                a_row[k] = v
                # Calculate diff from baseline if baseline has it
                if k in baseline_metrics and isinstance(baseline_metrics[k], (int, float)):
                    a_row[f"{k}_diff"] = v - baseline_metrics[k]
        rows.append(a_row)

    return pd.DataFrame(rows)

def summarize_ablation_results(ablation_df: pd.DataFrame) -> dict:
    if ablation_df.empty:
        return {"total_studies": 0}

    summary = {
        "total_studies": len(ablation_df) - 1 if "baseline" in ablation_df["ablation_id"].values else len(ablation_df),
        "metrics_analyzed": [c for c in ablation_df.columns if not c.endswith("_diff") and c not in ["ablation_id", "study_name"]]
    }
    return summary
