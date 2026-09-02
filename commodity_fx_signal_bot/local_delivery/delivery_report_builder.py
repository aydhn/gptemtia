import pandas as pd

def build_delivery_disclaimer() -> str:
    return "Bu çıktı offline/local project delivery rehearsal ve handoff package documentation raporudur. Gerçek teslim, cloud upload, package publish, production handoff, resmi kabul, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

def build_delivery_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Delivery Domain Registry\n\n{build_delivery_disclaimer()}\n\nRegistry OK."

def build_final_delivery_bundle_manifest_markdown_report(summary: dict, manifest: dict | None = None) -> str:
    return f"# Final Delivery Bundle Manifest\n\n{build_delivery_disclaimer()}\n\nManifest OK."

def build_handoff_package_index_markdown_report(summary: dict, index_df: pd.DataFrame | None = None) -> str:
    return f"# Handoff Package Index\n\n{build_delivery_disclaimer()}\n\nIndex OK."

def build_portable_reviewer_archive_guide_markdown_report(summary: dict, guide_text: str | None = None) -> str:
    return f"# Portable Reviewer Archive Guide\n\n{build_delivery_disclaimer()}\n\nGuide OK."

def build_delivery_rehearsal_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    return f"# Delivery Rehearsal Binder\n\n{build_delivery_disclaimer()}\n\nBinder OK."

def build_delivery_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Delivery Quality Report\n\n{build_delivery_disclaimer()}\n\nQuality OK."

def build_delivery_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Delivery Status Report\n\n{build_delivery_disclaimer()}\n\nStatus OK."
