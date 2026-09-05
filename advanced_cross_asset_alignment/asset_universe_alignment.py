from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    AssetUniverseAlignment,
    build_asset_universe_alignment_id,
)


DEFAULT_UNIVERSES: List[Dict[str, Any]] = [
    {
        "asset_domain": "fx",
        "canonical_symbol": "EUR/USD",
        "related_symbols": ["DXY_PLACEHOLDER", "USD/CHF"],
        "related_macro_indicators": ["FED_POLICY_RATE", "ECB_POLICY_RATE", "US_10Y_YIELD"],
        "related_calendar_events": ["FOMC_RATE_DECISION", "ECB_RATE_DECISION", "US_CPI_RELEASE", "US_NONFARM_PAYROLLS_RELEASE"],
        "related_news_tags": ["CENTRAL_BANK", "INFLATION", "RISK_SENTIMENT"],
        "alignment_note": "Euro ve ABD Doları çifti; ECB/FED faiz kararları ve enflasyon verileriyle hizalanır.",
        "manual_review_required": False,
    },
    {
        "asset_domain": "fx",
        "canonical_symbol": "USD/TRY",
        "related_symbols": ["DXY_PLACEHOLDER", "EUR/TRY"],
        "related_macro_indicators": ["CBRT_POLICY_RATE", "TR_CPI_PLACEHOLDER", "FED_POLICY_RATE"],
        "related_calendar_events": ["CBRT_RATE_DECISION", "TR_CPI_RELEASE", "FOMC_RATE_DECISION"],
        "related_news_tags": ["CENTRAL_BANK", "INFLATION", "TURKEY_ECONOMY"],
        "alignment_note": "USD/TRY kuru; TCMB faiz kararları ve yurt içi enflasyon verileriyle hizalanır.",
        "manual_review_required": False,
    },
    {
        "asset_domain": "commodity",
        "canonical_symbol": "XAU/USD",
        "related_symbols": ["US_10Y_YIELD", "DXY_PLACEHOLDER", "XAG/USD"],
        "related_macro_indicators": ["US_10Y_YIELD", "FED_POLICY_RATE", "GLOBAL_RISK_SENTIMENT"],
        "related_calendar_events": ["FOMC_RATE_DECISION", "US_CPI_RELEASE", "US_NONFARM_PAYROLLS_RELEASE"],
        "related_news_tags": ["PRECIOUS_METALS", "GOLD", "INFLATION", "RISK_SENTIMENT"],
        "alignment_note": "Spot altın; ABD 10 yıllık tahvil faizi, DXY ve küresel risk iştahı göstergeleriyle hizalanır.",
        "manual_review_required": False,
    },
    {
        "asset_domain": "commodity",
        "canonical_symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "related_symbols": ["BRENT_CRUDE_CONTINUOUS_PLACEHOLDER", "DXY_PLACEHOLDER"],
        "related_macro_indicators": ["US_CPI_RELEASE", "GLOBAL_GROWTH_SENTIMENT"],
        "related_calendar_events": ["EIA_CRUDE_INVENTORY_RELEASE", "OPEC_MEETING_PLACEHOLDER"],
        "related_news_tags": ["ENERGY", "CRUDE_OIL", "GEOPOLITICS"],
        "alignment_note": "WTI ham petrol; haftalık EIA ham petrol stok verileri ve enerji haber metadata etiketleriyle hizalanır.",
        "manual_review_required": False,
    },
    {
        "asset_domain": "commodity",
        "canonical_symbol": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
        "related_symbols": ["WTI_CRUDE_CONTINUOUS_PLACEHOLDER"],
        "related_macro_indicators": ["US_CPI_RELEASE"],
        "related_calendar_events": ["EIA_NATURAL_GAS_STORAGE_RELEASE"],
        "related_news_tags": ["ENERGY", "NATURAL_GAS", "WEATHER_SENTIMENT"],
        "alignment_note": "Doğal gaz sürekli sözleşmesi; EIA yer altı depolama verileri ve mevsimsel hava durumu temalarıyla hizalanır.",
        "manual_review_required": False,
    },
]


def build_asset_universe_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()

    rows = []
    for item_data in DEFAULT_UNIVERSES:
        item = AssetUniverseAlignment(
            universe_id=build_asset_universe_alignment_id(item_data["asset_domain"], item_data["canonical_symbol"]),
            asset_domain=item_data["asset_domain"],
            canonical_symbol=item_data["canonical_symbol"],
            related_symbols=item_data["related_symbols"],
            related_macro_indicators=item_data["related_macro_indicators"],
            related_calendar_events=item_data["related_calendar_events"],
            related_news_tags=item_data["related_news_tags"],
            alignment_note=item_data["alignment_note"],
            manual_review_required=item_data["manual_review_required"],
        )
        rows.append(item.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_asset_universe_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_asset_universe_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_universes": 0, "status": "EMPTY"}

    return {
        "total_universes": len(df),
        "total_asset_domains": int(df["asset_domain"].nunique()) if "asset_domain" in df.columns else 0,
        "canonical_symbols": list(df["canonical_symbol"]) if "canonical_symbol" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "non_signal": True,
        "status": "READY",
    }


build_asset_universe_registry = build_asset_universe_alignment_registry

