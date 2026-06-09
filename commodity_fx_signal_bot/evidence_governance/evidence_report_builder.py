import pandas as pd

def build_evidence_disclaimer() -> str:
    return "> **UYARI:** Bu çıktı offline/local governance evidence ve compliance-style binder raporudur. Resmi compliance sertifikası, hukuki görüş, canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"

def build_evidence_artifact_inventory_markdown_report(summary: dict, artifact_df: pd.DataFrame | None = None) -> str:
    md = "# Evidence Artifact Inventory\n\n"
    md += build_evidence_disclaimer()

    md += f"- **Total Artifacts:** {summary.get('total_artifacts', 0)}\n"
    md += f"- **Total Size (Bytes):** {summary.get('total_size_bytes', 0)}\n\n"

    if artifact_df is not None and not artifact_df.empty:
        md += "## Artifact List\n\n"
        md += artifact_df[["artifact_id", "artifact_label", "freshness_label", "relative_path"]].head(100).to_markdown(index=False)
        if len(artifact_df) > 100:
            md += f"\n\n*... and {len(artifact_df) - 100} more artifacts.*\n"

    return md

def build_policy_control_mapping_markdown_report(summary: dict, mapping_df: pd.DataFrame | None = None) -> str:
    md = "# Policy and Control Mapping\n\n"
    md += build_evidence_disclaimer()

    md += f"- **Total Mappings:** {summary.get('total_mappings', 0)}\n\n"

    if mapping_df is not None and not mapping_df.empty:
        md += "## Mappings\n\n"
        md += mapping_df.head(100).to_markdown(index=False)

    return md

def build_audit_evidence_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    md = ""
    md += build_evidence_disclaimer()
    if binder_text:
        md += binder_text
    else:
        md += "# Audit Evidence Binder\n\n(No content provided)"

    return md

def build_traceability_matrix_markdown_report(summary: dict, trace_df: pd.DataFrame | None = None) -> str:
    md = "# Evidence Traceability Matrix\n\n"
    md += build_evidence_disclaimer()

    md += f"- **Total Trace Links:** {summary.get('total_trace_links', 0)}\n\n"

    if trace_df is not None and not trace_df.empty:
        md += "## Traceability Details\n\n"
        md += trace_df.head(100).to_markdown(index=False)

    return md

def build_governance_evidence_export_markdown_report(summary: dict, export_index_df: pd.DataFrame | None = None) -> str:
    md = "# Governance Evidence Export Manifest\n\n"
    md += build_evidence_disclaimer()

    md += f"- **Export Ready Items:** {summary.get('export_ready_items', 0)}\n"
    md += f"- **Safe Local Only:** {summary.get('is_safe_local_only', True)}\n\n"

    if export_index_df is not None and not export_index_df.empty:
        md += "## Local Export Index\n\n"
        md += export_index_df.head(100).to_markdown(index=False)

    return md

def build_evidence_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    md = "# Evidence Quality Report\n\n"
    md += build_evidence_disclaimer()

    if quality:
        md += f"- **Passed:** {quality.get('passed', False)}\n"
        md += f"- **Warnings Count:** {quality.get('warning_count', 0)}\n\n"

        if quality.get("warnings"):
            md += "## Warnings\n\n"
            for w in quality["warnings"]:
                md += f"- {w}\n"

    return md

def build_evidence_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    md = "# Evidence Governance Status\n\n"
    md += build_evidence_disclaimer()

    if status_df is not None and not status_df.empty:
        md += "## Status\n\n"
        md += status_df.to_markdown(index=False)

    return md
