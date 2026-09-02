from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile

def build_executive_oversight_sections(project_root: Path, profile: LocalGovernanceControlProfile) -> list[dict]:
    return [
        {"title": "Executive recap", "content": "Yönetici özeti provası."},
        {"title": "System boundary recap", "content": "Sistem sınırlarının kontrolü."},
        {"title": "Safety recap", "content": "Güvenlik incelemesi."},
        {"title": "Readiness summary", "content": "Hazırlık skoru özeti."},
        {"title": "Quality summary", "content": "Kalite skoru özeti."},
        {"title": "Usability/performance/simplification recap", "content": "Geçmiş faz analizleri."},
        {"title": "Acceptance/delivery/archival/closure/reuse recap", "content": "Teslimat özeti."},
        {"title": "Key unresolved items", "content": "Çözülmemiş maddeler."},
        {"title": "Key risks", "content": "Temel riskler."},
        {"title": "Manual oversight recommendations", "content": "Yönetimsel inceleme önerileri."}
    ]

def build_executive_oversight_packet(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[str, dict]:
    sections = build_executive_oversight_sections(project_root, profile)
    lines = ["# Executive Oversight Packet", ""]
    for s in sections:
        lines.append(f"## {s['title']}")
        lines.append(s["content"])
        lines.append("")
    text = "\n".join(lines)
    return text, summarize_executive_oversight_packet(text)

def summarize_executive_oversight_packet(text: str) -> dict:
    if not text:
        return {"length": 0, "sections": 0}
    return {"length": len(text), "sections": text.count("## ")}

def save_executive_oversight_packet(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
