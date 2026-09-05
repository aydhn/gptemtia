
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityMetadata, build_commodity_metadata_id
from .commodity_universe import build_default_commodities

def build_default_commodity_metadata(profile: CommodityProviderProfile) -> list[CommodityMetadata]:
    items = []
    universe = build_default_commodities(profile)
    for c in universe:
        items.append(CommodityMetadata(
            commodity_id=build_commodity_metadata_id(c.canonical_symbol),
            canonical_symbol=c.canonical_symbol,
            commodity_name=c.commodity_name,
            category_label=c.category_label,
            unit_note=c.unit_note,
            contract_note="manual review gerektirebilir",
            liquidity_note="Placeholder liquidity note",
            data_availability_note="dry-run uyumlu",
            warnings=["Metadata yatırım tavsiyesi değildir."]
        ))
    return items

def build_commodity_metadata_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_metadata(df)

def summarize_commodity_metadata(df: pd.DataFrame) -> dict:
    return {"total_metadata": len(df)}
