# -*- coding: utf-8 -*-
"""Phase 140: Run Ensemble Dependencies, Lineage, and Inputs Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.ensemble_input_contracts import (
    build_ensemble_input_contracts,
    summarize_ensemble_input_contracts,
)
from advanced_ensemble_model_registry.ensemble_output_contracts import (
    build_ensemble_output_contracts,
    summarize_ensemble_output_contracts,
)
from advanced_ensemble_model_registry.ensemble_validation_dependencies import (
    build_ensemble_validation_dependencies,
    summarize_ensemble_validation_dependencies,
)
from advanced_ensemble_model_registry.ensemble_quality_dependencies import (
    build_ensemble_quality_dependencies,
    summarize_ensemble_quality_dependencies,
)
from advanced_ensemble_model_registry.ensemble_lineage import (
    build_ensemble_lineage,
    summarize_ensemble_lineage,
)
from advanced_ensemble_model_registry.ensemble_experiment_linkage import (
    build_ensemble_experiment_linkage,
    summarize_ensemble_experiment_linkage,
)
from advanced_ensemble_model_registry.ensemble_no_lookahead_guards import (
    build_ensemble_no_lookahead_guards,
    summarize_ensemble_no_lookahead_guards,
)
from advanced_ensemble_model_registry.ensemble_metadata_only_news_guards import (
    build_ensemble_metadata_only_news_guards,
    summarize_ensemble_metadata_only_news_guards,
)
from advanced_ensemble_model_registry.ensemble_source_preservation_guards import (
    build_ensemble_source_preservation_guards,
    summarize_ensemble_source_preservation_guards,
)
from advanced_ensemble_model_registry.ensemble_forbidden_column_policies import (
    summarize_ensemble_forbidden_column_policy,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    ens_inputs = build_ensemble_input_contracts()
    s_inp = summarize_ensemble_input_contracts(ens_inputs)
    df_inp = pd.DataFrame([{"contract_name": k, **v} for k, v in ens_inputs.items()])
    data_lake.save_ensemble_input_contract_registry(df_inp, s_inp)

    ens_outputs = build_ensemble_output_contracts()
    s_out = summarize_ensemble_output_contracts(ens_outputs)
    df_out = pd.DataFrame([{"contract_name": k, **v} for k, v in ens_outputs.items()])
    data_lake.save_ensemble_output_contract_registry(df_out, s_out)

    val_deps = build_ensemble_validation_dependencies()
    s_val = summarize_ensemble_validation_dependencies(val_deps)
    df_val = pd.DataFrame([{"dep_name": k, **v} for k, v in val_deps.items()])
    data_lake.save_ensemble_validation_dependency_registry(df_val, s_val)

    qual_deps = build_ensemble_quality_dependencies()
    s_qual = summarize_ensemble_quality_dependencies(qual_deps)
    df_qual = pd.DataFrame([{"dep_name": k, **v} for k, v in qual_deps.items()])
    data_lake.save_ensemble_quality_dependency_registry(df_qual, s_qual)

    lineage = build_ensemble_lineage()
    s_lin = summarize_ensemble_lineage(lineage)
    df_lin = pd.DataFrame(lineage.get("stages", []))
    data_lake.save_ensemble_lineage_registry(df_lin, s_lin)

    exp_link = build_ensemble_experiment_linkage()
    s_exp = summarize_ensemble_experiment_linkage(exp_link)
    df_exp = pd.DataFrame([{"linkage_key": k, **v} for k, v in exp_link.items()])
    data_lake.save_ensemble_experiment_linkage_registry(df_exp, s_exp)

    look_guards = build_ensemble_no_lookahead_guards()
    s_look = summarize_ensemble_no_lookahead_guards(look_guards)
    df_look = pd.DataFrame([{"guard_key": k, **v} for k, v in look_guards.items()])
    data_lake.save_ensemble_no_lookahead_guard_registry(df_look, s_look)

    news_guards = build_ensemble_metadata_only_news_guards()
    s_news = summarize_ensemble_metadata_only_news_guards(news_guards)
    df_news = pd.DataFrame([{"guard_key": k, **v} for k, v in news_guards.items()])
    data_lake.save_ensemble_metadata_only_news_guard_registry(df_news, s_news)

    src_guards = build_ensemble_source_preservation_guards()
    s_src = summarize_ensemble_source_preservation_guards(src_guards)
    df_src = pd.DataFrame([{"guard_key": k, **v} for k, v in src_guards.items()])
    data_lake.save_ensemble_source_preservation_guard_registry(df_src, s_src)

    s_forbid = summarize_ensemble_forbidden_column_policy()
    df_forbid = pd.DataFrame([{"pattern": p} for p in s_forbid.get("patterns", [])])
    data_lake.save_ensemble_forbidden_column_policy_registry(df_forbid, s_forbid)

    print("=" * 70)
    print("PHASE 140: ENSEMBLE DEPENDENCIES, LINEAGE & GUARDS")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Dependencies : {s_val['total_dependencies']}")
    print(f"Quality Dependencies    : {s_qual['total_dependencies']}")
    print(f"Lineage Stages          : {s_lin['total_stages']}")
    print(f"Experiments Linked      : {s_exp['total_experiments_linked']}")
    print(f"Lookahead Guards Safe   : {s_look['zero_leakage_guaranteed']}")
    print(f"Metadata Only News Safe : {s_news['raw_text_prohibited']}")
    print(f"Forbidden Patterns Count: {s_forbid['forbidden_patterns_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
