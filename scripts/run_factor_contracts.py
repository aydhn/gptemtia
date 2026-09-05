"""Phase 122: Run Factor Contracts and Schemas Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_contract_registry import build_factor_contract_registry
from advanced_factor_metadata.factor_input_feature_sets import build_factor_input_feature_set_registry
from advanced_factor_metadata.factor_namespace_registry import build_factor_namespace_registry
from advanced_factor_metadata.factor_output_schema import build_factor_output_schema_registry
from advanced_factor_metadata.factor_metadata_report_builder import build_factor_contract_markdown_report
from reports.report_builder import build_factor_contract_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_factor_metadata_profile()

    df_cntr, s_cntr = build_factor_contract_registry(profile)
    df_fset, s_fset = build_factor_input_feature_set_registry(profile)
    df_ns, s_ns = build_factor_namespace_registry(profile)
    df_sch, s_sch = build_factor_output_schema_registry(profile)

    data_lake.save_factor_contract_registry(df_cntr, s_cntr)
    data_lake.save_factor_input_feature_set_registry(df_fset, s_fset)
    data_lake.save_factor_namespace_registry(df_ns, s_ns)
    data_lake.save_factor_output_schema_registry(df_sch, s_sch)

    md_report = build_factor_contract_markdown_report(s_cntr, df_cntr)
    txt_report = build_factor_contract_text_report(s_cntr, df_cntr)

    reports_dir = Path("reports/output/advanced_factor_metadata")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "factor_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(reports_dir / "factor_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 122: FACTOR CONTRACTS AND SCHEMAS")
    print("=" * 70)
    print(f"Total Contracts    : {s_cntr['total_contracts']}")
    print(f"Valid Contracts    : {s_cntr['valid_contracts']}")
    print(f"Total Feature Sets : {s_fset['total_feature_sets']}")
    print(f"Total Namespaces   : {s_ns['total_namespaces']}")
    print(f"Total Schemas      : {s_sch['total_schemas']}")
    print(f"All Valid          : {s_cntr['all_contracts_valid']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
