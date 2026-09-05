from pathlib import Path
from .completion_config import LocalProjectCompletionProfile

def build_system_closure_dossier_sections(project_root: Path, profile: LocalProjectCompletionProfile) -> list[dict]:
    return [
        {"title": "Amaç ve Kapsam", "content": "Offline system closure rehearsal."},
        {"title": "Bu dossier ne değildir?", "content": "Gerçek project closure, official completion approval, production approval, legal sign-off veya yatırım tavsiyesi değildir."},
        {"title": "Phase 1-90 Genel Kapanış Özeti", "content": "Local framework and orchestration layer is complete."},
        {"title": "Offline/local system boundary", "content": "Local execution only."},
        {"title": "Final architecture recap", "content": "Modules are finalized in local context."},
        {"title": "Final manual review requirements", "content": "Manual review required for any production step."},
        {"title": "Final non-production boundary statement", "content": "Strictly no live trading, no broker integration."}
    ]

def build_final_local_system_closure_dossier(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    sections = build_system_closure_dossier_sections(project_root, profile)
    text = "# Final Local System Closure Dossier\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    return text, summarize_system_closure_dossier(text)

def summarize_system_closure_dossier(text: str) -> dict:
    return {"length": len(text), "note": "Not a real project closure."}

def save_system_closure_dossier(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
