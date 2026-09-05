"""Phase 128: Regime Rule-Free Safety Boundary.

Defines explicit NO-GO boundaries and SAFE-GO principles for Phase 128.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

NO_GO_CONDITIONS = [
    {"rule_id": "nogo_live_trading", "boundary": "live_trading", "description": "Sending real orders or live broker execution.", "enforced": True},
    {"rule_id": "nogo_broker_integration", "boundary": "broker_integration", "description": "Connecting live or paper trading broker APIs.", "enforced": True},
    {"rule_id": "nogo_investment_advice", "boundary": "investment_advice", "description": "Generating directional recommendations or investment advice.", "enforced": True},
    {"rule_id": "nogo_candidate_state_as_signal", "boundary": "candidate_as_signal", "description": "Using candidate state annotation as an actionable trade signal.", "enforced": True},
    {"rule_id": "nogo_pseudo_state_as_signal", "boundary": "pseudo_as_signal", "description": "Using pseudo-state definitions as entry/exit signals.", "enforced": True},
    {"rule_id": "nogo_directional_certainty", "boundary": "directional_claims", "description": "Asserting deterministic directional certainty (long/short).", "enforced": True},
    {"rule_id": "nogo_clustering_execution", "boundary": "algorithm_execution", "description": "Executing KMeans, DBSCAN, GMM, HDBSCAN, or SOM clustering.", "enforced": True},
    {"rule_id": "nogo_model_training", "boundary": "ml_training", "description": "Running model.fit(), train(), or model parameter optimization.", "enforced": True},
    {"rule_id": "nogo_model_predict", "boundary": "ml_predict", "description": "Running model.predict(), transform(), or generating inferences.", "enforced": True},
    {"rule_id": "nogo_dim_reduction_execution", "boundary": "dim_reduction", "description": "Executing PCA, UMAP, t-SNE, or autoencoder models.", "enforced": True},
    {"rule_id": "nogo_target_prediction_gen", "boundary": "supervised_labels", "description": "Generating future targets, supervised labels, or return forecasts.", "enforced": True},
    {"rule_id": "nogo_commercial_claims", "boundary": "commercial_claims", "description": "Claiming official approval, production-ready, or broker-ready status.", "enforced": True},
    {"rule_id": "nogo_source_overwrite", "boundary": "data_integrity", "description": "Overwriting source raw datasets or deleting records.", "enforced": True},
    {"rule_id": "nogo_destructive_cleaning", "boundary": "data_integrity", "description": "Performing automated destructive imputation or feature dropping.", "enforced": True},
    {"rule_id": "nogo_news_full_text", "boundary": "copyright", "description": "Scraping, storing, or processing full-text news article bodies.", "enforced": True},
    {"rule_id": "nogo_cloud_deployment", "boundary": "deployment", "description": "Pushing containers, deploying cloud web servers, or cloud publishing.", "enforced": True},
]

SAFE_GO_CONDITIONS = [
    {"rule_id": "safego_rule_free_contracts", "principle": "candidate_contracts", "description": "Local, offline rule-free candidate state contract definitions.", "active": True},
    {"rule_id": "safego_non_signal_pseudo_schema", "principle": "pseudo_state_schema", "description": "Pure exploratory pseudo-state schemas with mandatory non-signal flags.", "active": True},
    {"rule_id": "safego_unsupervised_prep_metadata", "principle": "unsupervised_prep", "description": "Contractual preparation metadata without fitting or running models.", "active": True},
    {"rule_id": "safego_clustering_inputs_no_exec", "principle": "clustering_inputs", "description": "Matrix schema contracts defining clustering inputs without execution.", "active": True},
    {"rule_id": "safego_algorithm_placeholders", "principle": "algorithm_placeholders", "description": "Metadata placeholders for distance and clustering algorithms.", "active": True},
    {"rule_id": "safego_no_lookahead_temporal_guard", "principle": "temporal_guard", "description": "Strict verification that context timestamps precede base observations.", "active": True},
    {"rule_id": "safego_source_preservation", "principle": "source_preservation", "description": "Explicit immutable copying and non-destructive manual review queues.", "active": True},
    {"rule_id": "safego_phase_129_diagnostics_handoff", "principle": "phase_129_handoff", "description": "Clean prerequisites handoff for Phase 129 market behavior diagnostics.", "active": True},
]


def build_regime_rule_free_no_go_conditions(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for NO-GO conditions."""
    df = pd.DataFrame(NO_GO_CONDITIONS)
    summary = {
        "total_no_go_rules": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "boundary_status": "SECURE",
    }
    return df, summary


def build_regime_rule_free_safe_go_conditions(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for SAFE-GO conditions."""
    df = pd.DataFrame(SAFE_GO_CONDITIONS)
    summary = {
        "total_safe_go_rules": len(df),
        "all_active": bool(df["active"].all()) if not df.empty else True,
        "principles_status": "ACTIVE",
    }
    return df, summary


def build_regime_rule_free_safety_boundary(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Combine NO-GO and SAFE-GO into a unified safety boundary registry."""
    df_nogo, s_nogo = build_regime_rule_free_no_go_conditions(profile)
    df_safego, s_safego = build_regime_rule_free_safe_go_conditions(profile)

    combined_rows = []
    for _, r in df_nogo.iterrows():
        combined_rows.append({
            "boundary_type": "NO_GO",
            "rule_id": r["rule_id"],
            "category": r["boundary"],
            "description": r["description"],
            "is_active": r["enforced"],
        })
    for _, r in df_safego.iterrows():
        combined_rows.append({
            "boundary_type": "SAFE_GO",
            "rule_id": r["rule_id"],
            "category": r["principle"],
            "description": r["description"],
            "is_active": r["active"],
        })

    df = pd.DataFrame(combined_rows)
    summary = summarize_regime_rule_free_safety_boundary(df)
    return df, summary


def summarize_regime_rule_free_safety_boundary(df: pd.DataFrame) -> Dict:
    """Summarize unified safety boundary."""
    no_go_count = int((df["boundary_type"] == "NO_GO").sum()) if not df.empty else 0
    safe_go_count = int((df["boundary_type"] == "SAFE_GO").sum()) if not df.empty else 0
    all_active = bool(df["is_active"].all()) if not df.empty else True

    return {
        "total_rules": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "all_active": all_active,
        "safety_status": "SECURE" if all_active and no_go_count >= 16 else "UNSAFE",
    }
