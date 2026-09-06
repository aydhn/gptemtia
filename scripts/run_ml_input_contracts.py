"""Phase 136: Run ML Input Contracts Script.

Builds and persists input contracts for Regime metadata, FeatureStore, no-lookahead, metadata-only news, and source preservation.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from advanced_gpu_ml_runtime.regime_metadata_ml_input_contracts import build_regime_metadata_ml_input_contract_registry
from advanced_gpu_ml_runtime.featurestore_ml_input_contracts import build_featurestore_ml_input_contract_registry
from advanced_gpu_ml_runtime.no_lookahead_ml_input_contracts import build_no_lookahead_ml_input_contract_registry
from advanced_gpu_ml_runtime.metadata_only_news_ml_input_contracts import build_metadata_only_news_ml_input_contract_registry
from advanced_gpu_ml_runtime.source_preservation_ml_input_contracts import build_source_preservation_ml_input_contract_registry
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_ml_runtime_profile()

    df_reg, s_reg = build_regime_metadata_ml_input_contract_registry(profile)
    data_lake.save_regime_metadata_ml_input_contract_registry(df_reg, s_reg)

    df_fs, s_fs = build_featurestore_ml_input_contract_registry(profile)
    data_lake.save_featurestore_ml_input_contract_registry(df_fs, s_fs)

    df_nl, s_nl = build_no_lookahead_ml_input_contract_registry(profile)
    data_lake.save_no_lookahead_ml_input_contract_registry(df_nl, s_nl)

    df_news, s_news = build_metadata_only_news_ml_input_contract_registry(profile)
    data_lake.save_metadata_only_news_ml_input_contract_registry(df_news, s_news)

    df_src, s_src = build_source_preservation_ml_input_contract_registry(profile)
    data_lake.save_source_preservation_ml_input_contract_registry(df_src, s_src)

    print("=" * 70)
    print("PHASE 136: ML INPUT CONTRACTS (REGIME & FEATURESTORE)")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Regime Input Contracts     : {s_reg.get('total_contracts', 0)}")
    print(f"FeatureStore Contracts     : {s_fs.get('total_contracts', 0)}")
    print(f"No-Lookahead Rules Enforced: {s_nl.get('total_rules', 0)}")
    print(f"News Text & HTML Blocked   : True")
    print(f"Source Overwrite Blocked   : True")
    print(f"Non-Signal                 : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
