# -*- coding: utf-8 -*-
"""Phase 159: Run Final Hardening Contracts Script.

Builds and persists final hardening, operator runbook, and release candidate contract registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_contracts import (
    build_final_hardening_contract_registry,
)
from advanced_final_hardening.operator_runbook_contracts import (
    build_operator_runbook_contract_registry,
)
from advanced_final_hardening.release_candidate_contracts import (
    build_release_candidate_contract_registry,
)
from advanced_final_hardening.final_hardening_report_builder import (
    build_final_hardening_contract_markdown_report,
)
from reports.report_builder import (
    build_final_hardening_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_c, s_c = build_final_hardening_contract_registry(profile)
    df_rb, s_rb = build_operator_runbook_contract_registry(profile)
    df_rc, s_rc = build_release_candidate_contract_registry(profile)

    data_lake.save_final_hardening_contract_registry(df_c, s_c)
    data_lake.save_operator_runbook_contract_registry(df_rb, s_rb)
    data_lake.save_release_candidate_contract_registry(df_rc, s_rc)

    out_dir = Path("reports/output/advanced_final_hardening")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_final_hardening_contract_markdown_report(s_c, df_c)
    txt_report = build_final_hardening_text_report(s_c, df_c)

    with open(out_dir / "contracts.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 159: FINAL HARDENING CONTRACTS INITIALIZED")
    print("=" * 70)
    print(f"Contracts: {s_c['contract_count']} | Runbooks: {s_rb['runbook_count']} | RC Contracts: {s_rc['candidate_contract_count']}")
    print(f"Status: {s_c['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
