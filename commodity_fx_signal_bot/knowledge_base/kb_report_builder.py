import pandas as pd
from typing import Dict, Optional
from knowledge_base.kb_models import ResearchMemoryCard

def build_kb_disclaimer() -> str:
    return (
        "---\n"
        "**DISCLAIMER**: Bu çıktı offline knowledge base/analyst workspace raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, otomatik trade onayı veya yatırım tavsiyesi değildir."
    )

def build_knowledge_index_markdown_report(summary: Dict, documents_df: pd.DataFrame, chunks_df: pd.DataFrame) -> str:
    lines = ["# Knowledge Index Report\n"]
    lines.append("## Summary")
    for k, v in summary.items():
        if isinstance(v, dict):
            lines.append(f"- **{k}**:")
            for sub_k, sub_v in v.items():
                lines.append(f"  - {sub_k}: {sub_v}")
        else:
            lines.append(f"- **{k}**: {v}")

    lines.append("\n## Documents Preview")
    if not documents_df.empty:
        cols = ['document_id', 'document_type', 'title', 'source_module']
        avail_cols = [c for c in cols if c in documents_df.columns]
        lines.append(documents_df[avail_cols].head(20).to_markdown(index=False))
    else:
        lines.append("No documents found.")

    lines.append("\n" + build_kb_disclaimer())
    return "\n".join(lines)

def build_research_query_markdown_report(query: str, summary: Dict, results_df: pd.DataFrame) -> str:
    lines = [f"# Research Query Results\n**Query**: {query}\n"]

    lines.append("## Summary")
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    lines.append("\n## Top Results")
    if not results_df.empty:
        for idx, row in results_df.iterrows():
            title = row.get('title', 'Unknown Document')
            score = row.get('final_score', 0.0)
            text = row.get('text', '')
            snippet = text[:200] + "..." if len(text) > 200 else text

            lines.append(f"### {idx + 1}. {title} (Score: {score:.2f})")
            lines.append(f"> {snippet}\n")
    else:
        lines.append("No results found.")

    lines.append(build_kb_disclaimer())
    return "\n".join(lines)

def build_symbol_memory_markdown_report(symbol: str, summary: Dict, memory_card: Optional[ResearchMemoryCard] = None) -> str:
    lines = [f"# Symbol Memory Report: {symbol}\n"]

    if memory_card:
        lines.append("## Summary")
        lines.append(memory_card.summary)

        lines.append("\n## Key Findings")
        if memory_card.key_findings:
            for f in memory_card.key_findings:
                lines.append(f"- {f}")
        else:
            lines.append("None found.")

        lines.append("\n## Warnings")
        if memory_card.warnings:
            for w in memory_card.warnings:
                lines.append(f"- {w}")
        else:
            lines.append("None found.")

    else:
        lines.append("No memory card generated.")

    lines.append("\n" + build_kb_disclaimer())
    return "\n".join(lines)

def build_decision_journal_markdown_report(summary: Dict, journal_df: pd.DataFrame) -> str:
    lines = ["# Decision Journal\n"]

    lines.append("## Summary")
    for k, v in summary.items():
        if isinstance(v, dict):
            lines.append(f"- **{k}**:")
            for sub_k, sub_v in v.items():
                lines.append(f"  - {sub_k}: {sub_v}")
        else:
            lines.append(f"- **{k}**: {v}")

    lines.append("\n## Entries")
    if not journal_df.empty:
        cols = ['status', 'title', 'description', 'created_at_utc']
        avail_cols = [c for c in cols if c in journal_df.columns]
        lines.append(journal_df[avail_cols].head(50).to_markdown(index=False))
    else:
        lines.append("No entries found.")

    lines.append("\n" + build_kb_disclaimer())
    return "\n".join(lines)

def build_recent_findings_markdown_report(summary: Dict, findings_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Recent Findings Digest\n"]

    lines.append("## Summary")
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    lines.append("\n## Findings Preview")
    if findings_df is not None and not findings_df.empty:
        # Just show snippet
        for idx, row in findings_df.head(20).iterrows():
            doc_id = row.get('document_id', 'unknown')
            text = row.get('text', '')
            snippet = text[:150] + "..." if len(text) > 150 else text
            lines.append(f"- **{doc_id}**: {snippet}")
    else:
        lines.append("No findings found.")

    lines.append("\n" + build_kb_disclaimer())
    return "\n".join(lines)

def build_analyst_workspace_status_markdown_report(summary: Dict, status_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Analyst Workspace Status\n"]

    lines.append("## Overall Status")
    for k, v in summary.items():
        if isinstance(v, dict):
            lines.append(f"- **{k}**:")
            for sub_k, sub_v in v.items():
                lines.append(f"  - {sub_k}: {sub_v}")
        else:
            lines.append(f"- **{k}**: {v}")

    lines.append("\n## Metrics")
    if status_df is not None and not status_df.empty:
        lines.append(status_df.to_markdown(index=False))
    else:
        lines.append("No status metrics available.")

    lines.append("\n" + build_kb_disclaimer())
    return "\n".join(lines)
