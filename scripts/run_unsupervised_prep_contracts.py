"""Phase 128: Run Unsupervised Prep Contracts Script.

Generates unsupervised preparation contracts, clustering inputs, and algorithm placeholders.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.unsupervised_prep_contracts import (
    build_unsupervised_prep_contract_registry,
)
from advanced_regime_rule_free.clustering_input_contracts import (
    build_clustering_input_contract_registry,
)
from advanced_regime_rule_free.clustering_algorithm_placeholders import (
    build_clustering_algorithm_placeholder_registry,
)
from advanced_regime_rule_free.distance_metric_placeholders import (
    build_distance_metric_placeholder_registry,
)
from advanced_regime_rule_free.normalization_prep_contracts import (
    build_normalization_prep_contract_registry,
)
from advanced_regime_rule_free.scaling_prep_contracts import (
    build_scaling_prep_contract_registry,
)
from advanced_regime_rule_free.dimensionality_reduction_placeholders import (
    build_dimensionality_reduction_placeholder_registry,
)
from advanced_regime_rule_free.regime_rule_free_report_builder import (
    build_unsupervised_prep_contract_markdown_report,
)
from reports.report_builder import build_unsupervised_prep_contract_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_rule_free_profile()

    df_prep, s_prep = build_unsupervised_prep_contract_registry(profile)
    df_cinp, s_cinp = build_clustering_input_contract_registry(profile)
    df_calg, s_calg = build_clustering_algorithm_placeholder_registry(profile)
    df_dist, s_dist = build_distance_metric_placeholder_registry(profile)
    df_norm, s_norm = build_normalization_prep_contract_registry(profile)
    df_scal, s_scal = build_scaling_prep_contract_registry(profile)
    df_dimr, s_dimr = build_dimensionality_reduction_placeholder_registry(profile)

    data_lake.save_unsupervised_prep_contract_registry(df_prep, s_prep)
    data_lake.save_clustering_input_contract_registry(df_cinp, s_cinp)
    data_lake.save_clustering_algorithm_placeholder_registry(df_calg, s_calg)
    data_lake.save_distance_metric_placeholder_registry(df_dist, s_dist)
    data_lake.save_normalization_prep_contract_registry(df_norm, s_norm)
    data_lake.save_scaling_prep_contract_registry(df_scal, s_scal)
    data_lake.save_dimensionality_reduction_placeholder_registry(df_dimr, s_dimr)

    md_prep = build_unsupervised_prep_contract_markdown_report(s_prep, df_prep)
    txt_prep = build_unsupervised_prep_contract_text_report(s_prep, df_prep)

    out_dir = Path("reports/output/advanced_regime_rule_free")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "unsupervised_prep_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_prep)
    with open(out_dir / "unsupervised_prep_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_prep)

    print("=" * 70)
    print("PHASE 128: UNSUPERVISED PREP & ALGORITHM PLACEHOLDERS")
    print("=" * 70)
    print(f"Total Prep Contracts   : {s_prep['total_prep_contracts']}")
    print(f"Clustering Input Specs : {s_cinp['total_clustering_input_contracts']}")
    print(f"Algorithm Placeholders : {s_calg['total_algorithm_placeholders']}")
    print(f"Distance Metrics       : {s_dist['total_distance_metrics']}")
    print(f"Normalization Contracts: {s_norm['total_normalization_contracts']}")
    print(f"Scaling Contracts      : {s_scal['total_scaling_contracts']}")
    print(f"Dim Reduction Placeh.  : {s_dimr['total_dim_reduction_placeholders']}")
    print(f"Clustering Executed    : False")
    print("=" * 70)


if __name__ == "__main__":
    main()
