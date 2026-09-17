# -*- coding: utf-8 -*-
"""Phase 158: Run System Contract Integration Script.

Builds and persists contract, manifest, and validation evidence integration registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_contract_integration import (
    build_system_contract_integration_registry,
)
from advanced_full_system_integration.system_manifest_integration import (
    build_system_manifest_integration_registry,
)
from advanced_full_system_integration.system_validation_evidence import (
    build_system_validation_evidence_registry,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_system_contract_integration_markdown_report,
    build_system_manifest_integration_markdown_report,
)
from reports.report_builder import (
    build_system_contract_integration_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_full_system_integration_profile()

    df_cnt, s_cnt = build_system_contract_integration_registry(profile)
    df_mnf, s_mnf = build_system_manifest_integration_registry(profile)
    df_evd, s_evd = build_system_validation_evidence_registry(profile)

    data_lake.save_system_contract_integration_registry(df_cnt, s_cnt)
    data_lake.save_system_manifest_integration_registry(df_mnf, s_mnf)
    data_lake.save_system_validation_evidence_registry(df_evd, s_evd)

    out_dir = Path("reports/output/advanced_full_system_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_cnt = build_system_contract_integration_markdown_report(s_cnt, df_cnt)
    txt_cnt = build_system_contract_integration_text_report(s_cnt, df_cnt)
    md_mnf = build_system_manifest_integration_markdown_report(s_mnf, df_mnf)

    with open(out_dir / "contracts.md", "w", encoding="utf-8") as f:
        f.write(md_cnt)
    with open(out_dir / "contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_cnt)
    with open(out_dir / "manifest_integration.md", "w", encoding="utf-8") as f:
        f.write(md_mnf)

    print("=" * 70)
    print("PHASE 158: SYSTEM CONTRACT & MANIFEST INTEGRATION INITIALIZED")
    print("=" * 70)
    print(f"Total Integrated Contracts : {s_cnt['total_contracts']}")
    print(f"Total Integrated Manifests : {s_mnf['total_manifests_integrated']}")
    print(f"Total Validation Evidence  : {s_evd['total_evidence_items']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
