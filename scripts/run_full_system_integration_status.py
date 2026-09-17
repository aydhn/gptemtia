# -*- coding: utf-8 -*-
"""Phase 158: Run Full-System Integration Status Script.

Executes the full pipeline orchestrator and generates consolidated status outputs.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_pipeline import (
    FullSystemIntegrationPipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_full_system_integration_profile()

    pipeline = FullSystemIntegrationPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    status_df, summary = pipeline.build_full_system_integration_status(save=True)

    print("=" * 70)
    print("PHASE 158: FULL-SYSTEM INTEGRATION STATUS COMPLETE")
    print("=" * 70)
    print(f"Active Profile  : {summary['active_profile']}")
    print(f"Readiness Score : {summary['readiness_score']:.4f}")
    print(f"Classification  : {summary['classification']}")
    print(f"Handoff Ready   : {summary['handoff_ready']}")
    print(f"Status          : {summary['status']}")
    print("=" * 70)
    print(status_df.to_string(index=False))
    print("=" * 70)


if __name__ == "__main__":
    main()
