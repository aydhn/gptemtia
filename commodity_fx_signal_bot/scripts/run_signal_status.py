import logging
import pandas as pd
from data.storage.data_lake import DataLake
from config.symbols import get_enabled_symbols
from reports.report_builder import build_signal_status_report
from config.paths import SIGNAL_REPORTS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    from config.paths import DATA_DIR

    lake = DataLake(DATA_DIR)
    specs = get_enabled_symbols()

    status_rows = []
    total_pool_cands = 0
    avg_pool_score = 0.0

    # Just check for 1d balanced
    timeframe = "1d"
    profile = "balanced_candidate_scoring"

    for spec in specs:
        if spec.asset_class in ["macro", "benchmark", "synthetic"]:
            continue

        has_cand = lake.has_features(spec, timeframe, "signal_candidates")
        cand_count = 0
        if has_cand:
            try:
                df = lake.load_features(spec, timeframe, "signal_candidates")
                cand_count = len(df)
            except:
                pass

        status_rows.append(
            {
                "symbol": spec.symbol,
                "has_candidates": has_cand,
                "candidate_count": cand_count,
            }
        )

    df_status = pd.DataFrame(status_rows)

    if lake.has_signal_pool(timeframe, profile):
        try:
            pool_df = lake.load_signal_pool(timeframe, profile)
            total_pool_cands = len(pool_df)
            if not pool_df.empty and "candidate_score" in pool_df.columns:
                avg_pool_score = pool_df["candidate_score"].mean()
        except:
            pass

    summary = {
        "total_with_candidates": (
            df_status["has_candidates"].sum() if not df_status.empty else 0
        ),
        "total_pool_candidates": total_pool_cands,
        "average_pool_score": avg_pool_score,
    }

    report = build_signal_status_report(df_status, summary)
    print(report)

    out_path = SIGNAL_REPORTS_DIR / "signal_status_report.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(report)

    if not df_status.empty:
        df_status.to_csv(SIGNAL_REPORTS_DIR / "signal_status.csv", index=False)

    logger.info(f"Status report saved to {out_path}")


if __name__ == "__main__":
    main()
