with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

new_functions = """
def build_synthetic_benchmark_text_report(summary: dict, definitions_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["SYNTHETIC BENCHMARK REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"{k}: {v}")
    if definitions_df is not None and not definitions_df.empty:
        lines.append("")
        lines.append(definitions_df.to_string())
    return "\n".join(lines)

def build_composite_index_text_report(summary: dict, performance_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["COMPOSITE INDEX PERFORMANCE REPORT", "=" * 40, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"{k}: {v}")
    if performance_df is not None and not performance_df.empty:
        lines.append("")
        lines.append(performance_df.to_string())
    return "\n".join(lines)

def build_relative_strength_text_report(summary: dict, rs_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["RELATIVE STRENGTH REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    if rs_df is not None and not rs_df.empty:
        lines.append(rs_df.to_string())
    return "\n".join(lines)

def build_universe_rotation_text_report(summary: dict, rotation_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["UNIVERSE ROTATION REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"{k}: {v}")
    if rotation_df is not None and not rotation_df.empty:
        lines.append("")
        lines.append(rotation_df.to_string())
    return "\n".join(lines)

def build_leadership_laggard_text_report(summary: dict, leader_laggard_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["LEADERSHIP AND LAGGARD REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"{k}: {v}")
    if leader_laggard_df is not None and not leader_laggard_df.empty:
        lines.append("")
        lines.append(leader_laggard_df.to_string())
    return "\n".join(lines)

def build_synthetic_index_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["SYNTHETIC INDEX STATUS REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if not status_df.empty:
        lines.append("")
        lines.append(status_df.to_string())
    return "\n".join(lines)
"""

with open("commodity_fx_signal_bot/reports/report_builder.py", "a") as f:
    f.write("\n" + new_functions + "\n")
