"""Phase 127: Regime Matrix Safety Boundary.

Enforces NO-GO restrictions and defines SAFE-GO operational principles for Phase 127.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

NO_GO_RULES: List[Dict[str, Any]] = [
    {"rule_id": "nogo_001_live_trading", "category": "execution", "description": "Prohibit live trading or real money account execution."},
    {"rule_id": "nogo_002_broker_integration", "category": "broker", "description": "Prohibit broker API integration or order transmission."},
    {"rule_id": "nogo_003_real_orders", "category": "execution", "description": "Prohibit real buy/sell orders or position modification."},
    {"rule_id": "nogo_004_investment_advice", "category": "legal", "description": "Prohibit financial or investment advice generation."},
    {"rule_id": "nogo_005_matrix_as_signal", "category": "signal", "description": "Prohibit treating regime feature matrix values as trading signals."},
    {"rule_id": "nogo_006_state_dataset_as_signal", "category": "signal", "description": "Prohibit treating state dataset rows or contexts as trade triggers."},
    {"rule_id": "nogo_007_directional_claims", "category": "claim", "description": "Prohibit directional certainty claims (e.g. guaranteed upward regime)."},
    {"rule_id": "nogo_008_strategy_backtest_optimizer", "category": "strategy", "description": "Prohibit strategy generation, backtests, or parameter optimization."},
    {"rule_id": "nogo_009_model_training_clustering", "category": "ml", "description": "Prohibit model training, clustering execution (HMM, GMM), or unsupervised fit."},
    {"rule_id": "nogo_010_target_label_generation", "category": "ml", "description": "Prohibit generating target labels or prediction columns."},
    {"rule_id": "nogo_011_official_approval_claims", "category": "claim", "description": "Prohibit claims of official approval, production readiness, or broker readiness."},
    {"rule_id": "nogo_012_source_overwrite_destruction", "category": "data", "description": "Prohibit destructive cleaning, file deletion, or overwriting raw data."},
    {"rule_id": "nogo_013_auto_imputation_drop", "category": "data", "description": "Prohibit synthetic imputation or silent auto-feature-dropping."},
    {"rule_id": "nogo_014_full_article_news_scraping", "category": "news", "description": "Prohibit scraping news web pages or storing full copyrighted article text."},
    {"rule_id": "nogo_015_credential_and_deployment", "category": "security", "description": "Prohibit outputting secrets/credentials or triggering cloud deployment."},
]

SAFE_GO_RULES: List[Dict[str, Any]] = [
    {"rule_id": "safego_001_local_offline_contracts", "category": "contracts", "description": "Local/offline regime feature matrix contracts."},
    {"rule_id": "safego_002_non_signal_state_datasets", "category": "datasets", "description": "Non-signal candidate context state dataset contracts."},
    {"rule_id": "safego_003_guarded_matrix_schema", "category": "alignment", "description": "Timestamp-aligned, no-lookahead guarded matrix schema."},
    {"rule_id": "safego_004_metadata_only_news", "category": "news", "description": "Metadata-only numerical news tag and frequency contexts."},
    {"rule_id": "safego_005_source_preserved_metadata", "category": "governance", "description": "Source-preserved dataset metadata with non-destructive copies."},
    {"rule_id": "safego_006_dependency_mapping", "category": "validation", "description": "Validation and quality dependency mapping for matrix rows."},
    {"rule_id": "safego_007_phase_128_handoff", "category": "handoff", "description": "Clean, structured handoff to Phase 128 Rule-Free Labeling & Unsupervised Prep."},
]


def build_regime_matrix_no_go_conditions(
    profile: Optional[RegimeMatrixProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of NO-GO boundaries."""
    p = profile or get_default_regime_matrix_profile()
    rows = []
    for r in NO_GO_RULES:
        r_copy = r.copy()
        r_copy["rule_type"] = "NO_GO"
        r_copy["status"] = "ENFORCED"
        r_copy["current_phase"] = p.current_phase
        rows.append(r_copy)
    return pd.DataFrame(rows)


def build_regime_matrix_safe_go_conditions(
    profile: Optional[RegimeMatrixProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of SAFE-GO principles."""
    p = profile or get_default_regime_matrix_profile()
    rows = []
    for r in SAFE_GO_RULES:
        r_copy = r.copy()
        r_copy["rule_type"] = "SAFE_GO"
        r_copy["status"] = "ACTIVE"
        r_copy["current_phase"] = p.current_phase
        rows.append(r_copy)
    return pd.DataFrame(rows)


def build_regime_matrix_safety_boundary(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build combined safety boundary DataFrame and summary."""
    df_nogo = build_regime_matrix_no_go_conditions(profile)
    df_safego = build_regime_matrix_safe_go_conditions(profile)
    combined = pd.concat([df_nogo, df_safego], ignore_index=True)
    summary = summarize_regime_matrix_safety_boundary(combined)
    return combined, summary


def is_safe_regime_matrix_operation(operation: str) -> bool:
    """Check whether a requested operation complies with Phase 127 safety boundaries."""
    op_lower = str(operation).lower()
    unsafe_tokens = [
        "trade", "order", "broker", "train", "clustering", "signal",
        "buy", "sell", "predict", "target", "label", "mutate", "delete", "scrape",
    ]
    for token in unsafe_tokens:
        if token in op_lower:
            return False
    return True


def summarize_regime_matrix_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the safety boundaries."""
    no_go_count = int((df["rule_type"] == "NO_GO").sum()) if not df.empty else 0
    safe_go_count = int((df["rule_type"] == "SAFE_GO").sum()) if not df.empty else 0

    return {
        "total_safety_rules": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "safety_status": "SECURE",
        "live_trading_prohibited": True,
        "broker_integration_prohibited": True,
        "model_training_prohibited": True,
        "source_mutation_prohibited": True,
        "non_signal": True,
        "source_preserved": True,
    }


audit_regime_matrix_safety_boundary = build_regime_matrix_safety_boundary

