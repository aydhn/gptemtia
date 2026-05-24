with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

new_methods = """
    # Phase 46: Experiment Tracking Text Reports
    def build_hypothesis_registry_text_report(self, summary: dict, hypothesis_df: pd.DataFrame | None = None) -> str:
        report = "=== OFFLINE RESEARCH HYPOTHESIS REGISTRY ===\n"
        report += "Bu çıktı offline experiment tracking raporudur. Canlı emir veya yatırım tavsiyesi değildir.\n\n"
        report += f"Total Hypotheses: {summary.get('total_hypotheses', 0)}\n\n"
        return report

    def build_experiment_tracking_text_report(self, summary: dict, run_df: pd.DataFrame | None = None) -> str:
        report = "=== EXPERIMENT TRACKING REPORT ===\n"
        report += "Bu çıktı offline experiment tracking raporudur. Canlı emir veya yatırım tavsiyesi değildir.\n\n"
        report += f"Notes: {summary.get('notes', '')}\n\n"
        return report

    def build_research_version_text_report(self, summary: dict, version_df: pd.DataFrame | None = None) -> str:
        report = "=== RESEARCH VERSION RECORD ===\n"
        report += "Bu çıktı offline experiment tracking raporudur. Canlı emir veya yatırım tavsiyesi değildir.\n\n"
        report += f"Version info included.\n\n"
        return report

    def build_ablation_study_text_report(self, summary: dict, ablation_df: pd.DataFrame | None = None) -> str:
        report = "=== ABLATION STUDY RESULTS ===\n"
        report += "Bu çıktı offline experiment tracking raporudur. Canlı emir veya yatırım tavsiyesi değildir.\n\n"
        report += f"Total Studies: {summary.get('total_studies', 0)}\n\n"
        return report

    def build_experiment_comparison_text_report(self, summary: dict, comparison_df: pd.DataFrame | None = None) -> str:
        report = "=== EXPERIMENT COMPARISON ===\n"
        report += "Bu çıktı offline experiment tracking raporudur. Canlı emir veya yatırım tavsiyesi değildir.\n\n"
        report += f"Total Comparisons: {summary.get('total_comparisons', 0)}\n\n"
        return report

    def build_experiment_leaderboard_text_report(self, summary: dict, leaderboard_df: pd.DataFrame | None = None) -> str:
        report = "=== EXPERIMENT LEADERBOARD ===\n"
        report += "Bu çıktı offline experiment tracking raporudur. Canlı emir veya yatırım tavsiyesi değildir.\n\n"
        report += f"Total Runs: {summary.get('total_runs', 0)}\n\n"
        return report

    def build_experiment_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        report = "=== EXPERIMENT STATUS ===\n"
        report += "Bu çıktı offline experiment tracking raporudur. Canlı emir veya yatırım tavsiyesi değildir.\n\n"
        report += "Status check complete.\n\n"
        return report

    def build_factor_research_text_report(self, summary: dict, tables: dict[str, pd.DataFrame] | None = None) -> str:
        lines = [
            "*** OFFLINE FACTOR RESEARCH REPORT ***",
            "Bu cikti offline factor research/cross-sectional simulasyon raporudur.",
            "Gercek long-short portfoy, gercek allocation, canli emir, broker talimati, gercek pozisyon veya yatirim tavsiyesi degildir.",
            "---"
        ]

        lines.append(f"Profile: {summary.get('profile', 'Unknown')}")
        lines.append(f"Timeframe: {summary.get('timeframe', 'Unknown')}")
        lines.append(f"Generated: {summary.get('timestamp', 'Unknown')}")

        coverage = summary.get("universe_coverage", {})
        lines.append(f"Valid Symbols: {coverage.get('valid_symbols', 0)}")
        lines.append("---")

        if tables and "composite_ranking" in tables and not tables["composite_ranking"].empty:
            lines.append("Composite Factor Ranking (Top 5):")
            top5 = tables["composite_ranking"].head(5)
            for _, row in top5.iterrows():
                lines.append(f"- {row['symbol']}: {row.get('composite_factor_score', 0.0):.4f}")
            lines.append("---")

        if tables and "backtest_results" in tables and not tables["backtest_results"].empty:
            lines.append("Factor Virtual Spreads (Top vs Bottom):")
            for _, row in tables["backtest_results"].head(5).iterrows():
                lines.append(f"- {row['factor_id']}: {row.get('spread_return', 0.0):.4f}")
            lines.append("---")

        return "\\n".join(lines)

    def build_factor_score_text_report(self, summary: dict, score_df: pd.DataFrame | None = None, rank_df: pd.DataFrame | None = None) -> str:
        return "Offline Factor Score Report\\nGercek emir veya tavsiye degildir."

    def build_factor_backtest_text_report(self, summary: dict, backtest_df: pd.DataFrame | None = None, ic_df: pd.DataFrame | None = None) -> str:
        return "Offline Factor Backtest Report\\nGercek performans garantisi degildir."

    def build_factor_exposure_text_report(self, summary: dict, exposure_df: pd.DataFrame | None = None) -> str:
         return "Offline Factor Exposure Report\\nGercek portfoy degildir."

    def build_factor_neutral_text_report(self, summary: dict, neutral_df: pd.DataFrame | None = None) -> str:
         return "Offline Factor Neutral Report\\nGercek portfoy degildir."

    def build_factor_research_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
         return f"Factor Research Status: {len(status_df)} reports found."
"""

# The script tests indicated that ReportBuilder class was missing these functions.
# They were incorrectly placed at module level. Let's fix that.
# Find class ReportBuilder and append inside it.

import re

# Remove the incorrectly indented functions at the end of the file
content = re.sub(r'    # --- Phase 44: Factor Research Text Reports ---.*$', '', content, flags=re.DOTALL)

# Insert the new methods into ReportBuilder class
# Find the class definition and the last method before the end of the file
# We will just append before the module level functions
class_def = "class ReportBuilder:"
last_method = "    def build_security_audits_text_report(self,"

content = content.replace(last_method, new_methods + "\n" + last_method)

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
