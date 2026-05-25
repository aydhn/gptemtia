"""
Interactive local query flows.
"""

import pandas as pd
from typing import Tuple
from command_center.command_config import CommandCenterProfile

def build_symbol_query_flow(symbol: str, profile: CommandCenterProfile) -> dict:
    return {
        "flow_type": "symbol_query",
        "target": symbol,
        "knowledge_index_check": f"Checking index for {symbol}...",
        "recommended_query_command": f"python -m scripts.run_research_query --query 'Latest findings for {symbol}'",
        "recommended_memory_report": f"python -m scripts.run_symbol_memory_report --symbol {symbol}",
        "related_module_status": "Check research_reports status",
        "expected_outputs": [f"{symbol}_memory_card.json", f"{symbol}_research_report.md"],
        "limitations": "Does not fetch live data. Uses local offline knowledge only.",
        "disclaimer": "This is an offline query flow. Not investment advice."
    }

def build_module_query_flow(module_name: str, profile: CommandCenterProfile) -> dict:
    return {
        "flow_type": "module_query",
        "target": module_name,
        "knowledge_index_check": f"Checking index for module {module_name}...",
        "recommended_query_command": f"python -m scripts.run_research_query --query 'What is the status of {module_name}?'",
        "recommended_memory_report": None,
        "related_module_status": f"python -m scripts.run_{module_name}_status",
        "expected_outputs": [f"{module_name}_status.md"],
        "limitations": "Checks local module artifacts only.",
        "disclaimer": "This is an offline query flow."
    }

def build_warning_query_flow(profile: CommandCenterProfile) -> dict:
    return {
        "flow_type": "warning_query",
        "target": "warnings",
        "knowledge_index_check": "Checking index for recent warnings...",
        "recommended_query_command": "python -m scripts.run_research_query --query 'Summarize recent system warnings'",
        "recommended_memory_report": None,
        "related_module_status": "python -m scripts.run_project_status_report",
        "expected_outputs": ["project_status_report.md"],
        "limitations": "Relies on previously generated reports.",
        "disclaimer": "This is an offline query flow."
    }

def build_project_question_flow(query_text: str, profile: CommandCenterProfile) -> dict:
    return {
        "flow_type": "project_question",
        "target": query_text,
        "knowledge_index_check": "Checking knowledge base index...",
        "recommended_query_command": f"python -m scripts.run_research_query --query '{query_text}'",
        "recommended_memory_report": None,
        "related_module_status": "None",
        "expected_outputs": ["query_result.md"],
        "limitations": "Only queries ingested documents.",
        "disclaimer": "This is an offline query flow. Not investment advice."
    }

def build_interactive_query_flow_report(flow: dict) -> Tuple[pd.DataFrame, dict]:
    summary = {
        "flow_type": flow["flow_type"],
        "target": flow["target"],
        "disclaimer": flow["disclaimer"]
    }
    data = [{k: str(v) for k, v in flow.items()}]
    return pd.DataFrame(data), summary
