import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def build_default_news_region_currency_mappings(profile: NewsProviderProfile) -> pd.DataFrame:
    records = [
        {"mapping_id": "reg_us_usd", "region": "US", "currency": "USD", "description": "United States to US Dollar", "manual_review_required": False},
        {"mapping_id": "reg_eu_eur", "region": "EU", "currency": "EUR", "description": "Eurozone to Euro", "manual_review_required": False},
        {"mapping_id": "reg_uk_gbp", "region": "UK", "currency": "GBP", "description": "United Kingdom to British Pound", "manual_review_required": False},
        {"mapping_id": "reg_jp_jpy", "region": "JP", "currency": "JPY", "description": "Japan to Japanese Yen", "manual_review_required": False},
        {"mapping_id": "reg_tr_try", "region": "TR", "currency": "TRY", "description": "Turkey to Turkish Lira", "manual_review_required": False},
        {"mapping_id": "reg_cn_cnh", "region": "CN", "currency": "CNH/CNY", "description": "China to Chinese Yuan", "manual_review_required": False},
        {"mapping_id": "reg_ca_cad", "region": "CA", "currency": "CAD", "description": "Canada to Canadian Dollar", "manual_review_required": False},
        {"mapping_id": "reg_au_aud", "region": "AU", "currency": "AUD", "description": "Australia to Australian Dollar", "manual_review_required": False},
        {"mapping_id": "reg_nz_nzd", "region": "NZ", "currency": "NZD", "description": "New Zealand to New Zealand Dollar", "manual_review_required": False},
        {"mapping_id": "reg_ch_chf", "region": "CH", "currency": "CHF", "description": "Switzerland to Swiss Franc", "manual_review_required": False}
    ]
    return pd.DataFrame(records)

def build_news_region_currency_mapping_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_news_region_currency_mappings(profile)
    summary = summarize_news_region_currency_mapping(df)
    return df, summary

def summarize_news_region_currency_mapping(df: pd.DataFrame) -> Dict:
    return {
        "total_mappings": len(df),
        "regions": df["region"].tolist() if not df.empty else [],
        "currencies": df["currency"].tolist() if not df.empty else []
    }
