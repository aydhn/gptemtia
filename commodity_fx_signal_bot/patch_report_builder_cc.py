import re

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

cc_methods = """
def build_command_catalog_text_report(summary: dict, commands_df: pd.DataFrame | None = None) -> str:
    txt = "COMMAND CATALOG REPORT\\n"
    txt += "=" * 40 + "\\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\\n"
    txt += "\\nCommands:\\n"
    if commands_df is not None and not commands_df.empty:
        txt += commands_df.to_string(index=False)
    else:
        txt += "No commands found.\\n"
    return txt

def build_guided_workflow_text_report(summary: dict, workflows_df: pd.DataFrame | None = None) -> str:
    txt = "GUIDED WORKFLOW REPORT\\n"
    txt += "=" * 40 + "\\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\\n"
    txt += "\\nWorkflows:\\n"
    if workflows_df is not None and not workflows_df.empty:
        txt += workflows_df.to_string(index=False)
    else:
        txt += "No workflows found.\\n"
    return txt

def build_safe_runbook_text_report(summary: dict, runbooks_df: pd.DataFrame | None = None) -> str:
    txt = "SAFE RUNBOOK REPORT\\n"
    txt += "=" * 40 + "\\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\\n"
    txt += "\\nRunbooks:\\n"
    if runbooks_df is not None and not runbooks_df.empty:
        txt += runbooks_df.to_string(index=False)
    else:
        txt += "No runbooks found.\\n"
    return txt

def build_project_status_text_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    txt = "PROJECT STATUS REPORT\\n"
    txt += "=" * 40 + "\\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\\n"
    txt += "\\nModule Status:\\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_string(index=False)
    else:
        txt += "No status data found.\\n"
    return txt

def build_project_consolidation_text_report(summary: dict, consolidation_df: pd.DataFrame | None = None) -> str:
    txt = "PROJECT CONSOLIDATION REPORT\\n"
    txt += "=" * 40 + "\\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
    for k, v in summary.items():
        if isinstance(v, dict):
            txt += f"{k}:\\n"
            for sub_k, sub_v in v.items():
                txt += f"  {sub_k}: {sub_v}\\n"
        else:
            txt += f"{k}: {v}\\n"
    txt += "\\nConsolidation Details:\\n"
    if consolidation_df is not None and not consolidation_df.empty:
        txt += consolidation_df.to_string(index=False)
    return txt

def build_analyst_command_query_text_report(summary: dict, result_df: pd.DataFrame | None = None) -> str:
    txt = "ANALYST COMMAND QUERY REPORT\\n"
    txt += "=" * 40 + "\\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\\n"
    txt += "\\nSuggested Commands:\\n"
    if result_df is not None and not result_df.empty:
        txt += result_df.to_string(index=False)
    else:
        txt += "No suggested commands found.\\n"
    return txt

def build_command_center_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    txt = "COMMAND CENTER STATUS REPORT\\n"
    txt += "=" * 40 + "\\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\\n"
    txt += "\\nStatus:\\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_string(index=False)
    return txt
"""

content = content + "\n\n" + cc_methods

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
