# -*- coding: utf-8 -*-
"""Phase 142: Run Drift Monitoring Contracts Script."""

import sys
from dataclasses import asdict
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.model_drift_monitoring_contracts import (
    build_model_drift_monitoring_contracts,
)
from advanced_model_drift_monitoring.data_drift_monitoring_contracts import (
    build_data_drift_monitoring_contracts,
)
from advanced_model_drift_monitoring.feature_drift_monitoring_contracts import (
    build_feature_drift_monitoring_contracts,
)
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    model_contracts = build_model_drift_monitoring_contracts()
    df_model = pd.DataFrame([asdict(c) for c in model_contracts])
    data_lake.save_model_drift_monitoring_contract_registry(df_model, {"total_model_contracts": len(model_contracts)})

    data_contracts = build_data_drift_monitoring_contracts()
    df_data = pd.DataFrame([asdict(c) for c in data_contracts])
    data_lake.save_data_drift_monitoring_contract_registry(df_data, {"total_data_contracts": len(data_contracts)})

    feature_contracts = build_feature_drift_monitoring_contracts()
    df_feat = pd.DataFrame([asdict(c) for c in feature_contracts])
    data_lake.save_feature_drift_monitoring_contract_registry(df_feat, {"total_feature_contracts": len(feature_contracts)})

    print("=" * 70)
    print("PHASE 142: MODEL, DATA & FEATURE DRIFT MONITORING CONTRACTS")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Model Drift Contracts   : {len(model_contracts)}")
    print(f"Data Drift Contracts    : {len(data_contracts)}")
    print(f"Feature Drift Contracts : {len(feature_contracts)}")
    print("All Contracts Status    : NON-EXECUTING (Contract-Only)")
    print("=" * 70)


if __name__ == "__main__":
    main()
