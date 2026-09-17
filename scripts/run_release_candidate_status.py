# -*- coding: utf-8 -*-
"""Phase 159: Run Release Candidate Status Script.

Aggregates and prints the complete Phase 159 output status and ready state.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_pipeline import FinalHardeningPipeline


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    pipeline = FinalHardeningPipeline(data_lake, settings, Path(__file__).resolve().parent.parent, profile)
    df_status, summary = pipeline.build_release_candidate_status(save=False)

    print("=" * 70)
    print("PHASE 159: RELEASE CANDIDATE STATUS REPORT")
    print("=" * 70)
    row = df_status.iloc[0].to_dict()
    for k, v in row.items():
        print(f"  {k:<35}: {v}")
    print("=" * 70)
    print(f"Overall Status: {summary['status']}")
    print(f"Phase 160 Handoff Ready: {summary['phase_160_handoff_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
