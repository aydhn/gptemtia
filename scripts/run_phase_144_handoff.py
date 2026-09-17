# -*- coding: utf-8 -*-
"""Phase 143: Run Phase 144 Handoff Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.phase_144_handoff import (
    generate_phase_144_handoff_contract,
    format_phase_144_handoff_text,
)
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    handoff_pkg = generate_phase_144_handoff_contract()
    df = pd.DataFrame([{
        "current_phase": handoff_pkg["current_phase"],
        "next_phase": handoff_pkg["next_phase"],
        "target_final_phase": handoff_pkg["target_final_phase"],
        "status": handoff_pkg["phase_143_status"],
        "readiness_score": handoff_pkg["readiness_score"],
        "classification": handoff_pkg["classification"],
    }])
    data_lake.save_phase_144_handoff(df, handoff_pkg)

    print("=" * 70)
    print("PHASE 143 -> PHASE 144 HANDOFF CONTRACT")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(format_phase_144_handoff_text(handoff_pkg))
    print("=" * 70)


if __name__ == "__main__":
    main()
