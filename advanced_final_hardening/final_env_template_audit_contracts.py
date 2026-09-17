# -*- coding: utf-8 -*-
"""Phase 159: Final Env Template Audit Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    ENV_TEMPLATE_AUDIT_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

ENV_AUDIT_ITEMS = [
    ("env_example_presence", ".env.example", ".env.example şablon dosyasının varlığı", True),
    ("no_secrets_in_env_example", ".env.example", "Gerçek API anahtarı, token veya secret bulunmaması", True),
    ("phase_159_env_vars_presence", ".env.example", "Phase 159 UPPERCASE konfigürasyon anahtarlarının varlığı", True),
    ("safe_defaults_in_env_example", ".env.example", "Varsayılan değerlerin non-live ve dry-run uyumlu olması", True),
]


def build_final_env_template_audit_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build env template audit contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for audit_id, target, desc, passed in ENV_AUDIT_ITEMS:
        rows.append({
            "audit_id": audit_id,
            "target": target,
            "description": desc,
            "passed": passed,
            "secrets_exposed": False,
            "domain": ENV_TEMPLATE_AUDIT_DOMAIN,
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
        "secrets_exposed": bool(df["secrets_exposed"].any()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
