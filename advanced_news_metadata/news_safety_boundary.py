import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def build_news_no_go_conditions(profile: NewsProviderProfile) -> pd.DataFrame:
    no_go = [
        {"boundary_id": "nogo_live_trading", "category": "execution", "rule": "live trading", "enforced": True},
        {"boundary_id": "nogo_broker_integration", "category": "execution", "rule": "broker integration", "enforced": True},
        {"boundary_id": "nogo_real_order", "category": "execution", "rule": "real order", "enforced": True},
        {"boundary_id": "nogo_buy_sell_instruction", "category": "advice", "rule": "exact buy/sell instruction", "enforced": True},
        {"boundary_id": "nogo_investment_advice", "category": "advice", "rule": "investment advice", "enforced": True},
        {"boundary_id": "nogo_directional_claim", "category": "signal", "rule": "news directional certainty claim", "enforced": True},
        {"boundary_id": "nogo_sentiment_signal", "category": "signal", "rule": "sentiment-as-signal", "enforced": True},
        {"boundary_id": "nogo_full_article_download", "category": "copyright", "rule": "full article download", "enforced": True},
        {"boundary_id": "nogo_copyright_copy", "category": "copyright", "rule": "copyrighted article copy", "enforced": True},
        {"boundary_id": "nogo_model_deployment", "category": "deployment", "rule": "model deployment", "enforced": True},
        {"boundary_id": "nogo_nlp_deployment", "category": "deployment", "rule": "NLP model deployment", "enforced": True},
        {"boundary_id": "nogo_production_deployment", "category": "deployment", "rule": "production deployment", "enforced": True},
        {"boundary_id": "nogo_web_server_dashboard", "category": "runtime", "rule": "web server/dashboard", "enforced": True},
        {"boundary_id": "nogo_external_llm_vector_embedding", "category": "runtime", "rule": "external LLM/vector/embedding", "enforced": True},
        {"boundary_id": "nogo_web_scraping", "category": "scraping", "rule": "web scraping", "enforced": True},
        {"boundary_id": "nogo_news_page_scraping", "category": "scraping", "rule": "news page scraping", "enforced": True},
        {"boundary_id": "nogo_html_scraping", "category": "scraping", "rule": "HTML scraping", "enforced": True},
        {"boundary_id": "nogo_browser_automation", "category": "scraping", "rule": "browser automation scraping", "enforced": True},
        {"boundary_id": "nogo_hidden_api", "category": "scraping", "rule": "hidden API reverse engineering", "enforced": True},
        {"boundary_id": "nogo_paywall_bypass", "category": "scraping", "rule": "paywall bypass", "enforced": True},
        {"boundary_id": "nogo_rate_limit_abuse", "category": "network", "rule": "rate limit abuse", "enforced": True},
        {"boundary_id": "nogo_credential_output", "category": "security", "rule": "credential output", "enforced": True},
        {"boundary_id": "nogo_paid_api_lockin", "category": "commercial", "rule": "required paid API lock-in", "enforced": True},
        {"boundary_id": "nogo_cloud_publish", "category": "packaging", "rule": "cloud publish", "enforced": True},
        {"boundary_id": "nogo_docker_push", "category": "packaging", "rule": "Docker push", "enforced": True},
        {"boundary_id": "nogo_git_tag", "category": "packaging", "rule": "git tag", "enforced": True},
        {"boundary_id": "nogo_archive_creation", "category": "packaging", "rule": "archive creation", "enforced": True},
        {"boundary_id": "nogo_destructive_file", "category": "filesystem", "rule": "destructive file action", "enforced": True},
        {"boundary_id": "nogo_official_approval", "category": "governance", "rule": "official approval wording", "enforced": True}
    ]
    return pd.DataFrame(no_go)

def build_news_safe_go_conditions(profile: NewsProviderProfile) -> pd.DataFrame:
    safe_go = [
        {"boundary_id": "safego_metadata_abstraction", "category": "architecture", "rule": "local/offline news metadata abstraction", "allowed": True},
        {"boundary_id": "safego_metadata_only_schema", "category": "data", "rule": "metadata-only schema", "allowed": True},
        {"boundary_id": "safego_dry_run_fixture", "category": "testing", "rule": "news dry-run fixture", "allowed": True},
        {"boundary_id": "safego_manual_file_placeholder", "category": "storage", "rule": "news manual file placeholder", "allowed": True},
        {"boundary_id": "safego_local_cache_placeholder", "category": "storage", "rule": "news local cache placeholder", "allowed": True},
        {"boundary_id": "safego_official_api_placeholder", "category": "adapter", "rule": "news official API placeholder without network call", "allowed": True},
        {"boundary_id": "safego_licensed_placeholder", "category": "adapter", "rule": "news licensed provider placeholder without credential", "allowed": True},
        {"boundary_id": "safego_public_dataset_placeholder", "category": "adapter", "rule": "news public dataset placeholder without network call", "allowed": True},
        {"boundary_id": "safego_source_registry", "category": "registry", "rule": "news source registry", "allowed": True},
        {"boundary_id": "safego_item_ref_schema", "category": "schema", "rule": "news item reference schema", "allowed": True},
        {"boundary_id": "safego_tag_registries", "category": "taxonomy", "rule": "asset/macro/commodity/FX tag registry", "allowed": True},
        {"boundary_id": "safego_event_linkage", "category": "taxonomy", "rule": "event linkage registry", "allowed": True},
        {"boundary_id": "safego_sentiment_requirements", "category": "requirements", "rule": "sentiment/impact placeholder requirements", "allowed": True},
        {"boundary_id": "safego_freshness_requirements", "category": "requirements", "rule": "freshness/dedup requirements", "allowed": True},
        {"boundary_id": "safego_capability_matching", "category": "matching", "rule": "news capability matching", "allowed": True},
        {"boundary_id": "safego_manual_review", "category": "governance", "rule": "manual review", "allowed": True},
        {"boundary_id": "safego_strict_prohibitions", "category": "governance", "rule": "no broker/no live/no advice/no deploy/no scraping/no copyrighted copy", "allowed": True}
    ]
    return pd.DataFrame(safe_go)

def build_news_safety_boundary(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df_nogo = build_news_no_go_conditions(profile)
    df_safego = build_news_safe_go_conditions(profile)
    df = pd.concat([df_nogo, df_safego], ignore_index=True)
    summary = summarize_news_safety_boundary(df)
    return df, summary

def summarize_news_safety_boundary(df: pd.DataFrame) -> Dict:
    return {
        "total_boundary_rules": len(df),
        "no_go_rules_count": len(df[df["enforced"] == True]) if "enforced" in df.columns else 0,
        "safe_go_rules_count": len(df[df["allowed"] == True]) if "allowed" in df.columns else 0
    }
