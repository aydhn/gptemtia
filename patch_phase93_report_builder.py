import os
import re

with open("commodity_fx_signal_bot/reports/report_builder.py", "r", encoding="utf-8") as f:
    content = f.read()

addition = """
    # Phase 93
    def _build_atlas_text(self, title: str, summary: dict, df: pd.DataFrame | None = None) -> str:
        lines = [f"{title.upper()}", "=" * len(title), ""]
        lines.append("Uyari: Bu cikti offline/local project atlas ve meta-index raporudur. Gercek enterprise search, cloud index, vector DB, official knowledge index, canli emir, broker talimati, model deployment veya yatirim tavsiyesi degildir.")
        lines.append("")
        for k, v in summary.items():
            lines.append(f"{k}: {v}")
        if df is not None and not df.empty:
            lines.append("")
            lines.append(df.to_string(index=False))
        return "\\n".join(lines)

    def build_atlas_domain_registry_text_report(self, summary: dict, domain_df: pd.DataFrame | None = None) -> str: return self._build_atlas_text("Atlas Domain Registry", summary, domain_df)
    def build_meta_index_text_report(self, summary: dict, meta_df: pd.DataFrame | None = None) -> str: return self._build_atlas_text("Final Local Meta-Index", summary, meta_df)
    def build_universal_navigation_text_report(self, summary: dict, nav_df: pd.DataFrame | None = None) -> str: return self._build_atlas_text("Universal Navigation Map", summary, nav_df)
    def build_cross_phase_lookup_text_report(self, summary: dict, lookup_df: pd.DataFrame | None = None) -> str: return self._build_atlas_text("Cross-Phase Lookup", summary, lookup_df)
    def build_semantic_toc_text_report(self, summary: dict, toc_text: str | None = None) -> str: return self._build_atlas_text("Semantic TOC", summary) + f"\\n\\n{toc_text or ''}"
    def build_terminal_project_atlas_text_report(self, summary: dict, atlas_text: str | None = None) -> str: return self._build_atlas_text("Terminal Project Atlas", summary) + f"\\n\\n{atlas_text or ''}"
    def build_meta_index_quality_text_report(self, summary: dict, quality: dict | None = None) -> str: return self._build_atlas_text("Quality Report", summary)
    def build_meta_index_status_report(self, status_df: pd.DataFrame, summary: dict) -> str: return self._build_atlas_text("Status Report", summary, status_df)
"""

if "build_atlas_domain_registry_text_report" not in content:
    content = content + "\n" + addition
    with open("commodity_fx_signal_bot/reports/report_builder.py", "w", encoding="utf-8") as f:
        f.write(content)

print("ReportBuilder patched")
