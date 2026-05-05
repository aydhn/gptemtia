"""
Script to check status of asset profiles in the data lake.
"""

import logging
import pandas as pd
from pathlib import Path

from config.settings import settings
from config.paths import LAKE_DIR, ASSET_PROFILE_REPORTS_DIR
from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from data.storage.data_lake import DataLake
import reports.report_builder as report_builder
from asset_profiles.asset_class_registry import filter_symbols_for_group_analysis

logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)


def main():
    data_lake = DataLake(LAKE_DIR)

    logger.info("Checking asset profile status...")

    tradeable_groups = filter_symbols_for_group_analysis(DEFAULT_SYMBOL_UNIVERSE)

    summary = {
        "total_symbols": sum(len(m) for m in tradeable_groups.values()),
        "total_asset_classes": len(tradeable_groups),
        "asset_classes": {},
    }

    rows = []

    for ac, members in tradeable_groups.items():
        ac_info = {
            "expected_profiles": len(members),
            "profiles_count": 0,
            "group_features_count": 0,
        }

        # Check group features
        # We check common timeframes
        for tf in ["1d", "4h", "1h"]:
            if data_lake.has_group_features(ac, tf):
                ac_info["group_features_count"] += 1

        for spec in members:
            # Check most common timeframe for the report
            tf = "1d"
            has_prof = data_lake.has_features(spec, tf, "asset_profiles")
            has_ev = data_lake.has_features(spec, tf, "asset_profile_events")

            if has_prof:
                ac_info["profiles_count"] += 1
                try:
                    df = data_lake.load_features(spec, tf, "asset_profiles")
                    regime = (
                        df["asset_behavior_regime_label"].iloc[-1]
                        if "asset_behavior_regime_label" in df.columns
                        else "Unknown"
                    )
                    group_regime = (
                        df["asset_group_regime_label"].iloc[-1]
                        if "asset_group_regime_label" in df.columns
                        else "Unknown"
                    )

                    rows.append(
                        {
                            "symbol": spec.symbol,
                            "asset_class": ac,
                            "timeframe": tf,
                            "has_profile": True,
                            "has_events": has_ev,
                            "rows": len(df),
                            "latest_regime": regime,
                            "latest_group_regime": group_regime,
                        }
                    )
                except Exception as e:
                    logger.error(f"Error reading profile for {spec.symbol}: {e}")
                    rows.append(
                        {
                            "symbol": spec.symbol,
                            "asset_class": ac,
                            "timeframe": tf,
                            "has_profile": True,
                            "has_events": has_ev,
                            "error": str(e),
                        }
                    )
            else:
                rows.append(
                    {
                        "symbol": spec.symbol,
                        "asset_class": ac,
                        "timeframe": tf,
                        "has_profile": False,
                        "has_events": False,
                    }
                )

        summary["asset_classes"][ac] = ac_info

    status_df = pd.DataFrame(rows) if rows else pd.DataFrame()

    report = report_builder.build_asset_profile_status_report(status_df, summary)

    print("\n" + report + "\n")

    ASSET_PROFILE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = ASSET_PROFILE_REPORTS_DIR / "asset_profile_status_report.txt"
    report_path.write_text(report)
    logger.info(f"Report saved to {report_path}")

    if not status_df.empty:
        csv_path = ASSET_PROFILE_REPORTS_DIR / "asset_profile_status.csv"
        status_df.to_csv(csv_path, index=False)
        logger.info(f"CSV status saved to {csv_path}")


if __name__ == "__main__":
    main()
