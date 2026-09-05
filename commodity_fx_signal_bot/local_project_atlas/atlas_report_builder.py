"""Atlas report builder module."""
import pandas as pd

def build_atlas_disclaimer() -> str:
    return "Bu rapor offline/local project atlas ve meta-index çıktısıdır; gerçek enterprise search, cloud index, vector DB, official knowledge index, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

def _build_markdown(title: str, summary: dict, df: pd.DataFrame | None = None) -> str:
    lines = [f"# {title}", "", build_atlas_disclaimer(), ""]
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")
    if df is not None and not df.empty:
        lines.append("")
        lines.append(df.to_markdown(index=False))
    return "\n".join(lines)

def build_atlas_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str: return _build_markdown("Atlas Domain Registry", summary, domain_df)
def build_meta_index_markdown_report(summary: dict, meta_df: pd.DataFrame | None = None) -> str: return _build_markdown("Final Local Meta-Index", summary, meta_df)
def build_universal_navigation_markdown_report(summary: dict, nav_df: pd.DataFrame | None = None) -> str: return _build_markdown("Universal Navigation Map", summary, nav_df)
def build_cross_phase_lookup_markdown_report(summary: dict, lookup_df: pd.DataFrame | None = None) -> str: return _build_markdown("Cross-Phase Lookup", summary, lookup_df)
def build_semantic_toc_markdown_report(summary: dict, toc_text: str | None = None) -> str: return _build_markdown("Semantic TOC", summary) + f"\n\n{toc_text or ''}"
def build_terminal_project_atlas_markdown_report(summary: dict, atlas_text: str | None = None) -> str: return _build_markdown("Terminal Project Atlas", summary) + f"\n\n{atlas_text or ''}"
def build_meta_index_quality_markdown_report(summary: dict, quality: dict | None = None) -> str: return _build_markdown("Quality Report", summary)
def build_meta_index_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str: return _build_markdown("Status Report", summary, status_df)
