from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_efficiency_planning_sections(profile: LocalPerformanceProfile) -> list[dict]:
    return [
        {"title": "Local-only efficiency principle", "content": "Hepsi offline manuel inceleme icindir."},
        {"title": "When to use lightweight mode", "content": "Kisa ve hizli incelemeler."},
        {"title": "How to reduce output review burden manually", "content": "Sadece hata icerenleri incele."},
        {"title": "How to prioritize quality/status scripts", "content": "Once bunlari calistir."},
        {"title": "How to avoid heavy reruns", "content": "Tekrar tekrar calistirmaktan kacin."},
        {"title": "How to read growth estimates", "content": "Manual rotasyon planla."},
        {"title": "How to handle retention manually", "content": "Kendin sil/arsivle."},
        {"title": "What not to do", "content": "Gercek yatirim karari alma. Otomatik silme yapma."}
    ]

def build_offline_efficiency_planning_guide(project_root: Path, profile: LocalPerformanceProfile) -> tuple[str, dict]:
    sections = build_efficiency_planning_sections(profile)
    text = "# Offline Efficiency Planning Guide\n"
    for s in sections:
        text += f"\n## {s['title']}\n{s['content']}\n"
    return text, summarize_efficiency_planning_guide(text)

def summarize_efficiency_planning_guide(text: str) -> dict: return {"length": len(text)}
