# -*- coding: utf-8 -*-
"""Phase 140: Run Ensemble Strategy Contracts Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.ensemble_strategy_contracts import (
    build_ensemble_strategy_contracts,
    summarize_ensemble_strategy_contracts,
)
from advanced_ensemble_model_registry.ensemble_voting_placeholders import (
    build_ensemble_voting_placeholders,
    summarize_ensemble_voting_placeholders,
)
from advanced_ensemble_model_registry.ensemble_blending_placeholders import (
    build_ensemble_blending_placeholders,
    summarize_ensemble_blending_placeholders,
)
from advanced_ensemble_model_registry.ensemble_stacking_placeholders import (
    build_ensemble_stacking_placeholders,
    summarize_ensemble_stacking_placeholders,
)
from advanced_ensemble_model_registry.ensemble_weighting_policy_placeholders import (
    build_ensemble_weighting_policy_placeholders,
    summarize_ensemble_weighting_policy_placeholders,
)
from advanced_ensemble_model_registry.ensemble_meta_model_placeholders import (
    build_ensemble_meta_model_placeholders,
    summarize_ensemble_meta_model_placeholders,
)
from advanced_ensemble_model_registry.ensemble_selection_policies import (
    build_ensemble_selection_policies,
    summarize_ensemble_selection_policies,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_strat, s_strat = build_ensemble_strategy_contracts()
    data_lake.save_ensemble_strategy_contract_registry(df_strat, s_strat)

    df_vot, s_vot = build_ensemble_voting_placeholders()
    data_lake.save_ensemble_voting_placeholder_registry(df_vot, s_vot)

    df_blend, s_blend = build_ensemble_blending_placeholders()
    data_lake.save_ensemble_blending_placeholder_registry(df_blend, s_blend)

    df_stack, s_stack = build_ensemble_stacking_placeholders()
    data_lake.save_ensemble_stacking_placeholder_registry(df_stack, s_stack)

    df_w, s_w = build_ensemble_weighting_policy_placeholders()
    data_lake.save_ensemble_weighting_policy_placeholder_registry(df_w, s_w)

    df_meta, s_meta = build_ensemble_meta_model_placeholders()
    data_lake.save_ensemble_meta_model_placeholder_registry(df_meta, s_meta)

    df_pol, s_pol = build_ensemble_selection_policies()
    data_lake.save_ensemble_selection_policy_registry(df_pol, s_pol)

    print("=" * 70)
    print("PHASE 140: ENSEMBLE STRATEGY CONTRACTS & PLACEHOLDERS")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Strategy Contracts   : {s_strat.get('total_strategies', len(df_strat))}")
    print(f"Voting Execution     : Allowed={not s_strat.get('all_voting_disabled', True)}")
    print(f"Blending Execution   : Allowed={not s_strat.get('all_blending_disabled', True)}")
    print(f"Stacking Execution   : Allowed={not s_strat.get('all_stacking_disabled', True)}")
    print(f"All Non-Signal       : {s_strat.get('all_non_signal_required', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()

