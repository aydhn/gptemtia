# -*- coding: utf-8 -*-
"""Phase 147: Validation Live Trading Disabled Report.

Documents and strictly enforces the disabled state of live trading execution.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_live_trading_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled live trading."""
    rows = [
        {
            "execution_target": "live_order_engine",
            "is_blocked": True,
            "reason": "Canli emir iletimi, borsa/piyasa baglantisi ve canli pozisyon acma kesinlikle yasaktir.",
            "enforced": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_blocked_live_trading": len(df),
        "all_blocked": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_validation_live_trading_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that request does not attempt live trading."""
    req_str = request if isinstance(request, str) else str(request.get("command", ""))
    req_lower = req_str.lower()
    blocked_keywords = ["live_trade", "send_order", "real_order", "buy_order", "sell_order"]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "message": "Canli emir istegi kesinlikle engellendi." if is_blocked else "Talep guvenli.",
        "non_signal": True,
    }
