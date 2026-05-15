import pandas as pd
from datetime import datetime, timezone

def build_header(title: str, severity: str = "info") -> str:
    icons = {
        "info": "ℹ️",
        "warning": "⚠️",
        "error": "❌",
        "critical": "🚨",
        "unknown": "❓"
    }
    icon = icons.get(severity, icons["unknown"])
    return f"<b>{icon} {title}</b>\n"

def build_disclaimer() -> str:
    return "\n<i>* Bu mesaj raporlama/simülasyon amaçlıdır; gerçek emir, canlı sinyal veya yatırım tavsiyesi değildir.</i>"

def build_section(title: str, lines: list[str]) -> str:
    if not lines:
        return ""
    section_text = f"\n<b>{title}</b>\n"
    section_text += "\n".join(lines)
    return section_text + "\n"

def build_key_value_lines(data: dict, max_items: int = 20) -> list[str]:
    lines = []
    count = 0
    for k, v in data.items():
        if count >= max_items:
            lines.append("... (Daha fazlası sınırlandırıldı)")
            break
        lines.append(f"• <b>{k}:</b> {v}")
        count += 1
    return lines

def build_table_like_lines(df: pd.DataFrame, columns: list[str], max_rows: int = 10) -> list[str]:
    if df is None or df.empty:
        return ["Kayıt bulunamadı."]

    lines = []
    available_cols = [c for c in columns if c in df.columns]

    if not available_cols:
        return ["İstenen kolonlar veride yok."]

    # Header
    header = " | ".join(available_cols)
    lines.append(f"<code>{header}</code>")
    lines.append("<code>" + "-" * len(header) + "</code>")

    # Rows
    for i, row in df.head(max_rows).iterrows():
        row_str = " | ".join(str(row[col]) for col in available_cols)
        lines.append(f"<code>{row_str}</code>")

    if len(df) > max_rows:
        lines.append(f"<i>... (+{len(df) - max_rows} satır)</i>")

    return lines

def build_footer(timestamp_utc: str | None = None) -> str:
    if not timestamp_utc:
        timestamp_utc = datetime.now(timezone.utc).isoformat()
    return f"\nZaman (UTC): <code>{timestamp_utc}</code>\n"
