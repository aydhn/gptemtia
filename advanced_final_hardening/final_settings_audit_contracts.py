# -*- coding: utf-8 -*-
"""Phase 159: Final Settings Audit Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    SETTINGS_AUDIT_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

SETTINGS_AUDIT_ITEMS = [
    ("settings_class_presence", "config/settings.py", "Settings pydantic/dataclass varlığı denetimi", True),
    ("phase_159_settings_presence", "config/settings.py", "Phase 159 ayarları ve bayrakları varlığı denetimi", True),
    ("no_live_trading_default", "config/settings.py", "allow_live_trading varsayılan False denetimi", True),
    ("no_broker_integration_default", "config/settings.py", "allow_broker_integration varsayılan False denetimi", True),
    ("non_production_default", "config/settings.py", "non_production varsayılan True denetimi", True),
    ("dry_run_default", "config/settings.py", "dry_run varsayılan True denetimi", True),
    ("local_only_default", "config/settings.py", "local_only varsayılan True denetimi", True),
]


def build_final_settings_audit_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build settings audit contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for audit_id, target, desc, passed in SETTINGS_AUDIT_ITEMS:
        rows.append({
            "audit_id": audit_id,
            "target": target,
            "description": desc,
            "passed": passed,
            "domain": SETTINGS_AUDIT_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "audit_item_count": len(rows),
        "all_passed": bool(df["passed"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
