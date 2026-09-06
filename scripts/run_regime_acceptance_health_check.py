"""Phase 135: Run Regime Acceptance Health Check Script.

Performs health check on all components and storage systems in the regime block.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_health import (
    build_regime_acceptance_health_check,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_health_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()
    root = Path(__file__).resolve().parent.parent

    df_hlth, s_hlth = build_regime_acceptance_health_check(root, profile)
    data_lake.save_regime_acceptance_health_check(df_hlth, s_hlth)

    md_hlth = build_regime_health_markdown_report(s_hlth, df_hlth)

    out_dir = Path("reports/output/advanced_regime_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health.md", "w", encoding="utf-8") as f:
        f.write(md_hlth)

    print("=" * 70)
    print("PHASE 135: REGIME ACCEPTANCE HEALTH CHECK")
    print("=" * 70)
    print(f"Total Checks : {s_hlth['total_checks']}")
    print(f"Healthy Count: {s_hlth['healthy_count']}")
    print(f"All Healthy  : {s_hlth['all_healthy']}")
    print(f"Status       : {s_hlth['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
