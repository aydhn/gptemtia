import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
import pandas as pd
from typing import Optional

@dataclass
class SymbolResearchSnapshot:
    symbol: str
    timeframe: str
    asset_class: Optional[str]
    latest_timestamp: Optional[str]
    technical_summary: dict
    risk_level_summary: dict
    backtest_summary: dict
    performance_summary: dict
    validation_summary: dict
    ml_summary: dict
    paper_summary: dict
    quality_summary: dict
    research_score: float
    research_status: str
    warnings: list[str] = field(default_factory=list)

@dataclass
class ResearchReport:
    report_id: str
    report_type: str
    title: str
    profile_name: str
    timeframe: str
    symbols: list[str]
    created_at_utc: str
    markdown: str
    tables: dict[str, pd.DataFrame]
    summary: dict
    warnings: list[str] = field(default_factory=list)

def clamp_research_score(value: Optional[float]) -> float:
    if value is None:
        return 0.0
    return max(0.0, min(1.0, float(value)))

def build_research_report_id(report_type: str, profile_name: str, timeframe: str, symbols: list[str]) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    symbols_str = "multi" if len(symbols) > 1 else (symbols[0] if symbols else "empty")

    # Make it path-safe
    raw_id = f"{report_type}_{profile_name}_{timeframe}_{symbols_str}_{timestamp}"
    safe_id = re.sub(r'[^a-zA-Z0-9_\-]', '_', raw_id)
    # limit length to prevent file system issues
    if len(safe_id) > 100:
       safe_id = safe_id[:100]
    return safe_id

def symbol_research_snapshot_to_dict(snapshot: SymbolResearchSnapshot) -> dict:
    return {
        "symbol": snapshot.symbol,
        "timeframe": snapshot.timeframe,
        "asset_class": snapshot.asset_class,
        "latest_timestamp": snapshot.latest_timestamp,
        "technical_summary": snapshot.technical_summary,
        "risk_level_summary": snapshot.risk_level_summary,
        "backtest_summary": snapshot.backtest_summary,
        "performance_summary": snapshot.performance_summary,
        "validation_summary": snapshot.validation_summary,
        "ml_summary": snapshot.ml_summary,
        "paper_summary": snapshot.paper_summary,
        "quality_summary": snapshot.quality_summary,
        "research_score": snapshot.research_score,
        "research_status": snapshot.research_status,
        "warnings": snapshot.warnings
    }

def research_report_to_dict(report: ResearchReport, include_markdown: bool = False) -> dict:
    data = {
        "report_id": report.report_id,
        "report_type": report.report_type,
        "title": report.title,
        "profile_name": report.profile_name,
        "timeframe": report.timeframe,
        "symbols": report.symbols,
        "created_at_utc": report.created_at_utc,
        "summary": report.summary,
        "warnings": report.warnings
    }
    if include_markdown:
        data["markdown"] = report.markdown
    return data
