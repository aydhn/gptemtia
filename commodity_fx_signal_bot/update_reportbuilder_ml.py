import os

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

ml_methods = """
    def build_ml_training_preview_report(self, symbol: str, timeframe: str, profile_name: str, summary: dict) -> str:
        lines = [
            "=== ML TRAINING PREVIEW ===",
            f"Sembol: {symbol}",
            f"Zaman Dilimi: {timeframe}",
            f"Profil: {profile_name}",
            "",
            "Uyarı: Bu çıktı offline ML eğitim raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
            "",
            "Model Bilgileri:",
            f"  Model ID: {summary.get('model_id')}",
            f"  Model Family: {summary.get('model_family')}",
            f"  Task Type: {summary.get('task_type')}",
            f"  Target: {summary.get('target_column')}",
            f"  Feature Count: {summary.get('feature_count')}",
            f"  Train Rows: {summary.get('train_rows')}",
            f"  Test Rows: {summary.get('test_rows')}",
            "",
            "Metrics:",
        ]

        metrics = summary.get('metrics', {})
        for k, v in metrics.items():
            if isinstance(v, float):
                lines.append(f"  {k}: {v:.4f}")
            else:
                lines.append(f"  {k}: {v}")

        lines.append("")
        lines.append("Quality Status:")
        quality = summary.get('quality_report', {})
        lines.append(f"  Passed: {quality.get('passed', False)}")

        if quality.get('warnings'):
            lines.append("  Warnings:")
            for w in quality['warnings']:
                lines.append(f"    - {w}")

        lines.append("")
        lines.append(f"Registry Status: {summary.get('registry_entry', {}).get('registry_status', 'unknown')}")

        return "\n".join(lines)

    def build_ml_model_evaluation_preview_report(self, symbol: str, timeframe: str, profile_name: str, summary: dict) -> str:
        lines = [
            "=== ML MODEL EVALUATION PREVIEW ===",
            f"Sembol: {symbol}",
            f"Zaman Dilimi: {timeframe}",
            f"Profil: {profile_name}",
            "",
            "Uyarı: Bu çıktı offline ML değerlendirme raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
            "",
        ]

        for k, v in summary.items():
            if k == "confusion_matrix" and isinstance(v, dict):
                lines.append("Confusion Matrix:")
                for k2, v2 in v.items():
                    lines.append(f"  {k2}: {v2}")
            elif k == "classification_report" and isinstance(v, dict):
                lines.append("Classification Report (subset):")
                lines.append(f"  Accuracy: {v.get('accuracy', 'N/A')}")
            else:
                if isinstance(v, float):
                    lines.append(f"{k}: {v:.4f}")
                else:
                    lines.append(f"{k}: {v}")

        return "\n".join(lines)

    def build_ml_training_batch_report(self, summary: dict, ranking_df: pd.DataFrame | None = None) -> str:
        lines = [
            "=== ML BATCH TRAINING SUMMARY ===",
            f"Total Processed: {summary.get('processed', 0)}",
            "",
            "Uyarı: Bu çıktı offline ML eğitim raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
            "",
        ]

        if ranking_df is not None and not ranking_df.empty:
            lines.append("Top Models:")
            lines.append(ranking_df.to_string())

        return "\n".join(lines)

    def build_ml_model_registry_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        lines = [
            "=== ML MODEL REGISTRY STATUS ===",
            f"Total Registered Models: {len(status_df) if not status_df.empty else 0}",
            "",
            "Uyarı: Bu çıktı offline model registry raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
            "",
        ]

        if not status_df.empty:
            cols = ['model_id', 'symbol', 'timeframe', 'model_family', 'registry_status']
            exist_cols = [c for c in cols if c in status_df.columns]
            if exist_cols:
                lines.append(status_df[exist_cols].to_string())

        return "\n".join(lines)

    def build_ml_model_artifact_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        lines = [
            "=== ML MODEL ARTIFACT STATUS ===",
            f"Total Models Checked: {len(status_df) if not status_df.empty else 0}",
            "",
            "Uyarı: Bu çıktı offline model artifact raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
            "",
        ]

        if not status_df.empty:
            lines.append(status_df.to_string())

        return "\n".join(lines)
"""

if "def build_ml_training_preview_report" not in content:
    content += ml_methods
    with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
        f.write(content)
    print("Added ML model methods to ReportBuilder")
