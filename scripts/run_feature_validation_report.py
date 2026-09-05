import sys
import pandas as pd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_validation.feature_validation_pipeline import run_feature_validation_pipeline
from advanced_feature_validation.feature_validation_report_builder import (
    build_feature_validation_report,
    build_feature_validation_markdown_report,
    build_feature_validation_text_summary,
)


def main():
    settings = get_settings()
    data_lake = DataLake()

    # Create dummy dataframe to test full pipeline reporting
    sample_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=10, freq="D"),
        "asset_symbol": ["BRENT"] * 10,
        "indicator_rsi_14": [50.0, 52.1, 48.9, 53.4, 55.0, 56.1, 54.8, 57.2, 58.0, 56.5],
        "grid_ret_5d": [0.01, -0.02, 0.005, 0.012, -0.004, 0.008, -0.001, 0.015, -0.003, 0.002],
    })

    pipeline_result = run_feature_validation_pipeline(sample_df, profile_name="default")
    report = build_feature_validation_report(pipeline_result, profile_name="default")
    markdown = build_feature_validation_markdown_report(report)
    text_summary = build_feature_validation_text_summary(report)

    data_lake.save_feature_validation_report("default", report, markdown=markdown)
    data_lake.save_feature_validation_report_markdown(markdown)
    data_lake.save_feature_validation_report_text(text_summary)

    print("=" * 70)
    print("PHASE 121: FEATURE VALIDATION REPORT GENERATION")
    print("=" * 70)
    print(f"Overall Quality Score : {report['scores']['overall_score']:.4f}")
    print(f"Lookahead Score       : {report['scores']['lookahead_score']:.4f}")
    print(f"Integrity Score       : {report['scores']['integrity_score']:.4f}")
    print(f"Validation Status     : {report['status']}")
    print(f"Reports Written       : JSON, MD, TXT to reports/output/advanced_feature_validation/")
    print("=" * 70)


if __name__ == "__main__":
    main()
