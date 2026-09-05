"""Phase 127: Run Regime Matrix Input Registries Script.

Generates and saves input features, factor inputs, context inputs, and quality inputs registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_matrix.regime_matrix_config import (
    get_default_regime_matrix_profile,
)
from advanced_regime_matrix.regime_matrix_input_features import (
    build_regime_matrix_input_features_registry,
)
from advanced_regime_matrix.regime_matrix_factor_inputs import (
    build_regime_matrix_factor_inputs_registry,
)
from advanced_regime_matrix.regime_matrix_context_inputs import (
    build_regime_matrix_context_inputs_registry,
)
from advanced_regime_matrix.regime_matrix_quality_inputs import (
    build_regime_matrix_quality_inputs_registry,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_matrix_profile()

    df_feat, s_feat = build_regime_matrix_input_features_registry()
    df_fact, s_fact = build_regime_matrix_factor_inputs_registry()
    df_ctx, s_ctx = build_regime_matrix_context_inputs_registry()
    df_qual, s_qual = build_regime_matrix_quality_inputs_registry()

    data_lake.save_regime_matrix_input_features(df_feat, s_feat)
    data_lake.save_regime_matrix_factor_inputs(df_fact, s_fact)
    data_lake.save_regime_matrix_context_inputs(df_ctx, s_ctx)
    data_lake.save_regime_matrix_quality_inputs(df_qual, s_qual)

    print("=" * 70)
    print("PHASE 127: REGIME MATRIX INPUT REGISTRIES")
    print("=" * 70)
    print(f"Technical Features : {s_feat['total_features']}")
    print(f"Factor Inputs      : {s_fact['total_factors']}")
    print(f"Context Inputs     : {s_ctx['total_contexts']}")
    print(f"Quality Inputs     : {s_qual['total_quality_inputs']}")
    print(f"All Non-Signal     : {s_feat['all_non_signal'] and s_fact['all_non_signal']}")
    print(f"No Article Text    : {s_ctx['no_article_text_guaranteed']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
