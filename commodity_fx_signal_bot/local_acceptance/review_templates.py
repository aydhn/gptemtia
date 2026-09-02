from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_review_template_sections(template_type: str, profile: LocalAcceptanceProfile) -> list[dict]:
    return [
        {"title": "İnceleyen kişi/rol", "content": "[Ad Soyad / Rol]"},
        {"title": "Tarih", "content": "[Tarih]"},
        {"title": "İncelenen evidence", "content": "[Evidence Listesi]"},
        {"title": "Sorulan sorular", "content": "[Sorular]"},
        {"title": "Yanıtlar", "content": "[Yanıtlar]"},
        {"title": "Eksikler", "content": "[Eksikler]"},
        {"title": "No-go gözlemleri", "content": "[Gözlemler]"},
        {"title": "Manual review notları", "content": "[Notlar]"},
        {"title": "Sonraki güvenli adımlar", "content": "[Adımlar]"},
        {"title": "Sınırlar", "content": "Bu bir resmi imza formu veya yatırım tavsiyesi değildir."}
    ]

def build_independent_review_notes_template(profile: LocalAcceptanceProfile) -> tuple[str, dict]:
    sections = build_review_template_sections("review_notes", profile)
    lines = ["# Independent Review Notes Template\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, {"length": len(text)}

def build_acceptance_response_template(profile: LocalAcceptanceProfile) -> tuple[str, dict]:
    sections = build_review_template_sections("response", profile)
    lines = ["# Acceptance Response Template\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, {"length": len(text)}

def save_review_template(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
