import pandas as pd
from synthetic_indices.index_config import SyntheticIndexProfile

def build_synthetic_index_disclaimer() -> str:
    return (
        "DİKKAT: Bu rapor/çıktı offline sentetik benchmark/custom index/relative strength "
        "araştırması çıktısıdır; gerçek endeks ürünü, gerçek portföy yönetimi, canlı emir, "
        "broker talimatı, kesin pozisyon yönlendirmesi veya yatırım tavsiyesi DEĞİLDİR. "
        "Buradaki 'leader', 'laggard', 'rotation candidate' gibi ifadeler tamamen araştırma "
        "bağlamındadır ve al/sat sinyali taşımaz."
    )

def build_synthetic_benchmark_markdown_report(summary: dict, tables: dict[str, pd.DataFrame], profile: SyntheticIndexProfile) -> str:
    lines = []
    lines.append("# Synthetic Benchmark Research Report")
    lines.append(f"**Profile:** {profile.name}")
    lines.append(f"**Description:** {profile.description}")
    lines.append("")
    lines.append("## Disclaimer")
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    lines.append("## Summary")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"- **{k}**: {v}")

    if summary.get("warnings"):
        lines.append("")
        lines.append("## Warnings")
        for w in summary["warnings"]:
            lines.append(f"- {w}")

    for table_name, df in tables.items():
         if not df.empty:
              lines.append("")
              lines.append(f"## {table_name}")
              lines.append(df.to_markdown(index=False))

    return "\n".join(lines)

def build_composite_index_markdown_report(summary: dict, performance_df: pd.DataFrame, profile: SyntheticIndexProfile) -> str:
    lines = []
    lines.append("# Composite Index Performance Report")
    lines.append(f"**Profile:** {profile.name}")
    lines.append("")
    lines.append("## Disclaimer")
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    lines.append("## Summary")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"- **{k}**: {v}")

    if not performance_df.empty:
         lines.append("")
         lines.append("## Performance Metrics")
         lines.append(performance_df.to_markdown(index=False))

    return "\n".join(lines)

def build_relative_strength_markdown_report(summary: dict, rs_df: pd.DataFrame, profile: SyntheticIndexProfile) -> str:
    lines = []
    lines.append("# Relative Strength Research Report")
    lines.append(f"**Profile:** {profile.name}")
    lines.append("")
    lines.append("## Disclaimer")
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")

    if not rs_df.empty:
         lines.append("## Relative Strength Rankings")
         lines.append(rs_df.to_markdown(index=False))

    return "\n".join(lines)

def build_universe_rotation_markdown_report(summary: dict, rotation_df: pd.DataFrame, profile: SyntheticIndexProfile) -> str:
    lines = []
    lines.append("# Universe Rotation Research Report")
    lines.append(f"**Profile:** {profile.name}")
    lines.append("")
    lines.append("## Disclaimer")
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    lines.append("## Stability Summary")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"- **{k}**: {v}")

    if not rotation_df.empty:
         lines.append("")
         lines.append("## Rotation Rankings")
         lines.append(rotation_df.to_markdown(index=False))

    return "\n".join(lines)

def build_leadership_laggard_markdown_report(summary: dict, leader_laggard_df: pd.DataFrame, profile: SyntheticIndexProfile) -> str:
    lines = []
    lines.append("# Cross-Asset Leadership and Laggard Report")
    lines.append(f"**Profile:** {profile.name}")
    lines.append("")
    lines.append("## Disclaimer")
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    lines.append("## Summary")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"- **{k}**: {v}")

    if not leader_laggard_df.empty:
         lines.append("")
         lines.append("## Leader/Laggard Groups")
         lines.append(leader_laggard_df.to_markdown(index=False))

    return "\n".join(lines)
