# -*- coding: utf-8 -*-
"""Phase 150: Backtest Deployment Disabled Report.

Documents the complete disabling of production deployments and release pipelines in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_DEPLOYMENT,
)

DISABLED_DEPLOYMENT_OPS: List[Dict[str, Any]] = [
    {
        "operation_name": "deploy_to_production",
        "description": "Deploying strategies or backtest models to production environments.",
        "status": "DISABLED",
    },
    {
        "operation_name": "promote_to_live",
        "description": "Promoting experimental models to active execution servers.",
        "status": "DISABLED",
    },
    {
        "operation_name": "cloud_release",
        "description": "Triggering cloud infrastructure releases for autonomous trading.",
        "status": "DISABLED",
    },
]

FORBIDDEN_DEPLOYMENT_WORDS = [
    "deploy_production",
    "release_to_prod",
    "promote_to_live",
    "cloud_deploy",
    "docker_push_prod",
    "deploy_strategy",
    "live_deployment",
]


def validate_no_backtest_deployment_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero production deployment or promotion."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_DEPLOYMENT_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_DEPLOYMENT if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Production deployment is disabled: violating words {violating_words}. System is local offline research only."
            if blocked
            else "Complies with zero production deployment policy."
        ),
        "non_signal": True,
    }


def build_backtest_deployment_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for deployment disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_DEPLOYMENT_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "description": op["description"],
            "status": op["status"],
            "deployment_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "deployment_disabled",
        "total_disabled_operations": len(df),
        "all_deployment_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
