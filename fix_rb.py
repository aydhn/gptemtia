path = "commodity_fx_signal_bot/reports/report_builder.py"
with open(path, "r") as f:
    content = f.read()

new_content = """
def build_artifact_inventory_text_report(summary: dict, inventory_df=None) -> str:
    rep = "=== ARTIFACT INVENTORY REPORT ===\\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\\n\\n"
    rep += f"Total Artifacts: {summary.get('total_artifacts', 0)}\\n"
    rep += f"Total Size (MB): {summary.get('total_size_mb', 0):.2f}\\n"
    rep += "\\nTypes:\\n"
    for t, c in summary.get("artifacts_by_type", {}).items():
        rep += f"- {t}: {c}\\n"
    return rep

def build_lineage_graph_text_report(summary: dict, node_df=None, edge_df=None) -> str:
    rep = "=== LINEAGE GRAPH REPORT ===\\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\\n\\n"
    rep += f"Nodes: {summary.get('node_count', 0)}\\n"
    rep += f"Edges: {summary.get('edge_count', 0)}\\n"
    cycles = summary.get("cycles", {})
    rep += f"Has Cycles: {cycles.get('has_cycles', False)}\\n"
    return rep

def build_provenance_text_report(summary: dict, provenance_df=None) -> str:
    rep = "=== PROVENANCE REPORT ===\\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\\n\\n"
    rep += f"Total Records: {summary.get('total_records', 0)}\\n"
    rep += f"Unique Artifacts: {summary.get('unique_artifacts', 0)}\\n"
    rep += "\\nSources:\\n"
    for s, c in summary.get("sources", {}).items():
        rep += f"- {s}: {c}\\n"
    return rep

def build_dependency_trace_text_report(summary: dict, trace_df=None) -> str:
    rep = "=== DEPENDENCY TRACE REPORT ===\\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\\n\\n"
    if summary.get("warnings"):
        rep += "Warnings:\\n"
        for w in summary["warnings"]:
            rep += f"- {w}\\n"
        rep += "\\n"
    if trace_df is not None and not trace_df.empty:
        rep += f"Trace nodes found: {len(trace_df)}\\n"
    else:
        rep += "No trace found.\\n"
    return rep

def build_audit_trail_text_report(summary: dict, audit_df=None) -> str:
    rep = "=== AUDIT TRAIL REPORT ===\\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\\n\\n"
    rep += f"Total Events: {summary.get('total_events', 0)}\\n"
    rep += "\\nEvent Types:\\n"
    for t, c in summary.get("event_types", {}).items():
        rep += f"- {t}: {c}\\n"
    return rep

def build_research_governance_text_report(summary: dict, checklist_df=None) -> str:
    rep = "=== RESEARCH GOVERNANCE REPORT ===\\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\\n\\n"
    q = summary.get("quality", {})
    rep += f"Passed Governance: {q.get('passed', False)}\\n"
    rep += f"Warning Count: {q.get('warning_count', 0)}\\n"
    return rep

def build_governance_status_report(status_df=None, summary: dict=None) -> str:
    rep = "=== GOVERNANCE STATUS REPORT ===\\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\\n\\n"
    if status_df is not None and not status_df.empty:
        rep += f"Files found: {len(status_df)}\\n"
        for _, r in status_df.iterrows():
            rep += f"- {r.get('report_name', 'unknown')}: {r.get('path', 'unknown')}\\n"
    else:
        rep += "No governance files found.\\n"
    return rep
"""
# Find where the class ends, or just replace the indented version with the unindented version
import re
content = re.sub(r'    def build_artifact_inventory_text_report.*?return rep', new_content, content, flags=re.DOTALL)
with open(path, "w") as f:
    f.write(content)
