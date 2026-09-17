# -*- coding: utf-8 -*-
"""Phase 146: Backtest Dependencies.

Tracks foundational dependencies inherited from Phase 1-145 required for realistic backtest contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

DEPENDENCIES: List[Dict[str, Any]] = [
    {"source_phase": 145, "dependency_name": "advanced_ml_acceptance", "description": "Phase 145 Advanced ML Acceptance Report ve kabul kanitlari.", "satisfied": True},
    {"source_phase": 137, "dependency_name": "advanced_ml_dataset_registry", "description": "Phase 137 veri seti sozlesmeleri ve oznitelik anlik goruntuleri.", "satisfied": True},
    {"source_phase": 134, "dependency_name": "advanced_regime_featurestore_integration", "description": "Phase 134 Rejim FeatureStore ve point-in-time erisim sozlesmeleri.", "satisfied": True},
    {"source_phase": 135, "dependency_name": "advanced_regime_acceptance", "description": "Phase 135 rejim kabul ve piyasa davranisi siniflandirma altyapisi.", "satisfied": True},
    {"source_phase": 123, "dependency_name": "advanced_feature_quality_drift", "description": "Phase 123 oznitelik kalitesi ve kayma teshisleri.", "satisfied": True},
    {"source_phase": 139, "dependency_name": "advanced_gpu_training_governance", "description": "Phase 139 GPU kaynak yonetimi ve egitim sinirlari.", "satisfied": True},
    {"source_phase": 144, "dependency_name": "advanced_model_governance", "description": "Phase 144 model yonetisimi ve onay sinirlari.", "satisfied": True},
    {"source_phase": 121, "dependency_name": "no_lookahead_infrastructure", "description": "Lookahead onleme ve zaman damgasi muhafiz altyapisi.", "satisfied": True},
    {"source_phase": 114, "dependency_name": "source_preservation_infrastructure", "description": "Ham veri degismezligi ve kaynagi koruma altyapisi.", "satisfied": True},
]


def build_backtest_dependency_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of backtest dependencies."""
    rows = []
    for d in DEPENDENCIES:
        rows.append(
            {
                "source_phase": d["source_phase"],
                "dependency_name": d["dependency_name"],
                "description": d["description"],
                "satisfied": d["satisfied"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_dependencies(df)
    return df, summary


def summarize_backtest_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize backtest dependencies."""
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool(df["satisfied"].all()) if not df.empty else True,
        "satisfied_count": int(df["satisfied"].sum()) if not df.empty else 0,
        "non_signal": True,
    }
