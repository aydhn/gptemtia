"""Run script: Overall Status of Phase 133 Regime Validation Acceptance subsystem."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)


def main():
    print("Evaluating Phase 133 Regime Validation Acceptance Subsystem Status...")
    pipeline = RegimeValidationAcceptancePipeline()
    df_status, summary = pipeline.build_regime_validation_acceptance_status(save=False)

    print("\n=======================================================")
    print("PHASE 133: REGIME VALIDATION ACCEPTANCE STATUS")
    print("=======================================================")
    for _, row in df_status.iterrows():
        print(f"[{row['status']}] {row['component']}: {row['details']}")

    print("\nOverall Status:", summary["overall_status"])
    print(f"Current Phase: {summary['current_phase']} -> Next Phase: {summary['next_phase']} (Final Target: {summary['target_final_phase']})")
    print("Non-Signal Certified:", summary["non_signal"])
    print("Source Preserved:", summary["source_preserved"])
    print("=======================================================")
    return 0


if __name__ == "__main__":
    sys.exit(main())
