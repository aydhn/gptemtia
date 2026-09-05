import sys
import pandas as pd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_validation.indicator_output_validation import validate_indicator_outputs
from advanced_feature_validation.feature_grid_output_validation import validate_feature_grid_outputs
from advanced_feature_validation.cross_asset_alignment_output_validation import validate_cross_asset_alignment_outputs
from advanced_feature_validation.fusion_feature_output_validation import validate_fusion_feature_outputs


def main():
    settings = get_settings()
    data_lake = DataLake()

    dummy_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5, freq="D"),
        "asset_symbol": ["BRENT"] * 5,
        "indicator_rsi_14": [50.0, 52.1, 48.9, 53.4, 55.0],
    })

    ind_res = validate_indicator_outputs(dummy_df)
    grid_res = validate_feature_grid_outputs(dummy_df)
    align_res = validate_cross_asset_alignment_outputs(dummy_df)
    fusion_res = validate_fusion_feature_outputs(dummy_df)

    data_lake.save_indicator_output_validation_registry(ind_res)
    data_lake.save_feature_grid_output_validation_registry(grid_res)
    data_lake.save_cross_asset_alignment_output_validation_registry(align_res)
    data_lake.save_fusion_feature_output_validation_registry(fusion_res)

    print("=" * 70)
    print("PHASE 121: DOMAIN FEATURE OUTPUT VALIDATION")
    print("=" * 70)
    print(f"Indicator Outputs Valid    : {ind_res['is_valid']}")
    print(f"Feature Grid Outputs Valid : {grid_res['is_valid']}")
    print(f"Cross-Asset Outputs Valid  : {align_res['is_valid']}")
    print(f"Fusion Feature Valid       : {fusion_res['is_valid']}")
    print(f"Current Phase              : 121")
    print(f"Next Phase                 : 122")
    print("=" * 70)


if __name__ == "__main__":
    main()
