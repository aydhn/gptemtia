import pandas as pd
from typing import Tuple, Dict, List, Optional, Any
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsProviderRequest, build_news_provider_request_id, to_dict

def create_news_provider_request(
    provider_name: str,
    data_type: str,
    topics: Optional[List[str]] = None,
    asset_tags: Optional[List[str]] = None,
    region: Optional[str] = None,
    start: Optional[str] = None,
    end: Optional[str] = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata_only: bool = True,
    metadata: Optional[Dict[str, Any]] = None,
) -> NewsProviderRequest:
    clean_topics = [t.lower().strip() for t in (topics or [])]
    clean_assets = [a.upper().strip() for a in (asset_tags or [])]
    clean_region = region.upper().strip() if region else None
    
    req_id = build_news_provider_request_id(provider_name, data_type)
    return NewsProviderRequest(
        request_id=req_id,
        provider_name=provider_name,
        data_type=data_type,
        topics=clean_topics,
        asset_tags=clean_assets,
        region=clean_region,
        start=start,
        end=end,
        dry_run=dry_run,
        local_only=local_only,
        metadata_only=metadata_only,
        metadata=metadata or {}
    )

def validate_news_provider_request(request: NewsProviderRequest, profile: NewsProviderProfile) -> Dict:
    errors = []
    if not request.provider_name:
        errors.append("provider_name must not be empty")
    if not request.data_type:
        errors.append("data_type must not be empty")
    if not request.metadata_only:
        errors.append("metadata_only must be True; full text extraction is strictly prohibited")
    if request.metadata.get("action") in ["scrape", "download_full_article", "bypass_paywall"]:
        errors.append("Forbidden scraping or full-text download action in request metadata")
    return {"valid": len(errors) == 0, "errors": errors}

def news_provider_request_to_dict(request: NewsProviderRequest) -> Dict:
    return to_dict(request)

def build_news_provider_request_schema(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    fields = [
        {"field_name": "request_id", "type": "string", "required": True, "description": "Unique request identifier"},
        {"field_name": "provider_name", "type": "string", "required": True, "description": "Target provider adapter name"},
        {"field_name": "data_type", "type": "string", "required": True, "description": "Requested news data type"},
        {"field_name": "topics", "type": "list[string]", "required": False, "description": "Requested news topics"},
        {"field_name": "asset_tags", "type": "list[string]", "required": False, "description": "Requested asset class tags"},
        {"field_name": "region", "type": "string", "required": False, "description": "Jurisdiction filter"},
        {"field_name": "start", "type": "string", "required": False, "description": "Start timestamp filter"},
        {"field_name": "end", "type": "string", "required": False, "description": "End timestamp filter"},
        {"field_name": "dry_run", "type": "boolean", "required": True, "description": "Dry-run execution mode flag (default True)"},
        {"field_name": "local_only", "type": "boolean", "required": True, "description": "Local-only execution flag (default True)"},
        {"field_name": "metadata_only", "type": "boolean", "required": True, "description": "Metadata-only flag (default True)"},
        {"field_name": "metadata", "type": "dict", "required": False, "description": "Auxiliary request attributes"}
    ]
    df = pd.DataFrame(fields)
    summary = {"total_fields": len(df), "required_fields": df[df["required"]]["field_name"].tolist()}
    return df, summary
