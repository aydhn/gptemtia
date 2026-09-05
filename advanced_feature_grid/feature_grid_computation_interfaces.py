from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any, List, Optional
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import (
    FeatureGridComputationResult,
    build_feature_grid_computation_result_id,
    FORBIDDEN_OUTPUT_WORDS,
)


class BaseFeatureGridComputer(ABC):
    """
    Güvenli, non-signal ve in-place mutasyonsuz feature grid hesaplama taban sınıfı.
    """

    def validate_input(self, df: pd.DataFrame, required_fields: List[str]) -> Dict[str, Any]:
        errors = []
        if df is None or not isinstance(df, pd.DataFrame):
            return {"valid": False, "errors": ["Girdi DataFrame geçerli değil."]}
        if df.empty:
            return {"valid": False, "errors": ["Girdi DataFrame boş."]}

        for rf in required_fields:
            if rf not in df.columns:
                errors.append(f"Zorunlu alan eksik: '{rf}'")

        return {
            "valid": len(errors) == 0,
            "row_count": len(df),
            "errors": errors,
        }

    @abstractmethod
    def compute_grid(
        self,
        df: pd.DataFrame,
        grid_name: str,
        parameter_grid: Optional[List[Dict[str, Any]]] = None,
    ) -> Tuple[pd.DataFrame, FeatureGridComputationResult]:
        """Alt sınıflar tarafından uygulanacak grid hesaplama metodu."""
        pass

    def metadata(self) -> Dict[str, Any]:
        return {
            "framework": "pandas/numpy",
            "pure_python": True,
            "ta_lib_required": False,
            "non_signal": True,
            "no_mutation": True,
        }


INTERFACE_CONTRACTS = [
    {
        "interface_name": "BaseFeatureGridComputer",
        "method": "validate_input",
        "signature": "(df: pd.DataFrame, required_fields: list[str]) -> dict",
        "description": "Girdi DataFrame'in boş olmadığını ve gerekli alanları içerdiğini doğrular.",
    },
    {
        "interface_name": "BaseFeatureGridComputer",
        "method": "compute_grid",
        "signature": "(df: pd.DataFrame, grid_name: str, parameter_grid: list[dict]) -> tuple[pd.DataFrame, FeatureGridComputationResult]",
        "description": "DataFrame'i mutate etmeden kopyası üzerinde çoklu window feature'ları üretir.",
    },
    {
        "interface_name": "BaseFeatureGridComputer",
        "method": "metadata",
        "signature": "() -> dict",
        "description": "Hesaplama motoru kısıtlarını ve metadata bilgilerini döner.",
    },
]


def build_feature_grid_computation_interface_contract(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(INTERFACE_CONTRACTS)
    summary = {
        "profile": active_profile.name,
        "total_interfaces": len(df),
        "in_place_mutation_prevented": True,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary
