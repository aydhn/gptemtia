"""Phase 128: Run Rule-Free Labeling Contracts Script.

Generates rule-free labeling contracts and candidate state assignment policies.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.rule_free_labeling_contracts import (
    build_rule_free_labeling_contract_registry,
)
from advanced_regime_rule_free.candidate_state_assignment_policies import (
    build_candidate_state_assignment_policy_registry,
)
from advanced_regime_rule_free.regime_rule_free_report_builder import (
    build_rule_free_labeling_contract_markdown_report,
)
from reports.report_builder import build_rule_free_labeling_contract_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_rule_free_profile()

    df_cont, s_cont = build_rule_free_labeling_contract_registry(profile)
    df_pol, s_pol = build_candidate_state_assignment_policy_registry(profile)

    data_lake.save_rule_free_labeling_contract_registry(df_cont, s_cont)
    data_lake.save_candidate_state_assignment_policy_registry(df_pol, s_pol)

    md_cont = build_rule_free_labeling_contract_markdown_report(s_cont, df_cont)
    txt_cont = build_rule_free_labeling_contract_text_report(s_cont, df_cont)

    out_dir = Path("reports/output/advanced_regime_rule_free")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "labeling_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_cont)
    with open(out_dir / "labeling_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_cont)

    print("=" * 70)
    print("PHASE 128: RULE-FREE LABELING CONTRACTS & ASSIGNMENT POLICIES")
    print("=" * 70)
    print(f"Total Contracts : {s_cont['total_contracts']}")
    print(f"Contract Status : {s_cont['contracts_status']}")
    print(f"Total Policies  : {s_pol['total_policies']}")
    print(f"All Non-Signal  : {s_cont['all_non_signal']}")
    print(f"Clustering Exec : False")
    print(f"Model Training  : False")
    print("=" * 70)


if __name__ == "__main__":
    main()
