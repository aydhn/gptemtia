with open("commodity_fx_signal_bot/reports/report_builder.py", "a") as f:
    f.write("""
def build_sizing_candidate_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        f"--- TEORİK SIZING CANDIDATE PREVIEW ---",
        f"Symbol: {symbol}",
        f"Timeframe: {timeframe}",
        f"Profile: {profile_name}",
        f"Loaded Risk Candidates: {summary.get('loaded_risk_candidates', 0)}",
        f"Sizing Candidates Produced: {summary.get('sizing_candidate_count', 0)}",
        f"Passed: {summary.get('passed_sizing_candidate_count', 0)}",
        f"Rejected: {summary.get('rejected_sizing_candidate_count', 0)}",
        f"Watchlist: {summary.get('watchlist_sizing_candidate_count', 0)}",
        ""
    ]
    if summary.get("warnings"):
        lines.append("Uyarılar:")
        for w in summary["warnings"]:
            lines.append(f" - {w}")
        lines.append("")

    lines.append("UYARI: Bu çıktılar teorik pozisyon boyutu simülasyon adaylarıdır. Gerçek lot/adet/kontrat, emir, pozisyon talimatı, kaldıraç veya canlı işlem kararı değildir. Canlı emir üretilmez.")
    lines.append("")

    if not tail_df.empty:
        lines.append("Son Sizing Adayları:")
        for idx, row in tail_df.iterrows():
            lines.append(
                f"[{idx}] Label: {row.get('sizing_label')} | Risk: {row.get('theoretical_risk_amount')} | "
                f"Adj Units: {row.get('adjusted_theoretical_units')} | Adj Notional: {row.get('adjusted_theoretical_notional')}"
            )
            if row.get('block_reasons'):
                lines.append(f"  Block Reasons: {row.get('block_reasons')}")
            if row.get('watchlist_reasons'):
                lines.append(f"  Watchlist Reasons: {row.get('watchlist_reasons')}")

    return "\\n".join(lines)

def build_sizing_batch_report(summary: dict) -> str:
    lines = [
        "--- TEORİK SIZING BATCH SUMMARY ---",
        f"Processed Symbols: {summary.get('processed_symbols', 0)}",
        f"Failed Symbols: {summary.get('failed_symbols', 0)}",
        f"Total Candidates in Pool: {summary.get('total_candidates', 0)}",
        ""
    ]
    pool_summary = summary.get("summary", {})
    if pool_summary:
        lines.append(f"Passed: {pool_summary.get('passed_sizing_candidates', 0)}")
        lines.append(f"Rejected: {pool_summary.get('rejected_sizing_candidates', 0)}")
        lines.append(f"Watchlist: {pool_summary.get('watchlist_sizing_candidates', 0)}")
        lines.append(f"Avg Readiness: {pool_summary.get('average_sizing_readiness', 0.0):.2f}")

    lines.append("")
    lines.append("UYARI: Bu çıktılar teorik pozisyon boyutu simülasyon adaylarıdır. Gerçek lot/adet/kontrat, emir, pozisyon talimatı, kaldıraç veya canlı işlem kararı değildir. Canlı emir üretilmez.")
    return "\\n".join(lines)

def build_sizing_pool_preview_report(
    timeframe: str, profile_name: str, summary: dict, top_df: pd.DataFrame
) -> str:
    lines = [
        "--- TEORİK SIZING POOL PREVIEW ---",
        f"Timeframe: {timeframe}",
        f"Profile: {profile_name}",
        f"Total Candidates: {summary.get('total_sizing_candidates', 0)}",
        f"Passed: {summary.get('passed_sizing_candidates', 0)}",
        f"Rejected: {summary.get('rejected_sizing_candidates', 0)}",
        f"Watchlist: {summary.get('watchlist_sizing_candidates', 0)}",
        f"Avg Readiness: {summary.get('average_sizing_readiness', 0.0):.2f}",
        ""
    ]
    lines.append("UYARI: Bu çıktılar teorik pozisyon boyutu simülasyon adaylarıdır. Gerçek lot/adet/kontrat, emir, pozisyon talimatı, kaldıraç veya canlı işlem kararı değildir. Canlı emir üretilmez.")
    lines.append("")

    if not top_df.empty:
        lines.append("En Yüksek Puanlı Sizing Adayları:")
        for _, row in top_df.iterrows():
            lines.append(
                f"{row.get('symbol')} | Label: {row.get('sizing_label')} | "
                f"Method: {row.get('sizing_method')} | Risk: {row.get('theoretical_risk_amount')} | "
                f"Readiness: {row.get('sizing_readiness_score', 0.0):.2f} | "
                f"Adj Notional: {row.get('adjusted_theoretical_notional')}"
            )

    return "\\n".join(lines)

def build_sizing_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "--- TEORİK SIZING STATUS ---",
        f"Total Sizing Pools: {summary.get('total_pools', 0)}",
        f"Total Individual Candidates: {summary.get('total_candidates', 0)}",
        ""
    ]
    lines.append("UYARI: Bu çıktılar teorik pozisyon boyutu simülasyon adaylarıdır. Gerçek lot/adet/kontrat, emir, pozisyon talimatı, kaldıraç veya canlı işlem kararı değildir. Canlı emir üretilmez.")
    return "\\n".join(lines)
""")
