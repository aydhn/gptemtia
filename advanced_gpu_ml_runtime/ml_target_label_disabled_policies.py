"""Phase 136: ML Target/Label Disabled Policies.

Enforces strict prohibition of forward return targets, future shift labels,
and trade signal recommendations.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    TARGET_LABEL_DISABLED_DOMAIN,
    RUNTIME_BLOCKED_BY_SAFETY,
)


FORBIDDEN_TARGET_LABEL_KEYWORDS = [
    "target",
    "label",
    "future_return",
    "forward_return",
    "next_return",
    "shift(-1)",
    "shift(-",
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "recommendation",
    "position_size",
]


def validate_no_target_label_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect a request or column list and intercept any target/label generation attempts."""
    req_text = str(request).lower()
    violations: List[str] = []

    for kw in FORBIDDEN_TARGET_LABEL_KEYWORDS:
        if kw in req_text:
            violations.append(kw)

    blocked = len(violations) > 0
    return {
        "is_safe": not blocked,
        "blocked": blocked,
        "violations": violations,
        "reason": f"Target/label forbidden keyword(s) detected: {violations}" if blocked else "Compliant with target/label disabled policy.",
        "non_signal": True,
        "source_preserved": True,
    }


def build_ml_target_label_disabled_policy_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for target/label disabled policies."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = [
        {
            "policy_id": "policy_no_future_returns",
            "forbidden_concept": "future_return / forward_return",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Calculating future price changes or forward returns is prohibited.",
        },
        {
            "policy_id": "policy_no_negative_shift",
            "forbidden_concept": "shift(-1) / forward lookahead",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Negative shift on time-series leads to lookahead and is strictly blocked.",
        },
        {
            "policy_id": "policy_no_trade_labels",
            "forbidden_concept": "buy/sell/long/short labels",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Directional trade recommendations or labels are prohibited.",
        },
    ]

    for r in rows:
        r["non_signal"] = True
        r["source_preserved"] = True
        r["official_approval"] = False
        r["production_ready"] = False
        r["broker_ready"] = False

    df = pd.DataFrame(rows)
    summary = summarize_ml_target_label_disabled_policies(df)
    summary["domain"] = TARGET_LABEL_DISABLED_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_target_label_disabled_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize target/label disabled policies DataFrame."""
    all_enf = bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False
    return {
        "total_policies": len(df),
        "all_enforced": all_enf,
        "target_label_blocked": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
