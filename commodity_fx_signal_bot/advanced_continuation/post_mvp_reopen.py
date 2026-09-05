from pathlib import Path
from .continuation_config import AdvancedContinuationProfile

def build_post_mvp_reopen_sections(profile: AdvancedContinuationProfile) -> list[dict]:
    return [
        {"title": "Amaç", "content": "Phase 101-160 hazırlığı"},
        {"title": "Phase 1-100 ne sağladı?", "content": "MVP local closing"},
        {"title": "Phase 101 neden gerekli?", "content": "İleri geliştirme hattını güvenle açmak için"},
        {"title": "MVP sonrası ileri geliştirme ilkeleri", "content": "Güvenlik, modülerlik"},
        {"title": "Non-production/local-only sınırları", "content": "Local run only"},
        {"title": "Phase 101-160 hedefi", "content": "Gelişmiş bot"},
        {"title": "Scraping olmadan veri ilkesi", "content": "Scraping no-go"},
        {"title": "Broker/live/advice/deployment dışı kullanım", "content": "Yasaklı hedefler"},
        {"title": "Phase 102 hazırlığı", "content": "Core runtime consolidation"}
    ]

def build_post_mvp_functional_reopen_manifesto(project_root: Path, profile: AdvancedContinuationProfile) -> tuple[str, dict]:
    sections = build_post_mvp_reopen_sections(profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_post_mvp_reopen(text)

def summarize_post_mvp_reopen(text: str) -> dict:
    return {"length": len(text), "status": "continuation_ready"}
