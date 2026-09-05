from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile

NO_GO_RULES: List[Tuple[str, str, str]] = [
    ("NO_GO_01", "Live Trading Execution", "Strictly prohibited from submitting real market orders or interacting with live exchange gateways"),
    ("NO_GO_02", "Broker Integration", "Strictly prohibited from binding broker accounts, protocols (FIX), or broker APIs"),
    ("NO_GO_03", "Broker Credentials", "Strictly prohibited from consuming or outputting broker API keys, tokens, or secret credentials"),
    ("NO_GO_04", "Exact Buy/Sell Instructions", "Strictly prohibited from generating deterministic buy/sell order recommendations"),
    ("NO_GO_05", "Investment Advice", "Strictly prohibited from offering fiduciary financial advice or capital allocation counsel"),
    ("NO_GO_06", "Benchmark Score as Signal", "Strictly prohibited from utilizing benchmark score values as trade entry/exit triggers"),
    ("NO_GO_07", "Official Approval Claim", "Strictly prohibited from claiming official endorsement or regulatory certification for any provider"),
    ("NO_GO_08", "Production Ready Claim", "Strictly prohibited from certifying providers as production-ready for live capital"),
    ("NO_GO_09", "Broker Ready Claim", "Strictly prohibited from declaring providers broker-compatible or broker-ready"),
    ("NO_GO_10", "Live Provider API Calls", "Strictly prohibited from requiring external network calls to paid or proprietary live endpoints"),
    ("NO_GO_11", "Real Data Download Requirement", "Strictly prohibited from enforcing real live data downloads to execute benchmarks"),
    ("NO_GO_12", "Web Scraping", "Strictly prohibited from conducting HTML scraping, DOM traversal, or web scraping"),
    ("NO_GO_13", "News Page Scraping", "Strictly prohibited from parsing online news portals or RSS web scraping"),
    ("NO_GO_14", "Browser Automation", "Strictly prohibited from utilizing Playwright, Selenium, Puppeteer, or headless browsers"),
    ("NO_GO_15", "Hidden API Reverse Engineering", "Strictly prohibited from reversing private endpoints or unauthorized REST calls"),
    ("NO_GO_16", "Paywall Bypass", "Strictly prohibited from circumventing content barriers or paywalls"),
    ("NO_GO_17", "Rate Limit Abuse", "Strictly prohibited from flooding endpoints or exceeding documented rate quotas"),
    ("NO_GO_18", "Full Article Harvesting", "Strictly prohibited from collecting full news article bodies or paragraphs"),
    ("NO_GO_19", "Copyrighted Content Reproduction", "Strictly prohibited from copying or redistributing copyrighted text"),
    ("NO_GO_20", "Source File Overwriting", "Strictly prohibited from modifying, mutating, or overwriting raw source data files"),
    ("NO_GO_21", "Destructive Auto-Cleaning", "Strictly prohibited from automatically dropping or deleting unmapped rows from sources"),
    ("NO_GO_22", "File Deletion", "Strictly prohibited from deleting existing historical data lake files"),
    ("NO_GO_23", "File Relocation", "Strictly prohibited from moving source files away from canonical paths"),
    ("NO_GO_24", "Model Deployment", "Strictly prohibited from deploying ML models to production inference services"),
    ("NO_GO_25", "Production Deployment", "Strictly prohibited from promoting pipeline artifacts to production servers"),
    ("NO_GO_26", "Web Server Daemon", "Strictly prohibited from running Flask, FastAPI, Uvicorn, or background web servers"),
    ("NO_GO_27", "Interactive Dashboard", "Strictly prohibited from launching web GUI/TUI dashboards"),
    ("NO_GO_28", "External LLM / Cloud API", "Strictly prohibited from calling remote AI APIs (OpenAI, Anthropic) during benchmark"),
    ("NO_GO_29", "Vector Database Engine", "Strictly prohibited from initializing Chroma, Pinecone, Milvus, or Qdrant"),
    ("NO_GO_30", "Embedding Generation", "Strictly prohibited from generating text embeddings via cloud APIs"),
    ("NO_GO_31", "Cloud Registry Publishing", "Strictly prohibited from executing docker push, cloud publishing, or git tagging"),
    ("NO_GO_32", "Real Archive Packaging", "Strictly prohibited from packaging production release archives or encrypted containers"),
]

SAFE_GO_RULES: List[Tuple[str, str, str]] = [
    ("SAFE_GO_01", "Local Offline Benchmark", "Executing fully offline, local benchmark reports using existing phase artifacts"),
    ("SAFE_GO_02", "Deterministic Mock Fixtures", "Running mock and fixture-based provider benchmark rehearsals without external network"),
    ("SAFE_GO_03", "Coverage Breadth Comparison", "Comparing asset, symbol, and indicator universe coverage across offline registries"),
    ("SAFE_GO_04", "Capability Analysis", "Evaluating technical timeseries, quote, OHLCV, and timestamp capabilities offline"),
    ("SAFE_GO_05", "Quality Engine Consolidation", "Consolidating Phase 112 data quality findings into diagnostic benchmark scores"),
    ("SAFE_GO_06", "Normalization Assessment", "Evaluating adherence to Phase 113 canonical schemas and unit standardization"),
    ("SAFE_GO_07", "Traceability Evaluation", "Auditing source-to-normalized transformation lineage from Phase 114"),
    ("SAFE_GO_08", "License Boundary Review", "Recording licensing restrictions and redistribution terms for research use"),
    ("SAFE_GO_09", "Strict No-Scraping Audit", "Enforcing 100% adherence to zero web scraping boundaries"),
    ("SAFE_GO_10", "Metadata-Only Verification", "Verifying zero full-text news article storage across all pipelines"),
    ("SAFE_GO_11", "Non-Destructive Manual Review", "Logging review items with destructive_action_allowed=False strictly"),
    ("SAFE_GO_12", "Research Ranking Matrix", "Compiling comparative suitability rankings labeled exclusively for research"),
    ("SAFE_GO_13", "Diagnostic Health Check", "Verifying module availability and directory integrity across Phases 106-115"),
    ("SAFE_GO_14", "Integrity Validation", "Scanning outputs for forbidden commercial and trading approval claims"),
    ("SAFE_GO_15", "Phase 116 Feature Engine Handoff", "Delivering clean data readiness notes to Phase 116 without generating signals"),
]


def build_provider_benchmark_no_go_conditions(
    profile: ProviderBenchmarkProfile,
) -> pd.DataFrame:
    records = []
    for r_id, name, desc in NO_GO_RULES:
        records.append({
            "condition_id": r_id,
            "rule_type": "NO_GO",
            "name": name,
            "description": desc,
            "enforced": True,
        })
    return pd.DataFrame.from_records(records)


def build_provider_benchmark_safe_go_conditions(
    profile: ProviderBenchmarkProfile,
) -> pd.DataFrame:
    records = []
    for r_id, name, desc in SAFE_GO_RULES:
        records.append({
            "condition_id": r_id,
            "rule_type": "SAFE_GO",
            "name": name,
            "description": desc,
            "permitted": True,
        })
    return pd.DataFrame.from_records(records)


def build_provider_benchmark_safety_boundary(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    no_go_df = build_provider_benchmark_no_go_conditions(profile)
    safe_go_df = build_provider_benchmark_safe_go_conditions(profile)
    combined_df = pd.concat([no_go_df, safe_go_df], ignore_index=True)
    summary = summarize_provider_benchmark_safety_boundary(combined_df)
    return combined_df, summary


def summarize_provider_benchmark_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    no_go_cnt = int((df["rule_type"] == "NO_GO").sum()) if not df.empty and "rule_type" in df.columns else len(NO_GO_RULES)
    safe_go_cnt = int((df["rule_type"] == "SAFE_GO").sum()) if not df.empty and "rule_type" in df.columns else len(SAFE_GO_RULES)
    return {
        "safety_status": "ACTIVE",
        "total_rules": len(df),
        "total_no_go_rules": no_go_cnt,
        "total_safe_go_rules": safe_go_cnt,
        "all_no_go_enforced": True,
        "all_safe_go_permitted": True,
        "current_phase": 115,
        "target_final_phase": 160,
    }
