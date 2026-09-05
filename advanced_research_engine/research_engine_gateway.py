import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchGatewayItem, ResearchRequest, ResearchResult, build_research_gateway_id, build_research_result_id

def build_default_research_gateway_items(profile: AdvancedResearchEngineProfile) -> list[ResearchGatewayItem]:
    return [ResearchGatewayItem(gateway_id=build_research_gateway_id("core", "data_access"), gateway_area="core", interface_ref="data_access", target_module_ref="future_provider", future_phase_range="106-115", gateway_status="ready", warnings=[])]

def build_research_engine_gateway_map(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([vars(i) for i in build_default_research_gateway_items(profile)])
    return df, summarize_research_engine_gateway(df)

def summarize_research_engine_gateway(df: pd.DataFrame) -> dict: return {"gateways": len(df)}

def route_research_request_dry_run(request: ResearchRequest, profile: AdvancedResearchEngineProfile) -> ResearchResult:
    known = ["request_data_access", "request_feature_build", "request_regime_analysis", "request_ml_research", "request_backtest_research", "request_portfolio_research", "request_report_build", "request_signal_research", "request_full_research_dry_run"]
    status = "success" if request.request_type in known else "graceful_error"
    return ResearchResult(result_id=build_research_result_id(request.request_id, "dry_run"), request_id=request.request_id, result_type="dry_run", status_label=status, output_ref="", summary={}, warnings=[], manual_review_required=True)
