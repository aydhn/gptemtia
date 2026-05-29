import pandas as pd
from .ux_config import AnalystUXProfile

def map_query_to_runbooks(query_text: str, profile: AnalystUXProfile) -> pd.DataFrame:
    q = query_text.lower()
    runbooks = []
    if "hata" in q:
        runbooks.append({"file": "TROUBLESHOOTING_COOKBOOK.md", "type": "troubleshooting"})
    if "komut" in q:
        runbooks.append({"file": "SAFE_COMMAND_REFERENCE.md", "type": "reference"})
    if "kurulum" in q:
        runbooks.append({"file": "INSTALLATION.md", "type": "setup"})
    if "konfigürasyon" in q:
        runbooks.append({"file": "CONFIGURATION.md", "type": "config"})
    return pd.DataFrame(runbooks)

def map_query_to_workflows(query_text: str, profile: AnalystUXProfile) -> pd.DataFrame:
    q = query_text.lower()
    workflows = []
    if "scenario" in q:
        workflows.append({"workflow": "Scenario Demo Flow", "description": "Run offline scenarios"})
    if "regression" in q:
        workflows.append({"workflow": "Regression Flow", "description": "Check for regressions"})
    return pd.DataFrame(workflows)

def map_query_to_docs(query_text: str, profile: AnalystUXProfile) -> pd.DataFrame:
    q = query_text.lower()
    docs = []
    if "scenario" in q:
        docs.append({"doc": "docs/generated/scenarios", "desc": "Scenario docs"})
    if "regression" in q:
        docs.append({"doc": "scenario_regression docs", "desc": "Regression docs"})
    if "final review" in q:
        docs.append({"doc": "final review README", "desc": "Final review docs"})
    if "cleanup" in q:
        docs.append({"doc": "MAINTENANCE_GUIDE.md", "desc": "Maintenance docs"})
    if "quality" in q:
        docs.append({"doc": "QUALITY_GATES_GUIDE.md", "desc": "Quality docs"})
    # Catch-all for investment advice queries
    if "al" in q or "sat" in q or "tavsiye" in q:
         docs.append({"doc": "SAFE_USAGE_GUIDE.md", "desc": "Disclaimer and safe usage. No investment advice."})
    return pd.DataFrame(docs)

def build_query_mapping_report(query_text: str, profile: AnalystUXProfile) -> tuple[dict[str, pd.DataFrame], dict]:
    tables = {
        "runbooks": map_query_to_runbooks(query_text, profile),
        "workflows": map_query_to_workflows(query_text, profile),
        "docs": map_query_to_docs(query_text, profile)
    }
    return tables, summarize_query_mapping(tables)

def summarize_query_mapping(mapping_tables: dict[str, pd.DataFrame]) -> dict:
    return {
        "runbooks_count": len(mapping_tables.get("runbooks", pd.DataFrame())),
        "workflows_count": len(mapping_tables.get("workflows", pd.DataFrame())),
        "docs_count": len(mapping_tables.get("docs", pd.DataFrame()))
    }
