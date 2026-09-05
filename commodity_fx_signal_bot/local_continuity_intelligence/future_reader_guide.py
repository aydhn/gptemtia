from pathlib import Path
def build_future_reader_guide(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_future_reader_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_future_reader_guide(text)
def build_future_reader_sections(profile) -> list[dict]:
    return [
        {"title": "Gelecekte bu projeyi okuyan kişi nereden başlamalı?", "content": "Start here."},
        {"title": "Bu sistem ne yapar?", "content": "Does stuff."},
        {"title": "Bu sistem ne yapmaz?", "content": "Does not deploy. No live trading."},
        {"title": "İlk saat planı", "content": "Read this."},
        {"title": "İlk gün planı", "content": "Read that."},
        {"title": "İlk hafta planı", "content": "Read more."},
        {"title": "Hangi raporlar önce okunmalı?", "content": "Reports."},
        {"title": "Hangi komutlar sadece rapor üretir?", "content": "Commands."},
        {"title": "Hangi sınırlar kesinlikle korunmalı?", "content": "Boundaries."},
        {"title": "Hangi çıktılar official approval değildir?", "content": "These."},
        {"title": "Manual review noktaları", "content": "Review here."}
    ]
def summarize_future_reader_guide(text: str) -> dict:
    return {"length": len(text)}