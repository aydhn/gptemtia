from typing import Tuple, Dict, Any, Optional, List
from abc import ABC, abstractmethod
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile
from advanced_technical_indicators.technical_indicator_models import IndicatorComputationResult


class BaseTechnicalIndicatorComputer(ABC):
    """Abstract base contract for non-signal technical indicator calculation."""

    @abstractmethod
    def validate_input(self, df: pd.DataFrame, required_fields: List[str]) -> Dict[str, Any]:
        """Validate input DataFrame contains required fields and numeric data."""
        pass

    @abstractmethod
    def compute(
        self,
        df: pd.DataFrame,
        indicator_name: str,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Tuple[pd.DataFrame, IndicatorComputationResult]:
        """Compute indicator features without mutating df, returning copy and result metadata."""
        pass

    @abstractmethod
    def metadata(self) -> Dict[str, Any]:
        """Return computer metadata and supported indicators."""
        pass


def build_indicator_computation_interface_contract(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {
            "interface_name": "BaseTechnicalIndicatorComputer",
            "method": "validate_input(df, required_fields)",
            "contract": "Returns dict with valid=bool and errors=list",
        },
        {
            "interface_name": "BaseTechnicalIndicatorComputer",
            "method": "compute(df, indicator_name, parameters)",
            "contract": "Returns tuple(out_df, IndicatorComputationResult); immutable input",
        },
        {
            "interface_name": "BaseTechnicalIndicatorComputer",
            "method": "metadata()",
            "contract": "Returns dict with provider, non_signal=True, phase=117",
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_interface_methods": len(df),
        "interface_ready": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
