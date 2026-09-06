"""Phase 132: Macro Regime Entity Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_MACRO_ENTITIES = [
    {
        "entity_id": "macro_us_cpi_yoy",
        "entity_name": "US Consumer Price Index YoY",
        "entity_type": "inflation_indicator",
        "country_code": "US",
        "currency_code": "USD",
        "source_provider": "BLS",
        "release_frequency": "monthly",
        "nominal_lag_days": 14,
        "revision_tracked": True,
    },
    {
        "entity_id": "macro_us_fed_funds_rate",
        "entity_name": "US Federal Funds Target Rate",
        "entity_type": "rate_indicator",
        "country_code": "US",
        "currency_code": "USD",
        "source_provider": "Federal Reserve",
        "release_frequency": "fomc_cycle",
        "nominal_lag_days": 0,
        "revision_tracked": False,
    },
    {
        "entity_id": "macro_us_real_gdp_qoq",
        "entity_name": "US Real GDP QoQ Annualized",
        "entity_type": "growth_indicator",
        "country_code": "US",
        "currency_code": "USD",
        "source_provider": "BEA",
        "release_frequency": "quarterly",
        "nominal_lag_days": 30,
        "revision_tracked": True,
    },
    {
        "entity_id": "macro_us_nfp",
        "entity_name": "US Non-Farm Payrolls",
        "entity_type": "employment_indicator",
        "country_code": "US",
        "currency_code": "USD",
        "source_provider": "BLS",
        "release_frequency": "monthly",
        "nominal_lag_days": 7,
        "revision_tracked": True,
    },
    {
        "entity_id": "macro_eu_hicp_yoy",
        "entity_name": "Eurozone HICP Inflation YoY",
        "entity_type": "fx_sensitive_macro_indicator",
        "country_code": "EU",
        "currency_code": "EUR",
        "source_provider": "Eurostat",
        "release_frequency": "monthly",
        "nominal_lag_days": 16,
        "revision_tracked": True,
    },
    {
        "entity_id": "macro_cn_manufacturing_pmi",
        "entity_name": "China Official Manufacturing PMI",
        "entity_type": "commodity_sensitive_macro_indicator",
        "country_code": "CN",
        "currency_code": "CNY",
        "source_provider": "NBS",
        "release_frequency": "monthly",
        "nominal_lag_days": 1,
        "revision_tracked": False,
    },
    {
        "entity_id": "macro_us_dxy_regime_ref",
        "entity_name": "US Dollar Index Broad Reference",
        "entity_type": "macro_indicator",
        "country_code": "US",
        "currency_code": "USD",
        "source_provider": "Federal Reserve",
        "release_frequency": "daily",
        "nominal_lag_days": 1,
        "revision_tracked": False,
    },
    {
        "entity_id": "macro_release_schedule_bundle",
        "entity_name": "Macro Release Schedule Synchronization Bundle",
        "entity_type": "macro_release",
        "country_code": "GLOBAL",
        "currency_code": "MULTI",
        "source_provider": "Official Calendar",
        "release_frequency": "continuous",
        "nominal_lag_days": 0,
        "revision_tracked": True,
    },
    {
        "entity_id": "macro_revision_ledger_bundle",
        "entity_name": "Macro Indicator Historical Revision Ledger",
        "entity_type": "macro_revision",
        "country_code": "GLOBAL",
        "currency_code": "MULTI",
        "source_provider": "Official Sources",
        "release_frequency": "event_driven",
        "nominal_lag_days": 30,
        "revision_tracked": True,
    },
    {
        "entity_id": "macro_surprise_contract_placeholder",
        "entity_name": "Macro Consensus vs Actual Delta Placeholder",
        "entity_type": "macro_surprise_placeholder",
        "country_code": "GLOBAL",
        "currency_code": "MULTI",
        "source_provider": "Consensus Engine",
        "release_frequency": "event_driven",
        "nominal_lag_days": 0,
        "revision_tracked": False,
    },
]


def build_macro_regime_entity_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of macro regime entities."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_MACRO_ENTITIES:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_macro_entities": len(df),
        "entity_types": df["entity_type"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_regime_entities(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for macro regime entities."""
    return {
        "total_macro_entities": len(df),
        "entity_types": df["entity_type"].nunique() if "entity_type" in df.columns else 0,
        "countries": df["country_code"].nunique() if "country_code" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
