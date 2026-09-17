import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import AdvancedMlDatasetProfile, get_default_advanced_ml_dataset_profile
from advanced_ml_dataset_registry.advanced_ml_dataset_models import MlDatasetContract

_CONTRACTS = [
    MlDatasetContract(
        contract_name="regime_metadata_ml_dataset_contract",
        dataset_family="regime_metadata",
        source_phase_refs=["phase_126","phase_127","phase_128","phase_129","phase_130","phase_131","phase_132","phase_133","phase_134","phase_135"],
        source_catalog_refs=["regime_acceptance_catalog","featurestore_catalog"],
        required_schema_ref="regime_metadata_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="regime_no_lookahead_guard",
        required_metadata_only_news_guard_ref="macro_event_metadata_only_news_guard",
        required_source_preservation_guard_ref="regime_source_preservation_guard",
        required_validation_dependency_ref="phase_135_acceptance_validation",
        required_quality_dependency_ref="phase_135_quality_dependency",
    ),
    MlDatasetContract(
        contract_name="featurestore_ml_dataset_contract",
        dataset_family="featurestore",
        source_phase_refs=["phase_116","phase_117","phase_118","phase_119","phase_120","phase_121","phase_122","phase_123","phase_124","phase_125"],
        source_catalog_refs=["featurestore_catalog","feature_quality_drift_catalog"],
        required_schema_ref="featurestore_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="featurestore_no_lookahead_guard",
        required_metadata_only_news_guard_ref="news_metadata_only_guard",
        required_source_preservation_guard_ref="featurestore_source_preservation_guard",
        required_validation_dependency_ref="phase_134_featurestore_validation",
        required_quality_dependency_ref="phase_134_featurestore_quality",
    ),
    MlDatasetContract(
        contract_name="technical_feature_ml_dataset_contract",
        dataset_family="technical_features",
        source_phase_refs=["phase_116","phase_117","phase_118"],
        source_catalog_refs=["technical_indicators_catalog","feature_engine_catalog"],
        required_schema_ref="technical_feature_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="technical_feature_no_lookahead_guard",
        required_metadata_only_news_guard_ref="news_metadata_only_guard",
        required_source_preservation_guard_ref="technical_source_preservation_guard",
        required_validation_dependency_ref="phase_121_validation",
        required_quality_dependency_ref="phase_123_quality_drift",
    ),
    MlDatasetContract(
        contract_name="factor_feature_ml_dataset_contract",
        dataset_family="factor_features",
        source_phase_refs=["phase_122","phase_123","phase_124","phase_125"],
        source_catalog_refs=["factor_metadata_catalog","feature_factor_acceptance_catalog"],
        required_schema_ref="factor_feature_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="factor_no_lookahead_guard",
        required_metadata_only_news_guard_ref="news_metadata_only_guard",
        required_source_preservation_guard_ref="factor_source_preservation_guard",
        required_validation_dependency_ref="phase_125_factor_validation",
        required_quality_dependency_ref="phase_123_quality_drift",
    ),
    MlDatasetContract(
        contract_name="cross_asset_feature_ml_dataset_contract",
        dataset_family="cross_asset_features",
        source_phase_refs=["phase_119","phase_120"],
        source_catalog_refs=["cross_asset_alignment_catalog"],
        required_schema_ref="cross_asset_feature_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="cross_asset_no_lookahead_guard",
        required_metadata_only_news_guard_ref="news_metadata_only_guard",
        required_source_preservation_guard_ref="cross_asset_source_preservation_guard",
        required_validation_dependency_ref="phase_121_validation",
        required_quality_dependency_ref="phase_123_quality_drift",
    ),
    MlDatasetContract(
        contract_name="macro_event_news_metadata_ml_dataset_contract",
        dataset_family="macro_event_news_metadata",
        source_phase_refs=["phase_126","phase_127","phase_128"],
        source_catalog_refs=["economic_calendar_catalog","news_metadata_catalog"],
        required_schema_ref="macro_event_news_metadata_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="macro_event_no_lookahead_guard",
        required_metadata_only_news_guard_ref="macro_event_metadata_only_news_guard",
        required_source_preservation_guard_ref="macro_event_source_preservation_guard",
        required_validation_dependency_ref="phase_133_regime_validation",
        required_quality_dependency_ref="phase_135_quality_dependency",
    ),
    MlDatasetContract(
        contract_name="validation_accepted_ml_dataset_contract",
        dataset_family="validation_accepted",
        source_phase_refs=["phase_133","phase_134","phase_135"],
        source_catalog_refs=["regime_validation_acceptance_catalog","featurestore_catalog"],
        required_schema_ref="validation_accepted_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="validation_accepted_no_lookahead_guard",
        required_metadata_only_news_guard_ref="news_metadata_only_guard",
        required_source_preservation_guard_ref="validation_source_preservation_guard",
        required_validation_dependency_ref="phase_135_acceptance_validation",
        required_quality_dependency_ref="phase_135_quality_dependency",
    ),
    MlDatasetContract(
        contract_name="dry_run_baseline_model_input_contract",
        dataset_family="dry_run_baseline",
        source_phase_refs=["phase_136"],
        source_catalog_refs=["gpu_ml_runtime_catalog"],
        required_schema_ref="dry_run_baseline_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="baseline_no_lookahead_guard",
        required_metadata_only_news_guard_ref="news_metadata_only_guard",
        required_source_preservation_guard_ref="baseline_source_preservation_guard",
        required_validation_dependency_ref="phase_136_runtime_validation",
        required_quality_dependency_ref="phase_136_runtime_quality",
    ),
    MlDatasetContract(
        contract_name="phase_138_training_harness_input_contract",
        dataset_family="phase_138_training_harness",
        source_phase_refs=["phase_136","phase_137"],
        source_catalog_refs=["gpu_ml_runtime_catalog","advanced_ml_dataset_registry_catalog"],
        required_schema_ref="phase_138_training_harness_schema",
        required_time_index_policy_ref="chronological_time_index_policy",
        required_split_policy_ref="chronological_train_validation_test_placeholder",
        required_no_lookahead_guard_ref="phase_138_no_lookahead_guard",
        required_metadata_only_news_guard_ref="news_metadata_only_guard",
        required_source_preservation_guard_ref="phase_138_source_preservation_guard",
        required_validation_dependency_ref="phase_137_validation",
        required_quality_dependency_ref="phase_137_quality",
    ),
]


def build_ml_dataset_contract_registry(
    profile: AdvancedMlDatasetProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build a registry DataFrame and summary dict for all ML dataset contracts.

    No data is materialized, no model training occurs, no targets/labels are
    generated.  dry_run=True, local_only=True, non_production=True.
    """
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()

    rows = []
    for c in _CONTRACTS:
        rows.append({
            "contract_name": c.contract_name,
            "dataset_family": c.dataset_family,
            "source_phase_refs": ", ".join(c.source_phase_refs),
            "required_schema_ref": c.required_schema_ref,
            "required_time_index_policy_ref": c.required_time_index_policy_ref,
            "required_split_policy_ref": c.required_split_policy_ref,
            "required_no_lookahead_guard_ref": c.required_no_lookahead_guard_ref,
            "required_metadata_only_news_guard_ref": c.required_metadata_only_news_guard_ref,
            "required_validation_dependency_ref": c.required_validation_dependency_ref,
            "target_label_generation_allowed": c.target_label_generation_allowed,
            "dataset_materialization_allowed": c.dataset_materialization_allowed,
            "model_training_allowed": c.model_training_allowed,
            "prediction_allowed": c.prediction_allowed,
            "artifact_persistence_allowed": c.artifact_persistence_allowed,
            "non_signal_required": c.non_signal_required,
            "manual_review_required": c.manual_review_required,
            "status": c.status,
        })

    df = pd.DataFrame(rows)
    summary = {
        "total_contracts": len(rows),
        "current_phase": 137,
        "target_final_phase": 160,
        "next_phase": 138,
        "non_signal": True,
        "dry_run": True,
        "dataset_materialized": False,
        "dataset_materialization_allowed": False,
        "materialization_allowed": False,
        "model_training_allowed": False,
        "training_allowed": False,
        "prediction_allowed": False,
        "target_label_allowed": False,
        "target_label_generation_allowed": False,
        "status": "READY",
    }
    return df, summary


def validate_ml_dataset_contract(contract: Dict) -> Dict:
    """Validate a single contract dict against non-production safety flags.

    Returns a dict with keys `valid` (bool), `issues` (list[str]), and
    `non_signal` (bool).
    """
    issues: List[str] = []
    if contract.get("target_label_generation_allowed", False):
        issues.append("target_label_generation_allowed must be False")
    if contract.get("dataset_materialization_allowed", False):
        issues.append("dataset_materialization_allowed must be False")
    if contract.get("model_training_allowed", False):
        issues.append("model_training_allowed must be False")
    if contract.get("prediction_allowed", False):
        issues.append("prediction_allowed must be False")
    if contract.get("artifact_persistence_allowed", False):
        issues.append("artifact_persistence_allowed must be False")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}


def summarize_ml_dataset_contracts(df: pd.DataFrame) -> Dict:
    """Return a lightweight summary dict for an existing contract registry DataFrame."""
    return {
        "total_contracts": len(df),
        "current_phase": 137,
        "non_signal": True,
        "dataset_materialized": False,
        "dataset_materialization_allowed": False,
        "materialization_allowed": False,
        "model_training_allowed": False,
        "training_allowed": False,
        "prediction_allowed": False,
        "target_label_allowed": False,
        "status": "READY",
    }
