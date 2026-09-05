import os
from pathlib import Path

def patch_report_builder():
    p = Path("reports/report_builder.py")
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "build_packaging_domain_registry_text_report" not in content:
        methods = """
    # Phase 96: Local Distribution Packaging Text Reports
    def build_packaging_domain_registry_text_report(self, summary: dict, domain_df: pd.DataFrame | None = None) -> str:
        return f"Packaging Domain Registry\\n{self._get_packaging_disclaimer()}"

    def build_distribution_bundle_text_report(self, summary: dict, bundle_text: str | None = None) -> str:
        return f"Distribution Bundle\\n{self._get_packaging_disclaimer()}\\n\\n{bundle_text or ''}"

    def build_portable_docs_bundle_text_report(self, summary: dict, portable_text: str | None = None) -> str:
        return f"Portable Docs Bundle\\n{self._get_packaging_disclaimer()}\\n\\n{portable_text or ''}"

    def build_release_folder_manifest_text_report(self, summary: dict, folder_text: str | None = None) -> str:
        return f"Release Folder Manifest\\n{self._get_packaging_disclaimer()}\\n\\n{folder_text or ''}"

    def build_handover_zip_map_text_report(self, summary: dict, zip_text: str | None = None) -> str:
        return f"Handover ZIP-Map\\n{self._get_packaging_disclaimer()}\\n\\n{zip_text or ''}"

    def build_packaging_governance_text_report(self, summary: dict, governance_text: str | None = None) -> str:
        return f"Packaging Governance\\n{self._get_packaging_disclaimer()}\\n\\n{governance_text or ''}"

    def build_packaging_quality_text_report(self, summary: dict, quality: dict | None = None) -> str:
        return f"Packaging Quality Report\\n{self._get_packaging_disclaimer()}"

    def build_packaging_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        return f"Packaging Status\\n{self._get_packaging_disclaimer()}"
        
    def _get_packaging_disclaimer(self) -> str:
        return "Bu cikti offline/local distribution bundle rehearsal ve packaging governance raporudur. Gercek ZIP/archive, package publish, deployment, official handover, canli emir, broker talimati, model deployment veya yatirim tavsiyesi degildir."
"""
        with open(p, "a", encoding="utf-8") as f:
            f.write(methods)
        print("Patched reports/report_builder.py")

if __name__ == "__main__":
    patch_report_builder()
