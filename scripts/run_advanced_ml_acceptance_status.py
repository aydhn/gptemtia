# -*- coding: utf-8 -*-
"""Phase 145: Run Advanced ML Acceptance Status Script.

Prints overall Phase 145 status and verifies generated artifact files.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_pipeline import (
    AdvancedMlAcceptancePipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_advanced_ml_acceptance_profile()

    pipeline = AdvancedMlAcceptancePipeline(data_lake, settings, Path("."), profile)
    df_status, summary = pipeline.build_advanced_ml_acceptance_status(save=True)

    print("=" * 70)
    print("PHASE 145: CONSOLIDATED ADVANCED ML ACCEPTANCE STATUS")
    print("=" * 70)
    print(f"Profile                 : {summary['active_profile']}")
    print(f"Current Phase           : {summary['current_phase']}")
    print(f"Target Final Phase      : {summary['target_final_phase']}")
    print(f"Next Phase              : {summary['next_phase']}")
    print(f"Readiness Score         : {summary['readiness_score']:.2f}")
    print(f"Classification          : {summary['classification']}")
    print(f"Status                  : {summary['status']}")
    print(f"Non-Signal              : {summary['non_signal']}")
    print(f"Production Ready        : False (Enforced)")
    print(f"Broker Ready            : False (Enforced)")
    print(f"Live Trading Ready      : False (Enforced)")
    print("=" * 70)

    out_dir = Path("reports/output/advanced_ml_acceptance")
    if out_dir.exists():
        files = list(out_dir.glob("*.*"))
        print(f"Generated output files ({len(files)}):")
        for f in sorted(files):
            print(f"  - {f.name} ({f.stat().st_size} bytes)")
    print("=" * 70)


if __name__ == "__main__":
    main()
