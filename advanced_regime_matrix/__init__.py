"""Phase 127: Regime Feature Matrix and State Dataset Contracts Layer.

Provides feature matrix contracts, non-signal regime state dataset schemas,
timestamp alignment and backward-only asof join policies, no-lookahead guards,
candidate context specifications, matrix integrity manifest, and Phase 128 handoff.
"""

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_regime_matrix_profile,
    list_regime_matrix_profiles,
    validate_regime_matrix_profiles,
    get_default_regime_matrix_profile,
)

__all__ = [
    "RegimeMatrixProfile",
    "get_regime_matrix_profile",
    "list_regime_matrix_profiles",
    "validate_regime_matrix_profiles",
    "get_default_regime_matrix_profile",
]
