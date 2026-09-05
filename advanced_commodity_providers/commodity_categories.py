
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityCategory, build_commodity_category_id
from .commodity_provider_labels import list_commodity_category_labels

def build_default_commodity_categories(profile: CommodityProviderProfile) -> list[CommodityCategory]:
    return [
        CommodityCategory(
            category_id=build_commodity_category_id(label),
            category_label=label,
            category_name=label.replace('_', ' ').title(),
            description=f"Category for {label}",
            example_symbols=[],
            warnings=[]
        ) for label in list_commodity_category_labels() if label != "commodity_unknown_category"
    ]

def build_commodity_category_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_categories(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_categories(df)

def summarize_commodity_categories(df: pd.DataFrame) -> dict:
    return {"total_categories": len(df)}
