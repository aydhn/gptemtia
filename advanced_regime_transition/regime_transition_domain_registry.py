"""Phase 130: Regime Transition Domain Registry.

Builds master domain registry cataloging all sub-domains within Phase 130.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)


def build_regime_transition_domain_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build domain registry dataframe and summary for Phase 130."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    domains = [
        ("state_sequence_contracts", "State Sequence Contracts", "Contracts governing candidate/pseudo state sequences"),
        ("candidate_sequence_schema", "Candidate Sequence Schema", "Tabular schema definition for candidate state sequences"),
        ("pseudo_sequence_schema", "Pseudo Sequence Schema", "Tabular schema definition for pseudo state sequences (zero-ML)"),
        ("transition_metrics", "Transition Metrics", "Specifications of transition frequency, count, rate, and ambiguity"),
        ("stability_metrics", "Stability Metrics", "Specifications of state persistence, duration, and stability score"),
        ("transition_thresholds", "Transition Thresholds", "Configurable bounds for transition ambiguity and stability"),
        ("timestamp_policies", "Timestamp Policies", "Chronological ordering and monotonic sequence validation"),
        ("no_lookahead_guards", "No-Lookahead Guards", "Guards preventing forward return leaks and future joins"),
        ("source_phases", "Source Phase Lineage", "Lineage to Phases 121, 123, 124, 126, 127, 128, 129"),
        ("persistence_diagnostics", "State Persistence Diagnostics", "Diagnostic estimation of state persistence and run-lengths"),
        ("transition_frequency", "Transition Frequency", "Diagnostic frequency metrics across candidate regimes"),
        ("transition_matrix_placeholders", "Transition Matrix Placeholders", "Structural matrix layout for transition frequencies without Markov fit"),
        ("transition_ambiguity", "Transition Ambiguity Diagnostics", "Diagnostic ambiguity detection between state transitions"),
        ("transition_continuity", "Transition Continuity Diagnostics", "Continuity checks and gap diagnostics across timestamps"),
        ("transition_stability", "Transition Stability Diagnostics", "Rolling stability and transition resistance diagnostics"),
        ("volatility_transition", "Volatility Transition Diagnostics", "Volatility expansion/compression regime transition context"),
        ("trend_transition", "Trend Transition Diagnostics", "Trend/range transition context and momentum decay proxies"),
        ("range_transition", "Range Transition Diagnostics", "Range breakout context and compression/expansion readiness"),
        ("macro_event_transition", "Macro Event Transition Context", "Transition readiness around macro release event windows"),
        ("news_metadata_transition", "News Metadata Transition Context", "Metadata-only news transition linkage context"),
        ("cross_asset_transition_prep", "Cross-Asset Transition Prep", "Readiness preparation for cross-asset state alignment"),
        ("quality_dependencies", "Quality Dependencies", "Dependencies on Phase 123 quality and Phase 129 behavior metrics"),
        ("validation_dependencies", "Validation Dependencies", "Dependencies on Phase 121/127/128 validation gates"),
        ("transition_findings", "Transition Quality Findings", "Observation registry of sequence/transition defects"),
        ("manual_review_queue", "Manual Review Queue", "Action items requiring manual inspection (no auto-fix)"),
        ("stability_scoring", "Transition Stability Scoring", "Aggregate stability index calculation"),
        ("diagnostics_manifest", "Diagnostics Manifest", "Integrity manifest certifying zero-signal and zero-execution"),
        ("phase_131_handoff", "Phase 131 Handoff", "Prerequisites and handoff report for Phase 131 Cross-Asset Context"),
    ]

    rows = []
    for domain_key, name, desc in domains:
        rows.append(
            {
                "domain_key": domain_key,
                "domain_name": name,
                "description": desc,
                "current_phase": profile.current_phase,
                "target_final_phase": profile.target_final_phase,
                "next_phase": profile.next_phase,
                "non_signal": True,
                "source_preserved": True,
                "model_training_allowed": False,
                "clustering_allowed": False,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": profile.profile_name,
        "total_domains": len(df),
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "all_non_signal": True,
        "all_source_preserved": True,
        "zero_model_training": True,
        "zero_clustering": True,
    }
    return df, summary
