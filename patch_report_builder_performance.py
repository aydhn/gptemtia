def patch_report_builder():
    path = "commodity_fx_signal_bot/reports/report_builder.py"
    with open(path, "r") as f:
        content = f.read()

    new_methods = """
    def build_performance_profile_text_report(self, summary: dict, runtime_df: pd.DataFrame | None = None, memory_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_performance_profile_markdown_report
        return build_performance_profile_markdown_report(summary, runtime_df, memory_df)

    def build_resource_budget_text_report(self, summary: dict, budget_df: pd.DataFrame | None = None, violation_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_resource_budget_markdown_report
        return build_resource_budget_markdown_report(summary, budget_df, violation_df)

    def build_cache_strategy_text_report(self, summary: dict, cache_df: pd.DataFrame | None = None, policy_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_cache_strategy_markdown_report
        return build_cache_strategy_markdown_report(summary, cache_df, policy_df)

    def build_large_run_stability_text_report(self, summary: dict, stability_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_large_run_stability_markdown_report
        return build_large_run_stability_markdown_report(summary, stability_df)

    def build_runtime_optimization_text_report(self, summary: dict, recommendation_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_runtime_optimization_markdown_report
        return build_runtime_optimization_markdown_report(summary, recommendation_df)

    def build_performance_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        from performance.performance_report_builder import build_performance_disclaimer
        txt = "Performance Status Report\\n"
        txt += build_performance_disclaimer()
        for k, v in summary.items():
            txt += f"{k}: {v}\\n"
        txt += "\\nReports:\\n"
        if not status_df.empty:
            txt += status_df.to_string(index=False)
        return txt
"""

    if "def build_performance_profile_text_report" not in content:
        # Append before the last class or at the end
        content += new_methods
        with open(path, "w") as f:
            f.write(content)

patch_report_builder()
