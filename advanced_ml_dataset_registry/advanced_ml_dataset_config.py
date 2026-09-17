# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Dataset profile configuration and registry helpers.

Constraints:
  current_phase=137, target_final_phase=160, next_phase=138
  dry_run=True, local_only=True, non_production=True, research_only=True
  All live/broker/training/prediction/materialization flags = False
  No dataset materialization, no model training/fit/predict/inference.
  No target/label/prediction generation, no artifact persistence writes.
  No credential output, no source overwrite, no auto-imputation/feature-drop.
  No official-approval / production-ready / broker-ready claims.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# Dataclass
# ---------------------------------------------------------------------------

@dataclass
class AdvancedMlDatasetProfile:
    """Immutable-intent profile describing dataset contract and experiment
    registry constraints for Phase 137 research workflows.

    All 'allow_*' flags default to False to enforce safety boundaries.
    All 'enable_*' flags default to True to enable contract/registry checks.
    """

    name: str
    description: str
    enabled: bool = True

    # Phase metadata
    current_phase: int = 137
    target_final_phase: int = 160
    next_phase: int = 138

    @property
    def profile_name(self) -> str:
        return self.name

    def __getitem__(self, item: str):
        return getattr(self, item)

    def get(self, item: str, default=None):
        return getattr(self, item, default)

    # Execution mode
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True

    # ------------------------------------------------------------------ #
    # Safety: ALL allow_ flags are False by default
    # ------------------------------------------------------------------ #
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_signal_generation: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False

    # Dataset / feature materialization
    allow_dataset_materialization: bool = False
    allow_feature_snapshot_materialization: bool = False

    # Model lifecycle
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_model_inference: bool = False
    allow_model_transform: bool = False

    # ML execution modes
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_ensemble_execution: bool = False
    allow_calibration_execution: bool = False

    # Target / prediction / output generation
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
    allow_sentiment_model_output: bool = False

    # Content / embedding / vector restrictions
    allow_full_article_usage: bool = False
    allow_article_body_usage: bool = False
    allow_raw_content_usage: bool = False
    allow_scraped_html_usage: bool = False
    allow_embedding_generation: bool = False
    allow_vector_db: bool = False

    # Artifact / registry writes
    allow_artifact_persistence: bool = False
    allow_model_registry_write: bool = False

    # Approval / deployment claims
    allow_official_approval_claim: bool = False
    allow_production_ready_claim: bool = False
    allow_broker_ready_claim: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False

    # Scraping / credentials
    allow_web_scraping: bool = False
    allow_credential_output: bool = False

    # Destructive operations
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False

    # ------------------------------------------------------------------ #
    # Enabled contract/registry features
    # ------------------------------------------------------------------ #
    enable_dataset_contracts: bool = True
    enable_schema_policies: bool = True
    enable_split_policies: bool = True
    enable_leakage_guards: bool = True
    enable_feature_snapshot_contracts: bool = True
    enable_experiment_registry: bool = True
    enable_disabled_training_contracts: bool = True
    enable_lineage: bool = True
    enable_quality_gates: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_138_handoff: bool = True

    # ------------------------------------------------------------------ #
    # Thresholds
    # ------------------------------------------------------------------ #
    min_readiness_score: float = 0.45
    save_reports: bool = True


# ---------------------------------------------------------------------------
# Profile definitions
# ---------------------------------------------------------------------------

_balanced_local = AdvancedMlDatasetProfile(
    name="balanced_local_ml_dataset_contracts",
    description=(
        "Default Phase 137 profile. Balanced dataset contract enforcement with "
        "full schema/split/leakage/lineage/quality gates enabled. "
        "Dry-run, local-only, research-only. All training and materialization blocked."
    ),
)

_strict_no_mat = AdvancedMlDatasetProfile(
    name="strict_no_materialization_no_training_dataset_safety",
    description=(
        "Strict safety profile. Zero materialization, zero training, zero prediction. "
        "Every potentially unsafe flag is explicitly confirmed False. "
        "Intended for schema-only audits and lineage reviews."
    ),
    min_readiness_score=0.60,
    allow_dataset_materialization=False,
    allow_feature_snapshot_materialization=False,
    allow_model_training=False,
    allow_model_fit=False,
    allow_model_predict=False,
    allow_model_inference=False,
    allow_model_transform=False,
    allow_target_label_generation=False,
    allow_prediction_generation=False,
    allow_artifact_persistence=False,
    allow_model_registry_write=False,
    allow_source_overwrite=False,
    allow_auto_destructive_cleaning=False,
    allow_auto_imputation=False,
    allow_auto_feature_drop=False,
)

_dry_run_registry = AdvancedMlDatasetProfile(
    name="dry_run_experiment_registry_focus",
    description=(
        "Experiment registry-focused profile. Maximises registry, manifest, "
        "findings and phase-138 handoff checks while keeping all execution "
        "modes blocked. Optimised for dry-run experiment metadata workflows."
    ),
    min_readiness_score=0.40,
    enable_experiment_registry=True,
    enable_manifest=True,
    enable_findings=True,
    enable_phase_138_handoff=True,
    enable_lineage=True,
    enable_quality_gates=True,
    enable_disabled_training_contracts=True,
    allow_model_training=False,
    allow_dataset_materialization=False,
    allow_feature_snapshot_materialization=False,
    allow_prediction_generation=False,
    allow_artifact_persistence=False,
)

_PROFILES: Dict[str, AdvancedMlDatasetProfile] = {
    _balanced_local.name: _balanced_local,
    _strict_no_mat.name: _strict_no_mat,
    _dry_run_registry.name: _dry_run_registry,
}

_DEFAULT_PROFILE_NAME: str = "balanced_local_ml_dataset_contracts"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_advanced_ml_dataset_profile(name: str) -> AdvancedMlDatasetProfile:
    """Return the profile matching *name*.

    Raises
    ------
    KeyError
        If *name* is not found in the profile registry.
    """
    if name not in _PROFILES:
        available = ", ".join(_PROFILES.keys())
        raise KeyError(
            f"Profile '{name}' not found. Available profiles: {available}"
        )
    return _PROFILES[name]


def list_advanced_ml_dataset_profiles(enabled_only: bool = True) -> List[AdvancedMlDatasetProfile]:
    """Return a list of registered AdvancedMlDatasetProfile objects.

    Parameters
    ----------
    enabled_only:
        When *True* (default), only profiles with ``enabled=True`` are returned.

    Returns
    -------
    List[AdvancedMlDatasetProfile]
    """
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_advanced_ml_dataset_profiles() -> Dict:
    """Validate all registered profiles against Phase 137 safety constraints.

    Checks that every profile has:
    - All dangerous ``allow_*`` flags set to False.
    - ``dry_run_default``, ``local_only``, ``non_production``,
      ``research_only`` all True.
    - ``current_phase == 137``, ``next_phase == 138``,
      ``target_final_phase == 160``.

    Returns
    -------
    Dict
        Keys: ``"all_valid"`` (bool), ``"profiles"`` (dict of per-profile results).
    """
    _must_be_false = [
        "allow_live_trading",
        "allow_broker_integration",
        "allow_real_order",
        "allow_investment_advice",
        "allow_signal_generation",
        "allow_directional_claim",
        "allow_strategy_generation",
        "allow_backtest_execution",
        "allow_optimizer_execution",
        "allow_dataset_materialization",
        "allow_feature_snapshot_materialization",
        "allow_model_training",
        "allow_model_fit",
        "allow_model_predict",
        "allow_model_inference",
        "allow_model_transform",
        "allow_clustering_execution",
        "allow_unsupervised_execution",
        "allow_ensemble_execution",
        "allow_calibration_execution",
        "allow_target_label_generation",
        "allow_prediction_generation",
        "allow_sentiment_model_output",
        "allow_full_article_usage",
        "allow_article_body_usage",
        "allow_raw_content_usage",
        "allow_scraped_html_usage",
        "allow_embedding_generation",
        "allow_vector_db",
        "allow_artifact_persistence",
        "allow_model_registry_write",
        "allow_official_approval_claim",
        "allow_production_ready_claim",
        "allow_broker_ready_claim",
        "allow_model_deployment",
        "allow_production_deployment",
        "allow_web_scraping",
        "allow_credential_output",
        "allow_source_overwrite",
        "allow_auto_destructive_cleaning",
        "allow_file_deletion",
        "allow_overwrite",
        "allow_auto_imputation",
        "allow_auto_feature_drop",
    ]

    _must_be_true = [
        "dry_run_default",
        "local_only",
        "non_production",
        "research_only",
    ]

    profiles_result: Dict[str, Dict] = {}
    all_valid = True

    for name, profile in _PROFILES.items():
        violations: List[str] = []

        for flag in _must_be_false:
            if getattr(profile, flag, False) is not False:
                violations.append(f"{flag} must be False")

        for flag in _must_be_true:
            if getattr(profile, flag, True) is not True:
                violations.append(f"{flag} must be True")

        if profile.current_phase != 137:
            violations.append(f"current_phase must be 137, got {profile.current_phase}")
        if profile.next_phase != 138:
            violations.append(f"next_phase must be 138, got {profile.next_phase}")
        if profile.target_final_phase != 160:
            violations.append(
                f"target_final_phase must be 160, got {profile.target_final_phase}"
            )

        is_valid = len(violations) == 0
        if not is_valid:
            all_valid = False

        profiles_result[name] = {
            "valid": is_valid,
            "enabled": profile.enabled,
            "violations": violations,
        }

    return {
        "valid": all_valid,
        "all_valid": all_valid,
        "profile_count": len(_PROFILES),
        "profiles": profiles_result,
    }


def get_default_advanced_ml_dataset_profile() -> AdvancedMlDatasetProfile:
    """Return the default Phase 137 dataset profile.

    Returns
    -------
    AdvancedMlDatasetProfile
        The ``balanced_local_ml_dataset_contracts`` profile.
    """
    return _PROFILES[_DEFAULT_PROFILE_NAME]
