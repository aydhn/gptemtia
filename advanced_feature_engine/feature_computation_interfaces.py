from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureInputContract,
    FeatureSchema,
    FeatureComputationResult,
    build_feature_computation_result_id,
)
from advanced_feature_engine.feature_input_contracts import validate_feature_input_contract


class BaseFeatureComputer(ABC):
    """Abstract base class for non-signal feature computers."""

    def validate_input(
        self,
        df: pd.DataFrame,
        contract: FeatureInputContract,
    ) -> Dict[str, Any]:
        return validate_feature_input_contract(df, contract.dataset_type)

    @abstractmethod
    def compute(
        self,
        df: pd.DataFrame,
        feature_schema: FeatureSchema,
    ) -> Tuple[pd.DataFrame, FeatureComputationResult]:
        """Must return a new dataframe copy with computed feature and result metadata.

        Must NEVER mutate the input dataframe.
        Must NEVER produce signal, target, position, or label columns.
        """
        pass

    def metadata(self) -> Dict[str, Any]:
        return {
            "computer_name": self.__class__.__name__,
            "non_signal": True,
            "lookahead_safe": True,
            "pure_dataframe_transform": True,
        }


def build_feature_computation_interface_contract(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = [
        {
            "contract_rule": "non_destructive_copy",
            "description": "Girdi dataframe'i mutate edilmez; her zaman df.copy() ile yeni dataframe döner.",
            "enforced": True,
        },
        {
            "contract_rule": "no_signal_columns",
            "description": "signal, buy, sell, long, short, position, target, label üretilmez.",
            "enforced": True,
        },
        {
            "contract_rule": "no_lookahead_bias",
            "description": "shift(-1) veya geleceğe dönük veri indeksleme kesinlikle yasaktır.",
            "enforced": True,
        },
        {
            "contract_rule": "pure_pandas_numpy",
            "description": "Dış C kütüphanesi veya ta-lib zorunluluğu olmadan saf pandas/numpy dönüşümleri.",
            "enforced": True,
        },
        {
            "contract_rule": "graceful_error_handling",
            "description": "Eksik alan durumunda graceful hata veya açıklayıcı istisna fırlatır.",
            "enforced": True,
        },
    ]
    df = pd.DataFrame.from_records(records)
    summary = {
        "total_rules": len(df),
        "all_enforced": bool(df["enforced"].all()),
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
