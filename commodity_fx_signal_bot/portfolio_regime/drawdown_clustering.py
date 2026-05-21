import pandas as pd
from typing import List, Dict, Tuple
from portfolio_regime.regime_config import PortfolioRegimeProfile
from portfolio_regime.regime_models import DrawdownCluster, build_drawdown_cluster_id
from core.logger import get_logger

logger = get_logger(__name__)

def calculate_drawdown_series(equity_curve: pd.Series) -> pd.Series:
    """Calculates drawdown from peak."""
    rolling_max = equity_curve.cummax()
    return (equity_curve - rolling_max) / rolling_max

def identify_drawdown_clusters(drawdown_series: pd.Series, basket_id: str, profile: PortfolioRegimeProfile) -> List[DrawdownCluster]:
    """Identifies clusters of drawdowns below threshold."""
    clusters = []

    # Placeholder logic
    if len(drawdown_series) > 0:
        clusters.append(DrawdownCluster(
            cluster_id=build_drawdown_cluster_id(basket_id, str(drawdown_series.index[0]), str(drawdown_series.index[-1])),
            basket_id=basket_id,
            start_timestamp=str(drawdown_series.index[0]),
            end_timestamp=str(drawdown_series.index[-1]),
            depth_pct=drawdown_series.min(),
            duration_bars=len(drawdown_series),
            recovery_bars=None,
            cluster_label=classify_drawdown_cluster(drawdown_series.min(), len(drawdown_series), None),
            warnings=[]
        ))

    return clusters

def classify_drawdown_cluster(depth_pct: float, duration_bars: int, recovery_bars: int | None) -> str:
    """Classifies a drawdown cluster."""
    if recovery_bars is not None:
        return "recovery_cluster"
    if depth_pct < -0.15:
        return "deep_drawdown_cluster"
    if duration_bars > 60:
        return "prolonged_drawdown_cluster"
    if depth_pct < -0.05:
        return "moderate_drawdown_cluster"
    return "shallow_drawdown_cluster"

def drawdown_clusters_to_dataframe(clusters: List[DrawdownCluster]) -> pd.DataFrame:
    """Converts clusters to dataframe."""
    from portfolio_regime.regime_models import drawdown_cluster_to_dict
    return pd.DataFrame([drawdown_cluster_to_dict(c) for c in clusters])

def build_drawdown_cluster_report(equity_curves: Dict[str, pd.DataFrame], profile: PortfolioRegimeProfile) -> Tuple[pd.DataFrame, dict]:
    """Builds drawdown cluster report."""
    logger.info("Building drawdown cluster report")

    all_clusters = []
    for basket_id, curve_df in equity_curves.items():
        if 'equity' in curve_df.columns:
            dd = calculate_drawdown_series(curve_df['equity'])
            clusters = identify_drawdown_clusters(dd, basket_id, profile)
            all_clusters.extend(clusters)

    df = drawdown_clusters_to_dataframe(all_clusters)

    summary = {
        "status": "success",
        "total_clusters": len(all_clusters),
        "baskets_analyzed": len(equity_curves)
    }

    return df, summary
