"""Run script: Contracts, Timestamp Policies, Asof Policies, and No-Lookahead Guards for Phase 131."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)


def main():
    print("Executing Phase 131 Alignment Guards and Contracts...")
    pipeline = CrossAssetRegimePipeline()
    dfs, summaries = pipeline.build_contracts_alignment_guards(save=True)

    print(f"Contracts: {len(dfs['contracts'])}")
    print(f"Timestamp Policies: {len(dfs['timestamp_policies'])}")
    print(f"Asof Join Policies: {len(dfs['asof_join_policies'])}")
    print(f"No-Lookahead Guards: {len(dfs['no_lookahead_guard'])}")

    print("\n--- Guard Enforcement Status ---")
    print(f"All Contracts Require Non-Signal: {summaries['contracts']['all_non_signal_required']}")
    print(f"All Contracts Require No-Lookahead: {summaries['contracts']['all_no_lookahead_required']}")
    print(f"All Asof Joins Backward: {summaries['asof_join_policies']['all_backward_direction']}")
    print(f"Zero Forward Joins Allowed: {summaries['asof_join_policies']['zero_forward_allowed']}")
    print("\nSUCCESS: Phase 131 Alignment Guards and Contracts generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
