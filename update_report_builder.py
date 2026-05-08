import re

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

rb_methods = """
    def build_ml_dataset_preview_report(
        self,
        symbol: str,
        timeframe: str,
        profile_name: str,
        summary: dict,
        tail_df: pd.DataFrame | None = None
    ) -> str:
        lines = [
            f"=== ML DATASET PREVIEW: {symbol} ({timeframe}) ===",
            f"Profile: {profile_name}",
            f"Dataset ID: {summary.get('dataset_id', 'N/A')}",
            f"Row Count: {summary.get('row_count', 0)}",
            f"Feature Count: {summary.get('feature_count', 0)}",
            f"Target Count: {summary.get('target_count', 0)}",
            "",
            "--- Quality ---",
            f"Quality Passed: {summary.get('quality_report', {}).get('passed', False)}",
            f"Feature NaN Ratio: {summary.get('quality_report', {}).get('feature_nan_ratio', 0.0):.2f}",
            f"Target NaN Ratio: {summary.get('quality_report', {}).get('target_nan_ratio', 0.0):.2f}",
            "",
            "--- Leakage Audit ---",
            f"Audit Passed: {summary.get('leakage_audit', {}).get('passed', False)}",
            f"Risk Score: {summary.get('leakage_audit', {}).get('leakage_risk_score', 0)}",
            "",
            "--- Missing Feature Sets ---",
            str(summary.get('missing_feature_sets', [])),
            "",
            "--- Warnings ---"
        ]

        warnings = summary.get("warnings", [])
        if warnings:
             for w in warnings:
                  lines.append(f"- {w}")
        else:
             lines.append("- Yok")

        lines.append("")
        lines.append("Uyarı: Bu çıktı ML dataset hazırlık raporudur. Model eğitimi, tahmin, canlı sinyal, gerçek emir veya yatırım tavsiyesi değildir.")

        if tail_df is not None and not tail_df.empty:
            lines.append("")
            lines.append("--- Tail Data ---")
            lines.append(tail_df.to_string())

        return "\\n".join(lines)

    def build_ml_target_preview_report(
        self,
        symbol: str,
        timeframe: str,
        profile_name: str,
        summary: dict,
        target_tail_df: pd.DataFrame | None = None
    ) -> str:
        lines = [
            f"=== ML TARGET PREVIEW: {symbol} ({timeframe}) ===",
            f"Profile: {profile_name}",
            ""
        ]

        warnings = summary.get("warnings", [])
        if warnings:
             lines.append("--- Warnings ---")
             for w in warnings:
                  lines.append(f"- {w}")
             lines.append("")

        lines.append("Uyarı: Bu çıktı ML dataset hazırlık raporudur. Model eğitimi, tahmin, canlı sinyal, gerçek emir veya yatırım tavsiyesi değildir.")
        lines.append("")

        if target_tail_df is not None and not target_tail_df.empty:
            lines.append("--- Target Data Tail ---")
            lines.append(target_tail_df.to_string())

        return "\\n".join(lines)

    def build_ml_dataset_batch_report(self, summary: dict, ranking_df: pd.DataFrame | None = None) -> str:
        lines = [
            "=== ML DATASET BATCH BUILD SUMMARY ===",
            f"Total Processed: {summary.get('processed', 0)}",
            "",
            "Uyarı: Bu çıktı ML dataset hazırlık raporudur. Model eğitimi, tahmin, canlı sinyal, gerçek emir veya yatırım tavsiyesi değildir.",
            ""
        ]

        if ranking_df is not None and not ranking_df.empty:
             lines.append("--- Dataset Ranking ---")
             lines.append(ranking_df.to_string(index=False))

        return "\\n".join(lines)

    def build_ml_dataset_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        lines = [
            "=== ML DATASET STATUS ===",
            f"Total Datasets: {len(status_df) if not status_df.empty else 0}",
            "",
            "Uyarı: Bu çıktı ML dataset hazırlık raporudur. Model eğitimi, tahmin, canlı sinyal, gerçek emir veya yatırım tavsiyesi değildir.",
            ""
        ]

        if not status_df.empty:
            lines.append("--- Current Datasets ---")
            display_cols = ["symbol", "timeframe", "profile", "row_count", "feature_count", "target_count", "quality_passed", "leakage_audit_passed"]
            avail_cols = [c for c in display_cols if c in status_df.columns]
            if avail_cols:
                 lines.append(status_df[avail_cols].to_string(index=False))
            else:
                 lines.append(status_df.to_string(index=False))

        return "\\n".join(lines)
"""

lines = content.split('\n')
for i in reversed(range(len(lines))):
    if lines[i].strip() != "":
         break

content = "\n".join(lines[:i+1]) + "\n" + rb_methods + "\n"

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
