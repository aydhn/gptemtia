"""Phase 127: Run Regime Matrix Timestamp Alignment and Guards Script.

Generates and saves timestamp alignment rules, asof join policies, no-lookahead audit, and forbidden column policies.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_matrix.regime_matrix_timestamp_alignment import (
    build_regime_matrix_timestamp_alignment_registry,
)
from advanced_regime_matrix.regime_matrix_asof_join_policies import (
    build_regime_matrix_asof_join_policies,
)
from advanced_regime_matrix.regime_matrix_no_lookahead_guard import (
    audit_dataframe_no_lookahead,
)
from advanced_regime_matrix.regime_matrix_forbidden_column_policies import (
    build_regime_matrix_forbidden_column_policies,
)


def main():
    data_lake = DataLake()

    df_align, s_align = build_regime_matrix_timestamp_alignment_registry()
    df_asof, s_asof = build_regime_matrix_asof_join_policies()
    df_forbid, s_forbid = build_regime_matrix_forbidden_column_policies()

    # Create dummy audit on clean baseline
    import pandas as pd
    clean_df = pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01", periods=5, freq="D", tz="UTC"),
        "entity_id": ["OIL_BRENT"] * 5,
        "canonical_symbol": ["BRENT"] * 5,
        "regime_matrix__volatility_atr_14": [1.2, 1.3, 1.1, 1.4, 1.2],
    })
    s_guard = audit_dataframe_no_lookahead(clean_df)

    data_lake.save_regime_matrix_timestamp_alignment(df_align, s_align)
    data_lake.save_regime_matrix_asof_join_policies(df_asof, s_asof)
    data_lake.save_regime_matrix_forbidden_column_policies(df_forbid, s_forbid)

    print("=" * 70)
    print("PHASE 127: REGIME MATRIX ALIGNMENT & LOOKAHEAD GUARDS")
    print("=" * 70)
    print(f"Alignment Rules     : {s_align['total_rules']}")
    print(f"Backward Only       : {s_align['backward_only_enforced']}")
    print(f"Asof Join Policies  : {s_asof['total_policies']}")
    print(f"Forbidden Col Types : {s_forbid['total_forbidden_column_types']}")
    print(f"No-Lookahead Audit  : {s_guard['guard_passed']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
