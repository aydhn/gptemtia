import pandas as pd
from typing import Optional

def build_documentation_disclaimer() -> str:
    return (
        "> **UYARI:** Bu çıktı offline/local documentation pack raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, "
        "production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
    )

def build_documentation_pack_markdown_report(summary: dict, docs_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Documentation Pack Raporu",
        build_documentation_disclaimer(),
        f"**Profil:** {summary.get('profile', 'Unknown')}",
        f"**Kalite Skoru:** {summary.get('quality_score', 0.0):.2f}",
        ""
    ]
    if docs_df is not None and not docs_df.empty:
        lines.append("## Üretilen/Taranan Dokümanlar")
        for _, row in docs_df.iterrows():
            lines.append(f"- `{row['relative_path']}`: {row['document_type']} ({row['status']})")

    return "\n".join(lines)

def build_documentation_quality_markdown_report(summary: dict, quality: dict) -> str:
    lines = [
        "# Documentation Quality Raporu",
        build_documentation_disclaimer(),
        f"**Genel Durum:** {'PASSED' if quality.get('passed') else 'FAILED'}",
        f"**Uyarı Sayısı:** {quality.get('warning_count', 0)}",
        "",
        "## Detaylar",
        f"- Envanter Geçerli mi: {quality.get('inventory_valid')}",
        f"- Kapsam Geçerli mi: {quality.get('coverage_valid')}",
        f"- Güvenlik Dili Uygun mu: {quality.get('safety_valid')}",
        ""
    ]
    warnings = quality.get("warnings", [])
    if warnings:
        lines.append("## Uyarılar")
        for w in warnings:
            lines.append(f"- {w}")

    return "\n".join(lines)

def build_documentation_status_markdown_report(summary: dict, status_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Documentation Status Raporu",
        build_documentation_disclaimer()
    ]
    if status_df is not None and not status_df.empty:
         lines.append(status_df.to_markdown(index=False))
    return "\n".join(lines)

def build_safe_usage_docs_markdown_report(summary: dict, safety_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Safe Usage Docs Raporu",
        build_documentation_disclaimer()
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append(safety_df.to_markdown(index=False))
    return "\n".join(lines)

def build_script_reference_markdown_report(summary: dict, scripts_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Script Reference Raporu",
        build_documentation_disclaimer()
    ]
    if scripts_df is not None and not scripts_df.empty:
        lines.append(scripts_df.to_markdown(index=False))
    return "\n".join(lines)

def build_output_reference_markdown_report(summary: dict, outputs_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Output Reference Raporu",
        build_documentation_disclaimer()
    ]
    if outputs_df is not None and not outputs_df.empty:
        lines.append(outputs_df.to_markdown(index=False))
    return "\n".join(lines)
