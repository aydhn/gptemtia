import os

def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def insert_after_pattern(content: str, pattern: str, insertion: str) -> str:
    parts = content.split(pattern)
    if len(parts) > 1:
        return parts[0] + pattern + "\n" + insertion + parts[1]
    return content

rb_content = read_file("reports/report_builder.py")

rb_methods = """
    # Phase 80: Local Closure support
    def _build_closure_disclaimer(self) -> str:
        return "UYARI: Bu çıktı offline/local v1.0 closure rehearsal ve final meta-review raporudur. Gerçek v1.0 release, production release, resmi proje kapanışı, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"

    def build_closure_domain_registry_text_report(self, summary: dict, domain_df: pd.DataFrame | None = None) -> str:
        text = "Closure Domain Registry\\n\\n" + self._build_closure_disclaimer()
        if domain_df is not None and not domain_df.empty:
            text += domain_df.to_string(index=False)
        return text

    def build_final_meta_review_text_report(self, summary: dict, meta_text: str | None = None) -> str:
        text = "Final Meta Review\\n\\n" + self._build_closure_disclaimer()
        if meta_text:
            text += meta_text
        return text

    def build_lessons_learned_text_report(self, summary: dict, lessons_df: pd.DataFrame | None = None) -> str:
        text = "Lessons Learned\\n\\n" + self._build_closure_disclaimer()
        if lessons_df is not None and not lessons_df.empty:
            text += lessons_df.to_string(index=False)
        return text

    def build_future_roadmap_text_report(self, summary: dict, roadmap_df: pd.DataFrame | None = None) -> str:
        text = "Future Roadmap\\n\\n" + self._build_closure_disclaimer()
        if roadmap_df is not None and not roadmap_df.empty:
            text += roadmap_df.to_string(index=False)
        return text

    def build_v1_local_closure_dossier_text_report(self, summary: dict, dossier_text: str | None = None) -> str:
        text = "V1 Local Closure Dossier\\n\\n" + self._build_closure_disclaimer()
        if dossier_text:
            text += dossier_text
        return text

    def build_closure_quality_text_report(self, summary: dict, quality: dict | None = None) -> str:
        text = "Closure Quality Report\\n\\n" + self._build_closure_disclaimer()
        if quality:
            for k, v in quality.items():
                text += f"{k}: {v}\\n"
        return text

    def build_closure_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        text = "Closure Status\\n\\n" + self._build_closure_disclaimer()
        if not status_df.empty:
            text += status_df.to_string(index=False)
        return text
"""

rb_content = insert_after_pattern(rb_content, "def __init__(self, data_lake: DataLake, feature_store: FeatureStore, settings: Settings):", rb_methods)
write_file("reports/report_builder.py", rb_content)
