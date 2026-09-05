"""Phase 129: Run Market Behavior Diagnostics Status Script.

Prints overall execution status and component breakdown of Phase 129.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_pipeline import (
    MarketBehaviorDiagnosticsPipeline,
)


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()
    pipeline = MarketBehaviorDiagnosticsPipeline(data_lake=data_lake, profile=profile)

    df_status, summary = pipeline.build_market_behavior_diagnostics_status(save=True)

    print("=" * 70)
    print("PHASE 129: MASTER MARKET BEHAVIOR DIAGNOSTICS PIPELINE STATUS")
    print("=" * 70)
    print(f"Profile Name   : {summary.get('profile_name', profile.profile_name)}")
    print(f"Current Phase  : {summary.get('current_phase', 129)}")
    print(f"Next Phase     : {summary.get('next_phase', 130)}")
    print(f"Target Phase   : {summary.get('target_final_phase', 160)}")
    print(f"Overall Status : {summary.get('overall_status', 'READY')}")
    print(f"Non-Signal     : {summary.get('non_signal', True)}")
    print(f"Zero Execution : {not summary.get('clustering_executed', False)}")
    print("-" * 70)
    for _, row in df_status.iterrows():
        comp = row.get("module", row.get("component", "module"))
        details = f"items: {row.get('items_count', 0)}"
        print(f"[{row['status']}] {comp:<32} : {details}")
    print("=" * 70)



if __name__ == "__main__":
    main()
