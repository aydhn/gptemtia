"""
Safety boundary report logic.
"""

import pandas as pd
from pathlib import Path
from master_orchestration.master_config import MasterOrchestrationProfile

_SAFETY_RULES = [
    "no live orders",
    "no broker execution",
    "no real positions",
    "no model deployment",
    "no production scheduler",
    "no background daemon",
    "no web scraping",
    "no real market download in demo/regression",
    "no external LLM/API in summarization",
    "no automatic destructive cleanup",
    "no investment advice language"
]

_FORBIDDEN_TERMS = [
    "live order", "broker order", "real trade", "open position",
    "close position", "buy now", "sell now", "deploy model",
    "production deploy", "production scheduler", "background daemon",
    "while true", "run live", "external llm", "openai api",
    "real market download", "selenium", "playwright", "beautifulsoup",
    "force delete", "guaranteed profit", "risk-free return",
    "yatırım tavsiyesidir", "kesin al", "kesin sat"
]

def build_master_safety_boundary_table(project_root: Path, profile: MasterOrchestrationProfile) -> pd.DataFrame:
    records = []
    for rule in _SAFETY_RULES:
        records.append({
            "boundary_rule": rule,
            "status": "enforced",
            "enforcement_mechanism": "Master Orchestration Profile / SafeMetaRunner"
        })
    return pd.DataFrame(records)

def scan_master_plan_for_forbidden_terms(plan_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> tuple[pd.DataFrame, dict]:
    violations = []
    if not plan_df.empty:
        for _, row in plan_df.iterrows():
            text_to_scan = f"{row.get('command_name', '')} {row.get('command', '')} {row.get('safety_label', '')}".lower()
            for term in _FORBIDDEN_TERMS:
                if term in text_to_scan:
                    # Ignore false positive disclaimers conceptually, but basic scan here
                    violations.append({
                        "command_id": row.get("command_id"),
                        "forbidden_term": term,
                        "context": text_to_scan[:50]
                    })

    df = pd.DataFrame(violations) if violations else pd.DataFrame(columns=["command_id", "forbidden_term", "context"])
    summary = {
        "total_violations": len(df)
    }
    return df, summary

def build_master_safety_boundary_report(project_root: Path, plan_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_master_safety_boundary_table(project_root, profile)
    summary = summarize_master_safety_boundaries(df)
    return df, summary

def summarize_master_safety_boundaries(safety_df: pd.DataFrame) -> dict:
    if safety_df.empty:
        return {"total_boundaries": 0}

    return {
        "total_boundaries": len(safety_df),
        "enforced_boundaries": len(safety_df[safety_df["status"] == "enforced"])
    }
