# -*- coding: utf-8 -*-
"""Phase 148: Scenario Output Contracts.

Provides specifications and registry for scenario simulation contract outputs.
Guarantees zero performance claims, zero scenario ranking/recommendation, and contract-only metadata.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

SCENARIO_OUTPUT_FIELDS: List[Dict[str, Any]] = [
    {"field_name": "scenario_id", "data_type": "string", "allowed": True, "description": "Senaryo kütüphanesi kimliği."},
    {"field_name": "scenario_contract_ready", "data_type": "boolean", "allowed": True, "description": "Senaryo sözleşmesinin hazır olma durumu."},
    {"field_name": "manual_review_required", "data_type": "boolean", "allowed": True, "description": "Manuel inceleme zorunluluğu bayrağı."},
    {"field_name": "actual_scenario_return", "data_type": "float", "allowed": False, "description": "YASAKLI: Gerçek senaryo getirisi üretilemez."},
    {"field_name": "actual_scenario_win_rate", "data_type": "float", "allowed": False, "description": "YASAKLI: Gerçek kazanma oranı üretilemez."},
    {"field_name": "strategy_recommendation", "data_type": "string", "allowed": False, "description": "YASAKLI: Senaryo bazlı yatırım tavsiyesi üretilemez."},
]


def build_scenario_output_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of scenario output schema contracts."""
    rows: List[Dict[str, Any]] = []
    for f in SCENARIO_OUTPUT_FIELDS:
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
