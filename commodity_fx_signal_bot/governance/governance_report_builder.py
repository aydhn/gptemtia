import pandas as pd


def build_governance_disclaimer() -> str:
    return "> **UYARI:** Bu çıktı offline research governance/data lineage raporudur. Canlı emir, broker talimatı, gerçek pozisyon, production compliance onayı veya yatırım tavsiyesi değildir.\n\n"

def build_artifact_inventory_markdown_report(summary: dict, inventory_df: pd.DataFrame) -> str:
    md = "# Artifact Inventory Report\n\n"
    md += build_governance_disclaimer()
    md += f"**Total Artifacts:** {summary.get('total_artifacts', 0)}\n\n"
    md += f"**Total Size (MB):** {summary.get('total_size_mb', 0):.2f}\n\n"

    md += "## Types\n"
    types = summary.get("artifacts_by_type", {})
    for t, c in types.items():
        md += f"- {t}: {c}\n"

    md += "\n## Sample Items\n"
    if not inventory_df.empty:
        sample = inventory_df.head(10)[["artifact_type", "file_name", "size_bytes"]]
        md += sample.to_markdown(index=False)

    return md

def build_lineage_graph_markdown_report(summary: dict, node_df: pd.DataFrame, edge_df: pd.DataFrame) -> str:
    md = "# Lineage Graph Report\n\n"
    md += build_governance_disclaimer()
    md += f"**Nodes:** {summary.get('node_count', 0)}\n"
    md += f"**Edges:** {summary.get('edge_count', 0)}\n"

    cycles = summary.get("cycles", {})
    md += f"**Has Cycles:** {cycles.get('has_cycles', False)}\n\n"

    if not edge_df.empty:
        md += "## Sample Edges\n"
        sample = edge_df.head(10)[["relation", "confidence_score"]]
        md += sample.to_markdown(index=False)

    return md

def build_provenance_markdown_report(summary: dict, provenance_df: pd.DataFrame) -> str:
    md = "# Provenance Report\n\n"
    md += build_governance_disclaimer()
    md += f"**Total Records:** {summary.get('total_records', 0)}\n"
    md += f"**Unique Artifacts:** {summary.get('unique_artifacts', 0)}\n\n"

    md += "## Sources\n"
    for s, c in summary.get("sources", {}).items():
        md += f"- {s}: {c}\n"

    return md

def build_dependency_trace_markdown_report(summary: dict, trace_df: pd.DataFrame) -> str:
    md = "# Dependency Trace Report\n\n"
    md += build_governance_disclaimer()

    if summary.get("warnings"):
        md += "**Warnings:**\n"
        for w in summary["warnings"]:
            md += f"- {w}\n"
        md += "\n"

    if not trace_df.empty:
        md += "## Trace\n"
        md += trace_df[["node_id", "artifact_type", "relation"]].to_markdown(index=False)
    else:
        md += "No trace found.\n"

    return md

def build_audit_trail_markdown_report(summary: dict, audit_df: pd.DataFrame) -> str:
    md = "# Audit Trail Report\n\n"
    md += build_governance_disclaimer()
    md += f"**Total Events:** {summary.get('total_events', 0)}\n\n"

    md += "## Event Types\n"
    for t, c in summary.get("event_types", {}).items():
        md += f"- {t}: {c}\n"

    return md

def build_research_governance_markdown_report(summary: dict, checklist_df: pd.DataFrame) -> str:
    md = "# Research Governance Report\n\n"
    md += build_governance_disclaimer()

    q = summary.get("quality", {})
    md += f"**Passed Governance:** {q.get('passed', False)}\n"
    md += f"**Warning Count:** {q.get('warning_count', 0)}\n\n"

    if not checklist_df.empty:
        md += "## Checklist\n"
        md += checklist_df[["item_id", "description", "status"]].to_markdown(index=False)

    return md
