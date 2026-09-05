import pandas as pd
from typing import Tuple, Dict, List, Optional
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsProviderResponse, build_news_provider_response_id, to_dict

def create_news_provider_response(
    request_id: str,
    provider_name: str,
    data_type: str,
    status_label: str,
    output_ref: str = "",
    row_count: int = 0,
    schema_ref: str = "",
    warnings: Optional[List[str]] = None,
    manual_review_required: bool = True,
) -> NewsProviderResponse:
    res_id = build_news_provider_response_id(request_id, provider_name)
    return NewsProviderResponse(
        response_id=res_id,
        request_id=request_id,
        provider_name=provider_name,
        data_type=data_type,
        status_label=status_label,
        output_ref=output_ref,
        row_count=row_count,
        schema_ref=schema_ref,
        warnings=warnings or [],
        manual_review_required=manual_review_required
    )

def validate_news_provider_response(response: NewsProviderResponse, profile: NewsProviderProfile) -> Dict:
    errors = []
    if not response.response_id:
        errors.append("response_id must not be empty")
    if not response.request_id:
        errors.append("request_id must not be empty")
    if response.row_count < 0:
        errors.append("row_count must be non-negative")
    return {"valid": len(errors) == 0, "errors": errors}

def news_provider_response_to_dict(response: NewsProviderResponse) -> Dict:
    return to_dict(response)

def build_news_provider_response_schema(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    fields = [
        {"field_name": "response_id", "type": "string", "required": True, "description": "Unique response identifier"},
        {"field_name": "request_id", "type": "string", "required": True, "description": "Matched request identifier"},
        {"field_name": "provider_name", "type": "string", "required": True, "description": "Responding provider adapter name"},
        {"field_name": "data_type", "type": "string", "required": True, "description": "Returned news metadata data type"},
        {"field_name": "status_label", "type": "string", "required": True, "description": "Execution status outcome"},
        {"field_name": "output_ref", "type": "string", "required": True, "description": "URI or location reference of output payload"},
        {"field_name": "row_count", "type": "integer", "required": True, "description": "Number of records processed (can be 0)"},
        {"field_name": "schema_ref", "type": "string", "required": True, "description": "Schema contract applied"},
        {"field_name": "warnings", "type": "list[string]", "required": True, "description": "Operational warnings"},
        {"field_name": "manual_review_required", "type": "boolean", "required": True, "description": "Mandatory human review flag (default True)"}
    ]
    df = pd.DataFrame(fields)
    summary = {"total_fields": len(df), "required_fields": df[df["required"]]["field_name"].tolist()}
    return df, summary
