from pathlib import Path
import pandas as pd
from .ux_config import AnalystUXProfile

def build_command_cheat_sheet(aliases_df: pd.DataFrame, profile: AnalystUXProfile) -> str:
    lines = ["# Command Cheat Sheet", ""]
    lines.append("Disclaimer: Cheat sheet canlı trade komutu içermez. AL/SAT örnekleri yok.")
    if aliases_df is not None and not aliases_df.empty:
        for _, row in aliases_df.iterrows():
            lines.append(f"- **{row['alias_name']}**: `{row['command']}` ({row['description']})")
    return "\n".join(lines)

def build_safe_query_examples(profile: AnalystUXProfile) -> str:
    return """# Safe Query Examples

- final review durumunu kontrol et
- scenario regression raporu üret
- quality gate hatalarını görmek istiyorum
- sistemin performans durumu nedir
- bakım adaylarını listele

Disclaimer: Yatırım tavsiyesi üretmeyen sorular olmalıdır.
"""

def build_module_quick_reference(profile: AnalystUXProfile) -> str:
    return """# Module Quick Reference

- **final_review**: Final checks and audits.
- **scenarios**: Synthetic scenarios.
- **quality_gates**: CI validation.
- **maintenance**: Data retention.
"""

def build_operator_shortcuts_reference(shortcuts_df: pd.DataFrame, profile: AnalystUXProfile) -> str:
    lines = ["# Operator Shortcuts Reference", ""]
    if shortcuts_df is not None and not shortcuts_df.empty:
        for _, row in shortcuts_df.iterrows():
            lines.append(f"- **{row['name']}**: {row['purpose']}")
    return "\n".join(lines)

def save_cheat_sheets(output_dir: Path, cheat_sheets: dict[str, str]) -> tuple[pd.DataFrame, dict]:
    records = []
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, content in cheat_sheets.items():
        file_path = output_dir / f"{name}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        records.append({"file": f"{name}.md", "length": len(content)})

    df = pd.DataFrame(records)
    return df, {"files_saved": len(records)}
