from typing import Tuple, Dict, Any, List
import pandas as pd
import re

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


ALLOWED_DOMAIN_PREFIXES = ["fx_", "commodity_", "macro_", "calendar_", "news_"]

FORBIDDEN_WORDS = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
]


def _slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_]+", "_", text.strip())
    return cleaned.strip("_").lower()


def build_namespaced_feature_name(
    domain: str,
    symbol: str,
    feature_name: str,
    window: str | None = None,
) -> str:
    domain_clean = _slugify(domain)
    # Ensure domain prefix matches format
    prefix = f"{domain_clean}_"
    if not any(prefix.startswith(allowed) for allowed in ALLOWED_DOMAIN_PREFIXES):
        # Default or fallback to standard prefix if known
        if "fx" in domain_clean:
            prefix = "fx_"
        elif "commodity" in domain_clean:
            prefix = "commodity_"
        elif "macro" in domain_clean:
            prefix = "macro_"
        elif "calendar" in domain_clean:
            prefix = "calendar_"
        elif "news" in domain_clean:
            prefix = "news_"
        else:
            prefix = f"{domain_clean}_"

    symbol_slug = _slugify(symbol)
    feat_slug = _slugify(feature_name)

    # Strip domain from feature_name if already present
    if feat_slug.startswith(prefix):
        feat_slug = feat_slug[len(prefix):]

    if window:
        window_slug = _slugify(str(window))
        return f"{prefix}{symbol_slug}_{feat_slug}_{window_slug}"

    return f"{prefix}{symbol_slug}_{feat_slug}"



def validate_namespaced_feature_name(name: str) -> Dict[str, Any]:
    issues = []
    lower_name = name.lower()

    # Check lowercase snake_case
    if not re.match(r"^[a-z0-9_]+$", name):
        issues.append("Feature adı yalnızca küçük harf, rakam ve alt tire içermelidir.")

    # Check domain prefix
    if not any(lower_name.startswith(p) for p in ALLOWED_DOMAIN_PREFIXES):
        issues.append(f"Feature adı zorunlu domain ön ekiyle başlamalıdır: {ALLOWED_DOMAIN_PREFIXES}")

    # Check forbidden words
    found_forbidden = [w for w in FORBIDDEN_WORDS if w in lower_name]
    if found_forbidden:
        issues.append(f"Feature adı yasaklı terim(ler) içeremez: {found_forbidden}")

    return {
        "feature_name": name,
        "is_valid": len(issues) == 0,
        "issues": issues,
        "forbidden_words_found": found_forbidden,
    }


DEFAULT_NAMESPACE_ENTRIES: List[Dict[str, Any]] = [
    {
        "domain": "fx",
        "symbol": "EUR/USD",
        "feature_name": "sma_w20",
        "namespaced_feature": "fx_eur_usd_sma_w20",
        "description": "EUR/USD 20 periyotluk basit hareketli ortalama.",
    },
    {
        "domain": "fx",
        "symbol": "EUR/USD",
        "feature_name": "rsi_w14",
        "namespaced_feature": "fx_eur_usd_rsi_w14",
        "description": "EUR/USD 14 periyotluk Göreceli Güç Endeksi.",
    },
    {
        "domain": "fx",
        "symbol": "USD/TRY",
        "feature_name": "atr_w14",
        "namespaced_feature": "fx_usd_try_atr_w14",
        "description": "USD/TRY 14 periyotluk Ortalama Gerçek Aralık.",
    },
    {
        "domain": "commodity",
        "symbol": "XAU/USD",
        "feature_name": "bb_width_w20_std2",
        "namespaced_feature": "commodity_xau_usd_bb_width_w20_std2",
        "description": "XAU/USD Bollinger Band genişliği.",
    },
    {
        "domain": "commodity",
        "symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "feature_name": "rolling_zscore_w20",
        "namespaced_feature": "commodity_wti_crude_continuous_placeholder_rolling_zscore_w20",
        "description": "WTI sürekli kontrat 20 periyotluk z-skoru.",
    },
    {
        "domain": "macro",
        "symbol": "US_10Y_YIELD",
        "feature_name": "yield_diff_1d",
        "namespaced_feature": "macro_us_10y_yield_yield_diff_1d",
        "description": "US 10Y faizi günlük fark göstergesi.",
    },
    {
        "domain": "calendar",
        "symbol": "FOMC_RATE_DECISION",
        "feature_name": "event_active_window",
        "namespaced_feature": "calendar_fomc_rate_decision_event_active_window",
        "description": "FOMC faiz kararı aktif pencere bayrağı.",
    },
    {
        "domain": "news",
        "symbol": "CRUDE_OIL",
        "feature_name": "news_mention_count_1d",
        "namespaced_feature": "news_crude_oil_news_mention_count_1d",
        "description": "Ham petrol haber başlığı günlük frekans sayımı (metadata-only).",
    },
]


def build_cross_domain_feature_namespace_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()

    rows = []
    for item in DEFAULT_NAMESPACE_ENTRIES:
        val_res = validate_namespaced_feature_name(item["namespaced_feature"])
        rows.append({
            "namespace_id": f"ns_{_slugify(item['namespaced_feature'])}",
            "domain": item["domain"],
            "symbol": item["symbol"],
            "raw_feature_name": item["feature_name"],
            "namespaced_feature": item["namespaced_feature"],
            "is_valid": val_res["is_valid"],
            "issues": val_res["issues"],
            "description": item["description"],
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    summary = summarize_cross_domain_feature_namespace(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_cross_domain_feature_namespace(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_namespaced_features": 0, "status": "EMPTY"}

    all_valid = bool(df["is_valid"].all()) if "is_valid" in df.columns else False
    return {
        "total_namespaced_features": len(df),
        "total_features": len(df),
        "all_valid": all_valid,
        "domains": list(df["domain"].unique()) if "domain" in df.columns else [],
        "non_signal": True,
        "status": "READY" if all_valid else "ISSUES_FOUND",
    }


build_feature_namespace_registry = build_cross_domain_feature_namespace_registry

