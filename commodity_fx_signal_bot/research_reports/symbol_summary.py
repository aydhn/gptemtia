import pandas as pd
from config.symbols import SymbolSpec
from research_reports.research_models import SymbolResearchSnapshot, clamp_research_score
from research_reports.research_config import ResearchReportProfile

def build_latest_price_summary(inputs: dict) -> dict:
    if 'ohlcv' not in inputs or inputs['ohlcv'].empty:
        return {
            "latest_close": None,
            "latest_timestamp": None,
            "volume_available": False,
            "warnings": ["OHLCV data is missing."]
        }

    ohlcv = inputs['ohlcv']
    latest_row = ohlcv.iloc[-1]

    # check if timestamp is in index or column
    timestamp = ohlcv.index[-1] if isinstance(ohlcv.index, pd.DatetimeIndex) else latest_row.get('timestamp')
    timestamp_str = str(timestamp) if timestamp else None

    return {
        "latest_close": float(latest_row.get('close', 0.0)),
        "latest_timestamp": timestamp_str,
        "volume_available": 'volume' in ohlcv.columns and not pd.isna(latest_row.get('volume')),
        "warnings": []
    }

def build_symbol_identity_summary(spec: SymbolSpec, inputs: dict) -> dict:
    return {
        "symbol": spec.symbol,
        "name": getattr(spec, 'name', spec.symbol),
        "asset_class": getattr(spec, 'asset_class', None),
        "quote_currency": getattr(spec, 'quote_currency', None),
    }

def calculate_symbol_research_score(sections: dict) -> float:
    # A simple scoring based on presence of data and some positive context
    # This is a stub for the actual complex logic.
    score = 0.5
    if sections.get('technical_summary', {}).get('strongest_signal_context') == 'supportive_context':
        score += 0.1
    if sections.get('risk_level_summary', {}).get('risk_approved_count', 0) > 0:
        score += 0.1
    if sections.get('ml_summary', {}).get('ml_context_available'):
        score += 0.1
    return clamp_research_score(score)

def build_symbol_research_snapshot(spec: SymbolSpec, timeframe: str, inputs: dict, metadata: dict, profile: ResearchReportProfile) -> SymbolResearchSnapshot:
    identity = build_symbol_identity_summary(spec, inputs)
    price_summary = build_latest_price_summary(inputs)

    # Import sections here to avoid circular dependencies if any
    from research_reports.technical_summary import build_technical_summary
    from research_reports.risk_level_summary import build_risk_level_summary
    from research_reports.backtest_summary import build_backtest_research_summary
    from research_reports.performance_summary import build_performance_research_summary
    from research_reports.validation_summary import build_validation_research_summary
    from research_reports.ml_summary import build_ml_research_summary
    from research_reports.paper_summary import build_paper_research_summary
    from research_reports.quality_summary import build_quality_research_summary

    technical_summary = build_technical_summary(inputs, profile) if profile.include_technical_summary else {}
    risk_level_summary = build_risk_level_summary(inputs, profile) if profile.include_risk_level_summary else {}
    backtest_summary = build_backtest_research_summary(inputs, profile) if profile.include_backtest_summary else {}
    performance_summary = build_performance_research_summary(inputs, profile) if profile.include_performance_summary else {}
    validation_summary = build_validation_research_summary(inputs, profile) if profile.include_validation_summary else {}
    ml_summary = build_ml_research_summary(inputs, profile) if profile.include_ml_summary else {}
    paper_summary = build_paper_research_summary(inputs, profile) if profile.include_paper_summary else {}
    quality_summary = build_quality_research_summary(inputs, metadata, profile) if profile.include_quality_summary else {}

    sections = {
        'technical_summary': technical_summary,
        'risk_level_summary': risk_level_summary,
        'ml_summary': ml_summary
    }

    research_score = calculate_symbol_research_score(sections)

    status = "research_report_ready"
    if not metadata.get('data_available', False):
        status = "research_report_insufficient_data"
    elif research_score < profile.min_quality_score:
        status = "research_report_warning"

    return SymbolResearchSnapshot(
        symbol=identity['symbol'],
        timeframe=timeframe,
        asset_class=identity['asset_class'],
        latest_timestamp=price_summary['latest_timestamp'],
        technical_summary=technical_summary,
        risk_level_summary=risk_level_summary,
        backtest_summary=backtest_summary,
        performance_summary=performance_summary,
        validation_summary=validation_summary,
        ml_summary=ml_summary,
        paper_summary=paper_summary,
        quality_summary=quality_summary,
        research_score=research_score,
        research_status=status,
        warnings=metadata.get('warnings', []) + price_summary.get('warnings', [])
    )
