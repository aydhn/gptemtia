import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchResult, build_research_result_id

def create_research_result(
    request_id: str,
    result_type: str,
    status_label: str,
    output_ref: str = "",
    summary: dict | None = None,
    warnings: list[str] | None = None,
    manual_review_required: bool = True,
) -> ResearchResult:
    return ResearchResult(
        result_id=build_research_result_id(request_id, result_type),
        request_id=request_id,
        result_type=result_type,
        status_label=status_label,
        output_ref=output_ref,
        summary=summary or {},
        warnings=warnings or [],
        manual_review_required=manual_review_required
    )

def validate_research_result(result: ResearchResult, profile: AdvancedResearchEngineProfile) -> dict:
    return {"valid": result.manual_review_required}

def research_result_to_dict(result: ResearchResult) -> dict:
    return vars(result)

def build_research_result_schema(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"field": "result_id", "type": "str"}])
    return df, {"schema_fields": 1}
