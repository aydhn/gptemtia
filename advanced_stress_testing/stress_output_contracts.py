# -*- coding: utf-8 -*-
"""Phase 148: Stress Output Contracts.

Provides specifications and registry for stress testing contract outputs.
Guarantees zero realized returns, zero stressed PnL, zero live signals, and contract-only metadata.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

STRESS_OUTPUT_FIELDS: List[Dict[str, Any]] = [
    {"field_name": "contract_name", "data_type": "string", "allowed": True, "description": "Doğrulanan stres sözleşmesi adı."},
    {"field_name": "contract_validation_status", "data_type": "string", "allowed": True, "description": "Sözleşme doğrulama durumu (stress_contract_ready vb.)."},
    {"field_name": "blocked_reason", "data_type": "string", "allowed": True, "description": "Yürütme engelleme gerekçesi."},
    {"field_name": "manual_review_required", "data_type": "boolean", "allowed": True, "description": "Operatör inceleme zorunluluğu bayrağı."},
    {"field_name": "non_signal", "data_type": "boolean", "allowed": True, "description": "Sinyal üretilmediği garantisi."},
    {"field_name": "actual_stressed_pnl", "data_type": "float", "allowed": False, "description": "YASAKLI: Gerçek stres PnL değeri üretilemez."},
    {"field_name": "actual_stressed_drawdown", "data_type": "float", "allowed": False, "description": "YASAKLI: Gerçek stres drawdown değeri üretilemez."},
    {"field_name": "actual_var", "data_type": "float", "allowed": False, "description": "YASAKLI: Gerçek VaR değeri üretilemez."},
    {"field_name": "trading_signal", "data_type": "string", "allowed": False, "description": "YASAKLI: AL/SAT sinyali üretilemez."},
]


def build_stress_output_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress output schema contracts."""
    rows: List[Dict[str, Any]] = []
    for f in STRESS_OUTPUT_FIELDS:
        rows.append(
            {
                "field_name": f["field_name"],
                "data_type": f["data_type"],
                "allowed": f["allowed"],
                "description": f["description"],
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_fields": len(df),
        "allowed_field_count": int(df["allowed"].sum()),
        "prohibited_field_count": int((~df["allowed"]).sum()),
        "all_prohibited_enforced": True,
        "non_signal": True,
    }
    return df, summary
