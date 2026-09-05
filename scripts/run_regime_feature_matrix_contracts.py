"""Phase 127: Run Regime Feature Matrix Contracts Script.

Generates and saves feature matrix contracts, namespace registry, and schema definitions.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_matrix.regime_matrix_config import (
    get_default_regime_matrix_profile,
)
from advanced_regime_matrix.regime_feature_matrix_contracts import (
    build_regime_feature_matrix_contracts,
)
from advanced_regime_matrix.regime_matrix_namespace import (
    build_regime_matrix_namespace_registry,
)
from advanced_regime_matrix.regime_matrix_schema import (
    build_regime_matrix_schema,
)
from advanced_regime_matrix.regime_matrix_report_builder import (
    build_regime_feature_matrix_contracts_markdown_report,
)
from reports.report_builder import build_regime_feature_matrix_contract_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_matrix_profile()

    df_fc, s_fc = build_regime_feature_matrix_contracts(profile)
    df_ns, s_ns = build_regime_matrix_namespace_registry()
    df_sc, s_sc = build_regime_matrix_schema()

    data_lake.save_regime_feature_matrix_contracts(df_fc, s_fc)
    data_lake.save_regime_matrix_namespace_registry(df_ns, s_ns)
    data_lake.save_regime_matrix_schema(df_sc, s_sc)

    md_fc = build_regime_feature_matrix_contracts_markdown_report(s_fc, df_fc)
    txt_fc = build_regime_feature_matrix_contract_text_report(s_fc, df_fc)

    out_dir = Path("reports/output/advanced_regime_matrix")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "feature_matrix_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_fc)
    with open(out_dir / "feature_matrix_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_fc)

    print("=" * 70)
    print("PHASE 127: REGIME FEATURE MATRIX CONTRACTS & SCHEMA")
    print("=" * 70)
    print(f"Total Contracts: {s_fc['total_contracts']}")
    print(f"Ready Contracts: {s_fc['ready_contracts']}")
    print(f"Schema Columns : {s_sc['column_count']}")
    print(f"All Non-Signal : {s_fc['all_non_signal']}")
    print(f"Source Preserved: {s_fc['all_source_preserved']}")
    print(f"No Predictions : {not s_fc['any_target_or_prediction']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
