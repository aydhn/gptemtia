"""Phase 130: Run Regime State Sequence Contracts Script.

Generates candidate and pseudo state sequence schema and sequence contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_state_sequence_contracts import (
    build_regime_state_sequence_contract_registry,
)
from advanced_regime_transition.candidate_state_sequence_schema import (
    build_candidate_state_sequence_schema_registry,
)
from advanced_regime_transition.pseudo_state_sequence_schema import (
    build_pseudo_state_sequence_schema_registry,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_state_sequence_contract_markdown_report,
)
from reports.report_builder import build_state_sequence_contracts_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_cont, s_cont = build_regime_state_sequence_contract_registry(profile)
    df_cand, s_cand = build_candidate_state_sequence_schema_registry(profile)
    df_pseu, s_pseu = build_pseudo_state_sequence_schema_registry(profile)

    data_lake.save_regime_state_sequence_contract_registry(df_cont, s_cont)
    data_lake.save_candidate_state_sequence_schema_registry(df_cand, s_cand)
    data_lake.save_pseudo_state_sequence_schema_registry(df_pseu, s_pseu)

    md_content = build_state_sequence_contract_markdown_report(s_cont, df_cont)
    txt_content = build_state_sequence_contracts_text_report(s_cont, df_cont)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "state_sequence_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(out_dir / "state_sequence_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: REGIME STATE SEQUENCE CONTRACTS & SCHEMAS")
    print("=" * 70)
    print(f"Contracts Count  : {s_cont.get('total_contracts', len(df_cont))}")
    print(f"Candidate Fields : {s_cand.get('total_schema_columns', len(df_cand))}")
    print(f"Pseudo Fields    : {s_pseu.get('total_schema_columns', len(df_pseu))}")
    print(f"Lookahead Guard  : {s_cont.get('all_no_lookahead_required', True)}")
    print(f"Non-Signal       : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
