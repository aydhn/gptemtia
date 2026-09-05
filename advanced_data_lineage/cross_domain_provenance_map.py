from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


CROSS_DOMAIN_MAP_ITEMS = [
    {
        "map_id": "cd_map_001",
        "domain_pair": "fx_to_news",
        "primary_entity": "EURUSD",
        "normalized_entity": "EUR/USD",
        "cross_domain_link": "FX_TAG:EUR_USD",
        "link_type": "entity_tag_linkage",
        "source_preserved": True,
        "notes": "FX pair mapped to news asset tag",
    },
    {
        "map_id": "cd_map_002",
        "domain_pair": "commodity_to_news",
        "primary_entity": "GOLD",
        "normalized_entity": "XAU/USD",
        "cross_domain_link": "COMMODITY_TAG:GOLD_SPOT",
        "link_type": "entity_tag_linkage",
        "source_preserved": True,
        "notes": "Commodity symbol mapped to news commodity tag",
    },
    {
        "map_id": "cd_map_003",
        "domain_pair": "macro_to_calendar",
        "primary_entity": "US_10Y_YIELD",
        "normalized_entity": "US10Y",
        "cross_domain_link": "CALENDAR_EVENT:US_TREASURY_AUCTION_10Y",
        "link_type": "macro_event_linkage",
        "source_preserved": True,
        "notes": "Macro timeseries linked to economic calendar auction event",
    },
    {
        "map_id": "cd_map_004",
        "domain_pair": "calendar_to_macro",
        "primary_entity": "US_NONFARM_PAYROLLS_RELEASE",
        "normalized_entity": "NFP",
        "cross_domain_link": "MACRO_SERIES:US_LABOR_NFP",
        "link_type": "release_to_series_linkage",
        "source_preserved": True,
        "notes": "Economic calendar actual release linked to macro series revision",
    },
    {
        "map_id": "cd_map_005",
        "domain_pair": "quality_to_lineage",
        "primary_entity": "provider_quality_score",
        "normalized_entity": "0.95",
        "cross_domain_link": "provider_traceability_score:0.95",
        "link_type": "diagnostic_correlation",
        "source_preserved": True,
        "notes": "Quality score and traceability score correlated for Phase 115 benchmark",
    },
    {
        "map_id": "cd_map_006",
        "domain_pair": "license_to_usage",
        "primary_entity": "license_provenance_note",
        "normalized_entity": "research_only",
        "cross_domain_link": "USAGE_BOUNDARY:NO_TRADING_SIGNAL",
        "link_type": "compliance_boundary",
        "source_preserved": True,
        "notes": "License constraints enforce no-trading-signal safety boundary",
    },
]


def build_cross_domain_provenance_map(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(CROSS_DOMAIN_MAP_ITEMS)
    summary = summarize_cross_domain_provenance_map(df)
    return df, summary


def summarize_cross_domain_provenance_map(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_cross_domain_mappings": len(df),
        "domain_pairs": df["domain_pair"].tolist() if "domain_pair" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
