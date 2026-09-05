"""Phase 128: Run Regime Rule-Free Status Script.

Prints overall execution status and component breakdown of Phase 128.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_pipeline import (
    RegimeRuleFreePipeline,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_rule_free_profile()
    pipeline = RegimeRuleFreePipeline(data_lake=data_lake, profile=profile)

    df_status, summary = pipeline.build_regime_rule_free_status(save=True)

    print("=" * 70)
    print("PHASE 128: MASTER REGIME RULE-FREE PIPELINE STATUS")
    print("=" * 70)
    print(f"Profile Name   : {summary['profile_name']}")
    print(f"Current Phase  : {summary['current_phase']}")
    print(f"Next Phase     : {summary['next_phase']}")
    print(f"Target Phase   : {summary['target_final_phase']}")
    print(f"Overall Status : {summary['overall_status']}")
    print(f"Non-Signal     : {summary['non_signal']}")
    print(f"Zero Execution : {summary['zero_execution']}")
    print("-" * 70)
    for _, row in df_status.iterrows():
        print(f"[{row['status']}] {row['component']:<30} : {row['details']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
