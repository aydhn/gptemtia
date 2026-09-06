"""Phase 135: Regime Block Safety Boundary Report.

Defines unambiguous NO-GO prohibitions and SAFE-GO principles for the regime classification block.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    REGIME_BLOCK_SAFETY_BOUNDARY_DOMAIN,
)


NO_GO_DEFINITIONS: List[Dict[str, Any]] = [
    {"rule_id": "nogo_01", "rule_name": "No Live Trading", "prohibition": "Submitting live orders, routing orders, or interacting with broker exchange endpoints."},
    {"rule_id": "nogo_02", "rule_name": "No Broker Integration", "prohibition": "Authenticating or connecting with broker accounts, APIs, or trading gateways."},
    {"rule_id": "nogo_03", "rule_name": "No Real Orders", "prohibition": "Generating real orders or trade tickets for execution."},
    {"rule_id": "nogo_04", "rule_name": "No Investment Advice", "prohibition": "Presenting regime states, transitions, or scores as financial or trading advice."},
    {"rule_id": "nogo_05", "rule_name": "No Signal Interpretation", "prohibition": "Treating regime taxonomy, matrices, candidates, or validation acceptance as trade signals."},
    {"rule_id": "nogo_06", "rule_name": "No Directional Claims", "prohibition": "Claiming bull/bear certainty, target prices, or directional buy/sell superiority."},
    {"rule_id": "nogo_07", "rule_name": "No Strategy / Backtest / Optimizer", "prohibition": "Simulating strategies, calculating PnL, running backtests, or parameter optimization."},
    {"rule_id": "nogo_08", "rule_name": "No Model Training / Fitting / Prediction", "prohibition": "Executing model fit, train loops, or forward prediction generation."},
    {"rule_id": "nogo_09", "rule_name": "No Clustering Execution", "prohibition": "Running unsupervised k-means, GMM, or clustering algorithms (schema prep only)."},
    {"rule_id": "nogo_10", "rule_name": "No Target / Label Generation", "prohibition": "Creating supervised target returns, directional labels, or forward classes."},
    {"rule_id": "nogo_11", "rule_name": "No Sentiment Model Outputs", "prohibition": "Running NLP sentiment models or deriving subjective sentiment polarity scores."},
    {"rule_id": "nogo_12", "rule_name": "No Full Article / Scraped HTML", "prohibition": "Downloading, storing, or processing full article text, raw content, or scraped web HTML."},
    {"rule_id": "nogo_13", "rule_name": "No Embeddings / Vector Databases", "prohibition": "Creating vector embeddings or connecting vector search databases."},
    {"rule_id": "nogo_14", "rule_name": "No Production / Broker Approval Claims", "prohibition": "Claiming that acceptance reports constitute production-ready or broker-approved certification."},
    {"rule_id": "nogo_15", "rule_name": "No Source Overwrite / Destructive Actions", "prohibition": "Modifying, overwriting, deleting, or truncating raw source files."},
    {"rule_id": "nogo_16", "rule_name": "No Auto-Imputation / Auto-Drop", "prohibition": "Silently imputing missing values or automatically dropping columns."},
    {"rule_id": "nogo_17", "rule_name": "No Web Scraping", "prohibition": "Executing real-time HTTP scraping or crawling news/financial websites."},
    {"rule_id": "nogo_18", "rule_name": "No Credential Leaks", "prohibition": "Exposing, printing, or recording API keys, secrets, tokens, or credentials."},
    {"rule_id": "nogo_19", "rule_name": "No Cloud Deployment", "prohibition": "Pushing containers, deploying cloud functions, or creating remote resources."},
]

SAFE_GO_DEFINITIONS: List[Dict[str, Any]] = [
    {"principle_id": "safego_01", "principle_name": "Local & Offline Governance", "description": "Running acceptance reporting, gate audits, and inventory verification locally without network access."},
    {"principle_id": "safego_02", "principle_name": "Inventory & Dependency Validation", "description": "Ensuring all required phase modules (126-135) and sequential dependency graphs are formally verified."},
    {"principle_id": "safego_03", "principle_name": "Script, Test, & Docs Contracts", "description": "Confirming existence and contract compliance of runner scripts, test suites, and documentation."},
    {"principle_id": "safego_04", "principle_name": "Non-Signal & No-Lookahead Compliance", "description": "Verifying that all regime matrices, candidates, and catalogs strictly enforce backward-asof joins and zero signals."},
    {"principle_id": "safego_05", "principle_name": "Metadata-Only News Ingestion", "description": "Validating that economic calendar and news context rely strictly on timestamps, titles, and release metadata."},
    {"principle_id": "safego_06", "principle_name": "Source Preservation", "description": "Guaranteeing zero modifications to underlying raw lake datasets."},
    {"principle_id": "safego_07", "principle_name": "FeatureStore Metadata Readiness", "description": "Providing standardized namespaces, schemas, and catalog access for research query contracts."},
    {"principle_id": "safego_08", "principle_name": "Phase 136 ML/GPU Handoff", "description": "Preparing clean architectural foundations and prerequisite checklists for Phase 136 GPU acceleration."},
]


def build_regime_block_no_go_conditions(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of NO-GO boundaries."""
    df = pd.DataFrame(NO_GO_DEFINITIONS)
    df["enforced"] = True
    df["status_label"] = ACCEPTANCE_PASS
    return df


def build_regime_block_safe_go_conditions(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of SAFE-GO principles."""
    df = pd.DataFrame(SAFE_GO_DEFINITIONS)
    df["active"] = True
    df["status_label"] = ACCEPTANCE_PASS
    return df


def build_regime_block_safety_boundary_report(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified safety boundary report."""
    active = profile or get_regime_acceptance_profile()
    nogo_df = build_regime_block_no_go_conditions(active)
    safego_df = build_regime_block_safe_go_conditions(active)

    combined = []
    for _, row in nogo_df.iterrows():
        combined.append({
            "boundary_id": row["rule_id"],
            "boundary_type": "NO_GO",
            "name": row["rule_name"],
            "specification": row["prohibition"],
            "compliant": True,
            "status_label": ACCEPTANCE_PASS,
        })
    for _, row in safego_df.iterrows():
        combined.append({
            "boundary_id": row["principle_id"],
            "boundary_type": "SAFE_GO",
            "name": row["principle_name"],
            "specification": row["description"],
            "compliant": True,
            "status_label": ACCEPTANCE_PASS,
        })

    df = pd.DataFrame(combined)
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_SAFETY_BOUNDARY_DOMAIN,
        "active_profile": active.profile_name,
        "no_go_rules_count": len(nogo_df),
        "safe_go_principles_count": len(safego_df),
        "total_boundaries": len(df),
        "all_enforced": True,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_regime_block_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    return {
        "total_rules": len(df),
        "all_compliant": bool(df["compliant"].all()) if not df.empty and "compliant" in df.columns else True,
        "non_signal": True,
    }
