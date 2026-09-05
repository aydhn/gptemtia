"""Phase 122 Factor Metadata Domain Registry.

Constructs registry records for all factor metadata and taxonomy domains.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import (
    FACTOR_METADATA_DOMAINS,
    FACTOR_READY,
)


def build_factor_metadata_domain_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Metadata Domain Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records: List[Dict[str, Any]] = []
    for domain in FACTOR_METADATA_DOMAINS:
        records.append(
            {
                "domain_label": domain,
                "domain_name": domain.replace("_", " ").title(),
                "current_phase": active_profile.current_phase,
                "target_final_phase": active_profile.target_final_phase,
                "next_phase": active_profile.next_phase,
                "non_signal": True,
                "status_label": FACTOR_READY,
                "local_only": active_profile.local_only,
                "dry_run": active_profile.dry_run_default,
            }
        )

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_domains": len(records),
        "non_signal": True,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "status": FACTOR_READY,
    }
    return df, summary
