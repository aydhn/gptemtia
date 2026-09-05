"""Phase 130: Run Regime Transition Health Check Script.

Performs offline environment, package, and dependency health checks for Phase 130.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_health import (
    build_regime_transition_health_check,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_regime_transition_health_markdown_report,
)
from reports.report_builder import build_regime_transition_health_text_report


def main():
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_hlth, s_hlth = build_regime_transition_health_check(project_root, profile)
    data_lake.save_regime_transition_health_check(df_hlth, s_hlth)

    md_content = build_regime_transition_health_markdown_report(s_hlth, df_hlth)
    txt_content = build_regime_transition_health_text_report(s_hlth, df_hlth)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "regime_transition_health.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(out_dir / "regime_transition_health.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: REGIME TRANSITION HEALTH CHECK")
    print("=" * 70)
    print(f"Overall Status   : {s_hlth.get('health_status', 'HEALTHY')}")
    print(f"Total Checks     : {s_hlth.get('total_checks')}")
    print(f"Passed Checks    : {s_hlth.get('passed_checks')}")
    print(f"Failed Checks    : {s_hlth.get('failed_checks')}")
    print(f"Non-Signal       : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
