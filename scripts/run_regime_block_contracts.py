"""Phase 135: Run Regime Block Contracts Script.

Audits documentation, runner scripts, and test contract files across Phases 126-135.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_block_documentation import (
    build_regime_block_documentation_report,
)
from advanced_regime_acceptance.regime_block_script_contracts import (
    build_regime_block_script_contract_report,
)
from advanced_regime_acceptance.regime_block_test_contracts import (
    build_regime_block_test_contract_report,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_contract_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()
    root = Path(__file__).resolve().parent.parent

    df_doc, s_doc = build_regime_block_documentation_report(root, profile)
    df_scr, s_scr = build_regime_block_script_contract_report(root, profile)
    df_tst, s_tst = build_regime_block_test_contract_report(root, profile)

    data_lake.save_regime_block_documentation_report(df_doc, s_doc)
    data_lake.save_regime_block_script_contract_report(df_scr, s_scr)
    data_lake.save_regime_block_test_contract_report(df_tst, s_tst)

    md_doc = build_regime_contract_markdown_report(s_doc, df_doc)
    md_scr = build_regime_contract_markdown_report(s_scr, df_scr)
    md_tst = build_regime_contract_markdown_report(s_tst, df_tst)

    out_dir = Path("reports/output/advanced_regime_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "documentation_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_doc)
    with open(out_dir / "script_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_scr)
    with open(out_dir / "test_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_tst)

    print("=" * 70)
    print("PHASE 135: REGIME BLOCK CONTRACTS AUDIT")
    print("=" * 70)
    print(f"Documentation All Exist : {s_doc['all_exist']} ({s_doc['docs_existing']}/{s_doc['total_docs']})")
    print(f"Scripts All Present     : {s_scr['all_present']} ({s_scr['present_scripts']}/{s_scr['total_scripts_checked']})")
    print(f"Tests All Present       : {s_tst['all_present']} ({s_tst['present_test_suites']}/{s_tst['total_test_suites_checked']})")
    print(f"Non-Signal              : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
