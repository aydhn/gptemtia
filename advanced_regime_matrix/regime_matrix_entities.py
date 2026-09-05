"""Phase 127: Regime Matrix Entities Registry.

Defines canonical entity types and mappings involved in regime feature matrix construction.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

CANONICAL_ENTITIES: List[Dict[str, Any]] = [
    {
        "entity_type": "fx_pair",
        "canonical_prefix": "fx",
        "description": "Foreign exchange currency pairs (e.g. EUR/USD, USD/TRY).",
        "source_phases": [107, 113, 116, 117, 118, 119, 124, 126],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "commodity_symbol",
        "canonical_prefix": "cmd",
        "description": "Commodity spot and continuous contract symbols (e.g. XAU/USD, BRENT).",
        "source_phases": [108, 113, 116, 117, 118, 119, 124, 126],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "macro_indicator",
        "canonical_prefix": "macro",
        "description": "Macroeconomic time-series indicators (e.g. US10Y, FEDFUNDS, CPI).",
        "source_phases": [109, 113, 120, 122, 124, 126],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "calendar_event",
        "canonical_prefix": "event",
        "description": "Economic calendar scheduled announcements and releases.",
        "source_phases": [110, 113, 120, 122, 124, 126],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "news_metadata_tag",
        "canonical_prefix": "news",
        "description": "Metadata-only news category, asset, and intensity tags (strictly zero full text).",
        "source_phases": [111, 113, 120, 122, 124, 126],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "cross_asset_context",
        "canonical_prefix": "cross",
        "description": "Intermarket coupling and relative spread relationships.",
        "source_phases": [119, 120, 122, 124, 126],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "factor_family",
        "canonical_prefix": "factor",
        "description": "Standard factor families from Phase 122 metadata (trend, vol, macro, etc.).",
        "source_phases": [122, 123, 124, 126],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "regime_family",
        "canonical_prefix": "regime",
        "description": "Master and specialized regime families from Phase 126 foundation.",
        "source_phases": [126],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "regime_state_candidate_context",
        "canonical_prefix": "candidate",
        "description": "Research candidate context indicators for Phase 128 preparation.",
        "source_phases": [126, 127],
        "status": "matrix_ready",
        "non_signal": True,
        "source_preserved": True,
    },
]


def build_regime_matrix_entity_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the entity registry for regime feature matrices."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for ent in CANONICAL_ENTITIES:
        ent_copy = ent.copy()
        ent_copy["current_phase"] = p.current_phase
        ent_copy["target_final_phase"] = p.target_final_phase
        ent_copy["next_phase"] = p.next_phase
        rows.append(ent_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_entities(df)
    return df, summary


def summarize_regime_matrix_entities(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime matrix entities."""
    return {
        "total_entities": len(df),
        "entity_types": df["entity_type"].tolist() if not df.empty else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_entities_registry = build_regime_matrix_entity_registry
