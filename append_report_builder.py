import re

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

methods = """
    def build_level_candidate_preview_report(self, symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame) -> str:
        report = []
        report.append(f"Level Candidate Preview: {symbol} - {timeframe} (Profile: {profile_name})")
        report.append("=" * 80)
        report.append("UYARI: Bu çıktılar teorik stop/target seviye simülasyon adaylarıdır. Stop/target/invalidation ifadeleri gerçek stop-loss, take-profit, emir, pozisyon kapatma/açma veya canlı işlem kararı değildir. Canlı emir üretilmez.")
        report.append("-" * 80)
        report.append(f"Missing Context: {summary.get('missing_context_frames', [])}")
        report.append(f"Total Candidates: {summary.get('total_level_candidates', 0)}")
        report.append("-" * 80)
        if tail_df.empty:
            report.append("No candidates available.")
        else:
            cols_to_show = ["level_label", "theoretical_stop_level", "theoretical_target_level", "reward_risk"]
            existing_cols = [c for c in cols_to_show if c in tail_df.columns]
            report.append(tail_df[existing_cols].to_string())
        return "\\n".join(report)

    def build_reward_risk_preview_report(self, symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame) -> str:
        report = []
        report.append(f"Reward/Risk Preview: {symbol} - {timeframe} (Profile: {profile_name})")
        report.append("=" * 80)
        report.append("UYARI: Bu çıktılar teorik stop/target seviye simülasyon adaylarıdır. Stop/target/invalidation ifadeleri gerçek stop-loss, take-profit, emir, pozisyon kapatma/açma veya canlı işlem kararı değildir. Canlı emir üretilmez.")
        report.append("-" * 80)
        report.append(f"Average Reward/Risk: {summary.get('average_reward_risk', 0.0):.2f}")
        report.append("-" * 80)
        if tail_df.empty:
            report.append("No candidates available.")
        else:
            cols_to_show = ["level_label", "reward_risk", "block_reasons"]
            existing_cols = [c for c in cols_to_show if c in tail_df.columns]
            report.append(tail_df[existing_cols].to_string())
        return "\\n".join(report)

    def build_level_batch_report(self, summary: dict) -> str:
        report = []
        report.append("Level Batch Report")
        report.append("=" * 80)
        report.append("UYARI: Bu çıktılar teorik stop/target seviye simülasyon adaylarıdır. Stop/target/invalidation ifadeleri gerçek stop-loss, take-profit, emir, pozisyon kapatma/açma veya canlı işlem kararı değildir. Canlı emir üretilmez.")
        report.append("-" * 80)
        report.append(f"Profile: {summary.get('profile')}")
        report.append(f"Processed Symbols: {summary.get('processed_symbols')}")
        report.append(f"Generated Rows: {summary.get('generated_rows')}")
        return "\\n".join(report)

    def build_level_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        report = []
        report.append("Level Status Report")
        report.append("=" * 80)
        report.append("UYARI: Bu çıktılar teorik stop/target seviye simülasyon adaylarıdır. Stop/target/invalidation ifadeleri gerçek stop-loss, take-profit, emir, pozisyon kapatma/açma veya canlı işlem kararı değildir. Canlı emir üretilmez.")
        report.append("-" * 80)
        if status_df.empty:
            report.append("No level data found.")
        else:
            report.append(status_df.to_string())
        return "\\n".join(report)
"""

content += "\n" + methods

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)

