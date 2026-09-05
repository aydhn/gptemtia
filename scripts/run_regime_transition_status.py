"""Phase 130: Run Regime Transition Status Script.

Executes master regime transition pipeline and reports full status.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_pipeline import (
    RegimeTransitionPipeline,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()
    pipeline = RegimeTransitionPipeline(data_lake=data_lake, profile=profile)

    df_status, summary = pipeline.build_regime_transition_status(save=True)

    print("=" * 70)
    print("PHASE 130: MASTER REGIME TRANSITION PIPELINE STATUS")
    print("=" * 70)
    print(f"Profile Name   : {summary.get('active_profile')}")
    print(f"Current Phase  : {summary.get('current_phase')}")
    print(f"Next Phase     : {summary.get('next_phase')}")
    print(f"Target Phase   : {summary.get('target_final_phase')}")
    print(f"Overall Status : {summary.get('overall_status')}")
    print(f"Stability Score: {summary.get('stability_score')}")
    print(f"Non-Signal     : {summary.get('non_signal')}")
    print(f"Zero ML/Model  : {not summary.get('model_training_executed')}")
    print(f"Zero Cluster   : {not summary.get('clustering_executed')}")
    print("-" * 70)
    for _, row in df_status.iterrows():
        comp = row.get("component", "unknown")
        count = row.get("item_count", 0)
        status = row.get("status", "READY")
        print(f"[{status}] {comp:<40} : items: {count}")
    print("=" * 70)


if __name__ == "__main__":
    main()
