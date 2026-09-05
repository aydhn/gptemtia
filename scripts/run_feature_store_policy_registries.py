"""Phase 124: Run Policy Registries Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_non_signal_policies import (
    build_feature_store_non_signal_policy_registry,
)
from advanced_feature_store_integration.feature_store_forbidden_column_policies import (
    build_feature_store_forbidden_column_policy_registry,
)
from advanced_feature_store_integration.feature_store_source_preservation_policies import (
    build_feature_store_source_preservation_policy_registry,
)
from advanced_feature_store_integration.phase_125_handoff import (
    build_phase_125_feature_factor_engine_acceptance_handoff_report,
)
from advanced_feature_store_integration.feature_store_integration_report_builder import (
    build_feature_store_policy_markdown_report,
    build_phase_125_handoff_markdown_report,
)
from reports.report_builder import (
    build_feature_store_policy_text_report,
    build_phase_125_handoff_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_store_integration_profile()

    df_nsig, s_nsig = build_feature_store_non_signal_policy_registry(profile)
    df_forbid, s_forbid = build_feature_store_forbidden_column_policy_registry(profile)
    df_pres, s_pres = build_feature_store_source_preservation_policy_registry(profile)
    df_hnd, s_hnd = build_phase_125_feature_factor_engine_acceptance_handoff_report(profile)

    data_lake.save_feature_store_non_signal_policy_registry(df_nsig, s_nsig)
    data_lake.save_feature_store_forbidden_column_policy_registry(df_forbid, s_forbid)
    data_lake.save_feature_store_source_preservation_policy_registry(df_pres, s_pres)
    data_lake.save_phase_125_feature_factor_engine_acceptance_handoff_report(df_hnd, s_hnd)

    md_pol = build_feature_store_policy_markdown_report(s_nsig, df_nsig)
    txt_pol = build_feature_store_policy_text_report(s_nsig, df_nsig)
    md_hnd = build_phase_125_handoff_markdown_report(s_hnd, df_hnd)
    txt_hnd = build_phase_125_handoff_text_report(s_hnd, df_hnd)

    reports_dir = Path("reports/output/advanced_feature_store_integration")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "feature_store_policies.md", "w", encoding="utf-8") as f:
        f.write(md_pol)
    with open(reports_dir / "feature_store_policies.txt", "w", encoding="utf-8") as f:
        f.write(txt_pol)
    with open(reports_dir / "phase_125_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_hnd)
    with open(reports_dir / "phase_125_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_hnd)

    print("=" * 70)
    print("PHASE 124: POLICIES & PHASE 125 HANDOFF")
    print("=" * 70)
    print(f"Non-Signal Policies        : {s_nsig['total_policies']}")
    print(f"Forbidden Columns Enforced : {s_forbid['total_forbidden_columns']}")
    print(f"Preservation Policies      : {s_pres['total_preservation_policies']}")
    print(f"Phase 125 Handoff Status   : {s_hnd['handoff_status']}")
    print(f"Ready Handoff Items        : {s_hnd['ready_items']}/{s_hnd['total_items']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
