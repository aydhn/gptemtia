# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Status Script.

Compiles and displays status across all Phase 160 subsystems.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_final_delivery.final_delivery_pipeline import FinalDeliveryPipeline


def main():
    save_flag = "--no-save" not in sys.argv
    pipeline = FinalDeliveryPipeline()
    df_status, summary = pipeline.build_final_delivery_status(save=save_flag)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY STATUS OVERVIEW")
    print("=" * 70)
    print(f"Current Phase: {summary['current_phase']} | Target Final Phase: {summary['target_final_phase']}")
    print(f"Readiness Score: {summary['readiness_score']:.2f} ({summary['classification']})")
    print(f"Phase 160 Completed: {summary['phase_160_completed']} | 160-Phase Plan Closed: {summary['final_plan_closed']}")
    print(f"Full Advanced Bot Final Delivery Completed: {summary['full_advanced_bot_final_delivery_completed']}")
    print("-" * 70)
    for _, row in df_status.iterrows():
        print(f"  {row['subsystem']:<35} : {row['items']:>3} items [{row['status']}]")
    print("=" * 70)
    print(f"Overall Status: {summary['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
