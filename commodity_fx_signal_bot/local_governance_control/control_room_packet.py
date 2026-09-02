from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile

def build_control_room_sections(project_root: Path, profile: LocalGovernanceControlProfile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Local governance control room rehearsal packet."},
        {"title": "Bu paket ne değildir?", "content": "Gerçek dashboard veya üretim onayı değildir."},
        {"title": "Governance rehearsal overview", "content": "Tüm süreçler offline provadır."},
        {"title": "Executive oversight summary", "content": "Yönetimsel gözden geçirme simülasyonu."},
        {"title": "Manual approval ledger summary", "content": "Manuel onay defteri simülasyonu."},
        {"title": "Risk committee rehearsal summary", "content": "Risk komitesi provası özeti."},
        {"title": "Operator supervision summary", "content": "Operatör gözetimi kılavuz özeti."},
        {"title": "Escalation matrix summary", "content": "Manuel escalation akışı."},
        {"title": "No-go/safe-go summary", "content": "Güvenlik sınırları kontrolü."},
        {"title": "Evidence and reading order", "content": "Kanıt dokümanları okuma sırası."},
        {"title": "Open decisions", "content": "Açık kararlar listesi."},
        {"title": "Manual review requirements", "content": "Gözden geçirme gereksinimleri."},
        {"title": "Final boundary statement", "content": "Canlı emir veya broker işlemi yapılmamıştır."}
    ]

def build_final_local_governance_control_room_packet(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[str, dict]:
    sections = build_control_room_sections(project_root, profile)
    lines = ["# Final Local Governance Control Room Packet", ""]
    for s in sections:
        lines.append(f"## {s['title']}")
        lines.append(s["content"])
        lines.append("")
    text = "\n".join(lines)
    return text, summarize_control_room_packet(text)

def summarize_control_room_packet(text: str) -> dict:
    if not text:
        return {"length": 0, "sections": 0}
    return {"length": len(text), "sections": text.count("## ")}

def save_control_room_packet(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
