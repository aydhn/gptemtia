import pandas as pd
from pathlib import Path
from .usability_config import LocalUsabilityProfile

def build_navigation_assistant_sections(doc_nav_df: pd.DataFrame, report_order_df: pd.DataFrame, command_index_df: pd.DataFrame) -> list[dict]:
    return [
        {"title": "Uyarı", "content": "Bu rapor offline/local usability review ve operator ergonomics rehearsal çıktısıdır; gerçek kullanıcı testi, telemetry, production usability approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."},
        {"title": "Başlangıç", "content": "README.md okuyun."},
        {"title": "En önemli belgeler", "content": "ARCHITECTURE.md"},
        {"title": "Komut aileleri", "content": "scripts/"},
        {"title": "Hangi rapor ne işe yarar?", "content": "reports/"},
        {"title": "Hangi DataLake klasörü ne işe yarar?", "content": "data/lake/"},
        {"title": "Generated docs nasıl okunur?", "content": "docs/generated/"},
        {"title": "Status vs quality vs registry çıktıları", "content": "Hepsi farklı amaca hizmet eder."},
        {"title": "No-go/safe-go nerede bulunur?", "content": "reports/output/"},
        {"title": "İnsan onayı gerektiren noktalar", "content": "Her şey."},
        {"title": "Hızlı yol / detaylı yol", "content": "Hızlı yol first_hour, detaylı yol weekly."},
        {"title": "Sınırlar", "content": "Gerçek LLM assistant değildir."}
    ]

def build_documentation_navigation_assistant_pack(doc_nav_df: pd.DataFrame, report_order_df: pd.DataFrame, command_index_df: pd.DataFrame, profile: LocalUsabilityProfile) -> tuple[str, dict]:
    sections = build_navigation_assistant_sections(doc_nav_df, report_order_df, command_index_df)
    text = "\n\n".join(f"## {s['title']}\n{s['content']}" for s in sections)
    return text, {"sections": len(sections)}

def save_documentation_navigation_assistant_pack(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_documentation_navigation_assistant_pack(text: str) -> dict:
    return {"length": len(text)}
