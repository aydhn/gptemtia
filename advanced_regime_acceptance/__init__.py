"""Phase 135: Regime Classification Block Final Acceptance Package.

Provides end-to-end acceptance, inventory, dependencies, gates, scoring,
compliance, component acceptance, manifest, and Phase 136 handoff.
"""

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
    get_default_regime_acceptance_profile,
    list_regime_acceptance_profiles,
    validate_regime_acceptance_profiles,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    list_regime_acceptance_domain_labels,
    list_regime_acceptance_status_labels,
    validate_regime_acceptance_domain_label,
    validate_regime_acceptance_status_label,
)
from advanced_regime_acceptance.regime_acceptance_models import (
    RegimeAcceptanceProfileItem,
    RegimeBlockInventoryItem,
    RegimeBlockDependencyItem,
    RegimeBlockAcceptanceGate,
    RegimeBlockAcceptanceScore,
    RegimeBlockManualReviewItem,
    RegimeBlockComplianceItem,
    RegimeBlockStatusItem,
    Phase126135AcceptanceManifest,
)
from advanced_regime_acceptance.regime_acceptance_profile_registry import (
    build_regime_acceptance_profile_registry,
    summarize_regime_acceptance_profiles,
)
from advanced_regime_acceptance.regime_acceptance_domain_registry import (
    build_regime_acceptance_domain_registry,
    summarize_regime_acceptance_domains,
)
from advanced_regime_acceptance.regime_block_inventory import (
    build_regime_block_inventory_report,
    summarize_regime_block_inventory,
)
from advanced_regime_acceptance.regime_block_dependencies import (
    build_regime_block_dependency_report,
    summarize_regime_block_dependencies,
)
from advanced_regime_acceptance.regime_block_acceptance_gates import (
    build_regime_block_acceptance_gate_registry,
    validate_regime_acceptance_gate,
    summarize_regime_acceptance_gates,
)
from advanced_regime_acceptance.regime_block_acceptance_scoring import (
    calculate_regime_block_acceptance_score,
    build_regime_block_acceptance_score_report,
    classify_regime_block_acceptance_score,
    summarize_regime_block_acceptance_score,
)
from advanced_regime_acceptance.regime_block_manual_review import (
    build_regime_block_manual_review_queue,
    summarize_regime_block_manual_review_queue,
)
from advanced_regime_acceptance.regime_block_safety_boundary import (
    build_regime_block_safety_boundary_report,
    build_regime_block_no_go_conditions,
    build_regime_block_safe_go_conditions,
    summarize_regime_block_safety_boundary,
)
from advanced_regime_acceptance.regime_block_compliance import (
    build_regime_block_non_signal_compliance_report,
    build_regime_block_no_lookahead_compliance_report,
    build_regime_block_metadata_only_news_compliance_report,
    build_regime_block_forbidden_column_compliance_report,
    build_regime_block_source_preservation_report,
    build_regime_block_featurestore_readiness_report,
    summarize_regime_block_compliance,
)
from advanced_regime_acceptance.regime_block_component_acceptance import (
    build_regime_block_component_acceptance_report,
    summarize_regime_block_component_acceptance,
)
from advanced_regime_acceptance.regime_block_documentation import (
    build_regime_block_documentation_report,
    summarize_regime_block_documentation,
)
from advanced_regime_acceptance.regime_block_script_contracts import (
    build_regime_block_script_contract_report,
    summarize_regime_block_script_contracts,
)
from advanced_regime_acceptance.regime_block_test_contracts import (
    build_regime_block_test_contract_report,
    summarize_regime_block_test_contracts,
)
from advanced_regime_acceptance.regime_block_status import (
    build_regime_block_status_report,
    summarize_regime_block_status,
)
from advanced_regime_acceptance.phase_126_135_acceptance_manifest import (
    build_phase_126_135_acceptance_manifest,
    create_phase_126_135_acceptance_manifest,
    summarize_phase_126_135_acceptance_manifest,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_acceptance_profile_markdown_report,
    build_regime_block_inventory_markdown_report,
    build_regime_block_dependency_markdown_report,
    build_regime_acceptance_gate_markdown_report,
    build_regime_acceptance_score_markdown_report,
    build_regime_manual_review_markdown_report,
    build_regime_compliance_markdown_report,
    build_regime_component_acceptance_markdown_report,
    build_regime_contract_markdown_report,
    build_regime_acceptance_manifest_markdown_report,
    build_regime_health_markdown_report,
    build_regime_validation_markdown_report,
    build_phase_136_handoff_markdown_report,
    build_regime_acceptance_disclaimer,
)
from advanced_regime_acceptance.regime_acceptance_health import (
    build_regime_acceptance_health_check,
    summarize_regime_acceptance_health,
)
from advanced_regime_acceptance.regime_acceptance_validation import (
    validate_regime_acceptance_profile_registry,
    validate_regime_block_inventory,
    validate_regime_acceptance_gates,
    validate_phase_126_135_acceptance_manifest,
    validate_no_forbidden_regime_acceptance_claims,
    build_regime_acceptance_validation_report,
)
from advanced_regime_acceptance.phase_136_handoff import (
    build_phase_136_advanced_ml_gpu_handoff_report,
    summarize_phase_136_handoff,
)
from advanced_regime_acceptance.regime_acceptance_pipeline import (
    RegimeAcceptancePipeline,
)

__all__ = [
    "RegimeAcceptanceProfile",
    "get_regime_acceptance_profile",
    "get_default_regime_acceptance_profile",
    "list_regime_acceptance_profiles",
    "validate_regime_acceptance_profiles",
    "list_regime_acceptance_domain_labels",
    "list_regime_acceptance_status_labels",
    "validate_regime_acceptance_domain_label",
    "validate_regime_acceptance_status_label",
    "RegimeAcceptanceProfileItem",
    "RegimeBlockInventoryItem",
    "RegimeBlockDependencyItem",
    "RegimeBlockAcceptanceGate",
    "RegimeBlockAcceptanceScore",
    "RegimeBlockManualReviewItem",
    "RegimeBlockComplianceItem",
    "RegimeBlockStatusItem",
    "Phase126135AcceptanceManifest",
    "build_regime_acceptance_profile_registry",
    "summarize_regime_acceptance_profiles",
    "build_regime_acceptance_domain_registry",
    "summarize_regime_acceptance_domains",
    "build_regime_block_inventory_report",
    "summarize_regime_block_inventory",
    "build_regime_block_dependency_report",
    "summarize_regime_block_dependencies",
    "build_regime_block_acceptance_gate_registry",
    "validate_regime_acceptance_gate",
    "summarize_regime_acceptance_gates",
    "calculate_regime_block_acceptance_score",
    "build_regime_block_acceptance_score_report",
    "classify_regime_block_acceptance_score",
    "summarize_regime_block_acceptance_score",
    "build_regime_block_manual_review_queue",
    "summarize_regime_block_manual_review_queue",
    "build_regime_block_safety_boundary_report",
    "build_regime_block_no_go_conditions",
    "build_regime_block_safe_go_conditions",
    "summarize_regime_block_safety_boundary",
    "build_regime_block_non_signal_compliance_report",
    "build_regime_block_no_lookahead_compliance_report",
    "build_regime_block_metadata_only_news_compliance_report",
    "build_regime_block_forbidden_column_compliance_report",
    "build_regime_block_source_preservation_report",
    "build_regime_block_featurestore_readiness_report",
    "summarize_regime_block_compliance",
    "build_regime_block_component_acceptance_report",
    "summarize_regime_block_component_acceptance",
    "build_regime_block_documentation_report",
    "summarize_regime_block_documentation",
    "build_regime_block_script_contract_report",
    "summarize_regime_block_script_contracts",
    "build_regime_block_test_contract_report",
    "summarize_regime_block_test_contracts",
    "build_regime_block_status_report",
    "summarize_regime_block_status",
    "build_phase_126_135_acceptance_manifest",
    "create_phase_126_135_acceptance_manifest",
    "summarize_phase_126_135_acceptance_manifest",
    "build_regime_acceptance_profile_markdown_report",
    "build_regime_block_inventory_markdown_report",
    "build_regime_block_dependency_markdown_report",
    "build_regime_acceptance_gate_markdown_report",
    "build_regime_acceptance_score_markdown_report",
    "build_regime_manual_review_markdown_report",
    "build_regime_compliance_markdown_report",
    "build_regime_component_acceptance_markdown_report",
    "build_regime_contract_markdown_report",
    "build_regime_acceptance_manifest_markdown_report",
    "build_regime_health_markdown_report",
    "build_regime_validation_markdown_report",
    "build_phase_136_handoff_markdown_report",
    "build_regime_acceptance_disclaimer",
    "build_regime_acceptance_health_check",
    "summarize_regime_acceptance_health",
    "validate_regime_acceptance_profile_registry",
    "validate_regime_block_inventory",
    "validate_regime_acceptance_gates",
    "validate_phase_126_135_acceptance_manifest",
    "validate_no_forbidden_regime_acceptance_claims",
    "build_regime_acceptance_validation_report",
    "build_phase_136_advanced_ml_gpu_handoff_report",
    "summarize_phase_136_handoff",
    "RegimeAcceptancePipeline",
]
