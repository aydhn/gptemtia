import argparse
import sys
import logging
from config.settings import settings
from config.paths import ProjectPaths
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from ml.training_config import get_ml_training_profile
from ml.training_pipeline import MLTrainingPipeline
import reports.report_builder as report_builder

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    parser = argparse.ArgumentParser(description="ML Model Evaluation Preview")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to evaluate")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_baseline_training", help="Training profile name")
    parser.add_argument("--model-id", type=str, default=None, help="Specific model_id to evaluate (not fully implemented in preview)")
    parser.add_argument("--save", action="store_true", help="Save report")

    args = parser.parse_args()

    spec = get_symbol_spec(args.symbol)
    if not spec:
        print(f"Symbol {args.symbol} not found in configuration.")
        sys.exit(1)

    try:
        profile = get_ml_training_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile {args.profile}: {e}")
        sys.exit(1)

    paths = ProjectPaths()
    data_lake = DataLake(paths)

    pipeline = MLTrainingPipeline(data_lake, settings, profile)

    # In a real evaluation we would load the saved model.
    # For preview without guaranteed saved model, we just run training pipeline with save=False
    # and print the evaluation part of the summary.
    summary, res = pipeline.train_for_symbol_timeframe(
        spec=spec,
        timeframe=args.timeframe,
        profile=profile,
        model_family=None,
        save=False
    )

    if not summary or "metrics" not in summary:
        print("Evaluation failed or was skipped.")
        if res.get("warnings"):
            for w in res["warnings"]:
                print(f"Warning: {w}")
        sys.exit(1)

    report = report_builder.build_ml_model_evaluation_preview_report(
        args.symbol, args.timeframe, args.profile, summary["metrics"]
    )

    print(report)

    if args.save:
        out_path = paths.ml_training_reports / f"ml_model_evaluation_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
        with open(out_path, "w") as f:
            f.write(report)
        print(f"Saved report to {out_path}")

if __name__ == "__main__":
    main()
