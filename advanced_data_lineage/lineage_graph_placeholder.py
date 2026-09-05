from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


GRAPH_EDGES = [
    ("prov_src_fx_fixture_provider_fx_dry_run_fixture_source", "prov_rec_advanced_fx_providers_engine", "provided_by"),
    ("prov_rec_advanced_fx_providers_engine", "ds_prov_advanced_fx_providers_engine_fx_quote_contract_dataset", "produces_dataset"),
    ("ds_prov_advanced_fx_providers_engine_fx_quote_contract_dataset", "schema_prov_dataset_fx_quote_v1_0", "conforms_to_schema"),
    ("ds_prov_advanced_fx_providers_engine_fx_quote_contract_dataset", "trans_prov_dataset_fx_quote_pair_to_normalized_pair", "transformed_by"),
    ("trans_prov_dataset_fx_quote_pair_to_normalized_pair", "out_lin_fx_quote", "yields_normalized_output"),
    ("prov_src_commodity_fixture_provider_commodity_dry_run_fixture_source", "prov_rec_advanced_commodity_providers_engine", "provided_by"),
    ("prov_rec_advanced_commodity_providers_engine", "ds_prov_advanced_commodity_providers_engine_commodity_spot_contract_dataset", "produces_dataset"),
    ("ds_prov_advanced_commodity_providers_engine_commodity_spot_contract_dataset", "schema_prov_dataset_commodity_spot_v1_0", "conforms_to_schema"),
    ("ds_prov_advanced_commodity_providers_engine_commodity_spot_contract_dataset", "trans_prov_dataset_commodity_spot_symbol_to_normalized_symbol", "transformed_by"),
    ("trans_prov_dataset_commodity_spot_symbol_to_normalized_symbol", "out_lin_commodity_spot", "yields_normalized_output"),
    ("prov_src_news_fixture_provider_news_metadata_dry_run_fixture_source", "prov_rec_advanced_news_metadata_engine", "provided_by"),
    ("prov_rec_advanced_news_metadata_engine", "ds_prov_advanced_news_metadata_engine_news_metadata_contract_dataset", "produces_dataset"),
    ("ds_prov_advanced_news_metadata_engine_news_metadata_contract_dataset", "schema_prov_dataset_news_metadata_v1_0", "conforms_to_schema"),
    ("ds_prov_advanced_news_metadata_engine_news_metadata_contract_dataset", "trans_prov_dataset_news_metadata_tags_to_normalized_tags", "transformed_by"),
    ("trans_prov_dataset_news_metadata_tags_to_normalized_tags", "out_lin_news_metadata", "yields_normalized_output"),
]


def build_lineage_graph_placeholder(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for src, dst, rel in GRAPH_EDGES:
        records.append({
            "source_node": src,
            "target_node": dst,
            "relationship_type": rel,
            "graph_type": "in_memory_placeholder",
            "is_vector_db": False,
            "is_graph_db": False,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_lineage_graph_placeholder(df)
    return df, summary


def summarize_lineage_graph_placeholder(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_edges": len(df),
        "unique_source_nodes": df["source_node"].nunique() if "source_node" in df.columns else 0,
        "unique_target_nodes": df["target_node"].nunique() if "target_node" in df.columns else 0,
        "relationships": df["relationship_type"].unique().tolist() if "relationship_type" in df.columns else [],
        "is_vector_db": False,
        "is_graph_db": False,
        "current_phase": 114,
        "target_final_phase": 160,
    }
