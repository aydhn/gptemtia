# -*- coding: utf-8 -*-
"""Phase 159: Run Operator Runbook Contracts Script.

Builds and persists operator startup/shutdown/config/health/troubleshooting runbooks and protocols.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.operator_startup_runbook_contracts import (
    build_operator_startup_runbook_contract_registry,
)
from advanced_final_hardening.operator_shutdown_runbook_contracts import (
    build_operator_shutdown_runbook_contract_registry,
)
from advanced_final_hardening.operator_config_check_runbook_contracts import (
    build_operator_config_check_runbook_contract_registry,
)
from advanced_final_hardening.operator_troubleshooting_runbook_contracts import (
    build_operator_troubleshooting_runbook_contract_registry,
)
from advanced_final_hardening.operator_recovery_runbook_contracts import (
    build_operator_recovery_runbook_contract_registry,
)
from advanced_final_hardening.operator_no_go_protocols import (
    build_operator_no_go_protocol_registry,
)
from advanced_final_hardening.operator_safe_usage_protocols import (
    build_operator_safe_usage_protocol_registry,
)
from advanced_final_hardening.final_hardening_report_builder import (
    build_operator_runbook_markdown_report,
)
from reports.report_builder import (
    build_operator_runbook_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_start, s_start = build_operator_startup_runbook_contract_registry(profile)
    df_shut, s_shut = build_operator_shutdown_runbook_contract_registry(profile)
    df_cfg, s_cfg = build_operator_config_check_runbook_contract_registry(profile)
    df_trbl, s_trbl = build_operator_troubleshooting_runbook_contract_registry(profile)
    df_rec, s_rec = build_operator_recovery_runbook_contract_registry(profile)
    df_nogo, s_nogo = build_operator_no_go_protocol_registry(profile)
    df_safe, s_safe = build_operator_safe_usage_protocol_registry(profile)

    data_lake.save_operator_startup_runbook_contract_registry(df_start, s_start)
    data_lake.save_operator_shutdown_runbook_contract_registry(df_shut, s_shut)
    data_lake.save_operator_config_check_runbook_contract_registry(df_cfg, s_cfg)
    data_lake.save_operator_troubleshooting_runbook_contract_registry(df_trbl, s_trbl)
    data_lake.save_operator_recovery_runbook_contract_registry(df_rec, s_rec)
    data_lake.save_operator_no_go_protocol_registry(df_nogo, s_nogo)
    data_lake.save_operator_safe_usage_protocol_registry(df_safe, s_safe)

    out_dir = Path("reports/output/advanced_final_hardening")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_operator_runbook_markdown_report(s_start, df_start)
    txt_report = build_operator_runbook_text_report(s_start, df_start)

    with open(out_dir / "runbooks.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "runbooks.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 159: OPERATOR RUNBOOK CONTRACTS INITIALIZED")
    print("=" * 70)
    print(f"Startup Steps: {s_start['step_count']} | Troubleshooting Scenarios: {s_trbl['scenario_count']}")
    print(f"NO-GO Rules: {s_nogo['rule_count']} | Safe Usage Rules: {s_safe['rule_count']}")
    print(f"Status: {s_start['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
