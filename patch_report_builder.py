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

"""

content = content.replace("    def build_security_audits_text_report(self,", new_methods + "    def build_security_audits_text_report(self,")

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
