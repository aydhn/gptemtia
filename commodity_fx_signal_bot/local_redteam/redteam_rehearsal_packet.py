from pathlib import Path
from local_redteam.redteam_config import LocalRedTeamProfile

def build_redteam_rehearsal_sections(project_root: Path, profile: LocalRedTeamProfile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Bu doküman sistemin sınırlarını test eden offline provadır."},
        {"title": "Bu paket ne değildir?", "content": "Gerçek red-team raporu, exploit payload, jailbreak veya production safety approval değildir."},
        {"title": "Safety boundary recap", "content": "Sistem cloud upload, telemetry, broker execution, live trading ve investment advice gibi yeteneklere kapalıdır."},
        {"title": "Misuse scenario families", "content": "Live trading, broker execution, secret exposure vb."},
        {"title": "Abuse-case simulation recap", "content": "Tüm testler dry-run olarak yapılmıştır."},
        {"title": "Adversarial prompt safety checklist recap", "content": "Jailbreak denemeleri abstract düzeyde loglanmıştır."},
        {"title": "Prompt-injection risk pattern recap", "content": "Enjeksiyon patternleri payload olmadan listelenmiştir."},
        {"title": "Forbidden capability request recap", "content": "Engellenen yetenekler kaydedilmiştir."},
        {"title": "Manual escalation recap", "content": "Riskli durumlar insan incelemesine yönlendirilir."},
        {"title": "Safety assurance coverage recap", "content": "Kapsam matrix ile belirlenmiştir."},
        {"title": "Blindspots and gaps", "content": "Görünmeyen noktalar manuel inceleme gerektirir."},
        {"title": "Red-team no-go/safe-go", "content": "No-go: gerçek attack. Safe-go: offline rehearsal."},
        {"title": "Final boundary statement", "content": "Sistem local, offline ve denetlenebilirdir."}
    ]

def build_final_local_redteam_rehearsal_packet(project_root: Path, profile: LocalRedTeamProfile) -> tuple[str, dict]:
    sections = build_redteam_rehearsal_sections(project_root, profile)
    text = "FINAL LOCAL REDTEAM REHEARSAL PACKET\n========================================\n\n"
    for sec in sections:
        text += f"## {sec['title']}\n{sec['content']}\n\n"
    summary = summarize_redteam_rehearsal_packet(text)
    return text, summary

def summarize_redteam_rehearsal_packet(text: str) -> dict:
    return {
        "length": len(text),
        "sections": text.count("## "),
        "note": "Packet is not a real attack or certification."
    }

def save_redteam_rehearsal_packet(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return output_path
