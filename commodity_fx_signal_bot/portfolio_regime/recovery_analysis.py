import pandas as pd
from typing import Tuple, Optional
from core.logger import get_logger

logger = get_logger(__name__)

def calculate_recovery_time_from_drawdown(equity_curve: pd.Series, peak_timestamp: pd.Timestamp, trough_timestamp: pd.Timestamp) -> Optional[int]:
    """Calculates bars to recover to peak level after a trough."""
    if peak_timestamp not in equity_curve.index or trough_timestamp not in equity_curve.index:
        return None

    peak_val = equity_curve.loc[peak_timestamp]

    # Look forward from trough
    forward_curve = equity_curve.loc[trough_timestamp:]
    recovery_points = forward_curve[forward_curve >= peak_val]

    if len(recovery_points) > 0:
        return len(equity_curve.loc[trough_timestamp:recovery_points.index[0]])

    return None

def calculate_recovery_statistics(cluster_df: pd.DataFrame) -> dict:
    """Calculates aggregate recovery stats."""
    if cluster_df.empty or 'recovery_bars' not in cluster_df.columns:
        return {"status": "empty"}

    recovered = cluster_df.dropna(subset=['recovery_bars'])

    return {
        "status": "success",
        "avg_recovery_bars": recovered['recovery_bars'].mean() if not recovered.empty else None,
        "median_recovery_bars": recovered['recovery_bars'].median() if not recovered.empty else None,
        "max_recovery_bars": recovered['recovery_bars'].max() if not recovered.empty else None,
        "unrecovered_cluster_count": len(cluster_df) - len(recovered),
        "recovery_quality_label": "good" if len(recovered) > len(cluster_df)/2 else "poor"
    }

def build_recovery_time_table(cluster_df: pd.DataFrame) -> pd.DataFrame:
    """Extracts recovery table from cluster dataframe."""
    if cluster_df.empty:
        return pd.DataFrame()

    cols = ['cluster_id', 'basket_id', 'depth_pct', 'duration_bars', 'recovery_bars']
    available_cols = [c for c in cols if c in cluster_df.columns]

    return cluster_df[available_cols].copy()

def build_recovery_analysis_report(cluster_df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
    """Builds full recovery analysis report."""
    logger.info("Building recovery analysis report")

    df = build_recovery_time_table(cluster_df)
    summary = calculate_recovery_statistics(cluster_df)

    return df, summary
