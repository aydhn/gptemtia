"""Phase 134 Script: Run Regime FeatureStore Integration Status.

Executes the end-to-end RegimeFeatureStorePipeline and displays overall status.
"""

from advanced_regime_featurestore_integration.regime_featurestore_pipeline import (
    RegimeFeatureStorePipeline,
)


def main() -> None:
    pipeline = RegimeFeatureStorePipeline()
    status_df, summary = pipeline.build_regime_featurestore_status(save=True)

    print("================================================================================")
    print("PHASE 134: REGIME FEATURESTORE INTEGRATION STATUS SUMMARY")
    print("================================================================================")
    for _, row in status_df.iterrows():
        print(f"[{row['status']}] {row['module']}: {row['count']} records (non_signal={row['non_signal']})")
    print("--------------------------------------------------------------------------------")
    print(f"Overall Status: {summary.get('overall_status')}")
    print(f"Active Profile: {summary.get('active_profile')}")
    print(f"All Healthy: {summary.get('all_healthy')}")
    print(f"All Validation Passed: {summary.get('all_validation_passed')}")
    print(f"All Handoff Ready: {summary.get('all_handoff_ready')}")
    print(f"Current Phase: {summary.get('current_phase')} -> Next Phase: {summary.get('next_phase')}")
    print("================================================================================")


if __name__ == "__main__":
    main()
