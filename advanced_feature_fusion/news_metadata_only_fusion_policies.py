from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)
from advanced_feature_fusion.fusion_feature_models import (
    FusionPolicy,
    build_fusion_policy_id,
)

FORBIDDEN_NEWS_COLUMNS = [
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "copyrighted_article_copy",
    "embedding",
    "vector",
    "raw_article",
    "scraped_text",
]


NEWS_METADATA_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "strict_metadata_only_news_boundary_policy",
        "policy_type": "news_metadata_only",
        "description": "Haber tarafında yalnızca etiket, konu, zaman damgası ve olay referansı kullanılır; tam metin kullanımı kesinlikle engellenir.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "forbidden_article_body_columns_policy",
        "policy_type": "news_metadata_only",
        "description": "Herhangi bir tabloda full_text, article_body, scraped_html veya embedding kolonu tespit edilirse pipeline durdurulur.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "zero_scraping_compliance_policy",
        "policy_type": "news_metadata_only",
        "description": "Web scraping, tarayıcı otomasyonu, paywall atlatma veya telifli içerik indirme kesin olarak yasaktır.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
]


def build_news_metadata_only_fusion_policy_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in NEWS_METADATA_POLICIES:
        p = FusionPolicy(
            policy_id=build_fusion_policy_id(spec["policy_name"], spec["policy_type"]),
            policy_name=spec["policy_name"],
            policy_type=spec["policy_type"],
            description=spec["description"],
            future_data_allowed=spec["future_data_allowed"],
            full_text_allowed=spec["full_text_allowed"],
            destructive_action_allowed=spec["destructive_action_allowed"],
            non_signal=spec["non_signal"],
            manual_review_required=spec["manual_review_required"],
        )
        rows.append(p.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_news_metadata_only_fusion_policies(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def validate_news_metadata_only_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    found_forbidden = []
    for col in df.columns:
        col_lower = str(col).lower()
        for forbidden in FORBIDDEN_NEWS_COLUMNS:
            if forbidden in col_lower:
                found_forbidden.append(col)

    passed = len(found_forbidden) == 0
    return {
        "valid": passed,
        "forbidden_columns_found": found_forbidden,
        "status": "PASS" if passed else "FAIL",
        "message": "Metadata-only news boundary verified." if passed else f"Yasaklı haber metin kolonları tespit edildi: {found_forbidden}",
    }


def summarize_news_metadata_only_fusion_policies(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_policies": 0, "status": "EMPTY"}
    return {
        "total_policies": len(df),
        "zero_full_text_enforced": bool((~df["full_text_allowed"]).all()),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }


def get_news_metadata_only_policies() -> List[Dict[str, Any]]:
    """Return list of news metadata only policies."""
    return [dict(p) for p in NEWS_METADATA_POLICIES]


def get_news_metadata_only_policies_summary() -> Dict[str, Any]:
    """Return summary dictionary of news metadata only policies."""
    df, summary = build_news_metadata_only_fusion_policy_registry()
    summary["policy_count"] = len(df)
    summary["full_article_prohibited"] = True
    summary["scraping_prohibited"] = True
    return summary
