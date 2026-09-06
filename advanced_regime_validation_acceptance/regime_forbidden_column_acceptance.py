"""Phase 133: Regime Forbidden Column Acceptance Report and Validators.

Detects and rejects forbidden columns such as trading signals, targets, labels,
predictions, future returns, full text, and sentiment scores.
"""

from typing import Any, Dict, List, Optional, Set, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)

FORBIDDEN_REGIME_COLUMNS: Set[str] = {
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
}


def validate_forbidden_regime_columns(column_names: List[str]) -> Dict[str, Any]:
    """Check a list of column names for forbidden trading, target, or content terms."""
    if not column_names:
        return {
            "passed": True,
            "forbidden_found": [],
            "status": "acceptance_pass",
            "message": "Empty column list; zero forbidden columns.",
        }

    violating = []
    for col in column_names:
        clean_col = col.lower().strip()
        if clean_col in FORBIDDEN_REGIME_COLUMNS:
            violating.append(col)
        elif any(f"_{term}_" in f"_{clean_col}_" for term in ["future_return", "forward_return", "next_return"]):
            violating.append(col)
        elif clean_col in ["buy_signal", "sell_signal", "trade_signal", "target_label"]:
            violating.append(col)

    if violating:
        return {
            "passed": False,
            "forbidden_found": violating,
            "status": "acceptance_fail",
            "message": f"Detected forbidden columns: {violating}",
        }

    return {
        "passed": True,
        "forbidden_found": [],
        "status": "acceptance_pass",
        "message": "Zero forbidden columns found; all columns adhere to acceptance boundaries.",
    }


def build_regime_forbidden_column_acceptance_report(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Forbidden Column Acceptance."""
    p = profile or get_default_regime_validation_acceptance_profile()

    rows = []
    for term in sorted(list(FORBIDDEN_REGIME_COLUMNS)):
        category = "signal"
        if term in {"buy", "sell", "long", "short", "position", "recommendation"}:
            category = "trade_direction"
        elif term in {"target", "label", "prediction"}:
            category = "supervised_learning"
        elif term in {"future_return", "forward_return", "next_return"}:
            category = "lookahead_return"
        elif term in {"full_text", "article_body", "raw_content", "scraped_html", "page_html", "html"}:
            category = "raw_content"
        elif term in {"embedding", "vector", "sentiment", "sentiment_score"}:
            category = "ml_nlp_output"

        rows.append(
            {
                "forbidden_term": term,
                "category": category,
                "rejection_action": "block_and_flag",
                "severity": "acceptance_critical",
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_forbidden_rules": len(df),
        "profile_name": p.profile_name,
        "all_rules_active": True,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_regime_forbidden_column_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column acceptance DataFrame."""
    return {
        "total_rules": len(df),
        "all_rules_active": True,
        "categories_checked": df["category"].nunique() if "category" in df.columns else 0,
    }
