import pandas as pd

def build_readiness_disclaimer() -> str:
    return (
        "*** WARNING / UYARI ***\n"
        "Bu çıktı offline/local non-production readiness dry-run raporudur. "
        "Production release onayı, canlı emir, broker talimatı, gerçek pozisyon, "
        "model deployment, production scheduler, otomatik trade onayı veya "
        "yatırım tavsiyesi değildir.\n"
        "***\n\n"
    )

def build_readiness_gate_registry_markdown_report(summary: dict, gate_df: pd.DataFrame | None = None) -> str:
    txt = build_readiness_disclaimer()
    txt += "# Readiness Gate Registry\n\n"
    if gate_df is not None and not gate_df.empty:
        txt += gate_df.to_markdown() + "\n"
    return txt

def build_final_operator_checklist_markdown_report(summary: dict, checklist_df: pd.DataFrame | None = None) -> str:
    txt = build_readiness_disclaimer()
    txt += "# Final Operator Checklist\n\n"
    if checklist_df is not None and not checklist_df.empty:
        txt += checklist_df.to_markdown() + "\n"
    return txt

def build_readiness_reports_markdown_report(summary: dict, readiness_df: pd.DataFrame | None = None) -> str:
    txt = build_readiness_disclaimer()
    txt += "# Readiness Reports\n\n"
    if readiness_df is not None and not readiness_df.empty:
        txt += readiness_df.to_markdown() + "\n"
    return txt

def build_handoff_package_manifest_markdown_report(summary: dict, manifest: dict | None = None) -> str:
    txt = build_readiness_disclaimer()
    txt += "# Handoff Package Manifest\n\n"
    if manifest:
        import json
        txt += f"```json\n{json.dumps(manifest, indent=2)}\n```\n"
    return txt

def build_final_local_readiness_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    txt = build_readiness_disclaimer()
    txt += "# Final Local Readiness Binder\n\n"
    if binder_text:
        txt += binder_text + "\n"
    return txt

def build_readiness_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    txt = build_readiness_disclaimer()
    txt += "# Readiness Quality Report\n\n"
    if quality:
        import json
        txt += f"```json\n{json.dumps(quality, indent=2)}\n```\n"
    return txt

def build_readiness_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    txt = build_readiness_disclaimer()
    txt += "# Readiness Status Report\n\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_markdown() + "\n"
    return txt
