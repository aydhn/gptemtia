from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile

DEPENDENCY_EDGES: List[Dict[str, Any]] = [
    {"source_node": "close", "target_node": "close_return_1", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "close", "target_node": "log_return_1", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "close", "target_node": "sma_20", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "close", "target_node": "ema_20", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "close", "target_node": "rsi_14", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "high", "target_node": "atr_14", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "low", "target_node": "atr_14", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "close", "target_node": "bollinger_zscore_20", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "bid", "target_node": "quote_spread", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "ask", "target_node": "quote_spread", "relation_type": "computed_from", "layer": "raw_to_feature"},
    {"source_node": "sma_20", "target_node": "trend_factor_placeholder", "relation_type": "aggregated_into", "layer": "feature_to_factor"},
    {"source_node": "ema_20", "target_node": "trend_factor_placeholder", "relation_type": "aggregated_into", "layer": "feature_to_factor"},
    {"source_node": "rsi_14", "target_node": "momentum_factor_placeholder", "relation_type": "aggregated_into", "layer": "feature_to_factor"},
    {"source_node": "atr_14", "target_node": "volatility_factor_placeholder", "relation_type": "aggregated_into", "layer": "feature_to_factor"},
    {"source_node": "bollinger_zscore_20", "target_node": "mean_reversion_factor_placeholder", "relation_type": "aggregated_into", "layer": "feature_to_factor"},
]


def build_feature_dependency_graph_placeholder(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for edge in DEPENDENCY_EDGES:
        records.append({
            "edge_id": f"dep_{edge['source_node']}_to_{edge['target_node']}",
            "source_node": edge["source_node"],
            "target_node": edge["target_node"],
            "relation_type": edge["relation_type"],
            "layer": edge["layer"],
            "graph_engine": "in_memory_tabular_placeholder",
            "non_signal": True,
        })

    df = pd.DataFrame.from_records(records)
    summary = summarize_feature_dependency_graph(df)
    return df, summary


def summarize_feature_dependency_graph(df: pd.DataFrame) -> Dict[str, Any]:
    sources = df["source_node"].unique().tolist() if not df.empty and "source_node" in df.columns else []
    targets = df["target_node"].unique().tolist() if not df.empty and "target_node" in df.columns else []
    return {
        "total_edges": len(df),
        "total_source_nodes": len(sources),
        "total_target_nodes": len(targets),
        "graph_type": "tabular_dag_placeholder",
        "external_database_required": False,
        "all_non_signal": True,
        "non_signal": True,
    }
