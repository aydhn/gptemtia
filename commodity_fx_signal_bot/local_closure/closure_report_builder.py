
import pandas as pd

def build_closure_disclaimer() -> str:
    return "> **UYARI**: Bu çıktı offline/local v1.0 closure rehearsal ve final meta-review raporudur. Gerçek v1.0 release, production release, resmi proje kapanışı, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"

def build_closure_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    md = "# Closure Domain Registry\n\n" + build_closure_disclaimer()
    if domain_df is not None and not domain_df.empty:
        md += domain_df.to_markdown(index=False)
    return md

def build_final_meta_review_markdown_report(summary: dict, meta_text: str | None = None) -> str:
    md = "# Final Meta Review\n\n" + build_closure_disclaimer()
    if meta_text:
        md += meta_text
    return md

def build_lessons_learned_markdown_report(summary: dict, lessons_df: pd.DataFrame | None = None) -> str:
    md = "# Lessons Learned\n\n" + build_closure_disclaimer()
    if lessons_df is not None and not lessons_df.empty:
        md += lessons_df.to_markdown(index=False)
    return md

def build_future_roadmap_markdown_report(summary: dict, roadmap_df: pd.DataFrame | None = None) -> str:
    md = "# Future Roadmap\n\n" + build_closure_disclaimer()
    if roadmap_df is not None and not roadmap_df.empty:
        md += roadmap_df.to_markdown(index=False)
    return md

def build_v1_local_closure_dossier_markdown_report(summary: dict, dossier_text: str | None = None) -> str:
    md = "# V1 Local Closure Dossier\n\n" + build_closure_disclaimer()
    if dossier_text:
        md += dossier_text
    return md

def build_closure_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    md = "# Closure Quality Report\n\n" + build_closure_disclaimer()
    if quality:
        for k, v in quality.items():
            md += f"- **{k}**: {v}\n"
    return md

def build_closure_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    md = "# Closure Status\n\n" + build_closure_disclaimer()
    if status_df is not None and not status_df.empty:
        md += status_df.to_markdown(index=False)
    return md
