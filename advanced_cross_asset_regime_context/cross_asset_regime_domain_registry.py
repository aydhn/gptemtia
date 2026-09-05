"""Phase 131: Cross-Asset Regime Domain Registry.

Builds and registers functional domains for Cross-Asset Regime Context Expansion.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)
from advanced_cross_asset_regime_context.cross_asset_regime_labels import (
    CROSS_ASSET_REGIME_DOMAIN_LABELS,
)


def build_cross_asset_regime_domain_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of cross-asset regime functional domains."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for idx, domain_label in enumerate(CROSS_ASSET_REGIME_DOMAIN_LABELS, start=1):
        domain_name = domain_label.replace("_domain", "").replace("_", " ").title()
        rows.append(
            {
                "domain_index": idx,
                "domain_label": domain_label,
                "domain_name": domain_name,
                "current_phase": profile.current_phase,
                "target_final_phase": profile.target_final_phase,
                "non_signal": True,
                "source_preserved": True,
                "requires_no_lookahead": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_domains": len(df),
        "active_profile": profile.profile_name,
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "all_non_signal": bool(df["non_signal"].all()),
        "all_source_preserved": bool(df["source_preserved"].all()),
        "all_requires_no_lookahead": bool(df["requires_no_lookahead"].all()),
    }
    return df, summary
