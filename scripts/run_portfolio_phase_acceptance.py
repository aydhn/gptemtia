# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Phase Acceptance Script.

Evaluates and persists individual acceptance registries for Phases 153, 154, 155, and 156.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_default_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.phase_153_portfolio_construction_acceptance import (
    build_phase_153_portfolio_construction_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_154_portfolio_optimization_acceptance import (
    build_phase_154_portfolio_optimization_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_155_risk_reporting_acceptance import (
    build_phase_155_risk_reporting_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_156_portfolio_scenario_control_acceptance import (
    build_phase_156_portfolio_scenario_control_acceptance_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    build_portfolio_phase_acceptance_markdown_report,
)
from reports.report_builder import (
    build_portfolio_phase_acceptance_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    df_153, s_153 = build_phase_153_portfolio_construction_acceptance_registry(profile)
    df_154, s_154 = build_phase_154_portfolio_optimization_acceptance_registry(profile)
    df_155, s_155 = build_phase_155_risk_reporting_acceptance_registry(profile)
    df_156, s_156 = build_phase_156_portfolio_scenario_control_acceptance_registry(profile)

    data_lake.save_phase_153_portfolio_construction_acceptance_registry(df_153, s_153)
    data_lake.save_phase_154_portfolio_optimization_acceptance_registry(df_154, s_154)
    data_lake.save_phase_155_risk_reporting_acceptance_registry(df_155, s_155)
    data_lake.save_phase_156_portfolio_scenario_control_acceptance_registry(df_156, s_156)

    out_dir = Path("reports/output/advanced_portfolio_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    for p_num, s_val, df_val in [
        (153, s_153, df_153),
        (154, s_154, df_154),
        (155, s_155, df_155),
        (156, s_156, df_156),
    ]:
        with open(out_dir / f"phase_{p_num}_acceptance.md", "w", encoding="utf-8") as f:
            f.write(build_portfolio_phase_acceptance_markdown_report(s_val, df_val))
        with open(out_dir / f"phase_{p_num}_acceptance.txt", "w", encoding="utf-8") as f:
            f.write(build_portfolio_phase_acceptance_text_report(s_val, df_val))

    print("=" * 70)
    print("PHASE 157: PORTFOLIO PHASE-LEVEL ACCEPTANCE (153-156)")
    print("=" * 70)
    print(f"Phase 153 Construction Accepted: {s_153['all_satisfied']}")
    print(f"Phase 154 Optimization Accepted: {s_154['all_satisfied']}")
    print(f"Phase 155 Risk Reporting Accepted: {s_155['all_satisfied']}")
    print(f"Phase 156 Scenario Control Accepted: {s_156['all_satisfied']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
