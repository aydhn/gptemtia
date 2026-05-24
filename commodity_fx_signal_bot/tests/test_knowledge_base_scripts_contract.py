import importlib

def test_script_imports():
    importlib.import_module("scripts.run_knowledge_index_report")
    importlib.import_module("scripts.run_research_query")
    importlib.import_module("scripts.run_symbol_memory_report")
    importlib.import_module("scripts.run_decision_journal_report")
    importlib.import_module("scripts.run_recent_findings_digest")
    importlib.import_module("scripts.run_analyst_workspace_status")
