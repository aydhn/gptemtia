"""Run script: Health Check for Phase 132 Macro/Event/News Regime Context Expansion."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)


def main():
    print("Executing Phase 132 Health Check...")
    pipeline = MacroEventNewsRegimePipeline()
    dfs, summaries = pipeline.build_health_validation_safety_handoff(save=True)

    health_df = dfs["health"]
    print(f"Health Checks Total: {len(health_df)}")
    print(f"Passed: {int((health_df['status'] == 'PASS').sum())}")
    print(f"Failed: {int((health_df['status'] != 'PASS').sum())}")
    print(f"Overall Health Status: {summaries['health_status']}")

    if summaries["health_status"] == "HEALTHY":
        print("\nSUCCESS: Phase 132 Health Check Passed.")
        return 0
    else:
        print("\nWARNING: Some health checks did not pass.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
