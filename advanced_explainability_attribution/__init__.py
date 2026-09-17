# -*- coding: utf-8 -*-
"""Phase 143: Explainability and Feature Attribution Package."""

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
    get_strict_explainability_profile,
    get_governance_focus_explainability_profile,
)
from advanced_explainability_attribution.explainability_models import (
    ExplainabilityProfileItem,
    ExplainabilityReportContract,
    FeatureAttributionContract,
    ExplanationPlaceholderItem,
    AttributionMethodPolicy,
    AttributionInputContract,
    AttributionOutputContract,
    ExplainabilityDisabledExecutionItem,
    ExplainabilityGuardItem,
    ExplainabilityFinding,
    ExplainabilityReadinessScore,
    ExplainabilityManifest,
    ExplainabilityManualReviewItem,
)
from advanced_explainability_attribution.explainability_report_contracts import (
    build_explainability_report_contracts,
    summarize_explainability_report_contracts,
)
from advanced_explainability_attribution.feature_attribution_contracts import (
    build_feature_attribution_contracts,
    summarize_feature_attribution_contracts,
)
from advanced_explainability_attribution.explainability_pipeline import (
    run_explainability_pipeline,
)
from advanced_explainability_attribution.explainability_health import (
    check_explainability_health,
)
from advanced_explainability_attribution.explainability_validation import (
    validate_explainability_layer,
)
from advanced_explainability_attribution.phase_144_handoff import (
    generate_phase_144_handoff_contract,
    format_phase_144_handoff_text,
)

__all__ = [
    "ExplainabilityProfile",
    "get_explainability_profile",
    "get_strict_explainability_profile",
    "get_governance_focus_explainability_profile",
    "ExplainabilityProfileItem",
    "ExplainabilityReportContract",
    "FeatureAttributionContract",
    "ExplanationPlaceholderItem",
    "AttributionMethodPolicy",
    "AttributionInputContract",
    "AttributionOutputContract",
    "ExplainabilityDisabledExecutionItem",
    "ExplainabilityGuardItem",
    "ExplainabilityFinding",
    "ExplainabilityReadinessScore",
    "ExplainabilityManifest",
    "ExplainabilityManualReviewItem",
    "build_explainability_report_contracts",
    "summarize_explainability_report_contracts",
    "build_feature_attribution_contracts",
    "summarize_feature_attribution_contracts",
    "run_explainability_pipeline",
    "check_explainability_health",
    "validate_explainability_layer",
    "generate_phase_144_handoff_contract",
    "format_phase_144_handoff_text",
]
