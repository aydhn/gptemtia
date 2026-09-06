"""Run script: Overall Status of Phase 132 Macro/Event/News Regime Context Expansion."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)


def main():
    print("================================================================================")
    print("PHASE 132: MACRO/EVENT/NEWS REGIME CONTEXT EXPANSION STATUS")
    print("================================================================================")
    pipeline = MacroEventNewsRegimePipeline()
    status_df, summary = pipeline.build_macro_event_news_regime_status(save=True)

    print("\n--- Component Status Table ---")
    print(status_df.to_string(index=False))

    print("\n--- Summary ---")
    for k, v in summary.items():
        print(f"{k}: {v}")

    print("\n================================================================================")
    print("Zero live trading, zero broker execution, zero signals, zero sentiment models,")
    print("strictly metadata-only news, zero lookahead bias, zero destructive changes.")
    print("Target Final Phase: 160 | Next Phase: 133")
    print("================================================================================")
    return 0


if __name__ == "__main__":
    sys.exit(main())
