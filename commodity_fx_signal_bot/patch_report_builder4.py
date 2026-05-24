import re
from pathlib import Path

def patch_report_builder():
    path = Path("reports/report_builder.py")
    content = path.read_text()

    if "build_knowledge_index_text_report" in content:
        print("Report builder already patched.")
        return

    addition = """
# Phase 49: Knowledge Base & Analyst Workspace Text Reports

def _kb_disclaimer() -> str:
    return "\\n--- \\nBu çıktı offline knowledge base/analyst workspace raporudur. Canlı emir, broker talimatı, gerçek pozisyon, otomatik trade onayı veya yatırım tavsiyesi değildir."

def build_knowledge_index_text_report(summary: dict, documents_df: pd.DataFrame | None = None, chunks_df: pd.DataFrame | None = None) -> str:
    lines = ["*** KNOWLEDGE INDEX REPORT ***\\n"]
    for k, v in summary.items():
        if isinstance(v, dict):
            lines.append(f"{k.upper()}:")
            for sub_k, sub_v in v.items():
                lines.append(f"  - {sub_k}: {sub_v}")
        else:
            lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\\n".join(lines)

def build_research_query_text_report(summary: dict, results_df: pd.DataFrame | None = None) -> str:
    lines = ["*** RESEARCH QUERY REPORT ***\\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\\n".join(lines)

def build_symbol_memory_text_report(summary: dict, memory_card: dict | None = None) -> str:
    lines = ["*** SYMBOL MEMORY REPORT ***\\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")

    if memory_card:
        lines.append("\\nCARD DATA:")
        lines.append(f"Summary: {memory_card.get('summary', '')}")
        lines.append(f"Warnings: {len(memory_card.get('warnings', []))}")

    lines.append(_kb_disclaimer())
    return "\\n".join(lines)

def build_decision_journal_text_report(summary: dict, journal_df: pd.DataFrame | None = None) -> str:
    lines = ["*** DECISION JOURNAL ***\\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\\n".join(lines)

def build_recent_findings_text_report(summary: dict, findings_df: pd.DataFrame | None = None) -> str:
    lines = ["*** RECENT FINDINGS DIGEST ***\\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\\n".join(lines)

def build_analyst_workspace_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = ["*** ANALYST WORKSPACE STATUS ***\\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\\n".join(lines)
"""

    path.write_text(content + "\n" + addition)
    print("Report Builder patched successfully.")

if __name__ == "__main__":
    patch_report_builder()
