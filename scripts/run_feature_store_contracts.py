"""Phase 124: Run Feature Store Contracts Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_contract_registry import (
    build_feature_store_contract_registry,
)
from advanced_feature_store_integration.feature_store_read_contracts import (
    build_feature_store_read_contract_registry,
)
from advanced_feature_store_integration.feature_store_write_contracts import (
    build_feature_store_write_contract_registry,
)
from advanced_feature_store_integration.feature_store_query_contracts import (
    build_feature_store_query_contract_registry,
)
from advanced_feature_store_integration.feature_store_version_policies import (
    build_feature_store_version_policy_registry,
)
from advanced_feature_store_integration.feature_store_partition_policies import (
    build_feature_store_partition_policy_registry,
)
from advanced_feature_store_integration.feature_store_integration_report_builder import (
    build_feature_store_contract_markdown_report,
)
from reports.report_builder import build_feature_store_contract_text_report


def main():
    data_lake = DataLake()
    profile = get_default_feature_store_integration_profile()

    df_con, s_con = build_feature_store_contract_registry(profile)
    df_read, s_read = build_feature_store_read_contract_registry(profile)
    df_write, s_write = build_feature_store_write_contract_registry(profile)
    df_query, s_query = build_feature_store_query_contract_registry(profile)
    df_ver, s_ver = build_feature_store_version_policy_registry(profile)
    df_part, s_part = build_feature_store_partition_policy_registry(profile)

    data_lake.save_feature_store_contract_registry(df_con, s_con)
    data_lake.save_feature_store_read_contract_registry(df_read, s_read)
    data_lake.save_feature_store_write_contract_registry(df_write, s_write)
    data_lake.save_feature_store_query_contract_registry(df_query, s_query)
    data_lake.save_feature_store_version_policy_registry(df_ver, s_ver)
    data_lake.save_feature_store_partition_policy_registry(df_part, s_part)

    md_report = build_feature_store_contract_markdown_report(s_con, df_con)
    txt_report = build_feature_store_contract_text_report(s_con, df_con)

    reports_dir = Path("reports/output/advanced_feature_store_integration")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "feature_store_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(reports_dir / "feature_store_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 124: FEATURE STORE CONTRACTS & POLICIES")
    print("=" * 70)
    print(f"Total Store Contracts : {s_con['total_contracts']}")
    print(f"Total Read Contracts  : {s_read['total_read_contracts']}")
    print(f"Total Write Contracts : {s_write['total_write_contracts']}")
    print(f"Total Query Contracts : {s_query['total_query_contracts']}")
    print(f"All Non-Signal        : {s_con['all_non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
