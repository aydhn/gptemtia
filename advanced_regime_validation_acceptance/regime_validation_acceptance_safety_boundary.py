"""Phase 133: Regime Validation Acceptance Safety Boundary.

Enforces explicit NO-GO barriers and SAFE-GO operating principles.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)

NO_GO_CONDITIONS = [
    ("NO_GO_01_LIVE_TRADING", "live trading", "Prohibits live order submission or real exchange connections."),
    ("NO_GO_02_BROKER_INTEGRATION", "broker integration", "Prohibits broker API credentials or execution hooks."),
    ("NO_GO_03_REAL_ORDER", "real order", "Prohibits execution of actual capital orders."),
    ("NO_GO_04_INVESTMENT_ADVICE", "investment advice", "Prohibits financial or investment advice generation."),
    ("NO_GO_05_VALIDATION_AS_SIGNAL", "validation as signal", "Prohibits treating validation pass/fail as a trade signal."),
    ("NO_GO_06_ACCEPTANCE_AS_SIGNAL", "acceptance as signal", "Prohibits treating acceptance score as a trade signal."),
    ("NO_GO_07_DIRECTIONAL_CLAIM", "directional certainty", "Prohibits asserting bullish/bearish market directional claims."),
    ("NO_GO_08_MODEL_EXECUTION", "model training / fit / predict", "Prohibits ML model training, fitting, or predictive inference."),
    ("NO_GO_09_CLUSTERING_EXECUTION", "clustering execution", "Prohibits unsupervised clustering execution (KMeans, GMM, HMM)."),
    ("NO_GO_10_TARGET_LABEL", "target / label / prediction", "Prohibits generating supervised target or label series."),
    ("NO_GO_11_SENTIMENT_OUTPUT", "sentiment model output", "Prohibits sentiment model scoring or sentiment features."),
    ("NO_GO_12_FULL_ARTICLE_USAGE", "full article / raw content", "Prohibits copyrighted article bodies, raw text, or scraped HTML."),
    ("NO_GO_13_EMBEDDING_VECTOR", "embedding / vector generation", "Prohibits embedding generation and vector DB deployment."),
    ("NO_GO_14_OFFICIAL_APPROVAL", "official approval claim", "Prohibits claiming official regulator or exchange approval."),
    ("NO_GO_15_PRODUCTION_READY", "production-ready / broker-ready claim", "Prohibits claiming production or broker readiness."),
    ("NO_GO_16_SOURCE_OVERWRITE", "source overwrite / destructive clean", "Prohibits overwriting, modifying, or deleting source records."),
    ("NO_GO_17_AUTO_IMPUTATION", "auto-imputation / auto-feature-drop", "Prohibits automatic dropping or imputing of features."),
    ("NO_GO_18_WEB_SCRAPING", "scraping / rate limit abuse", "Prohibits active web scraping or paywall bypass."),
    ("NO_GO_19_DEPLOYMENT", "model / production deployment", "Prohibits cloud deployment, docker push, or release tagging."),
]

SAFE_GO_CONDITIONS = [
    ("SAFE_GO_01_LOCAL_VALIDATION", "local/offline validation acceptance", "Permits offline local verification of regime datasets."),
    ("SAFE_GO_02_NO_LOOKAHEAD", "no-lookahead acceptance", "Enforces backward timestamp checks and negative shift detection."),
    ("SAFE_GO_03_TIMESTAMP_ORDER", "timestamp order acceptance", "Verifies monotonic ordering and point-in-time constraints."),
    ("SAFE_GO_04_BACKWARD_ASOF", "backward-asof acceptance", "Enforces strictly backward direction for time-series joins."),
    ("SAFE_GO_05_FORBIDDEN_COLUMN", "forbidden column acceptance", "Rejects columns representing signals, targets, or raw text."),
    ("SAFE_GO_06_METADATA_ONLY_NEWS", "metadata-only news acceptance", "Restricts news to tags, topics, source IDs, and published_at."),
    ("SAFE_GO_07_SOURCE_PRESERVATION", "source preservation acceptance", "Guarantees raw data and lake immutability."),
    ("SAFE_GO_08_NON_SIGNAL", "non-signal acceptance", "Ensures all outputs remain purely structural and descriptive."),
    ("SAFE_GO_09_COMPONENT_ACCEPTANCE", "component acceptance", "Validates Phases 127-132 regime components locally."),
    ("SAFE_GO_10_DEPENDENCY_ACCEPTANCE", "dependency acceptance", "Validates upstream validation and quality prerequisites."),
    ("SAFE_GO_11_ACCEPTANCE_MANIFEST", "source-preserved acceptance manifest", "Emits structured audit manifest certifying boundaries."),
    ("SAFE_GO_12_PHASE_134_HANDOFF", "Phase 134 FeatureStore integration handoff", "Delivers clean, verified metadata to Phase 134."),
]


def build_regime_validation_acceptance_no_go_conditions(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of NO-GO boundaries."""
    p = profile or get_default_regime_validation_acceptance_profile()
    rows = []
    for cond_id, name, desc in NO_GO_CONDITIONS:
        rows.append(
            {
                "condition_id": cond_id,
                "condition_name": name,
                "description": desc,
                "enforced": True,
                "violated": False,
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )
    return pd.DataFrame(rows)


def build_regime_validation_acceptance_safe_go_conditions(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of SAFE-GO operating principles."""
    p = profile or get_default_regime_validation_acceptance_profile()
    rows = []
    for cond_id, name, desc in SAFE_GO_CONDITIONS:
        rows.append(
            {
                "condition_id": cond_id,
                "condition_name": name,
                "description": desc,
                "permitted": True,
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )
    return pd.DataFrame(rows)


def build_regime_validation_acceptance_safety_boundary(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build complete safety boundary DataFrame and summary."""
    p = profile or get_default_regime_validation_acceptance_profile()
    no_go_df = build_regime_validation_acceptance_no_go_conditions(p)
    safe_go_df = build_regime_validation_acceptance_safe_go_conditions(p)

    all_rows = []
    for _, r in no_go_df.iterrows():
        all_rows.append({"boundary_type": "NO_GO", "item_name": r["condition_name"], "description": r["description"], "status": "ENFORCED"})
    for _, r in safe_go_df.iterrows():
        all_rows.append({"boundary_type": "SAFE_GO", "item_name": r["condition_name"], "description": r["description"], "status": "ACTIVE"})

    df = pd.DataFrame(all_rows)
    summary = {
        "safety_status": "SECURE",
        "no_go_count": len(no_go_df),
        "safe_go_count": len(safe_go_df),
        "total_boundaries": len(df),
        "profile_name": p.profile_name,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_regime_validation_acceptance_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    no_go = int((df["boundary_type"] == "NO_GO").sum()) if "boundary_type" in df.columns else 0
    safe_go = int((df["boundary_type"] == "SAFE_GO").sum()) if "boundary_type" in df.columns else 0
    return {
        "safety_status": "SECURE",
        "no_go_count": no_go,
        "safe_go_count": safe_go,
        "total_boundaries": len(df),
    }
