"""Phase 127: Run Regime State Dataset Contracts Script.

Generates and saves state dataset contracts, state dataset schema, state metadata, and candidate contexts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_matrix.regime_matrix_config import (
    get_default_regime_matrix_profile,
)
from advanced_regime_matrix.regime_state_dataset_contracts import (
    build_regime_state_dataset_contracts,
)
from advanced_regime_matrix.regime_state_dataset_schema import (
    build_regime_state_dataset_schema,
)
from advanced_regime_matrix.regime_state_dataset_metadata import (
    build_regime_state_dataset_metadata_registry,
)
from advanced_regime_matrix.regime_state_candidate_context import (
    build_regime_state_candidate_contexts,
)
from advanced_regime_matrix.regime_matrix_report_builder import (
    build_regime_state_dataset_contracts_markdown_report,
)
from reports.report_builder import build_regime_state_dataset_contract_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_matrix_profile()

    df_sc, s_sc = build_regime_state_dataset_contracts(profile)
    df_sch, s_sch = build_regime_state_dataset_schema()
    df_meta, s_meta = build_regime_state_dataset_metadata_registry()
    df_cand, s_cand = build_regime_state_candidate_contexts()

    data_lake.save_regime_state_dataset_contracts(df_sc, s_sc)
    data_lake.save_regime_state_dataset_schema(df_sch, s_sch)
    data_lake.save_regime_state_dataset_metadata(df_meta, s_meta)
    data_lake.save_regime_state_candidate_contexts(df_cand, s_cand)

    md_sc = build_regime_state_dataset_contracts_markdown_report(s_sc, df_sc)
    txt_sc = build_regime_state_dataset_contract_text_report(s_sc, df_sc)

    out_dir = Path("reports/output/advanced_regime_matrix")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "state_dataset_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_sc)
    with open(out_dir / "state_dataset_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_sc)

    print("=" * 70)
    print("PHASE 127: REGIME STATE DATASET CONTRACTS & CANDIDATE CONTEXTS")
    print("=" * 70)
    print(f"Total State Contracts: {s_sc['total_contracts']}")
    print(f"Candidate Contexts   : {s_cand['total_candidate_contexts']}")
    print(f"Contexts as Targets  : {s_cand['candidate_contexts_as_targets']}")
    print(f"State Schema Fields  : {s_sch['field_count']}")
    print(f"Contains Prediction  : {s_sc['any_target_or_prediction']}")
    print(f"Non-Signal Invariant : {s_sc['all_non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
