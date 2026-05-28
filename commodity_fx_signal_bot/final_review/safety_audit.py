import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, List
import re
from final_review.final_review_config import FinalReviewProfile

_LIVE_TRADING_PATTERNS = ["create_order", "place_order", "market_order", "live_order", "buy_now", "sell_now", "open_position", "close_position"]
_BROKER_EXECUTION_PATTERNS = ["broker_order", "leverage order", "requests to private broker endpoint"]
_DEPLOYMENT_PATTERNS = ["production deploy", "deploy model"]
_DAEMON_PATTERNS = ["while True daemon", "schedule.every live"]
_WEB_SCRAPING_PATTERNS = ["selenium", "playwright", "beautifulsoup"]
_INVESTMENT_ADVICE_PATTERNS = ["guaranteed profit", "risk-free return", "kesin al", "kesin sat", "yatırım tavsiyesidir"]

_FALSE_POSITIVES = [
    "canlı emir yoktur", "yatırım tavsiyesi değildir", "broker entegrasyonu yoktur", "not investment advice", "no live trading"
]

def _scan_files_for_patterns(project_root: Path, patterns: List[str], scan_type: str) -> pd.DataFrame:
    rows = []
    # simplified scan for mock/offline use
    for ext in ["*.py", "*.md", "*.sh"]:
        for file in project_root.rglob(ext):
            if "venv" in str(file) or ".git" in str(file):
                continue

            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read().lower()

                    for fp in _FALSE_POSITIVES:
                        content = content.replace(fp.lower(), "")

                    for p in patterns:
                        if p.lower() in content:
                            rows.append({
                                "file": str(file.relative_to(project_root)),
                                "scan_type": scan_type,
                                "pattern_found": p,
                                "critical": True
                            })
            except Exception:
                pass

    if not rows:
        return pd.DataFrame(columns=["file", "scan_type", "pattern_found", "critical"])

    return pd.DataFrame(rows)

def scan_project_for_live_trading_risk(project_root: Path) -> pd.DataFrame:
    return _scan_files_for_patterns(project_root, _LIVE_TRADING_PATTERNS, "live_trading")

def scan_project_for_broker_execution_risk(project_root: Path) -> pd.DataFrame:
    return _scan_files_for_patterns(project_root, _BROKER_EXECUTION_PATTERNS, "broker_execution")

def scan_project_for_deployment_risk(project_root: Path) -> pd.DataFrame:
    return _scan_files_for_patterns(project_root, _DEPLOYMENT_PATTERNS, "deployment")

def scan_project_for_daemon_loop_risk(project_root: Path) -> pd.DataFrame:
    return _scan_files_for_patterns(project_root, _DAEMON_PATTERNS, "daemon_loop")

def scan_project_for_web_scraping_risk(project_root: Path) -> pd.DataFrame:
    return _scan_files_for_patterns(project_root, _WEB_SCRAPING_PATTERNS, "web_scraping")

def scan_reports_for_investment_advice_language(project_root: Path) -> pd.DataFrame:
    return _scan_files_for_patterns(project_root, _INVESTMENT_ADVICE_PATTERNS, "investment_advice")

def build_safety_audit_report(project_root: Path, profile: FinalReviewProfile) -> Tuple[pd.DataFrame, dict]:
    dfs = [
        scan_project_for_live_trading_risk(project_root),
        scan_project_for_broker_execution_risk(project_root),
        scan_project_for_deployment_risk(project_root),
        scan_project_for_daemon_loop_risk(project_root),
        scan_project_for_web_scraping_risk(project_root),
        scan_reports_for_investment_advice_language(project_root)
    ]

    df = pd.concat(dfs, ignore_index=True) if any(not d.empty for d in dfs) else pd.DataFrame(columns=["file", "scan_type", "pattern_found", "critical"])

    critical_count = len(df[df["critical"] == True])

    summary = {
        "total_issues_found": len(df),
        "critical_issues": critical_count,
        "passed": critical_count == 0,
        "status": "blocked_by_safety_issue" if critical_count > 0 else "audit_passed"
    }

    return df, summary
