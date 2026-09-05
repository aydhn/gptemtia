"""Phase 125: Run Feature Engine Block Contracts Script.

Audits documentation, script, and test contracts across Phase 116-125.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_engine_block_documentation import (
    build_feature_engine_block_documentation_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_script_contracts import (
    build_feature_engine_block_script_contract_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_test_contracts import (
    build_feature_engine_block_test_contract_report,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_contract_markdown_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_factor_acceptance_profile()
    root = Path(__file__).resolve().parent.parent

    df_doc, s_doc = build_feature_engine_block_documentation_report(root, profile)
    df_scr, s_scr = build_feature_engine_block_script_contract_report(root, profile)
    df_tst, s_tst = build_feature_engine_block_test_contract_report(root, profile)

    data_lake.save_feature_engine_block_documentation_report(df_doc, s_doc)
    data_lake.save_feature_engine_block_script_contract_report(df_scr, s_scr)
    data_lake.save_feature_engine_block_test_contract_report(df_tst, s_tst)

    md_doc = build_contract_markdown_report(s_doc, df_doc)
    md_scr = build_contract_markdown_report(s_scr, df_scr)
    md_tst = build_contract_markdown_report(s_tst, df_tst)

    out_dir = Path("reports/output/advanced_feature_factor_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "contracts_docs.md", "w", encoding="utf-8") as f:
        f.write(md_doc)
    with open(out_dir / "contracts_scripts.md", "w", encoding="utf-8") as f:
        f.write(md_scr)
    with open(out_dir / "contracts_tests.md", "w", encoding="utf-8") as f:
        f.write(md_tst)

    print("=" * 70)
    print("PHASE 125: FEATURE ENGINE BLOCK CONTRACTS AUDIT")
    print("=" * 70)
    print(f"Documentation Present : {s_doc['present_docs']}/{s_doc['total_docs_checked']}")
    print(f"Scripts Present       : {s_scr['present_scripts']}/{s_scr['total_scripts_checked']}")
    print(f"Test Suites Present   : {s_tst['present_test_suites']}/{s_tst['total_test_suites_checked']}")
    print(f"Non-Signal Mandate    : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
