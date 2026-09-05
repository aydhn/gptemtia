import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchRequest, build_research_request_id

def create_research_request(
    request_type: str,
    universe: list[str] | None = None,
    timeframe: str = "1d",
    horizon: str = "research",
    requested_modules: list[str] | None = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: dict | None = None,
) -> ResearchRequest:
    return ResearchRequest(
        request_id=build_research_request_id(request_type, timeframe, horizon),
        request_type=request_type,
        universe=universe or [],
        timeframe=timeframe,
        horizon=horizon,
        requested_modules=requested_modules or [],
        dry_run=dry_run,
        local_only=local_only,
        metadata=metadata or {}
    )

def validate_research_request(request: ResearchRequest, profile: AdvancedResearchEngineProfile) -> dict:
    return {"valid": request.dry_run and request.local_only}

def research_request_to_dict(request: ResearchRequest) -> dict:
    return vars(request)

def build_research_request_schema(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"field": "request_type", "type": "str"}])
    return df, {"schema_fields": 1}
