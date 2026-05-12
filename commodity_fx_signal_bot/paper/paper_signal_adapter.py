import pandas as pd
from paper.paper_config import PaperTradingProfile
from paper.paper_models import VirtualOrder, build_virtual_order_id

def filter_paper_eligible_level_candidates(level_df: pd.DataFrame, profile: PaperTradingProfile) -> pd.DataFrame:
    if level_df.empty:
        return level_df

    if profile.allow_watchlist_candidates:
        mask = level_df['level_label'].isin(['level_approved_candidate', 'watchlist_candidate'])
    else:
        if profile.require_level_approved_candidate:
            mask = level_df['level_label'] == 'level_approved_candidate'
        else:
            mask = pd.Series(True, index=level_df.index)

    df = level_df[mask].copy()
    if 'directional_bias' in df.columns:
        if profile.allow_short_bias_simulation:
            bias_mask = df['directional_bias'].isin(['long_bias', 'short_bias'])
        else:
            bias_mask = df['directional_bias'] == 'long_bias'
        df = df[bias_mask]

    return df

def merge_level_sizing_risk_candidates(level_df: pd.DataFrame, sizing_df: pd.DataFrame | None, risk_df: pd.DataFrame | None) -> tuple[pd.DataFrame, dict]:
    if level_df.empty:
        return pd.DataFrame(), {}

    df = level_df.copy()
    warnings = {}

    if sizing_df is not None and not sizing_df.empty:
        df = df.join(sizing_df, rsuffix="_sizing")
    else:
        warnings["sizing_missing"] = "Sizing frame is missing, using fallbacks."

    if risk_df is not None and not risk_df.empty:
        df = df.join(risk_df, rsuffix="_risk")
    else:
        warnings["risk_missing"] = "Risk frame is missing, using fallbacks."

    return df, warnings

def infer_virtual_order_side(row: pd.Series) -> str:
    bias = row.get("directional_bias", "")
    if bias == "long_bias":
        return "virtual_long_bias"
    elif bias == "short_bias":
        return "virtual_short_bias"
    elif bias == "neutral_bias":
        return "virtual_neutral"
    return "virtual_unknown_side"

def build_virtual_order_from_candidate(row: pd.Series, profile: PaperTradingProfile) -> VirtualOrder:
    symbol = row.get("symbol", "UNKNOWN")
    timeframe = row.get("timeframe", "1d")
    timestamp = str(row.name) if isinstance(row.name, pd.Timestamp) else str(row.get("timestamp", ""))

    source_level_id = row.get("level_candidate_id", "unknown_level")
    order_id = build_virtual_order_id(symbol, timeframe, timestamp, source_level_id)

    adj_units = float(row.get("adjusted_theoretical_units", 0.0))
    if pd.isna(adj_units) or adj_units <= 0:
        adj_units = 1.0 # fallback for sim

    order = VirtualOrder(
        order_id=order_id,
        symbol=symbol,
        timeframe=timeframe,
        created_timestamp=timestamp,
        expiry_timestamp=None,
        source_level_id=source_level_id,
        source_sizing_id=row.get("sizing_candidate_id", "unknown_sizing"),
        source_risk_id=row.get("risk_candidate_id", "unknown_risk"),
        strategy_family=row.get("strategy_family", "unknown_family"),
        order_side=infer_virtual_order_side(row),
        order_status="virtual_pending",
        requested_price=float(row.get("requested_price", row.get("close", 0.0))),
        theoretical_units=float(row.get("theoretical_units", adj_units)),
        adjusted_theoretical_units=adj_units,
        theoretical_notional=float(row.get("theoretical_notional", 0.0)) if "theoretical_notional" in row else None,
        stop_level=float(row.get("stop_level", 0.0)) if "stop_level" in row else None,
        target_level=float(row.get("target_level", 0.0)) if "target_level" in row else None,
        risk_label=row.get("risk_label", "unknown_risk_label"),
        sizing_label=row.get("sizing_label", "unknown_sizing_label"),
        level_label=row.get("level_label", "unknown_level_label"),
        rejection_reasons=[],
        warnings=[],
        notes="Generated via paper simulation adapter."
    )
    return order

def build_virtual_order_candidates(level_df: pd.DataFrame, sizing_df: pd.DataFrame | None, risk_df: pd.DataFrame | None, profile: PaperTradingProfile) -> tuple[list[VirtualOrder], dict]:
    eligible_df = filter_paper_eligible_level_candidates(level_df, profile)
    merged_df, warnings = merge_level_sizing_risk_candidates(eligible_df, sizing_df, risk_df)

    orders = []
    if merged_df.empty:
        return orders, warnings

    for idx, row in merged_df.iterrows():
        # Check risk and sizing requirements if needed
        if profile.require_risk_approval_candidate and row.get("risk_label") != "risk_approval_candidate":
            if not profile.allow_watchlist_candidates:
                continue
        if profile.require_sizing_approved_candidate and row.get("sizing_label") != "sizing_approved_candidate":
            if not profile.allow_watchlist_candidates:
                continue

        order = build_virtual_order_from_candidate(row, profile)
        orders.append(order)

    return orders, warnings
