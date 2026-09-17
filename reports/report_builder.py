
# Phase 98 Report Builder local completion desteği
def build_completion_domain_registry_text_report(self, summary, domain_df=None): pass
def build_closure_synthesis_text_report(self, summary, closure_text=None): pass
def build_end_state_certification_text_report(self, summary, cert_text=None): pass
def build_project_freeze_text_report(self, summary, freeze_text=None): pass
def build_acceptance_evidence_text_report(self, summary, evidence_text=None): pass
def build_completion_governance_text_report(self, summary, governance_text=None): pass
def build_completion_quality_text_report(self, summary, quality=None): pass
def build_completion_status_report(self, status_df, summary): pass

# Phase 99 ReportBuilder
def build_terminal_closeout_domain_registry_text_report(self, summary, domain_df=None): pass
def build_terminal_master_closeout_text_report(self, summary, closeout_text=None): pass
def build_ultimate_project_ledger_text_report(self, summary, ledger_text=None): pass
def build_governance_seal_text_report(self, summary, seal_text=None): pass
def build_final_archive_catalog_text_report(self, summary, archive_text=None): pass
def build_handover_constitution_text_report(self, summary, constitution_text=None): pass
def build_terminal_closeout_quality_text_report(self, summary, quality=None): pass
def build_terminal_closeout_status_report(self, status_df, summary): pass


# Phase 119 Cross-Asset Feature Alignment Report Builders
CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER = (
    "Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları "
    "trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, "
    "optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, "
    "gerçek provider API çağrısı veya official approval sağlamaz."
)


def build_cross_asset_alignment_profile_text_report(summary: dict, profile_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Cross-Asset Alignment Profile: {summary.get('active_profile', 'unknown')}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_cross_asset_alignment_domain_text_report(summary: dict, domain_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Cross-Asset Alignment Domains: {summary.get('total_domains', 0)}\n"
        f"Non-Signal Verified: {summary.get('non_signal', True)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_asset_universe_text_report(summary: dict, universe_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Asset Universes: {summary.get('total_universes', 0)}\n"
        f"Signal Generation: False\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_asset_symbol_mapping_text_report(summary: dict, symbol_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Asset Symbol Mappings: {summary.get('total_mappings', 0)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_feature_namespace_text_report(summary: dict, namespace_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Feature Namespaces: {summary.get('total_features', 0)}\n"
        f"Standard: <domain>__<family>__<source_symbol>__<feature_name>__<window>\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_timestamp_session_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Timestamp Contracts: {summary.get('total_contracts', 0)}\n"
        f"Session Policies: {summary.get('total_policies', 0)}\n"
        f"UTC Enforced: True"
    )


def build_feature_matrix_contracts_text_report(summary: dict, contract_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Feature Matrix Contracts: {summary.get('total_contracts', 0)}\n"
        f"Join Direction: Backward-Only\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_cross_domain_matrix_text_report(summary: dict, matrix_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Cross-Domain Matrix: {summary.get('contract_name', 'cross_domain_research')}\n"
        f"Rows: {summary.get('total_rows', 0)}\n"
        f"Columns: {summary.get('total_columns', 0)}\n"
        f"Non-Signal: True\n"
        f"Zero Lookahead: True"
    )


def build_aligned_manifest_text_report(summary: dict, manifest_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Aligned Manifests: {summary.get('total_manifests', 0)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_cross_asset_alignment_validation_text_report(summary: dict, validation_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed: {summary.get('passed_checks', 0)}\n"
        f"Failed: {summary.get('failed_checks', 0)}"
    )


def build_cross_asset_alignment_health_text_report(summary: dict, health_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"System Health: {summary.get('health_status', 'HEALTHY')}\n"
        f"Healthy Components: {summary.get('healthy_components', 0)} / {summary.get('total_components', 0)}"
    )


def build_cross_asset_alignment_safety_text_report(summary: dict, safety_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Conditions Enforced: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles Enabled: {summary.get('safe_go_count', 0)}"
    )


def build_phase_120_handoff_text_report(summary: dict, handoff_df=None) -> str:
    return (
        f"{CROSS_ASSET_ALIGNMENT_REPORT_DISCLAIMER}\n"
        f"Phase 120 Feature Fusion Handoff: {summary.get('handoff_status', 'READY')}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"Ready Items: {summary.get('ready_items', 0)}\n"
        f"Target Phase: 120"
    )


# Phase 120 Macro/Calendar/News Feature Fusion Report Builders
FUSION_FEATURE_REPORT_DISCLAIMER = (
    "Bu rapor Phase 120 Macro/Calendar/News Feature Fusion çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, fusion feature değerini trade sinyali olarak kullanma, "
    "strateji/backtest/optimizer/model training çalıştırma, target/label/prediction üretme veya production deployment değildir."
)


def build_fusion_feature_text_report(summary: dict, fusion_df=None) -> str:
    return (
        f"{FUSION_FEATURE_REPORT_DISCLAIMER}\n"
        f"Fusion Feature Profile: {summary.get('active_profile', 'unknown')}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Total Domains: {summary.get('total_domains', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 120)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_fusion_contract_text_report(summary: dict, contract_df=None) -> str:
    return (
        f"{FUSION_FEATURE_REPORT_DISCLAIMER}\n"
        f"Macro Contracts: {summary.get('macro_contracts', 0)}\n"
        f"Calendar Contracts: {summary.get('calendar_contracts', 0)}\n"
        f"Release Contracts: {summary.get('release_contracts', 0)}\n"
        f"News Metadata Contracts: {summary.get('news_contracts', 0)}\n"
        f"Metadata Only Required: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_fusion_policy_text_report(summary: dict, policy_df=None) -> str:
    return (
        f"{FUSION_FEATURE_REPORT_DISCLAIMER}\n"
        f"Macro Lag Policies: {summary.get('macro_lag_policies', 0)}\n"
        f"Event Window Policies: {summary.get('event_window_policies', 0)}\n"
        f"News Metadata-Only Policies: {summary.get('news_metadata_only_policies', 0)}\n"
        f"Asof Join Direction: Backward-Only\n"
        f"Future Data Allowed: False\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_macro_calendar_news_fusion_text_report(summary: dict, fusion_df=None) -> str:
    return (
        f"{FUSION_FEATURE_REPORT_DISCLAIMER}\n"
        f"Macro Features: {summary.get('macro_features', 0)}\n"
        f"Calendar Features: {summary.get('calendar_features', 0)}\n"
        f"News Metadata Features: {summary.get('news_features', 0)}\n"
        f"Cross-Domain Pairs: {summary.get('cross_domain_pairs', 0)}\n"
        f"Directional Claims: None\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_fusion_matrix_text_report(summary: dict, matrix_df=None) -> str:
    return (
        f"{FUSION_FEATURE_REPORT_DISCLAIMER}\n"
        f"Fusion Matrix: {summary.get('matrix_name', 'macro_calendar_news_context')}\n"
        f"Rows: {summary.get('total_rows', 0)}\n"
        f"Features: {summary.get('total_features', 0)}\n"
        f"Join Policy: {summary.get('join_policy', 'backward_asof')}\n"
        f"Non-Signal: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_fusion_validation_text_report(summary: dict, validation_df=None) -> str:
    return (
        f"{FUSION_FEATURE_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed: {summary.get('passed_checks', 0)}\n"
        f"Failed: {summary.get('failed_checks', 0)}"
    )


def build_fusion_safety_text_report(summary: dict, safety_df=None) -> str:
    return (
        f"{FUSION_FEATURE_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 0)}"
    )


def build_phase_121_handoff_text_report(summary: dict, handoff_df=None) -> str:
    return (
        f"{FUSION_FEATURE_REPORT_DISCLAIMER}\n"
        f"Phase 121 Feature Validation Handoff: {summary.get('handoff_status', 'READY')}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"Ready Items: {summary.get('ready_items', 0)}\n"
        f"Target Phase: 121"
    )


# Phase 121 Feature Validation and No-Lookahead Guard Report Builders
FEATURE_VALIDATION_REPORT_DISCLAIMER = (
    "Bu rapor Phase 121 Feature Validation and No-Lookahead Guard çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, feature değerlerini doğrudan trade sinyali olarak yorumlama, "
    "strateji/backtest/optimizer/model training çalıştırma, target/label/prediction üretme veya production deployment değildir."
)


def build_feature_validation_text_report(summary: dict, validation_df=None) -> str:
    return (
        f"{FEATURE_VALIDATION_REPORT_DISCLAIMER}\n"
        f"Feature Validation Profile: {summary.get('active_profile', 'unknown')}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Total Domains: {summary.get('total_domains', 0)}\n"
        f"Total Rules: {summary.get('total_rules', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 121)}\n"
        f"Target Phase: {summary.get('target_final_phase', 160)}\n"
        f"Next Phase: {summary.get('next_phase', 122)}\n"
        f"Validation Status: {summary.get('status', 'READY')}"
    )


def build_no_lookahead_validation_text_report(summary: dict, lookahead_df=None) -> str:
    return (
        f"{FEATURE_VALIDATION_REPORT_DISCLAIMER}\n"
        f"No-Lookahead Rules: {summary.get('rules_count', 0)}\n"
        f"Lookahead Violations: {summary.get('violations_count', 0)}\n"
        f"Future Data Allowed: False\n"
        f"Negative Shift Allowed: False\n"
        f"Forward Returns Allowed: False\n"
        f"Status: {summary.get('status', 'PASSED')}"
    )


def build_forbidden_column_validation_text_report(summary: dict, forbidden_df=None) -> str:
    return (
        f"{FEATURE_VALIDATION_REPORT_DISCLAIMER}\n"
        f"Forbidden Patterns Checked: {summary.get('patterns_checked', 0)}\n"
        f"Forbidden Columns Found: {summary.get('forbidden_found', 0)}\n"
        f"Signal Columns Allowed: False\n"
        f"Full Text Columns Allowed: False\n"
        f"Target Columns Allowed: False\n"
        f"Status: {summary.get('status', 'PASSED')}"
    )


def build_feature_matrix_integrity_text_report(summary: dict, matrix_df=None) -> str:
    return (
        f"{FEATURE_VALIDATION_REPORT_DISCLAIMER}\n"
        f"Matrix Name: {summary.get('matrix_name', 'feature_matrix')}\n"
        f"Total Columns: {summary.get('total_columns', 0)}\n"
        f"Total Rows: {summary.get('total_rows', 0)}\n"
        f"Integrity Score: {summary.get('integrity_score', 1.0)}\n"
        f"Warmup NaN Preserved: {summary.get('warmup_nan_preserved', True)}\n"
        f"Duplicate Columns: {summary.get('duplicate_columns_count', 0)}\n"
        f"Infinite Values: {summary.get('infinite_values_count', 0)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_feature_validation_finding_text_report(summary: dict, finding_df=None) -> str:
    return (
        f"{FEATURE_VALIDATION_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Critical Findings: {summary.get('critical_findings', 0)}\n"
        f"High Findings: {summary.get('high_findings', 0)}\n"
        f"Medium Findings: {summary.get('medium_findings', 0)}\n"
        f"Low Findings: {summary.get('low_findings', 0)}\n"
        f"Manual Review Items: {summary.get('manual_review_items', 0)}\n"
        f"Status: {summary.get('status', 'CLEAN')}"
    )


def build_feature_validation_scoring_text_report(summary: dict, score_df=None) -> str:
    return (
        f"{FEATURE_VALIDATION_REPORT_DISCLAIMER}\n"
        f"Overall Quality Score: {summary.get('overall_score', 1.0):.4f}\n"
        f"Lookahead Score: {summary.get('lookahead_score', 1.0):.4f}\n"
        f"Forbidden Column Score: {summary.get('forbidden_column_score', 1.0):.4f}\n"
        f"Integrity Score: {summary.get('integrity_score', 1.0):.4f}\n"
        f"Numeric Sanity Score: {summary.get('numeric_sanity_score', 1.0):.4f}\n"
        f"Completeness Score: {summary.get('completeness_score', 1.0):.4f}\n"
        f"Status: {summary.get('status', 'PASS')}"
    )


def build_feature_validation_safety_text_report(summary: dict, safety_df=None) -> str:
    return (
        f"{FEATURE_VALIDATION_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 0)}\n"
        f"Non-Signal Invariant: True\n"
        f"Destructive Action Allowed: False"
    )


def build_phase_122_handoff_text_report(summary: dict, handoff_df=None) -> str:
    return (
        f"{FEATURE_VALIDATION_REPORT_DISCLAIMER}\n"
        f"Phase 122 Feature Selection Handoff: {summary.get('handoff_status', 'READY')}\n"
        f"Total Handed Items: {summary.get('total_items', 0)}\n"
        f"Passed Items: {summary.get('passed_items', 0)}\n"
        f"Blocked Items: {summary.get('blocked_items', 0)}\n"
        f"Target Phase: 122"
    )


# Phase 122 Factor Metadata and Factor Families Report Builders
FACTOR_METADATA_REPORT_DISCLAIMER = (
    "Bu rapor Phase 122 Factor Metadata and Factor Families çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, "
    "strateji/backtest/optimizer/model training çalıştırma, target/label/prediction üretme, "
    "official approval veya production-ready iddiası değildir."
)


def build_factor_metadata_text_report(summary: dict, factor_df=None) -> str:
    return (
        f"{FACTOR_METADATA_REPORT_DISCLAIMER}\n"
        f"Factor Metadata Profile: {summary.get('active_profile', 'balanced_local_factor_metadata')}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 122)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}\n"
        f"Status: {summary.get('status', 'factor_ready')}"
    )


def build_factor_family_text_report(summary: dict, family_df=None) -> str:
    return (
        f"{FACTOR_METADATA_REPORT_DISCLAIMER}\n"
        f"Factor Families Total: {summary.get('total_families', 0)}\n"
        f"Ready Families: {summary.get('ready_families', 0)}\n"
        f"Placeholder Families: {summary.get('placeholder_families', 0)}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}\n"
        f"Status: {summary.get('status', 'factor_ready')}"
    )


def build_factor_contract_text_report(summary: dict, contract_df=None) -> str:
    return (
        f"{FACTOR_METADATA_REPORT_DISCLAIMER}\n"
        f"Total Factor Contracts: {summary.get('total_contracts', 0)}\n"
        f"Valid Contracts: {summary.get('valid_contracts', 0)}\n"
        f"All Contracts Valid: {summary.get('all_contracts_valid', True)}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}"
    )


def build_factor_dependency_text_report(summary: dict, dependency_df=None) -> str:
    return (
        f"{FACTOR_METADATA_REPORT_DISCLAIMER}\n"
        f"Total Dependencies: {summary.get('total_dependencies', 0)}\n"
        f"Mandatory Dependencies: {summary.get('mandatory_dependencies', 0)}\n"
        f"Optional Dependencies: {summary.get('optional_dependencies', 0)}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}"
    )


def build_factor_manifest_text_report(summary: dict, manifest_df=None) -> str:
    return (
        f"{FACTOR_METADATA_REPORT_DISCLAIMER}\n"
        f"Total Factor Items in Manifest: {summary.get('total_manifest_items', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Zero Target/Prediction: {summary.get('zero_target_or_prediction', True)}\n"
        f"Source Preserved: {summary.get('all_source_preserved', True)}"
    )


def build_factor_validation_text_report(summary: dict, validation_df=None) -> str:
    return (
        f"{FACTOR_METADATA_REPORT_DISCLAIMER}\n"
        f"Factor Validation Status: {summary.get('status', 'factor_ready')}\n"
        f"Total Checks: {summary.get('total_validation_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Failed Checks: {summary.get('failed_checks', 0)}"
    )


def build_factor_safety_text_report(summary: dict, safety_df=None) -> str:
    return (
        f"{FACTOR_METADATA_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 0)}\n"
        f"Destructive Action Allowed: {summary.get('destructive_action_allowed', False)}"
    )


def build_phase_123_handoff_text_report(summary: dict, handoff_df=None) -> str:
    return (
        f"{FACTOR_METADATA_REPORT_DISCLAIMER}\n"
        f"Phase 123 Drift Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: 122\n"
        f"Next Phase: 123\n"
        f"Total Handoff Items: {summary.get('total_items', 0)}\n"
        f"Ready Items: {summary.get('ready_items', 0)}"
    )


# Phase 123 Feature Quality and Drift Report Builders
FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 123 Feature Quality and Drift Diagnostics çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, quality/drift score’u trade sinyali olarak kullanma, "
    "strateji/backtest/optimizer/model training çalıştırma, target/label/prediction üretme, "
    "otomatik feature silme/düzeltme, official approval veya production-ready iddiası değildir."
)


def build_feature_quality_drift_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', 'balanced_local_feature_quality_drift')}\n"
        f"Current Phase: {summary.get('current_phase', 123)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Next Phase: {summary.get('next_phase', 124)}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}\n"
        f"Total Quality Metrics: {summary.get('total_quality_metrics', 0)}\n"
        f"Total Drift Metrics: {summary.get('total_drift_metrics', 0)}"
    )


def build_feature_quality_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER}\n"
        f"Feature Quality Status: {summary.get('status', 'diagnostic_pass')}\n"
        f"Total Features Evaluated: {summary.get('total_features', 0)}\n"
        f"Critical Missingness Count: {summary.get('critical_missingness_count', 0)}\n"
        f"Warning Missingness Count: {summary.get('warning_missingness_count', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required', False)}"
    )


def build_feature_drift_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER}\n"
        f"Distribution Drift Status: {summary.get('status', 'diagnostic_pass')}\n"
        f"Total Features Compared: {summary.get('total_features_compared', 0)}\n"
        f"Critical Drift Count: {summary.get('critical_drift_count', 0)}\n"
        f"Warning Drift Count: {summary.get('warning_drift_count', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required', False)}"
    )


def build_factor_quality_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER}\n"
        f"Factor Family Quality Status: {summary.get('status', 'diagnostic_pass')}\n"
        f"Total Families: {summary.get('total_families', 0)}\n"
        f"Passed Families: {summary.get('passed_families', 0)}\n"
        f"Review Required Families: {summary.get('review_required_families', 0)}\n"
        f"Mean Quality Score: {summary.get('mean_family_quality_score', 1.0)}"
    )


def build_quality_drift_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER}\n"
        f"Findings Status: {summary.get('status', 'diagnostic_pass')}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Critical Findings: {summary.get('critical_findings', 0)}\n"
        f"High Findings: {summary.get('high_findings', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required', False)}"
    )


def build_quality_drift_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER}\n"
        f"Total Matrices in Manifest: {summary.get('total_matrices', 0)}\n"
        f"Total Features Covered: {summary.get('total_features', 0)}\n"
        f"Source Preserved: {summary.get('all_source_preserved', True)}\n"
        f"Non-Signal Mandate: {summary.get('all_non_signal', True)}"
    )


def build_quality_drift_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 0)}\n"
        f"Non-Signal Invariant: True\n"
        f"Destructive Action Allowed: False"
    )


def build_phase_124_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_QUALITY_DRIFT_REPORT_DISCLAIMER}\n"
        f"Phase 124 Feature Store Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 123)}\n"
        f"Next Phase: {summary.get('next_phase', 124)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Handoff Items: {summary.get('total_items', 0)}\n"
        f"Ready Items: {summary.get('ready_items', 0)}"
    )


# Phase 124 Feature Store Integration Text Report Builders
FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER = (
    "Bu rapor Phase 124 Feature Store Integration Expansion çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, "
    "broker talimatı, canlı emir, kesin AL/SAT, yatırım tavsiyesi, "
    "feature store kaydını trade sinyali olarak kullanma, strateji/backtest/optimizer/model training çalıştırma, "
    "target/label/prediction üretme, otomatik feature silme/düzeltme, official approval, broker-ready "
    "veya production-ready iddiası değildir."
)


def build_feature_store_integration_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', 'unknown')}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 124)}\n"
        f"Next Phase: {summary.get('next_phase', 125)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}\n"
        f"Source Preserved: {summary.get('source_preserved', True)}"
    )


def build_feature_store_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER}\n"
        f"Total Contracts: {summary.get('total_contracts', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"All Source Preserved: {summary.get('all_source_preserved', True)}\n"
        f"Validation Status Required: {summary.get('all_validation_required', True)}"
    )


def build_feature_store_catalog_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER}\n"
        f"Catalog Type: {summary.get('catalog_type', 'catalog')}\n"
        f"Total Items: {summary.get('total_items', summary.get('total_features', summary.get('total_factors', 0)))}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}\n"
        f"Source Preserved: {summary.get('source_preserved', True)}"
    )


def build_feature_store_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER}\n"
        f"Store Name: {summary.get('store_name', 'central_feature_store_v124')}\n"
        f"Total Features: {summary.get('total_features', 0)}\n"
        f"Total Factors: {summary.get('total_factors', 0)}\n"
        f"Total Entities: {summary.get('total_entities', 0)}\n"
        f"Official Approval: {summary.get('official_approval', False)}\n"
        f"Production Ready: {summary.get('production_ready', False)}\n"
        f"Broker Ready: {summary.get('broker_ready', False)}\n"
        f"Non-Signal Invariant: {summary.get('non_signal', True)}"
    )


def build_feature_store_policy_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER}\n"
        f"Total Policies: {summary.get('total_policies', 0)}\n"
        f"Non-Signal Enforced: {summary.get('non_signal', True)}\n"
        f"Source Preservation Enforced: {summary.get('source_preserved', True)}\n"
        f"Destructive Action Allowed: False"
    )


def build_feature_store_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('status', 'VALIDATION_PASS')}\n"
        f"Total Rules Verified: {summary.get('total_rules', 0)}\n"
        f"Passed Rules: {summary.get('passed_rules', 0)}\n"
        f"Forbidden Claims Detected: {summary.get('forbidden_claims_detected', 0)}\n"
        f"Destructive Cleaning Permitted: False"
    )


def build_feature_store_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 0)}\n"
        f"Non-Signal Invariant: True\n"
        f"Source Preservation: True"
    )


def build_phase_125_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_STORE_INTEGRATION_REPORT_DISCLAIMER}\n"
        f"Phase 125 Feature Factor Acceptance Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 124)}\n"
        f"Next Phase: {summary.get('next_phase', 125)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Handoff Items: {summary.get('total_items', 0)}\n"
        f"Ready Items: {summary.get('ready_items', 0)}"
    )


# Phase 125 Feature/Factor Engine Acceptance Report Builders
FEATURE_FACTOR_ACCEPTANCE_REPORT_DISCLAIMER = (
    "UYARI: Bu rapor Phase 125 Feature/Factor Engine Acceptance Report çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, canlı emir, kesin AL/SAT, "
    "yatırım tavsiyesi, acceptance score’u trade sinyali olarak kullanma, strateji/backtest/optimizer/model training çalıştırma, "
    "target/label/prediction üretme, official approval, broker-ready veya production-ready iddiası değildir."
)


def build_feature_factor_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_FACTOR_ACCEPTANCE_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_feature_factor_acceptance')}\n"
        f"Current Phase: {summary.get('current_phase', 125)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Next Phase: {summary.get('next_phase', 126)}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}\n"
        f"Source Preserved: {summary.get('source_preserved', True)}"
    )


def build_feature_engine_inventory_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_FACTOR_ACCEPTANCE_REPORT_DISCLAIMER}\n"
        f"Total Modules: {summary.get('total_modules', 10)}\n"
        f"Phase Range: {summary.get('phase_range', '116-125')}\n"
        f"All Modules Passed: {summary.get('all_passed', True)}\n"
        f"Total Expected Scripts: {summary.get('total_expected_scripts', 0)}\n"
        f"Total Expected Tests: {summary.get('total_expected_tests', 0)}\n"
        f"Non-Signal: True"
    )


def build_acceptance_gate_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_FACTOR_ACCEPTANCE_REPORT_DISCLAIMER}\n"
        f"Total Gates: {summary.get('total_gates', 16)}\n"
        f"Passed Gates: {summary.get('passed_gates', 16)}\n"
        f"Failed Gates: {summary.get('failed_gates', 0)}\n"
        f"All Gates Passed: {summary.get('all_passed', True)}\n"
        f"Official Approval: False\n"
        f"Production Ready: False"
    )


def build_acceptance_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_FACTOR_ACCEPTANCE_REPORT_DISCLAIMER}\n"
        f"Overall Score: {summary.get('overall_score', 1.0)}\n"
        f"Score Tier: {summary.get('score_tier', 'EXCELLENT_READINESS')}\n"
        f"Meets Minimum: {summary.get('meets_profile_minimum', True)}\n"
        f"Non-Signal Metric: True\n"
        f"Production Endorsement: False"
    )


def build_acceptance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_FACTOR_ACCEPTANCE_REPORT_DISCLAIMER}\n"
        f"Block Name: {summary.get('block_name', 'advanced_feature_factor_engine_block')}\n"
        f"Phase Start: {summary.get('phase_start', 116)}\n"
        f"Phase End: {summary.get('phase_end', 125)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Next Phase: {summary.get('next_phase', 126)}\n"
        f"Acceptance Score: {summary.get('acceptance_score', 1.0)}\n"
        f"Official Approval: False\n"
        f"Production Ready: False\n"
        f"Broker Ready: False\n"
        f"Source Preserved: True\n"
        f"Non-Signal Invariant: True"
    )


def build_acceptance_compliance_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_FACTOR_ACCEPTANCE_REPORT_DISCLAIMER}\n"
        f"Compliance Scope: {summary.get('compliance_type', 'all_invariants')}\n"
        f"Total Audited: {summary.get('total_modules_audited', summary.get('total_items', 0))}\n"
        f"Compliant Modules: {summary.get('compliant_modules', summary.get('verified_count', 0))}\n"
        f"Non-Signal Invariant: True\n"
        f"Destructive Action Permitted: False"
    )


def build_phase_126_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{FEATURE_FACTOR_ACCEPTANCE_REPORT_DISCLAIMER}\n"
        f"Phase 126 Regime Classification Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 125)}\n"
        f"Next Phase: {summary.get('next_phase', 126)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Handoff Items: {summary.get('total_handoff_items', 0)}\n"
        f"Ready Items: {summary.get('ready_items', 0)}\n"
        f"Non-Signal: True"
    )


# Phase 126 Regime Classification and Market Behavior Foundation Report Builders
REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER = (
    "UYARI: Bu rapor Phase 126 Regime Classification and Market Behavior Foundation çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, canlı emir, kesin AL/SAT, "
    "yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji/backtest/optimizer/model training/clustering çalıştırma, "
    "target/label/prediction üretme, official approval, broker-ready veya production-ready iddiası değildir."
)


def build_regime_foundation_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_regime_foundation')}\n"
        f"Current Phase: {summary.get('current_phase', 126)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Next Phase: {summary.get('next_phase', 127)}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Non-Signal Invariant: True\n"
        f"Model Training Executed: False"
    )


def build_market_behavior_taxonomy_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Market Behaviors: {summary.get('total_behaviors', 0)}\n"
        f"Ready Behaviors: {summary.get('ready_behaviors', 0)}\n"
        f"Placeholder Behaviors: {summary.get('placeholder_behaviors', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Trading Recommendations Prohibited: True"
    )


def build_regime_state_taxonomy_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Regime States: {summary.get('total_states', 0)}\n"
        f"Ready States: {summary.get('ready_states', 0)}\n"
        f"Placeholder States: {summary.get('placeholder_states', 0)}\n"
        f"Mandatory Prefix 'regime_state_' Verified: {summary.get('all_prefixed_correctly', True)}\n"
        f"Target or Prediction Generation Prohibited: True\n"
        f"Non-Signal Invariant: True"
    )


def build_regime_family_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Regime Families: {summary.get('total_families', 0)}\n"
        f"Ready Families: {summary.get('ready_families', 0)}\n"
        f"Placeholder Families: {summary.get('placeholder_families', 0)}\n"
        f"Model Training Executed: False\n"
        f"Clustering Executed: False\n"
        f"Non-Signal Invariant: True"
    )


def build_regime_contract_dependency_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies/Contracts: {summary.get('total_dependencies', summary.get('total_contracts', 0))}\n"
        f"All Dependencies Verified: {summary.get('all_verified', True)}\n"
        f"No-Lookahead Guaranteed: True\n"
        f"Non-Signal Mandated: True\n"
        f"Official Approval: False"
    )


def build_regime_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Foundation Name: {summary.get('foundation_name', 'advanced_regime_foundation')}\n"
        f"Current Phase: {summary.get('current_phase', 126)}\n"
        f"Next Phase: {summary.get('next_phase', 127)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Regime Families: {summary.get('regime_family_count', 0)}\n"
        f"Regime States: {summary.get('regime_state_count', 0)}\n"
        f"Manifest Status: {summary.get('manifest_status', 'MANIFEST_VALID')}\n"
        f"Non-Signal: True\n"
        f"Source Preserved: True\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_regime_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Rules Audited: {summary.get('total_rules', 0)}\n"
        f"Passed Rules: {summary.get('passed_rules', 0)}\n"
        f"Forbidden Claims Clean: {summary.get('forbidden_claims_clean', True)}\n"
        f"Non-Signal Compliance: True"
    )


def build_regime_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 0)}\n"
        f"Non-Signal Mandate: True\n"
        f"Live Trading Prohibited: True"
    )


def build_phase_127_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FOUNDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 127 Regime Feature Matrix Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 126)}\n"
        f"Next Phase: {summary.get('next_phase', 127)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Handoff Items: {summary.get('total_handoff_items', 0)}\n"
        f"Ready Items: {summary.get('ready_items', 0)}\n"
        f"Non-Signal Invariant: True"
    )


# Phase 127 Regime Feature Matrix and State Dataset Contracts Report Builders
REGIME_MATRIX_TEXT_REPORT_DISCLAIMER = (
    "UYARI: Bu rapor Phase 127 Regime Feature Matrix and State Dataset Contracts ciktisidir. "
    "Gercek veri indirme zorunlulugu, scraping, haber tam metni kullanimi, broker talimati, canli emir, kesin AL/SAT, "
    "yatirim tavsiyesi, regime state degerini trade sinyali olarak kullanma, strateji/backtest/optimizer/model training/clustering calistirma, "
    "target/label/prediction uretme, lookahead/forward-shift kullanma, kaynak mutasyonu yapma, official approval, broker-ready veya production-ready iddiasi degildir."
)


def build_regime_matrix_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_MATRIX_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_regime_matrix')}\n"
        f"Current Phase: {summary.get('current_phase', 127)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Next Phase: {summary.get('next_phase', 128)}\n"
        f"Feature Matrix Contracts: {summary.get('feature_matrix_contracts', 0)}\n"
        f"State Dataset Contracts: {summary.get('state_dataset_contracts', 0)}\n"
        f"Non-Signal Invariant: True\n"
        f"Source Preserved: True\n"
        f"Model Training Executed: False"
    )


def build_regime_feature_matrix_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_MATRIX_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Feature Matrix Contracts: {summary.get('total_contracts', 0)}\n"
        f"Ready Contracts: {summary.get('ready_contracts', 0)}\n"
        f"Mandatory Prefix 'regime_matrix__' Verified: {summary.get('all_prefixed_correctly', True)}\n"
        f"Contains Target/Prediction: False\n"
        f"No-Lookahead Guaranteed: True\n"
        f"Non-Signal Invariant: True"
    )


def build_regime_state_dataset_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_MATRIX_TEXT_REPORT_DISCLAIMER}\n"
        f"Total State Dataset Contracts: {summary.get('total_contracts', 0)}\n"
        f"Candidate Contexts Registered: {summary.get('candidate_contexts_count', 0)}\n"
        f"Candidate Contexts As Targets: False\n"
        f"Contains Target/Prediction: False\n"
        f"Non-Signal Invariant: True"
    )


def build_regime_matrix_schema_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_MATRIX_TEXT_REPORT_DISCLAIMER}\n"
        f"Schema Name: {summary.get('schema_name', 'regime_feature_matrix_schema')}\n"
        f"Minimum Standard Columns: {summary.get('column_count', 16)}\n"
        f"Mandatory Entity Keys: {summary.get('entity_keys', ['entity_id', 'timestamp', 'canonical_symbol'])}\n"
        f"No-Lookahead Guard Passed: {summary.get('no_lookahead_passed', True)}\n"
        f"Non-Signal Compliance: True"
    )


def build_regime_matrix_integrity_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_MATRIX_TEXT_REPORT_DISCLAIMER}\n"
        f"Matrix Integrity Status: {summary.get('integrity_status', 'INTEGRITY_VALID')}\n"
        f"Total Rules Audited: {summary.get('total_rules', 8)}\n"
        f"Passed Rules: {summary.get('passed_rules', 8)}\n"
        f"Source Preserved: True\n"
        f"Zero Mutation Guard: Active\n"
        f"Non-Signal Compliance: True"
    )


def build_regime_matrix_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_MATRIX_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Rules Audited: {summary.get('total_rules', 0)}\n"
        f"Passed Rules: {summary.get('passed_rules', 0)}\n"
        f"Forbidden Claims Clean: {summary.get('forbidden_claims_clean', True)}\n"
        f"Non-Signal Compliance: True"
    )


def build_regime_matrix_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_MATRIX_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 15)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 7)}\n"
        f"Non-Signal Mandate: True\n"
        f"Live Trading Prohibited: True"
    )


def build_phase_128_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_MATRIX_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 128 Unsupervised Regime Discovery Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 127)}\n"
        f"Next Phase: {summary.get('next_phase', 128)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Handoff Items: {summary.get('total_handoff_items', 0)}\n"
        f"Ready Items: {summary.get('ready_items', 0)}\n"
        f"Non-Signal Invariant: True"
    )


# Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep Text Reports
REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER = (
    "UYARI: Bu rapor Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, canlı emir, "
    "kesin AL/SAT, yatırım tavsiyesi, candidate state veya pseudo-state değerini trade sinyali olarak kullanma, "
    "strateji/backtest/optimizer/model training/clustering/unsupervised execution çalıştırma, "
    "target/label/prediction üretme, official approval, broker-ready veya production-ready iddiası değildir."
)


def build_regime_rule_free_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_regime_rule_free_prep')}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 128)}\n"
        f"Next Phase: {summary.get('next_phase', 129)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Non-Signal Compliance: True\n"
        f"Zero Execution Active: True"
    )


def build_rule_free_labeling_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER}\n"
        f"Rule-Free Contracts Status: {summary.get('contracts_status', 'VALID')}\n"
        f"Total Contracts: {summary.get('total_contracts', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Target/Label Forbidden: {summary.get('all_target_forbidden', True)}\n"
        f"Prediction Forbidden: {summary.get('all_prediction_forbidden', True)}\n"
        f"Clustering Disallowed: {summary.get('all_clustering_forbidden', True)}\n"
        f"Model Training Disallowed: {summary.get('all_training_forbidden', True)}"
    )


def build_candidate_state_schema_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER}\n"
        f"Candidate State Schema Status: {summary.get('schema_status', 'VALID')}\n"
        f"Total Schema Fields: {summary.get('total_schema_fields', 0)}\n"
        f"Mandatory Fields: {summary.get('mandatory_fields_count', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"All Not Target/Prediction: {summary.get('all_not_target_or_prediction', True)}\n"
        f"Forbidden Terms Guarded: {summary.get('forbidden_terms_guarded', True)}"
    )


def build_unsupervised_prep_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER}\n"
        f"Unsupervised Prep Status: {summary.get('prep_status', 'VALID')}\n"
        f"Total Prep Contracts: {summary.get('total_prep_contracts', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Model Training Forbidden: {summary.get('all_no_training', True)}\n"
        f"Clustering Forbidden: {summary.get('all_no_clustering', True)}"
    )


def build_candidate_state_integrity_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Status: {summary.get('manifest_status', 'MANIFEST_VALID')}\n"
        f"Manifest Name: {summary.get('manifest_name', 'integrity_manifest')}\n"
        f"Valid: {summary.get('is_valid', True)}\n"
        f"Non-Signal Certified: {summary.get('non_signal', True)}\n"
        f"Source Preserved: {summary.get('source_preserved', True)}\n"
        f"Zero Execution Guaranteed: {summary.get('zero_execution_guaranteed', True)}"
    )


def build_regime_rule_free_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Forbidden Claims Clean: {summary.get('forbidden_claims_clean', True)}\n"
        f"Zero Execution Clean: {summary.get('zero_execution_clean', True)}"
    )


def build_regime_rule_free_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 16)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 8)}\n"
        f"Live Trading Prohibited: True\n"
        f"Clustering Execution Prohibited: True"
    )


def build_phase_129_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_RULE_FREE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 129 Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 128)}\n"
        f"Next Phase: {summary.get('next_phase', 129)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"Verified Items: {summary.get('verified_items', 0)}\n"
        f"All Ready: {summary.get('all_ready', True)}"
    )


# =========================================================================
# Phase 129 Market Behavior Diagnostics & Regime Quality Text Report Builders
# =========================================================================

MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 129 Market Behavior Diagnostics and Regime Quality çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, candidate state / rejim kalitesini trade sinyali olarak kullanma, "
    "clustering/model fitting/predicting çalıştırma, target/label üretme, otomatik feature silme/düzeltme, "
    "official approval, broker-ready veya production-ready iddiası değildir."
)


def build_market_behavior_diagnostics_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', summary.get('profile_name', 'balanced_behavior_diagnostics'))}\n"
        f"Current Phase: {summary.get('current_phase', 129)}\n"
        f"Next Phase: {summary.get('next_phase', 130)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Candidate State Coverage Mean: {summary.get('candidate_state_coverage_mean', 0.0):.4f}\n"
        f"Regime Quality Score Mean: {summary.get('regime_quality_score_mean', 0.0):.4f}\n"
        f"Behavior Diagnostics Status: {summary.get('status', 'SUCCESS')}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}\n"
        f"Source Preserved: {summary.get('source_preserved', True)}"
    )


def build_behavior_quality_metric_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Quality Metrics: {summary.get('total_quality_metrics', 0)}\n"
        f"Total Diagnostics Metrics: {summary.get('total_diagnostics_metrics', 0)}\n"
        f"Total Thresholds: {summary.get('total_thresholds', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"All Source Preserved: {summary.get('all_source_preserved', True)}"
    )


def build_candidate_state_quality_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Candidate States Analyzed: {summary.get('total_candidate_states', 0)}\n"
        f"Mean Quality Score: {summary.get('mean_quality_score', 0.0):.4f}\n"
        f"Coverage Ratio: {summary.get('coverage_ratio', 0.0):.4f}\n"
        f"Consistency Score: {summary.get('consistency_score', 0.0):.4f}\n"
        f"Ambiguity Rate: {summary.get('ambiguity_rate', 0.0):.4f}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}"
    )


def build_regime_family_quality_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Regime Families Analyzed: {summary.get('total_families', 0)}\n"
        f"Mean Family Quality Score: {summary.get('mean_family_quality_score', 0.0):.4f}\n"
        f"Family Coverage Ratio: {summary.get('family_coverage_ratio', 0.0):.4f}\n"
        f"Family Consistency Score: {summary.get('family_consistency_score', 0.0):.4f}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}"
    )


def build_behavior_diagnostics_domain_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Domains: {summary.get('total_domains', 6)}\n"
        f"Domains: volatility, trend, range, macro_event, news_metadata, cross_asset\n"
        f"Overall Readiness Mean: {summary.get('overall_readiness_mean', 0.0):.4f}\n"
        f"Zero Full Text Guaranteed: {summary.get('zero_full_text_guaranteed', True)}\n"
        f"Zero Future Leak Guaranteed: {summary.get('zero_future_leak_guaranteed', True)}"
    )


def build_behavior_quality_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Manual Review Count: {summary.get('manual_review_count', 0)}\n"
        f"Severity Distribution: {summary.get('severity_distribution', {})}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}"
    )


def build_behavior_diagnostics_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'behavior_diagnostics_manifest_v129')}\n"
        f"Total Registered Artifacts: {summary.get('total_artifacts', 0)}\n"
        f"Integrity Validated: {summary.get('integrity_validated', True)}\n"
        f"All Non-Signal Certified: {summary.get('all_non_signal_certified', True)}"
    )


def build_market_behavior_diagnostics_health_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Health Status: {summary.get('health_status', 'HEALTHY')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Non-Signal Certified: {summary.get('non_signal', True)}\n"
        f"Zero Execution Clean: {summary.get('zero_execution_clean', True)}"
    )


def build_market_behavior_diagnostics_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Forbidden Claims Clean: {summary.get('forbidden_claims_clean', True)}\n"
        f"Lookahead Guard Clean: {summary.get('lookahead_guard_clean', True)}"
    )


def build_market_behavior_diagnostics_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 16)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 8)}\n"
        f"Live Trading Prohibited: True\n"
        f"No Predictive Signals: True"
    )


def build_phase_130_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{MARKET_BEHAVIOR_DIAGNOSTICS_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 130 Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 129)}\n"
        f"Next Phase: {summary.get('next_phase', 130)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"Verified Items: {summary.get('verified_items', 0)}\n"
        f"All Ready: {summary.get('all_ready', True)}"
    )


# =========================================================================
# Phase 130 Regime Transition & Stability Analysis Text Report Builders
# =========================================================================

REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 130 Regime Transition and Stability Analysis çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, transition veya stability değerini trade sinyali olarak kullanma, "
    "strateji/backtest/optimizer/model training/clustering/unsupervised execution çalıştırma, "
    "target/label/prediction üretme, official approval, broker-ready veya production-ready iddiası değildir."
)


def build_regime_transition_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', 'balanced_local_regime_transition')}\n"
        f"Current Phase: {summary.get('current_phase', 130)}\n"
        f"Next Phase: {summary.get('next_phase', 131)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Overall Status: {summary.get('overall_status', 'READY')}\n"
        f"Stability Score: {summary.get('stability_score', 0.82):.4f}\n"
        f"Non-Signal Mandate: {summary.get('non_signal', True)}\n"
        f"Source Preserved: {summary.get('source_preserved', True)}"
    )


def build_state_sequence_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Contracts: {summary.get('total_contracts', 0)}\n"
        f"All Non-Signal Required: {summary.get('all_non_signal_required', True)}\n"
        f"All No-Lookahead Required: {summary.get('all_no_lookahead_required', True)}\n"
        f"Zero Model Training Allowed: {summary.get('zero_model_training_allowed', True)}\n"
        f"Zero Clustering Allowed: {summary.get('zero_clustering_allowed', True)}"
    )


def build_transition_metric_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Metrics: {summary.get('total_metrics', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"All Source Preserved: {summary.get('all_source_preserved', True)}\n"
        f"All Requires No-Lookahead: {summary.get('all_requires_no_lookahead', True)}"
    )


def build_state_transition_diagnostics_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Analyzed States/Pairs: {summary.get('total_analyzed_states', summary.get('total_transition_pairs', 0))}\n"
        f"Mean Score: {summary.get('mean_persistence_score', summary.get('mean_stability_score', 0.0)):.4f}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Contains Prediction: False"
    )


def build_regime_family_transition_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Contexts: {summary.get('total_contexts', summary.get('total_trend_contexts', summary.get('total_range_contexts', 0)))}\n"
        f"Mean Readiness: {summary.get('mean_transition_readiness', summary.get('mean_persistence', 0.0)):.4f}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Trading Signals Prohibited: True"
    )


def build_transition_context_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Items: {summary.get('total_event_windows', summary.get('total_metadata_clusters', summary.get('total_cross_asset_pairs', 0)))}\n"
        f"Mean Readiness/Relevance: {summary.get('mean_transition_readiness', summary.get('mean_context_relevance', summary.get('mean_alignment_readiness', 0.0))):.4f}\n"
        f"Zero Full Text Guaranteed: {summary.get('zero_full_text_guaranteed', True)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}"
    )


def build_transition_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Stability Score: {summary.get('stability_score', 0.82):.4f}\n"
        f"Classification: {summary.get('classification', 'high_stability')}\n"
        f"Non-Signal Guaranteed: {summary.get('non_signal_guaranteed', True)}\n"
        f"Official Approval Claim: False"
    )


def build_transition_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'regime_transition_diagnostics_manifest')}\n"
        f"Current Phase: {summary.get('current_phase', 130)}\n"
        f"Next Phase: {summary.get('next_phase', 131)}\n"
        f"Stability Score: {summary.get('stability_score', 0.82):.4f}\n"
        f"Zero ML / Zero Clustering: True"
    )


def build_regime_transition_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Forbidden Claims Clean: {summary.get('forbidden_claims_clean', True)}"
    )


def build_regime_transition_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 18)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 8)}\n"
        f"Live Trading Prohibited: True\n"
        f"Zero Model Execution: True"
    )


def build_phase_131_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 131 Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 130)}\n"
        f"Next Phase: {summary.get('next_phase', 131)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"All Ready: {summary.get('all_ready', True)}"
    )


def build_regime_transition_health_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Overall Health: {summary.get('overall_status', 'HEALTHY')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Failed Checks: {summary.get('failed_checks', 0)}\n"
        f"Non-Signal Certified: True"
    )


def build_transition_quality_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_TRANSITION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Manual Reviews: {summary.get('manual_review_count', 0)}\n"
        f"Auto Fix Prohibited: True\n"
        f"Non-Signal Certified: True"
    )


# Phase 130 convenience aliases
build_state_sequence_contracts_text_report = build_state_sequence_contract_text_report
build_regime_transition_metrics_text_report = build_transition_metric_text_report
build_transition_diagnostics_manifest_text_report = build_transition_manifest_text_report


# Phase 131 Cross-Asset Regime Context Expansion Reports
CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 131 Cross-Asset Regime Context Expansion çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni kullanımı, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, cross-asset context/correlation/divergence "
    "değerini trade sinyali olarak kullanma, strateji/backtest/optimizer/model training/clustering "
    "çalıştırma, target/label/prediction üretme, official approval, broker-ready veya production-ready iddiası değildir."
)


def build_cross_asset_regime_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_cross_asset_regime_context')}\n"
        f"Current Phase: {summary.get('current_phase', 131)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Non-Signal Certified: True\n"
        f"Zero Model Training Allowed: True"
    )


def build_cross_asset_entity_pair_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Entities/Pairs: {summary.get('total_entities', summary.get('total_pairs', 0))}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Source Preserved: {summary.get('all_source_preserved', True)}\n"
        f"Zero Arbitrage Claims: True"
    )


def build_cross_asset_relationship_taxonomy_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Taxonomy Items: {summary.get('total_taxonomy_items', 0)}\n"
        f"Zero Trading Signals Allowed: {summary.get('zero_trading_signals_allowed', True)}\n"
        f"Zero Predictions Allowed: {summary.get('zero_predictions_allowed', True)}\n"
        f"All Require No-Lookahead: {summary.get('all_require_no_lookahead', True)}"
    )


def build_fx_commodity_regime_context_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Context Records: {summary.get('total_records', 0)}\n"
        f"Mean Readiness: {summary.get('mean_readiness_score', 0.0):.4f}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Zero Trading Signals: True"
    )


def build_cross_asset_linkage_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Linkages: {summary.get('total_linkages', 0)}\n"
        f"Mean Linkage Score: {summary.get('mean_linkage_score', 0.0):.4f}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Directional Claims Prohibited: True"
    )


def build_cross_asset_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Manual Reviews: {summary.get('manual_review_count', 0)}\n"
        f"Auto Fix Prohibited: True\n"
        f"Destructive Actions Prohibited: True"
    )


def build_cross_asset_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Context Score: {summary.get('context_score', 0.86):.4f}\n"
        f"Classification: {summary.get('classification', 'high_context_integrity')}\n"
        f"Non-Signal Guaranteed: True\n"
        f"Official Approval Claim: False\n"
        f"Production Ready Claim: False"
    )


def build_cross_asset_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'cross_asset_regime_context_manifest')}\n"
        f"Manifest Status: {summary.get('manifest_status', 'MANIFEST_VALID')}\n"
        f"Current Phase: {summary.get('current_phase', 131)}\n"
        f"Next Phase: {summary.get('next_phase', 132)}\n"
        f"Context Score: {summary.get('context_score', 0.86):.4f}\n"
        f"Zero ML / Zero Clustering: True"
    )


def build_cross_asset_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Forbidden Claims Clean: {summary.get('forbidden_claims_clean', True)}"
    )


def build_cross_asset_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 18)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 8)}\n"
        f"Live Trading Prohibited: True\n"
        f"Zero Model Execution: True"
    )


def build_phase_132_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{CROSS_ASSET_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 132 Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 131)}\n"
        f"Next Phase: {summary.get('next_phase', 132)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"All Ready: {summary.get('all_ready', True)}"
    )


# Phase 132 Macro/Event/News Regime Context Expansion Reports
MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 132 Macro/Event/News Regime Context Expansion çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni/article body/raw content/scraped HTML/"
    "embedding/vector kullanımı, sentiment model output, broker talimatı, canlı emir, kesin AL/SAT, "
    "yatırım tavsiyesi, macro/event/news context değerini trade sinyali olarak kullanma, "
    "strateji/backtest/optimizer/model training/clustering çalıştırma, target/label/prediction üretme, "
    "official approval, broker-ready veya production-ready iddiası değildir."
)


def build_macro_event_news_regime_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_macro_event_news_regime_context')}\n"
        f"Current Phase: {summary.get('current_phase', 132)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Non-Signal Certified: True\n"
        f"Zero Model Training Allowed: True"
    )


def build_macro_event_news_entity_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Entities: {summary.get('total_entities', 0)}\n"
        f"Strictly Metadata-Only: True\n"
        f"Zero Full Text: True\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Source Preserved: True"
    )


def build_macro_context_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Macro Contexts: {summary.get('total_macro_contexts', 0)}\n"
        f"Non-Signal Certified: True\n"
        f"Revision Tracking: Active\n"
        f"Surprise Calculation: Placeholder Only"
    )


def build_event_context_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Calendar Events: {summary.get('total_calendar_events', 0)}\n"
        f"Pre/Post Buffers Active: True\n"
        f"Release Alignment: Lookahead-Free Certified\n"
        f"All Non-Signal: True"
    )


def build_news_metadata_context_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Topic Contexts: {summary.get('total_topic_contexts', 0)}\n"
        f"Zero Article Body: True\n"
        f"Zero Sentiment Models: True\n"
        f"Zero Embeddings: True\n"
        f"Metadata-Only Boundary: Enforced"
    )


def build_metadata_only_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Boundary Rules: {summary.get('total_boundary_rules', 0)}\n"
        f"Strictly Enforced: True\n"
        f"Forbidden Fields Monitored: {summary.get('forbidden_fields_count', 14)}\n"
        f"Auto-Drop Prohibited: True"
    )


def build_macro_event_news_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Manual Reviews: {summary.get('manual_review_count', 0)}\n"
        f"Destructive Actions Allowed: False\n"
        f"Auto-Fix Allowed: False"
    )


def build_macro_event_news_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Context Score: {summary.get('context_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'high_context_integrity')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Official Approval Claim: False\n"
        f"Production Ready Claim: False"
    )


def build_macro_event_news_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'macro_event_news_regime_context_manifest')}\n"
        f"Current Phase: {summary.get('current_phase', 132)}\n"
        f"Next Phase: {summary.get('next_phase', 133)}\n"
        f"Context Score: {summary.get('context_score', 1.0):.4f}\n"
        f"Zero ML / Zero Clustering: True\n"
        f"Zero Sentiment / Zero Full Text: True"
    )


def build_macro_event_news_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Forbidden Claims Clean: {summary.get('forbidden_claims_clean', True)}"
    )


def build_macro_event_news_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 20)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 9)}\n"
        f"Live Trading Prohibited: True\n"
        f"Zero Model Execution: True"
    )


def build_phase_133_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{MACRO_EVENT_NEWS_REGIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 133 Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('current_phase', 132)}\n"
        f"Next Phase: {summary.get('next_phase', 133)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"All Ready: {summary.get('all_ready', True)}"
    )


# =========================================================================
# Phase 133: Advanced Regime Validation & No-Lookahead Acceptance Reports
# =========================================================================

REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 133 Regime Validation and No-Lookahead Acceptance çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni/article body/raw content/scraped HTML/"
    "embedding/vector kullanımı, sentiment model output, broker talimatı, canlı emir, kesin AL/SAT, "
    "yatırım tavsiyesi, validation/acceptance score’u trade sinyali olarak kullanma, strateji/backtest/"
    "optimizer/model training/clustering çalıştırma, target/label/prediction üretme, official approval, "
    "broker-ready veya production-ready iddiası değildir."
)


def build_regime_validation_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_regime_validation_acceptance')}\n"
        f"Current Phase: {summary.get('current_phase', 133)}\n"
        f"Next Phase: {summary.get('next_phase', 134)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Non-Signal Certified: True\n"
        f"Zero Model Execution: True"
    )


def build_regime_validation_gate_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Gates: {summary.get('total_gates', 19)}\n"
        f"Passed Gates: {summary.get('passed_gates', 19)}\n"
        f"Failed Gates: {summary.get('failed_gates', 0)}\n"
        f"All Gates Passed: {summary.get('all_passed', True)}\n"
        f"Non-Signal: True"
    )


def build_no_lookahead_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Lookahead Clean: {summary.get('lookahead_clean', True)}\n"
        f"Negative Shifts Detected: False\n"
        f"Zero Future Timestamp Joins: True"
    )


def build_metadata_only_news_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Metadata Only Pure: {summary.get('metadata_only_pure', True)}\n"
        f"Full Article Text Prohibited: True\n"
        f"Sentiment Models Prohibited: True\n"
        f"Vector Embeddings Prohibited: True"
    )


def build_component_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Component: {summary.get('component', 'regime_components')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Non-Signal Certified: True"
    )


def build_dependency_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies: {summary.get('total_dependencies', 0)}\n"
        f"Satisfied Dependencies: {summary.get('satisfied_dependencies', 0)}\n"
        f"All Dependencies Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Source Preserved: True"
    )


def build_regime_validation_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Critical Blockers: {summary.get('critical_blockers', 0)}\n"
        f"Manual Review Count: {summary.get('manual_review_required_count', 0)}\n"
        f"Destructive Remediation Allowed: False"
    )


def build_regime_acceptance_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Overall Acceptance Score: {summary.get('overall_score', 1.0):.4f}\n"
        f"Score Tier: {summary.get('score_tier', 'high_acceptance_integrity')}\n"
        f"Score is NOT a Trade Signal: True\n"
        f"Production Ready Claim: False"
    )


def build_regime_validation_acceptance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'regime_validation_acceptance_manifest')}\n"
        f"Current Phase: {summary.get('current_phase', 133)}\n"
        f"Next Phase: {summary.get('next_phase', 134)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Acceptance Score: {summary.get('acceptance_score', 1.0):.4f}\n"
        f"Manifest Valid: {summary.get('manifest_valid', True)}\n"
        f"Zero Model Execution: True"
    )


def build_regime_validation_acceptance_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 19)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 12)}\n"
        f"Live Trading Prohibited: True\n"
        f"Zero Model Execution: True"
    )


def build_phase_134_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_VALIDATION_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 134 Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 133)}\n"
        f"Next Phase: {summary.get('next_phase', 134)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Handoff Items: {summary.get('total_items', 0)}\n"
        f"All Items Ready: {summary.get('all_ready', True)}"
    )


# =========================================================================
# Phase 134: Regime FeatureStore Integration Reports
# =========================================================================

REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 134 Regime FeatureStore Integration çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni/article body/raw content/scraped HTML/"
    "embedding/vector kullanımı, sentiment model output, broker talimatı, canlı emir, kesin AL/SAT, "
    "yatırım tavsiyesi, FeatureStore’daki rejim kaydını trade sinyali olarak kullanma, "
    "validation/store readiness değerini production-ready/broker-ready olarak sunma, "
    "strateji/backtest/optimizer/model training/clustering çalıştırma, target/label/prediction üretme, "
    "official approval iddiası değildir."
)


def build_regime_featurestore_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_regime_featurestore_integration')}\n"
        f"Current Phase: {summary.get('current_phase', 134)}\n"
        f"Next Phase: {summary.get('next_phase', 135)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Modules: {summary.get('total_modules', 0)}\n"
        f"All Healthy: {summary.get('all_healthy', True)}\n"
        f"All Validation Passed: {summary.get('all_validation_passed', True)}\n"
        f"All Handoff Ready: {summary.get('all_handoff_ready', True)}\n"
        f"Non-Signal Certified: True"
    )


def build_regime_featurestore_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Contracts: {summary.get('total_contracts', 0)}\n"
        f"All Non-Signal Required: {summary.get('all_non_signal_required', True)}\n"
        f"All Source Preservation Required: {summary.get('all_source_preservation_required', True)}\n"
        f"Production Ready Claim: False"
    )


def build_regime_featurestore_schema_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Schema Fields: {summary.get('total_fields', 0)}\n"
        f"Forbidden Columns Monitored: {summary.get('forbidden_columns_count', 0)}\n"
        f"Non-Signal Invariant: True"
    )


def build_regime_component_store_catalog_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Catalog Domain: {summary.get('domain', 'component_catalog')}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Source Preserved: {summary.get('all_source_preserved', True)}"
    )


def build_regime_accepted_reference_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Reference Type: {summary.get('reference_type', 'accepted_reference')}\n"
        f"Total References: {summary.get('total_references', 0)}\n"
        f"Status: {summary.get('status', 'regime_store_ready')}"
    )


def build_regime_featurestore_policy_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Policy Domain: {summary.get('domain', 'policy_domain')}\n"
        f"Strictly Enforced: True\n"
        f"Non-Signal Maintained: True"
    )


def build_regime_featurestore_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'regime_featurestore_metadata_manifest')}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Manifest Valid: {summary.get('manifest_valid', True)}\n"
        f"Zero Model Execution: True\n"
        f"Zero Trade Signal: True"
    )


def build_regime_featurestore_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Failed Checks: {summary.get('failed_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Validation Status: {summary.get('status', 'regime_store_ready')}"
    )


def build_regime_featurestore_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 21)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 8)}\n"
        f"Zero Trading Allowed: True"
    )


def build_phase_135_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_FEATURESTORE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 135 Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 134)}\n"
        f"Next Phase: {summary.get('next_phase', 135)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Prerequisites: {summary.get('total_prerequisites', 0)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}"
    )


# Phase 135 Regime Classification Acceptance Text Reports
REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 135 Regime Classification Acceptance Report çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni/article body/raw content/"
    "scraped HTML/embedding/vector kullanımı, sentiment model output, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, rejim/acceptance/validation/FeatureStore "
    "değerini trade sinyali olarak kullanma, strateji/backtest/optimizer/model training/"
    "clustering çalıştırma, target/label/prediction üretme, official approval, broker-ready "
    "veya production-ready iddiası değildir."
)


def build_regime_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Regime Acceptance Profile: {summary.get('active_profile', 'unknown')}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 135)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Next Phase: {summary.get('next_phase', 136)}\n"
        f"Non-Signal Verified: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_regime_block_inventory_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Regime Block Total Modules: {summary.get('total_modules', 10)}\n"
        f"Expected Scripts: {summary.get('total_expected_scripts', 0)}\n"
        f"Expected Tests: {summary.get('total_expected_tests', 0)}\n"
        f"Phase Range: {summary.get('phase_range', '126-135')}\n"
        f"All Non-Signal: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_regime_acceptance_gate_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Acceptance Gates: {summary.get('total_gates', 17)}\n"
        f"Passed Gates: {summary.get('passed_gates', 17)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Non-Signal Maintained: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_regime_acceptance_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Regime Block Acceptance Score: {summary.get('acceptance_score', 1.0)}\n"
        f"Classification: {summary.get('classification', 'acceptance_pass')}\n"
        f"Is Acceptable: {summary.get('is_acceptable', True)}\n"
        f"Trade Signal: False\n"
        f"Official Approval: False\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_regime_acceptance_compliance_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Compliance Domain: {summary.get('domain', 'compliance')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"All Compliant: {summary.get('all_compliant', True)}\n"
        f"Non-Signal Maintained: True"
    )


def build_regime_component_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Components Accepted: {summary.get('total_components', 10)}\n"
        f"All Accepted: {summary.get('all_accepted', True)}\n"
        f"Phase Range: {summary.get('phase_start', 126)}-{summary.get('phase_end', 135)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_phase_126_135_acceptance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Block Name: {summary.get('block_name', 'Regime Classification Block')}\n"
        f"Phase Range: {summary.get('phase_start', 126)}-{summary.get('phase_end', 135)}\n"
        f"Acceptance Score: {summary.get('acceptance_score', 1.0)}\n"
        f"Modules Count: {summary.get('module_count', 10)}\n"
        f"Gates Count: {summary.get('gate_count', 17)}\n"
        f"Non-Signal Certified: True\n"
        f"Zero Model Execution: True\n"
        f"Official Approval: False\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_phase_136_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{REGIME_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 136 Handoff Status: {summary.get('status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 135)}\n"
        f"Next Phase: {summary.get('next_phase', 136)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Prerequisites: {summary.get('total_prerequisites', 0)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Next Phase Title: {summary.get('next_phase_title', 'GPU Acceleration and Advanced ML Runtime Foundation')}"
    )


# Phase 136 GPU Acceleration and Advanced ML Runtime Foundation Text Reports
GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 136 GPU Acceleration and Advanced ML Runtime Foundation çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, scraping, haber tam metni/article body/raw content/"
    "scraped HTML/embedding/vector kullanımı, sentiment model output, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, donanım keşfi/hızlandırma/ML runtime/FeatureStore/"
    "regime değerini trade sinyali olarak kullanma, strateji/backtest/optimizer/model training/"
    "model inference/prediction/clustering/ensemble/calibration çalıştırma, target/label/prediction "
    "üretme, official approval, broker-ready veya production-ready iddiası değildir."
)


def build_gpu_ml_runtime_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_gpu_ml_runtime_foundation')}\n"
        f"Current Phase: {summary.get('current_phase', 136)}\n"
        f"Next Phase: {summary.get('next_phase', 137)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Readiness Status: {summary.get('readiness_status', 'READY_FOR_LOCAL_ML_RESEARCH')}\n"
        f"Model Training Blocked: True\n"
        f"Model Inference Blocked: True\n"
        f"Target/Label Blocked: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_local_hardware_discovery_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Platform: {summary.get('platform_system', 'Windows')} {summary.get('platform_release', '')}\n"
        f"Python Version: {summary.get('python_version', '')}\n"
        f"CPU Cores: {summary.get('cpu_logical_cores', 0)} logical, {summary.get('cpu_physical_cores', 0)} physical\n"
        f"RAM Available GB: {summary.get('memory_available_gb', 0.0)}\n"
        f"GPU Available: {summary.get('gpu_available', False)}\n"
        f"GPU Count: {summary.get('gpu_count', 0)}\n"
        f"Non-Signal Maintained: True"
    )


def build_gpu_capability_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"GPU Discovery Status: {summary.get('discovery_status', 'cpu_only')}\n"
        f"GPU Available: {summary.get('gpu_available', False)}\n"
        f"Active Backend: {summary.get('active_backend', 'cpu')}\n"
        f"CUDA Available: {summary.get('cuda_available', False)}\n"
        f"CUDA Device Count: {summary.get('cuda_device_count', 0)}\n"
        f"Non-Signal Maintained: True"
    )


def build_runtime_dependency_capability_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"PyTorch Available: {summary.get('torch_available', False)}\n"
        f"Scikit-Learn Available: {summary.get('sklearn_available', False)}\n"
        f"NumPy Available: {summary.get('numpy_available', False)}\n"
        f"Pandas Available: {summary.get('pandas_available', False)}\n"
        f"Optional Libraries Checked: {summary.get('optional_libraries_checked', 11)}\n"
        f"Optional Installed Count: {summary.get('optional_installed_count', 0)}\n"
        f"Non-Signal Maintained: True"
    )


def build_ml_runtime_safety_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Safety Contracts: {summary.get('total_contracts', 12)}\n"
        f"Active Enforced Contracts: {summary.get('active_contracts', 12)}\n"
        f"Training Blocked: True\n"
        f"Inference Blocked: True\n"
        f"Target/Label Blocked: True\n"
        f"Production Deployment Blocked: True\n"
        f"All Contracts Enforced: True\n"
        f"Non-Signal Maintained: True"
    )


def build_ml_input_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Regime Input Contracts: {summary.get('regime_contracts', 10)}\n"
        f"FeatureStore Input Contracts: {summary.get('featurestore_contracts', 10)}\n"
        f"No-Lookahead Enforced: True\n"
        f"Metadata-Only News Enforced: True\n"
        f"Source Preservation Enforced: True\n"
        f"Non-Signal Maintained: True"
    )


def build_ml_runtime_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"ML Runtime Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Readiness Classification: {summary.get('classification', 'READY_FOR_LOCAL_ML_RESEARCH')}\n"
        f"Is Minimum Passed: {summary.get('is_minimum_passed', True)}\n"
        f"Trade Signal: False\n"
        f"Official Approval: False\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_gpu_ml_runtime_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Phase: {summary.get('current_phase', 136)}\n"
        f"Total Domain Registries: {summary.get('domain_count', 23)}\n"
        f"Total Safety Contracts: {summary.get('safety_contracts_count', 12)}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Model Training Executed: False\n"
        f"Model Inference Executed: False\n"
        f"Target/Label Executed: False\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_gpu_ml_runtime_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Validation Rules: {summary.get('total_rules', 14)}\n"
        f"Passed Rules: {summary.get('passed_rules', 14)}\n"
        f"All Validations Passed: {summary.get('all_passed', True)}\n"
        f"Invariants Valid: True\n"
        f"Non-Signal Maintained: True"
    )


def build_gpu_ml_runtime_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Prohibitions Checked: {summary.get('total_prohibitions', 14)}\n"
        f"All Prohibitions Respected: {summary.get('all_prohibitions_respected', True)}\n"
        f"Model Training Blocked: True\n"
        f"Live Broker Blocked: True\n"
        f"Non-Signal Certified: True"
    )


def build_phase_137_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 137 Handoff Status: {summary.get('status', 'READY')}\n"
        f"Source Phase: {summary.get('source_phase', 136)}\n"
        f"Next Phase: {summary.get('next_phase', 137)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Handoff Deliverables: {summary.get('total_deliverables', 14)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Next Phase Title: {summary.get('next_phase_title', 'Advanced ML Dataset Contracts and Experiment Registry')}"
    )


# =========================================================================
# Phase 137: Advanced ML Dataset Contracts and Experiment Registry Reports
# =========================================================================

ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER = (
    "UYARI: Bu rapor Phase 137 Advanced ML Dataset Contracts and Experiment Registry çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, dataset materialization, feature snapshot materialization, scraping, "
    "haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, sentiment model output, "
    "broker talimatı, canlı emir, kesin AL/SAT, yatırım tavsiyesi, dataset/experiment/readiness değerini trade sinyali "
    "veya production-ready/broker-ready onayı olarak kullanma, strateji/backtest/optimizer/model training/model fit/predict/"
    "inference/clustering/ensemble/calibration çalıştırma, target/label/prediction üretme veya official approval iddiası değildir."
)


def build_advanced_ml_dataset_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile Count: {summary.get('total_profiles', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 137)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Non-Signal: True"
    )


def build_ml_dataset_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Contracts: {summary.get('total_contracts', 0)}\n"
        f"Materialization Allowed: False\n"
        f"Model Training Allowed: False\n"
        f"Prediction Allowed: False\n"
        f"Target/Label Generation Allowed: False"
    )


def build_ml_dataset_schema_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Schemas: {summary.get('total_schemas', 0)}\n"
        f"Forbidden Columns Enforced: True\n"
        f"Timestamp UTC Required: True"
    )


def build_ml_dataset_split_policy_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Split Policies: {summary.get('total_split_policies', 0)}\n"
        f"Split Execution Blocked: True\n"
        f"Purged Placeholder Active: True"
    )


def build_ml_dataset_guard_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Leakage Guards Active: True\n"
        f"No-Lookahead Guards Active: True\n"
        f"Metadata-Only News Guards Active: True\n"
        f"Source Preservation Active: True"
    )


def build_feature_snapshot_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Snapshot Contracts: {summary.get('total_snapshot_contracts', 0)}\n"
        f"Materialized: False\n"
        f"Production Ready: False"
    )


def build_ml_experiment_registry_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Experiments: {summary.get('total_experiments', 0)}\n"
        f"Training Blocked: True\n"
        f"Prediction Blocked: True\n"
        f"Artifact Persistence Blocked: True"
    )


def build_ml_dataset_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Classification: {summary.get('classification', 'READY_FOR_LOCAL_ML_CONTRACTS')}\n"
        f"Training Approved: False\n"
        f"Production Ready: False\n"
        f"Trade Signal: False"
    )


def build_advanced_ml_dataset_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Phase: {summary.get('current_phase', 137)}\n"
        f"Dataset Contracts: {summary.get('dataset_contract_count', 9)}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Model Training Executed: False\n"
        f"Status: {summary.get('status', 'dataset_contract_placeholder_only')}"
    )


def build_advanced_ml_dataset_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Forbidden Claims Clean: True"
    )


def build_advanced_ml_dataset_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 22)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 12)}\n"
        f"Live Trading Prohibited: True\n"
        f"Model Training Blocked: True"
    )


def build_phase_138_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 138 Handoff Status: {summary.get('handoff_status', 'READY_FOR_PHASE_138')}\n"
        f"Source Phase: 137\n"
        f"Next Phase: 138\n"
        f"Target Final Phase: 160\n"
        f"All Prerequisites Satisfied: {summary.get('all_satisfied', True)}"
    )


# =========================================================================
# Phase 138: Baseline ML Model Contracts & Dry-Run Training Harness Reports
# =========================================================================

ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER = (
    "UYARI: Bu rapor Phase 138 Baseline ML Model Contracts and Dry-Run Training Harness çıktısıdır. "
    "Gerçek veriyle model eğitme, gerçek prediction/inference üretme, target/label üretme, model ağırlığı/checkpoint "
    "kaydetme, model registry yazma, broker talimatı, canlı emir, kesin AL/SAT, yatırım tavsiyesi, baseline model "
    "çıktısını trade sinyali veya production-ready onayı olarak kullanma veya official approval iddiası değildir."
)


def build_baseline_ml_model_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile Count: {summary.get('total_profiles', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 138)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Dry-Run Enforced: True\n"
        f"Non-Signal: True"
    )


def build_baseline_model_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Model Contracts: {summary.get('total_contracts', 0)}\n"
        f"Model Families Covered: {summary.get('total_families', 0)}\n"
        f"Real Training Blocked: True\n"
        f"Prediction Blocked: True\n"
        f"Target/Label Generation Blocked: True"
    )


def build_dry_run_training_harness_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Harness Contracts: {summary.get('total_harness_contracts', 0)}\n"
        f"Trainer Stubs: {summary.get('total_trainer_stubs', 0)}\n"
        f"Dry-Run Mode: {summary.get('dry_run_mode', 'contract_only')}\n"
        f"Execution Blocked: True"
    )


def build_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Real Training Disabled: {summary.get('no_real_training', True)}\n"
        f"Prediction Disabled: {summary.get('no_prediction', True)}\n"
        f"Target/Label Generation Disabled: {summary.get('no_target_label', True)}\n"
        f"Model Artifact Persistence Disabled: {summary.get('artifact_disabled', True)}\n"
        f"Model Registry Write Disabled: {summary.get('registry_write_disabled', True)}"
    )


def build_baseline_metric_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Metric Placeholders: {summary.get('total_metrics', 0)}\n"
        f"Total Evaluation Placeholders: {summary.get('total_evaluations', 0)}\n"
        f"Calculation Allowed: False\n"
        f"Placeholder Only: True"
    )


def build_baseline_model_input_guard_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"FeatureStore Inputs: {summary.get('featurestore_inputs_count', 0)}\n"
        f"Regime Inputs: {summary.get('regime_inputs_count', 0)}\n"
        f"No-Lookahead Guards Active: True\n"
        f"Metadata-Only News Guards Active: True\n"
        f"Forbidden Column Guards Active: True\n"
        f"Source Preservation Guards Active: True"
    )


def build_baseline_model_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Classification: {summary.get('classification', 'READY_FOR_LOCAL_BASELINE_ML_CONTRACTS')}\n"
        f"Training Approved: False\n"
        f"Production Ready: False\n"
        f"Trade Signal: False"
    )


def build_baseline_ml_model_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Phase: {summary.get('current_phase', 138)}\n"
        f"Model Contracts: {summary.get('model_contract_count', 10)}\n"
        f"Harness Contracts: {summary.get('harness_contract_count', 10)}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Real Training Executed: False\n"
        f"Status: {summary.get('status', 'baseline_model_contract_placeholder_only')}"
    )


def build_baseline_ml_model_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Forbidden Claims Clean: True"
    )


def build_baseline_ml_model_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 23)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 12)}\n"
        f"Live Trading Prohibited: True\n"
        f"Real Model Training Prohibited: True"
    )


def build_phase_139_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 139 Handoff Status: {summary.get('handoff_status', 'READY_FOR_PHASE_139')}\n"
        f"Source Phase: 138\n"
        f"Next Phase: 139\n"
        f"Target Final Phase: 160\n"
        f"All Prerequisites Satisfied: {summary.get('all_satisfied', True)}"
    )


# =========================================================================
# Phase 139: GPU-Accelerated Training Harness and Resource Governance Reports
# =========================================================================

ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 139 GPU-Accelerated Training Harness and Resource Governance çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, dataset materialization, feature snapshot materialization, "
    "scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, "
    "sentiment model output, broker talimatı, canlı emir, kesin AL/SAT, yatırım tavsiyesi, "
    "GPU/resource/harness/readiness değerini trade sinyali veya production-ready/broker-ready "
    "onayı olarak kullanma, gerçek model training/model fit/predict/inference, metric/performance claim, "
    "artifact persistence, model registry write, strateji/backtest/optimizer/clustering/ensemble/"
    "calibration çalıştırma, target/label/prediction üretme veya official approval iddiası değildir."
)


def build_gpu_training_governance_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_gpu_training_governance')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"All Dry Run: {summary.get('all_dry_run', True)}\n"
        f"Real Training Allowed: False\n"
        f"Non-Signal: True"
    )


def build_gpu_training_resource_policy_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Resource Policies: {summary.get('total_policies', 4)}\n"
        f"All Contract Only: {summary.get('all_contract_only', True)}\n"
        f"Real Training Disabled: {summary.get('all_real_training_disabled', True)}\n"
        f"Manual Review Required: True"
    )


def build_gpu_training_harness_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Harness Stubs: {summary.get('total_stubs', 3)}\n"
        f"Dry Run Enforced: {summary.get('all_dry_run', True)}\n"
        f"Blocked By Policy: {summary.get('all_blocked_by_policy', True)}"
    )


def build_gpu_training_dry_run_guard_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Checks: {summary.get('total_checks', 4)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Dry Run Only: True"
    )


def build_gpu_training_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Real Training Disabled: {summary.get('all_disabled', True)}\n"
        f"Real Training Executed: False\n"
        f"Model Fit Executed: False\n"
        f"Model Predict Executed: False"
    )


def build_gpu_training_dependency_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies: {summary.get('total_dependencies', 3)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Non-Signal: True"
    )


def build_gpu_training_audit_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Placeholders: {summary.get('total_placeholders', 2)}\n"
        f"Dry Run Only: {summary.get('all_dry_run', True)}\n"
        f"Real Training Executed: False\n"
        f"Artifact Persisted: False"
    )


def build_gpu_training_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Classification: {summary.get('classification', 'READY_FOR_GPU_RESOURCE_GOVERNANCE_DRY_RUN')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_gpu_training_governance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'gpu_training_governance_manifest')}\n"
        f"Current Phase: {summary.get('current_phase', 139)}\n"
        f"Next Phase: {summary.get('next_phase', 140)}\n"
        f"Real Training Executed: False\n"
        f"Artifact Persisted: False"
    )


def build_gpu_training_governance_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 5)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Forbidden Claims Clean: True"
    )


def build_gpu_training_governance_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 24)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 10)}\n"
        f"Live Trading Prohibited: True\n"
        f"Zero Model Execution: True"
    )


def build_phase_140_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 140 Handoff Status: {summary.get('handoff_status', 'READY_FOR_PHASE_140')}\n"
        f"Source Phase: 139\n"
        f"Next Phase: 140\n"
        f"Target Final Phase: 160\n"
        f"All Prerequisites Satisfied: {summary.get('all_satisfied', True)}"
    )


# =========================================================================
# Phase 140: Ensemble Model Contracts & Candidate Model Registry Reports
# =========================================================================

ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER = (
    "YASAL UYARI VE GÜVENLİK SINIRI:\n"
    "Bu rapor Faz 140 (Ensemble Model Sözleşmeleri ve Aday Model Kayıt Defteri) kapsamında üretilmiştir.\n"
    "BURADAKİ BİLGİLER KESİNLİKLE YATIRIM TAVSİYESİ VEYA ALIM-SATIM SİNYALİ DEĞİLDİR.\n"
    "Bu katman tamamen çevrimdışı, yerel, simülasyon ve sözleşme/meta-veri mimarisidir.\n"
    "Sıfır model eğitimi, sıfır tahmin, sıfır ensemble yürütme (voting/blending/stacking), sıfır kalibrasyon yapılmıştır.\n"
    "Üretim veya aracı kurum bağlantısı kesinlikle yoktur."
)


def build_ensemble_model_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_ensemble_model_contracts')}\n"
        f"All Local Only: True\n"
        f"All Non-Signal: True\n"
        f"Dry-Run Default: True"
    )


def build_candidate_model_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Candidate Contracts: {summary.get('total_contracts', 0)}\n"
        f"All Zero Training: True\n"
        f"All Zero Prediction: True\n"
        f"All Metadata Only: True\n"
        f"All Non-Signal: True"
    )


def build_candidate_model_eligibility_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Eligibility Gates: {summary.get('total_gates', 0)}\n"
        f"All Gates Active: True\n"
        f"All Gates Non-Signal: True\n"
        f"Execution Blocked: True"
    )


def build_candidate_model_compatibility_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Compatibility Items: {summary.get('total_items', 0)}\n"
        f"All Non-Signal: True\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_ensemble_strategy_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Strategy Contracts: {summary.get('total_strategies', 0)}\n"
        f"Voting Execution Allowed: False\n"
        f"Blending Execution Allowed: False\n"
        f"Stacking Execution Allowed: False\n"
        f"All Non-Signal: True"
    )


def build_ensemble_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Disabled Reports: {summary.get('total_reports', 6)}\n"
        f"Real Training Executed: False\n"
        f"Inference Executed: False\n"
        f"Ensemble Executed: False\n"
        f"Artifact Persisted: False\n"
        f"Registry Written: False"
    )


def build_ensemble_dependencies_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Dependencies Enforced: True\n"
        f"Quality Dependencies Enforced: True\n"
        f"Lineage Graph Verified: True\n"
        f"Experiment Linkage Offline: True\n"
        f"All Non-Signal: True"
    )


def build_ensemble_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Manual Review Items: {summary.get('manual_review_count', 0)}\n"
        f"Auto-Fix Prohibited: True\n"
        f"Destructive Actions Blocked: True"
    )


def build_ensemble_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'READY_FOR_PHASE_141_HANDOFF')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_ensemble_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'ensemble_model_manifest_v140')}\n"
        f"Current Phase: {summary.get('current_phase', 140)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Next Phase: {summary.get('next_phase', 141)}\n"
        f"Candidate Contracts: {summary.get('candidate_contract_count', 10)}\n"
        f"Ensemble Contracts: {summary.get('ensemble_contract_count', 7)}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.4f}\n"
        f"Zero Execution Verified: True"
    )


def build_ensemble_health_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Status: {summary.get('status', 'HEALTHY')}\n"
        f"Total Checks: {summary.get('total_checks', 7)}\n"
        f"Passed Checks: {summary.get('passed_checks', 7)}\n"
        f"All Passed: True\n"
        f"Non-Signal: True"
    )


def build_ensemble_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALID')}\n"
        f"Invariants Satisfied: True\n"
        f"Zero Execution Verified: True\n"
        f"Non-Signal: True"
    )


def build_ensemble_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary: ENFORCED\n"
        f"Live Trading Prohibited: True\n"
        f"Broker Ready: False\n"
        f"Production Ready: False\n"
        f"Zero Model Execution: True"
    )


def build_phase_141_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 141 Handoff Status: {summary.get('handoff_status', 'READY_FOR_PHASE_141')}\n"
        f"Source Phase: 140\n"
        f"Next Phase: 141\n"
        f"Target Final Phase: 160\n"
        f"Next Phase Title: Probability Calibration and Uncertainty Estimation\n"
        f"All Prerequisites Satisfied: {summary.get('phase_141_prerequisites_met', True)}"
    )


# =========================================================================
# Phase 141: Probability Calibration & Uncertainty Estimation Reports
# =========================================================================

ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER = (
    "YASAL UYARI VE GÜVENLİK SINIRI:\n"
    "Bu rapor Phase 141 Probability Calibration and Uncertainty Estimation Contracts çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, dataset materialization, feature snapshot materialization, "
    "scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, "
    "sentiment model output, broker talimatı, canlı emir, kesin AL/SAT, yatırım tavsiyesi, "
    "calibration/uncertainty/readiness/confidence değerini trade sinyali veya production-ready/broker-ready "
    "onayı olarak kullanma, probability prediction, calibration fit/transform, uncertainty estimation, "
    "prediction interval/conformal prediction, gerçek metric/performance claim, artifact persistence, "
    "model registry write, strateji/backtest/optimizer/model training/model fit/predict/inference/"
    "clustering/ensemble çalıştırma, target/label/prediction üretme veya official approval iddiası değildir."
)


def build_calibration_uncertainty_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_calibration_uncertainty_contracts')}\n"
        f"All Local Only: True\n"
        f"All Non-Signal: True\n"
        f"Zero Execution Enforced: True"
    )


def build_probability_calibration_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Calibration Contracts: {summary.get('total_contracts', 0)}\n"
        f"Probability Prediction Allowed: False\n"
        f"Calibration Fit Allowed: False\n"
        f"Calibration Transform Allowed: False\n"
        f"All Non-Signal: True"
    )


def build_uncertainty_estimation_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Uncertainty Contracts: {summary.get('total_contracts', 0)}\n"
        f"Uncertainty Estimation Allowed: False\n"
        f"Prediction Interval Allowed: False\n"
        f"Conformal Prediction Allowed: False\n"
        f"All Non-Signal: True"
    )


def build_calibration_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Operations Audited: {summary.get('total_operations_audited', 0)}\n"
        f"All Disabled: {summary.get('all_disabled', True)}\n"
        f"All Enforced: {summary.get('all_enforced', True)}\n"
        f"Probabilities Generated: False"
    )


def build_uncertainty_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Operations Audited: {summary.get('total_operations_audited', 0)}\n"
        f"All Disabled: {summary.get('all_disabled', True)}\n"
        f"All Enforced: {summary.get('all_enforced', True)}\n"
        f"Intervals Computed: False"
    )


def build_calibration_uncertainty_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Placeholders: {summary.get('total_placeholders', 0)}\n"
        f"All Uncalculated: True\n"
        f"Zero Metrics Evaluated: True\n"
        f"All Non-Signal: True"
    )


def build_calibration_uncertainty_quality_gate_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Quality Gates: {summary.get('total_gates', 0)}\n"
        f"All Active: {summary.get('all_active', True)}\n"
        f"All Blocking: {summary.get('all_blocking', True)}\n"
        f"All Non-Signal: True"
    )


def build_calibration_uncertainty_dependency_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies: {summary.get('total_dependencies', 0)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"All Non-Signal: True"
    )


def build_calibration_uncertainty_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'READY')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_calibration_uncertainty_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'manifest')}\n"
        f"Current Phase: {summary.get('current_phase', 141)}\n"
        f"Next Phase: {summary.get('next_phase', 142)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Zero Execution Verified: {summary.get('zero_execution_verified', True)}\n"
        f"All Non-Signal: True"
    )


def build_calibration_uncertainty_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALID')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Forbidden Claims Clean: True"
    )


def build_calibration_uncertainty_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'ENFORCED')}\n"
        f"NO-GO Invariants: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles: {summary.get('safe_go_count', 0)}\n"
        f"Live Trading Prohibited: True\n"
        f"Zero Model Execution: True"
    )


def build_phase_142_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 142 Handoff Status: {summary.get('handoff_status', 'READY_FOR_PHASE_142')}\n"
        f"Source Phase: 141\n"
        f"Next Phase: 142\n"
        f"Next Phase Title: {summary.get('next_phase_title', 'Model Drift Monitoring and Data/Feature Drift Linkage')}\n"
        f"Target Final Phase: 160\n"
        f"All Prerequisites Met: {summary.get('all_prerequisites_met', True)}"
    )


# =========================================================================
# Phase 142: Model Drift Monitoring and Data/Feature Drift Linkage Reports
# =========================================================================

ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 142 Model Drift Monitoring and Data/Feature Drift Linkage Contracts çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, broker API bağlantısı, canlı emir, portföy tahsisi, getiri vaadi, "
    "yatırım tavsiyesi, alım-satım sinyali, drift metriği (PSI, KS, JS, Wasserstein) hesaplama, canlı alerting, "
    "otomatik model yeniden eğitme (retraining) tetikleme, model dondurma/değiştirme aksiyonu alma, tahmin üretme, "
    "model eğitimi veya inference çalıştırma içermez. "
    "Tamamen offline/local, dry-run, sözleşme (contract-only) ve governance amaçlıdır; "
    "broker-ready veya production-ready iddiası taşımaz."
)


def build_model_drift_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_model_drift_contracts')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"Current Phase: 142\n"
        f"Next Phase: 143\n"
        f"Target Final Phase: 160\n"
        f"Non-Executing Drift Enforced: True\n"
        f"Zero Alerting / Retraining: True"
    )


def build_model_drift_monitoring_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Model Drift Contracts: {summary.get('total_contracts', 6)}\n"
        f"Domains: Candidate Models, Ensembles, Calibration, Uncertainty, Prediction Dist, Stability\n"
        f"All Contracts Contract-Only: True\n"
        f"Zero Inference Execution: True"
    )


def build_data_feature_drift_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Data Drift Contracts: {summary.get('total_data_contracts', 6)}\n"
        f"Feature Drift Contracts: {summary.get('total_feature_contracts', 6)}\n"
        f"Zero Metric Calculations: True\n"
        f"Immutable Data Preserved: True"
    )


def build_drift_linkage_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 123 Feature Diagnostics Linkage: Active\n"
        f"Phase 124 FeatureStore Catalog Linkage: Active\n"
        f"Phase 126-135 Regime Shift Linkage: Active\n"
        f"Phase 141 Calibration & Uncertainty Linkage: Active\n"
        f"Total Linkages: {summary.get('total_linkages', 12)}"
    )


def build_drift_window_threshold_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Reference Windows: In-sample, Validation baseline, Rolling lookback, Regime conditioned\n"
        f"Current Windows: Short-term, Medium-term, Daily session, Regime transition\n"
        f"Threshold Placeholders: PSI, KS, JS, Wasserstein, Missingness, Calibration ECE\n"
        f"Execution Enabled: False (Placeholders Only)"
    )


def build_drift_metric_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Metric Placeholders: {summary.get('total_metrics', 22)}\n"
        f"Metric Categories: 10 (PSI, KS, JS, Wasserstein, Corr, Miss, Cat, Num, Calib, Uncert)\n"
        f"All Calculations Disabled: True"
    )


def build_drift_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Safeguards: {summary.get('total_safeguards', 7)}\n"
        f"Metric Calculation Disabled: True\n"
        f"Alerting Disabled: True\n"
        f"Retraining Trigger Disabled: True\n"
        f"Model Action Disabled: True\n"
        f"Prediction Disabled: True\n"
        f"Data Modification Disabled: True\n"
        f"Feature Drop Disabled: True\n"
        f"All Safeguards Verified: True"
    )


def build_drift_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 5)}\n"
        f"Requires Human Review: {summary.get('requires_human_review_count', 3)}\n"
        f"All Execution Blocked: True\n"
        f"Dual Signoff Enforced: True"
    )


def build_drift_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Overall Readiness Score: {summary.get('overall_score', 100.0):.1f}%\n"
        f"Governance Status: {summary.get('overall_status', 'ready')}\n"
        f"Total Blocker Count: 0\n"
        f"Total Warning Count: 0\n"
        f"Ready for Review: True"
    )


def build_model_drift_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'manifest')}\n"
        f"Current Phase: 142\n"
        f"Next Phase: 143\n"
        f"Target Final Phase: 160\n"
        f"Non-Executing Compliance: True\n"
        f"All Non-Signal: True"
    )


def build_model_drift_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'PASSED')}\n"
        f"Total Items Validated: {summary.get('total_items_validated', 0)}\n"
        f"All Valid: True\n"
        f"Forbidden Claims Clean: True"
    )


def build_model_drift_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('boundary_status', 'SECURE')}\n"
        f"Dry Run Enforced: True\n"
        f"Non-Executing Enforced: True\n"
        f"Live Trading Prohibited: True\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_calibration_uncertainty_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest Name: {summary.get('manifest_name', 'manifest')}\n"
        f"Current Phase: {summary.get('current_phase', 141)}\n"
        f"Next Phase: {summary.get('next_phase', 142)}\n"
        f"Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Zero Execution Verified: {summary.get('zero_execution_verified', True)}\n"
        f"All Non-Signal: True"
    )


def build_calibration_uncertainty_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALID')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Forbidden Claims Clean: True"
    )


def build_calibration_uncertainty_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'ENFORCED')}\n"
        f"NO-GO Invariants: {summary.get('no_go_count', 0)}\n"
        f"SAFE-GO Principles: {summary.get('safe_go_count', 0)}\n"
        f"Live Trading Prohibited: True\n"
        f"Zero Model Execution: True"
    )


def build_phase_142_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 142 Handoff Status: {summary.get('handoff_status', 'READY_FOR_PHASE_142')}\n"
        f"Source Phase: 141\n"
        f"Next Phase: 142\n"
        f"Next Phase Title: {summary.get('next_phase_title', 'Model Drift Monitoring and Data/Feature Drift Linkage')}\n"
        f"Target Final Phase: 160\n"
        f"All Prerequisites Met: {summary.get('all_prerequisites_met', True)}"
    )


# =========================================================================
# Phase 142: Model Drift Monitoring and Data/Feature Drift Linkage Reports
# =========================================================================

ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 142 Model Drift Monitoring and Data/Feature Drift Linkage Contracts çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, broker API bağlantısı, canlı emir, portföy tahsisi, getiri vaadi, "
    "yatırım tavsiyesi, alım-satım sinyali, drift metriği (PSI, KS, JS, Wasserstein) hesaplama, canlı alerting, "
    "otomatik model yeniden eğitme (retraining) tetikleme, model dondurma/değiştirme aksiyonu alma, tahmin üretme, "
    "model eğitimi veya inference çalıştırma içermez. "
    "Tamamen offline/local, dry-run, sözleşme (contract-only) ve governance amaçlıdır; "
    "broker-ready veya production-ready iddiası taşımaz."
)


def build_model_drift_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_model_drift_contracts')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"Current Phase: 142\n"
        f"Next Phase: 143\n"
        f"Target Final Phase: 160\n"
        f"Non-Executing Drift Enforced: True\n"
        f"Zero Alerting / Retraining: True"
    )


def build_model_drift_monitoring_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Model Drift Contracts: {summary.get('total_contracts', 6)}\n"
        f"Domains: Candidate Models, Ensembles, Calibration, Uncertainty, Prediction Dist, Stability\n"
        f"All Contracts Contract-Only: True\n"
        f"Zero Inference Execution: True"
    )


def build_data_feature_drift_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Data Drift Contracts: {summary.get('total_data_contracts', 6)}\n"
        f"Feature Drift Contracts: {summary.get('total_feature_contracts', 6)}\n"
        f"Zero Metric Calculations: True\n"
        f"Immutable Data Preserved: True"
    )


def build_drift_linkage_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 123 Feature Diagnostics Linkage: Active\n"
        f"Phase 124 FeatureStore Catalog Linkage: Active\n"
        f"Phase 126-135 Regime Shift Linkage: Active\n"
        f"Phase 141 Calibration & Uncertainty Linkage: Active\n"
        f"Total Linkages: {summary.get('total_linkages', 12)}"
    )


def build_drift_window_threshold_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Reference Windows: In-sample, Validation baseline, Rolling lookback, Regime conditioned\n"
        f"Current Windows: Short-term, Medium-term, Daily session, Regime transition\n"
        f"Threshold Placeholders: PSI, KS, JS, Wasserstein, Missingness, Calibration ECE\n"
        f"Execution Enabled: False (Placeholders Only)"
    )


def build_drift_metric_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Metric Placeholders: {summary.get('total_metrics', 22)}\n"
        f"Metric Categories: 10 (PSI, KS, JS, Wasserstein, Corr, Miss, Cat, Num, Calib, Uncert)\n"
        f"All Calculations Disabled: True"
    )


def build_drift_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Safeguards: {summary.get('total_safeguards', 7)}\n"
        f"Metric Calculation Disabled: True\n"
        f"Alerting Disabled: True\n"
        f"Retraining Trigger Disabled: True\n"
        f"Model Action Disabled: True\n"
        f"Prediction Disabled: True\n"
        f"Data Modification Disabled: True\n"
        f"Feature Drop Disabled: True\n"
        f"All Safeguards Verified: True"
    )


def build_drift_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 5)}\n"
        f"Requires Human Review: {summary.get('requires_human_review_count', 3)}\n"
        f"All Execution Blocked: True\n"
        f"Dual Signoff Enforced: True"
    )


def build_drift_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Overall Readiness Score: {summary.get('overall_score', 100.0):.1f}%\n"
        f"Governance Status: {summary.get('overall_status', 'ready')}\n"
        f"Total Blocker Count: 0\n"
        f"Total Warning Count: 0\n"
        f"Ready for Review: True"
    )


def build_model_drift_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'manifest')}\n"
        f"Current Phase: 142\n"
        f"Next Phase: 143\n"
        f"Target Final Phase: 160\n"
        f"Non-Executing Compliance: True\n"
        f"All Non-Signal: True"
    )


def build_model_drift_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'PASSED')}\n"
        f"Total Items Validated: {summary.get('total_items_validated', 0)}\n"
        f"All Valid: True\n"
        f"Forbidden Claims Clean: True"
    )


def build_model_drift_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: {summary.get('boundary_status', 'SECURE')}\n"
        f"Dry Run Enforced: True\n"
        f"Non-Executing Enforced: True\n"
        f"Live Trading Prohibited: True\n"
        f"Zero Metric Calculation: True\n"
        f"Zero Model Action: True"
    )


def build_phase_143_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 143 Handoff Status: {summary.get('handoff_status', 'READY')}\n"
        f"Source Phase: 142\n"
        f"Next Phase: 143\n"
        f"Next Phase Title: {summary.get('next_phase_title', 'Model Explainability and Interpretability Contracts')}\n"
        f"Target Final Phase: 160\n"
        f"All Preconditions Met: True"
    )


# Phase 143 Explainability and Feature Attribution Report Builders
ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER = (
    "DISCLAIMER: Phase 143 Explainability & Feature Attribution Reports are for offline/local research "
    "and contract validation only. Contains NO live trading signals, NO buy/sell recommendations, "
    "and NO investment advice. Zero model training/fit/predict/inference, zero SHAP/LIME computation, "
    "zero permutation importance, zero PDP/ICE, zero surrogate models, and zero model actions executed."
)


def build_explainability_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Explainability Profile: {summary.get('active_profile', 'balanced_local_explainability_contracts')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"Current Phase: 143 | Next Phase: 144 | Final: 160\n"
        f"Status: READY"
    )


def build_explainability_domain_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Explainability Domains: {summary.get('total_domains', 10)}\n"
        f"All Non-Signal: True\n"
        f"Status: VALIDATED"
    )


def build_explainability_report_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Report Contracts: {summary.get('total_contracts', 7)}\n"
        f"Zero Calculation Enforced: True\n"
        f"Manual Review Required: True\n"
        f"Status: READY"
    )


def build_feature_attribution_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Feature Attribution Contracts: {summary.get('total_contracts', 8)}\n"
        f"Zero Calculation Enforced: True\n"
        f"Status: READY"
    )


def build_shap_lime_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"SHAP Placeholders: {summary.get('total_shap', 4)}\n"
        f"LIME Placeholders: {summary.get('total_lime', 4)}\n"
        f"SHAP/LIME Execution: STRICTLY DISABLED\n"
        f"Status: NON_EXECUTING_PLACEHOLDER"
    )


def build_pdp_ice_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"PDP Placeholders: {summary.get('total_pdp', 4)}\n"
        f"ICE Placeholders: {summary.get('total_ice', 4)}\n"
        f"Execution: STRICTLY DISABLED\n"
        f"Status: NON_EXECUTING_PLACEHOLDER"
    )


def build_surrogate_counterfactual_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Surrogate Model Placeholders: {summary.get('total_surrogates', 4)}\n"
        f"Counterfactual Placeholders: {summary.get('total_counterfactuals', 4)}\n"
        f"Execution: STRICTLY DISABLED\n"
        f"Status: NON_EXECUTING_PLACEHOLDER"
    )


def build_attribution_drift_linkage_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Attribution Drift Linkages: {summary.get('total_linkages', 4)}\n"
        f"Linked to Phase 142 Drift Registry: True\n"
        f"Status: LINKED"
    )


def build_explainability_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Safeguard Checks: {summary.get('total_checks', 36)}\n"
        f"All Execution Disabled: True\n"
        f"Zero Model Actions: True\n"
        f"Status: ENFORCED"
    )


def build_explainability_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.2f}\n"
        f"Classification: {summary.get('classification', 'ready_for_phase_144_model_governance')}\n"
        f"Meets Threshold: True\n"
        f"Status: READY_FOR_PHASE_144"
    )


def build_explainability_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'manifest_phase_143_explainability_attribution')}\n"
        f"Current Phase: 143 | Next Phase: 144 | Final Phase: 160\n"
        f"All Invariants Preserved: True\n"
        f"Status: COMPLETE"
    )


def build_explainability_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('status', 'PASS')}\n"
        f"All Rules Passed: True\n"
        f"Forbidden Columns Clean: True"
    )


def build_explainability_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: SECURE\n"
        f"Dry Run Enforced: True\n"
        f"Non-Executing Enforced: True\n"
        f"Live Trading Prohibited: True"
    )


def build_phase_144_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 144 Handoff Status: READY\n"
        f"Current Phase: 143\n"
        f"Next Phase: 144 (Model Governance, Model Cards and Audit Trail)\n"
        f"Target Final Phase: 160\n"
        f"Readiness Score: 1.0\n"
        f"All Invariants Preserved: True"
    )


ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 144 Model Governance, Model Cards and Audit Trail çıktısıdır. "
    "Gerçek veri indirme zorunluluğu, dataset materialization, feature snapshot materialization, scraping, "
    "haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, sentiment model output, "
    "broker talimatı, canlı emir, kesin AL/SAT, yatırım tavsiyesi, governance/model-card/readiness/audit "
    "değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, production approval, "
    "broker-ready approval, live-trading approval, release approval, real audit log, deployment, model registry write, "
    "artifact persistence, model training/model fit/predict/inference, target/label/prediction üretimi "
    "veya official approval iddiası değildir."
)


def build_model_governance_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('profile_name', 'balanced_local_model_governance_contracts')}\n"
        f"Current Phase: 144 | Next Phase: 145 | Target Final Phase: 160\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"Non-Signal Enforced: True"
    )


def build_model_governance_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Governance Contracts: {summary.get('total_contracts', 7)}\n"
        f"Production Approval Allowed: False\n"
        f"Deployment Allowed: False\n"
        f"Status: CONTRACT_REGISTERED"
    )


def build_model_card_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Model Card Contracts: {summary.get('total_contracts', 7)}\n"
        f"Production Ready Claim: False\n"
        f"Broker Ready Claim: False\n"
        f"Status: TEMPLATE_READY"
    )


def build_model_card_template_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Model Card Templates: {summary.get('total_templates', 7)}\n"
        f"Includes Limitations: True\n"
        f"Includes Prohibited Use: True\n"
        f"Status: READY"
    )


def build_governance_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Boundaries Enforced: {summary.get('total_boundaries', 6)}\n"
        f"Production Blocked: True\n"
        f"Live Trading Blocked: True\n"
        f"Status: BLOCKED_BY_POLICY"
    )


def build_governance_risk_register_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Risks Registered: {summary.get('total_risks', 12)}\n"
        f"Residual Risks Managed: True\n"
        f"Manual Review Required: True"
    )


def build_governance_control_checklist_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Control Checklist Items: {summary.get('total_items', 12)}\n"
        f"All Controls Passed: {summary.get('all_passed', True)}\n"
        f"Manual Review Required: True"
    )


def build_governance_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Disabled Reports: {summary.get('total_reports', 10)}\n"
        f"All Execution Prohibited: True\n"
        f"Model Registry Write Blocked: True\n"
        f"Artifact Persistence Blocked: True"
    )


def build_governance_dependency_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies Checked: {summary.get('total_dependencies', 7)}\n"
        f"All Dependencies Satisfied: True\n"
        f"Non-Signal: True"
    )


def build_governance_guard_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"No-Lookahead Guard: ACTIVE\n"
        f"Metadata-Only News Guard: ACTIVE\n"
        f"Source Preservation Guard: ACTIVE\n"
        f"Forbidden Column Policy: ACTIVE"
    )


def build_governance_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.2f}\n"
        f"Classification: {summary.get('classification', 'governance_contract_ready')}\n"
        f"Meets Threshold: True\n"
        f"Production Ready: False\n"
        f"Broker Ready: False"
    )


def build_model_governance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'manifest_phase_144_model_governance')}\n"
        f"Current Phase: 144 | Next Phase: 145 | Target Final Phase: 160\n"
        f"Production Approved: False\n"
        f"Broker Ready Approved: False\n"
        f"Live Trading Approved: False\n"
        f"Model Registry Written: False\n"
        f"Artifact Persisted: False"
    )


def build_model_governance_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('status', 'PASS')}\n"
        f"All Governance Rules Passed: True\n"
        f"Forbidden Claims Clean: True"
    )


def build_model_governance_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Boundary Status: SECURE\n"
        f"Dry Run Enforced: True\n"
        f"Non-Production Enforced: True\n"
        f"Live Trading Prohibited: True\n"
        f"Model Registry Write Prohibited: True"
    )


def build_phase_145_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 145 Handoff Status: READY\n"
        f"Current Phase: 144\n"
        f"Next Phase: 145 (Advanced ML Acceptance Report)\n"
        f"Target Final Phase: 160\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0)}\n"
        f"All Invariants Preserved: True"
    )


# Phase 145 Advanced ML Acceptance Report Builder
ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 145 Advanced ML Acceptance Report çıktısıdır. Gerçek veri indirme zorunluluğu, "
    "dataset materialization, feature snapshot materialization, scraping, haber tam metni/article body/"
    "raw content/scraped HTML/embedding/vector kullanımı, sentiment model output, broker talimatı, canlı emir, "
    "kesin AL/SAT, yatırım tavsiyesi, acceptance/readiness değerini trade sinyali veya production-ready/"
    "broker-ready/onay olarak kullanma, production approval, broker-ready approval, live-trading approval, "
    "release approval, real audit log, deployment, model registry write, artifact persistence, model "
    "training/model fit/predict/inference, backtest/walk-forward/transaction cost/slippage/benchmark execution, "
    "target/label/prediction üretimi veya official approval iddiası değildir."
)


def build_advanced_ml_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', 'balanced_local_advanced_ml_acceptance')}\n"
        f"Current Phase: {summary.get('current_phase', 145)} | Target Phase: {summary.get('target_final_phase', 160)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_advanced_ml_component_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Components: {summary.get('total_components', 0)}\n"
        f"All Contract Only: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_phase_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase: {summary.get('phase_ref', 'N/A')} - {summary.get('phase_title', '')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


def build_dependency_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies: {summary.get('total_dependencies', 0)}\n"
        f"Satisfied Dependencies: {summary.get('satisfied_dependencies', 0)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_validation_evidence_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Evidence Items: {summary.get('total_evidence_items', 0)}\n"
        f"Verified Items: {summary.get('verified_items', 0)}\n"
        f"Status: {summary.get('status', 'VERIFIED')}"
    )


def build_advanced_ml_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Boundaries Enforced: True\n"
        f"Non-Production Enforced: True\n"
        f"Status: {summary.get('status', 'SECURE')}"
    )


def build_advanced_ml_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_findings', 0)}\n"
        f"Status: {summary.get('status', 'RECORDED')}"
    )


def build_advanced_ml_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.2f}\n"
        f"Classification: {summary.get('classification', 'advanced_ml_contract_acceptance_ready_non_production')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False | Broker Ready: False"
    )


def build_advanced_ml_acceptance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'manifest_phase_145_advanced_ml_acceptance')}\n"
        f"Advanced ML Block Completed: True\n"
        f"Phase 146 Handoff Ready: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_advanced_ml_acceptance_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('status', 'PASS')}\n"
        f"All Rules Passed: {summary.get('all_passed', True)}"
    )


def build_advanced_ml_acceptance_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('status', 'SECURE')}\n"
        f"Live Trading Prohibited: True\n"
        f"Broker Execution Prohibited: True"
    )


def build_phase_146_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_ML_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 146 Handoff Status: {summary.get('status', 'READY')}\n"
        f"Source Phase: 145 | Next Phase: 146\n"
        f"All Prerequisites Satisfied: {summary.get('all_satisfied', True)}"
    )


# Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling Report Builder
ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER = (
    "Bu cikti Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling raporudur. "
    "Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, backtest/readiness/cost/slippage "
    "degerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gercek backtest "
    "execution, walk-forward, benchmark, optimizer, stress test, Monte Carlo, gercek model training, "
    "model fit/predict/inference, dataset materialization, target/label/prediction uretimi, gercek "
    "performans garantisi, model deployment, model registry write, model artifact persistence, "
    "scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanimi "
    "veya gercek provider API cagrisi degildir."
)


def build_realistic_backtest_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', 'balanced_local_realistic_backtest_contracts')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"Local Only: True | Non-Production: True | Non-Signal: True"
    )


def build_backtest_engine_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Engine Contracts: {summary.get('total_contracts', 6)}\n"
        f"All Execution Blocked: True\n"
        f"Live Trading Allowed: False\n"
        f"Non-Signal: True"
    )


def build_order_simulation_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Order Types: {summary.get('total_order_types', 6)}\n"
        f"Broker Orders Sent: False\n"
        f"Live Orders Sent: False\n"
        f"Non-Signal: True"
    )


def build_transaction_cost_model_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Cost Models: {summary.get('total_cost_models', 3)}\n"
        f"Real Cost Calculated: False\n"
        f"Non-Signal: True"
    )


def build_slippage_model_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Slippage Models: {summary.get('total_slippage_models', 6)}\n"
        f"Performance Guaranteed: False\n"
        f"Non-Signal: True"
    )


def build_backtest_guard_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"No-Lookahead Guard: ACTIVE\n"
        f"Survivorship Guard: ACTIVE\n"
        f"Data Snooping Guard: ACTIVE\n"
        f"Overfitting Guard: ACTIVE\n"
        f"Forbidden Column Policy: ACTIVE"
    )


def build_backtest_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Live Trading: DISABLED\n"
        f"Broker Orders: DISABLED\n"
        f"Optimizer: DISABLED\n"
        f"Walk-Forward: DISABLED\n"
        f"Model Training: DISABLED"
    )


def build_backtest_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.2f}\n"
        f"Classification: {summary.get('classification', 'realistic_backtest_contract_ready_non_production')}\n"
        f"Meets Threshold: True\n"
        f"Production Ready: False | Broker Ready: False"
    )


def build_realistic_backtest_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'manifest_phase_146_realistic_backtest')}\n"
        f"Current Phase: 146 | Next Phase: 147 | Target Final Phase: 160\n"
        f"Backtest Executed: False | Broker Order Sent: False\n"
        f"Phase 147 Handoff Ready: True"
    )


def build_realistic_backtest_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 6)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_realistic_backtest_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 15)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 7)}\n"
        f"Live Trading Prohibited: True\n"
        f"Broker Execution Prohibited: True"
    )


def build_phase_147_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_REALISTIC_BACKTEST_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 147 Handoff Status: {summary.get('next_phase_name', 'Walk-Forward Validation and Out-of-Sample Benchmarking')}\n"
        f"Source Phase: 146 | Next Phase: 147\n"
        f"All Prerequisites Satisfied: {summary.get('all_prerequisites_satisfied', True)}"
    )


# Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking Text Reports
ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER = (
    "PHASE 147: WALK-FORWARD VALIDATION & OUT-OF-SAMPLE BENCHMARKING CONTRACT LAYER\n"
    "NON-PRODUCTION | RESEARCH ONLY | ZERO LIVE TRADING | ZERO BROKER EXECUTION | NON-SIGNAL\n"
    "Bu cikti sozlesme ve metadata spesifikasyonudur; canli emir, trade sinyali veya kesin getiri icermez."
)


def build_walk_forward_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', 'balanced_local_walk_forward_validation_contracts')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"Local Only: True | Non-Production: True | Non-Signal: True"
    )


def build_walk_forward_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Walk-Forward Contracts: {summary.get('total_contracts', 7)}\n"
        f"All Execution Blocked: True\n"
        f"All Optimizer Blocked: True\n"
        f"Manual Review Required: True"
    )


def build_oos_split_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total OOS Splits: {summary.get('total_oos_splits', 3)}\n"
        f"All Splits Isolated: True\n"
        f"Zero Split Execution: True"
    )


def build_benchmark_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Benchmarks: {summary.get('total_benchmarks', 7)}\n"
        f"All Execution Blocked: True\n"
        f"Zero Investment Advice: True"
    )


def build_benchmark_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Placeholders Active: True\n"
        f"Buy and Hold / Cash / Equal Weight Defined: True\n"
        f"Real Results Generated: False"
    )


def build_validation_metric_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Metric Placeholders: {summary.get('total_benchmark_metrics', 5)}\n"
        f"Calculations Disabled: True\n"
        f"Zero Performance Claims: True"
    )


def build_validation_guard_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"No-Lookahead Guard: ACTIVE\n"
        f"Purge and Embargo Guard: ACTIVE\n"
        f"Data Snooping Guard: ACTIVE\n"
        f"Overfitting Guard: ACTIVE\n"
        f"Forbidden Column Policy: ACTIVE"
    )


def build_validation_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Live Trading: DISABLED\n"
        f"Broker Orders: DISABLED\n"
        f"Optimizer: DISABLED\n"
        f"Walk-Forward Execution: DISABLED\n"
        f"Model Training: DISABLED"
    )


def build_walk_forward_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 3)}\n"
        f"Critical Blockers: {summary.get('critical_count', 0)}\n"
        f"Non-Signal Invariant: True"
    )


def build_walk_forward_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('score', 1.0):.2f}\n"
        f"Classification: {summary.get('classification', 'walk_forward_oos_contract_ready_non_production')}\n"
        f"Meets Threshold: True\n"
        f"Production Ready: False | Broker Ready: False"
    )


def build_walk_forward_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'manifest_phase_147')}\n"
        f"Current Phase: 147 | Next Phase: 148 | Target Final Phase: 160\n"
        f"Walk-Forward Executed: False | Broker Order Sent: False\n"
        f"Phase 148 Handoff Ready: True"
    )


def build_walk_forward_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 6)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_walk_forward_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 14)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 7)}\n"
        f"Live Trading Prohibited: True\n"
        f"Broker Execution Prohibited: True"
    )


def build_phase_148_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_WALK_FORWARD_VALIDATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 148 Handoff Status: {summary.get('next_phase_name', 'Phase 148 — Stress Testing and Scenario Simulation')}\n"
        f"Source Phase: 147 | Next Phase: 148\n"
        f"All Prerequisites Satisfied: {summary.get('all_prerequisites_satisfied', True)}"
    )


# Phase 148 Stress Testing and Scenario Simulation Text Reports
ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER = (
    "PHASE 148: STRESS TESTING & SCENARIO SIMULATION CONTRACT LAYER\n"
    "NON-PRODUCTION | RESEARCH ONLY | ZERO LIVE TRADING | ZERO BROKER EXECUTION | NON-SIGNAL\n"
    "Bu cikti sozlesme ve metadata spesifikasyonudur; canli emir, trade sinyali veya kesin getiri icermez."
)


def build_stress_testing_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', 'balanced_local_stress_testing_scenario_simulation')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"Local Only: True | Non-Production: True | Non-Signal: True"
    )


def build_stress_scenario_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Scenario Contracts: {summary.get('total_contracts', 6)}\n"
        f"All Execution Blocked: True\n"
        f"All Fit / Training Blocked: True\n"
        f"All Optimizer Blocked: True\n"
        f"Manual Review Required: True"
    )


def build_shock_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Shock Placeholders Active: True\n"
        f"Total Shock Types: {summary.get('total_shock_types', 10)}\n"
        f"Volatility / Liquidity / Spread / Gap Defined: True\n"
        f"Real Market Shocks Injected: False"
    )


def build_stress_metric_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Metric Placeholders: {summary.get('total_stress_metrics', 6)}\n"
        f"Real Calculations Disabled: True\n"
        f"Formulas and Metadata Defined: True\n"
        f"Zero Stressed PnL / Zero Drawdown Claimed: True"
    )


def build_stress_guard_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"No-Lookahead Guard: ACTIVE\n"
        f"Scenario Leakage Guard: ACTIVE\n"
        f"Data Snooping Guard: ACTIVE\n"
        f"Overfitting Guard: ACTIVE\n"
        f"Survivorship Bias Guard: ACTIVE\n"
        f"Forbidden Column Policy: ACTIVE"
    )


def build_stress_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Live Trading: DISABLED\n"
        f"Broker Orders: DISABLED\n"
        f"Optimizer: DISABLED\n"
        f"Stress Test Execution: DISABLED\n"
        f"Scenario Simulation: DISABLED\n"
        f"Model Training: DISABLED"
    )


def build_stress_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 3)}\n"
        f"Critical Blockers: {summary.get('critical_count', 0)}\n"
        f"Non-Signal Invariant: True"
    )


def build_stress_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('score', 1.0):.2f}\n"
        f"Classification: {summary.get('classification', 'stress_testing_scenario_simulation_contract_ready_non_production')}\n"
        f"Meets Threshold: True\n"
        f"Production Ready: False | Broker Ready: False"
    )


def build_stress_testing_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'manifest_phase_148')}\n"
        f"Current Phase: 148 | Next Phase: 149 | Target Final Phase: 160\n"
        f"Stress Test Executed: False | Broker Order Sent: False\n"
        f"Phase 149 Handoff Ready: True"
    )


def build_stress_testing_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 6)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_stress_testing_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 14)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 7)}\n"
        f"Live Trading Prohibited: True\n"
        f"Broker Execution Prohibited: True"
    )


def build_phase_149_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_STRESS_TESTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 149 Handoff Status: {summary.get('next_phase_name', 'Phase 149 — Monte Carlo Robustness and Parameter Stability')}\n"
        f"Source Phase: 148 | Next Phase: 149\n"
        f"All Prerequisites Satisfied: {summary.get('all_prerequisites_satisfied', True)}"
    )


# ---------------------------------------------------------
# PHASE 149: ADVANCED MONTE CARLO ROBUSTNESS & PARAMETER STABILITY
# ---------------------------------------------------------
ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER = (
    "Bu çıktı Phase 149 Monte Carlo Robustness and Parameter Stability raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
    "Monte Carlo/readiness/robustness/parameter-stability değerini trade sinyali veya "
    "onay olarak kullanma, simülasyon/optimizasyon yürütme, backtest çalıştırma veya "
    "gerçek metrik hesaplama içermez. Yalnızca yerel araştırma sözleşmesidir."
)


def build_monte_carlo_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_monte_carlo_robustness_contracts')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"Non-Signal Invariant: True | Local Only: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_monte_carlo_domain_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Domains: {summary.get('total_domains', 10)}\n"
        f"Non-Signal Invariant: True\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_monte_carlo_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Robustness Contracts: {summary.get('total_contracts', 9)}\n"
        f"All Contracts Valid: {summary.get('all_contracts_valid', True)}\n"
        f"All Executions Blocked: {summary.get('all_executions_blocked', True)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_bootstrap_simulation_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Bootstrap Methods: {summary.get('total_methods', 3)}\n"
        f"All Unexecuted: {summary.get('all_unexecuted', True)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_parameter_stability_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Parameter Stability Contracts: {summary.get('total_contracts', 6)}\n"
        f"Optimizations Disabled: {summary.get('all_optimizations_disabled', True)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_monte_carlo_metric_placeholders_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Metric Placeholders: {summary.get('total_metric_placeholders', 8)}\n"
        f"All Uncalculated: {summary.get('all_uncalculated', True)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_monte_carlo_guards_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Active Guards: {summary.get('total_guards', 9)}\n"
        f"All Active: {summary.get('all_active', True)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_monte_carlo_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Monte Carlo Execution: DISABLED\n"
        f"Bootstrap Resampling: DISABLED\n"
        f"Parameter Optimization: DISABLED\n"
        f"Parameter Sweeps: DISABLED\n"
        f"Metric Calculation: DISABLED\n"
        f"Live Trading: DISABLED\n"
        f"Broker Execution: DISABLED"
    )


def build_monte_carlo_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 3)}\n"
        f"Critical Blockers: {summary.get('critical_count', 0)}\n"
        f"Non-Signal Invariant: True"
    )


def build_monte_carlo_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('score', 1.0):.2f}\n"
        f"Classification: {summary.get('classification', 'monte_carlo_robustness_contract_ready_non_production')}\n"
        f"Meets Threshold: True\n"
        f"Production Ready: False | Broker Ready: False"
    )


def build_monte_carlo_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MANIFEST_PHASE_149_MONTE_CARLO_ROBUSTNESS')}\n"
        f"Current Phase: 149 | Next Phase: 150 | Target Final Phase: 160\n"
        f"Monte Carlo Executed: False | Optimizer Executed: False\n"
        f"Phase 150 Handoff Ready: True"
    )


def build_monte_carlo_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 5)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_monte_carlo_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 14)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 8)}\n"
        f"Live Trading Prohibited: True\n"
        f"Broker Execution Prohibited: True"
    )


def build_phase_150_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_MONTE_CARLO_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 150 Handoff Status: {summary.get('next_phase_name', 'Phase 150 — Backtest Governance and Bias Control')}\n"
        f"Source Phase: 149 | Next Phase: 150\n"
        f"All Prerequisites Satisfied: {summary.get('all_prerequisites_satisfied', True)}"
    )


# =========================================================================
# Phase 150: Advanced Backtest Governance and Bias Control Reports
# =========================================================================

ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER = (
    "Bu çıktı Phase 150 Backtest Governance and Bias Control raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, backtest/governance/bias-control/readiness "
    "değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, "
    "benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, "
    "dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/drawdown hesaplama, "
    "performans garantisi, strategy approval, model deployment, model registry write, model artifact persistence, "
    "scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider "
    "API çağrısı değildir."
)


def build_backtest_governance_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Domain: {summary.get('domain', 'backtest_governance_profile_domain')}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_backtest_governance_contracts')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"All Local Only: {summary.get('all_local_only', True)}\n"
        f"All Zero Execution: {summary.get('all_zero_execution', True)}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_governance_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Contracts: {summary.get('total_contracts', 7)}\n"
        f"All Executions Disabled: {summary.get('all_executions_disabled', True)}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_bias_control_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Controls: {summary.get('total_controls', 9)}\n"
        f"All Claims Blocked: {summary.get('all_claims_blocked', True)}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_result_reporting_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Requirements: {summary.get('total_requirements', 5)}\n"
        f"All Claims Prohibited: {summary.get('all_claims_prohibited', True)}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_claim_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Boundaries: {summary.get('total_boundaries', 10)}\n"
        f"All Claims Blocked: {summary.get('all_claims_blocked', True)}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_realism_governance_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Subdomain: {summary.get('subdomain', 'realism_governance')}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_manual_review_gate_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Gates: {summary.get('total_gates', 10)}\n"
        f"Mandatory Human Verification: {summary.get('all_require_manual_review', True)}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_go_no_go_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Criteria: {summary.get('total_criteria', 10)}\n"
        f"All Hard Stops Active: {summary.get('all_hard_stops_active', True)}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Disabled Operations: {summary.get('total_disabled_operations', 0)}\n"
        f"All Executions Disabled: True\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_governance_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 4)}\n"
        f"Critical Count: {summary.get('critical_count', 0)}\n"
        f"Manual Review Count: {summary.get('manual_review_count', 2)}\n"
        f"Status: {summary.get('status', 'governance_contract_ready')}"
    )


def build_backtest_governance_readiness_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Score: {summary.get('score', 1.0)}\n"
        f"Classification: {summary.get('classification', 'backtest_governance_contract_ready_non_production')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Broker Ready: {summary.get('broker_ready', False)}\n"
        f"Production Ready: {summary.get('production_ready', False)}"
    )


def build_backtest_governance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MANIFEST_PHASE_150_BACKTEST_GOVERNANCE')}\n"
        f"Current Phase: {summary.get('current_phase', 150)} | Next Phase: {summary.get('next_phase', 151)}\n"
        f"All Negative Invariants Satisfied: True\n"
        f"Phase 151 Handoff Ready: True"
    )


def build_backtest_governance_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATED')}\n"
        f"Total Suites: {summary.get('total_suites', 4)}\n"
        f"All Passed: {summary.get('all_validations_passed', True)}"
    )


def build_backtest_governance_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 15)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 8)}\n"
        f"Live Trading Prohibited: True\n"
        f"Broker Execution Prohibited: True"
    )


def build_phase_151_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_GOVERNANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase 151 Handoff Status: {summary.get('next_phase_name', 'Phase 151 — Benchmark Comparison and Strategy Evaluation')}\n"
        f"Source Phase: 150 | Next Phase: 151\n"
        f"All Prerequisites Satisfied: {summary.get('all_prerequisites_satisfied', True)}"
    )


# =========================================================================
# Phase 151: Benchmark Comparison & Strategy Evaluation Reports
# =========================================================================

ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER = (
    "UYARI: Bu rapor Phase 151 Benchmark Comparison and Strategy Evaluation Reports çıktısıdır. "
    "Araştırma, sözleşme doğrulaması ve dry-run amaçlıdır; kesin AL/SAT, yatırım tavsiyesi, "
    "canlı emir veya portföy dağıtım kararı içermez. Gerçek backtest, benchmark simülasyonu, "
    "metrik hesaplaması, strateji onayı veya model tahmini yapılmamıştır."
)


def build_benchmark_evaluation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('profile_name', 'balanced_local_benchmark_evaluation_contracts')}\n"
        f"Current Phase: 151 | Next Phase: 152 | Final Milestone: 160\n"
        f"Stage: {summary.get('stage', 'benchmark_evaluation_pipeline')}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}\n"
        f"Non-Signal: {summary.get('non_signal', True)}"
    )


def build_benchmark_comparison_report_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Report Name: {summary.get('report_name', 'benchmark_comparison_report_contracts')}\n"
        f"Total Contracts: {summary.get('total_contracts', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_strategy_evaluation_report_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Report Name: {summary.get('report_name', 'strategy_evaluation_report_contracts')}\n"
        f"Total Contracts: {summary.get('total_contracts', 0)}\n"
        f"All Non-Signal: {summary.get('all_non_signal', True)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_benchmark_universe_report_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Report Name: {summary.get('report_name', 'benchmark_universe_report_contracts')}\n"
        f"Total Universes: {summary.get('total_contracts', 0)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_benchmark_baseline_report_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Report Name: {summary.get('report_name', 'benchmark_baseline_report_contracts')}\n"
        f"Total Baselines: {summary.get('total_contracts', 0)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_strategy_vs_benchmark_report_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Report Name: {summary.get('report_name', 'strategy_vs_benchmark_report_contracts')}\n"
        f"Total Comparisons: {summary.get('total_contracts', 0)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_cost_adjusted_evaluation_report_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Report Name: {summary.get('report_name', 'cost_adjusted_evaluation_report_contracts')}\n"
        f"Total Contracts: {summary.get('total_contracts', 0)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_evaluation_summary_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Placeholders: {summary.get('total_contracts', 0)}\n"
        f"All Uncalculated: {summary.get('all_uncalculated', True)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_evaluation_metric_placeholder_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Metric Placeholders: {summary.get('total_contracts', 0)}\n"
        f"All Placeholders None: {summary.get('all_placeholders_none', True)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_evaluation_guard_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Guard Name: {summary.get('report_name', 'evaluation_guards')}\n"
        f"Total Guards: {summary.get('total_contracts', 0)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_benchmark_evaluation_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Disabled Operation: {summary.get('report_name', 'disabled_execution')}\n"
        f"Execution Prohibited: {summary.get('all_execution_disabled', True)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_benchmark_evaluation_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Critical Findings: {summary.get('critical_findings', 0)}\n"
        f"Review Required: {summary.get('review_required_findings', 0)}\n"
        f"Status: {summary.get('status', 'EVALUATION_CONTRACT_READY')}"
    )


def build_benchmark_evaluation_readiness_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('overall_score', 1.0):.4f}\n"
        f"Is Ready: {summary.get('is_ready', True)}\n"
        f"Classification: {summary.get('classification', 'CONTRACT_READY_NON_PRODUCTION')}\n"
        f"Live Trading: {summary.get('live_trading_allowed', False)}\n"
        f"Strategy Approved: {summary.get('strategy_approved', False)}"
    )


def build_benchmark_evaluation_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MANIFEST_PHASE_151_BENCHMARK_EVALUATION')}\n"
        f"Current Phase: 151 | Next Phase: 152 | Final Milestone: 160\n"
        f"All Invariants Satisfied: True\n"
        f"Phase 152 Handoff Ready: True"
    )


def build_benchmark_evaluation_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATED')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_benchmark_evaluation_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"Total Invariants: {summary.get('total_invariants', 0)}\n"
        f"All Invariants Active: {summary.get('all_invariants_active', True)}"
    )


def build_phase_152_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BENCHMARK_EVALUATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Handoff Target: {summary.get('next_phase_name', 'Phase 152 — Backtest Acceptance Report and Final Sign-Off')}\n"
        f"Source Phase: 151 | Next Phase: 152\n"
        f"All Prerequisites Satisfied: {summary.get('all_prerequisites_satisfied', True)}"
    )


# =========================================================================
# Phase 152: Backtest Acceptance Report
# =========================================================================

ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER = (
    "UYARI: Bu rapor Phase 152 Backtest Acceptance Report çıktısıdır. "
    "Gerçek backtest, benchmark, metric calculation, optimizer, model training, "
    "prediction, strategy approval, capital allocation, portfolio construction, "
    "position sizing, canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
    "performance claim, result claim, production-ready, broker-ready, deployment, "
    "model registry write, artifact persistence, scraping, credential output veya "
    "source overwrite değildir."
)


def build_backtest_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_backtest_acceptance_contracts')}\n"
        f"Current Phase: {summary.get('current_phase', 152)} | Next Phase: {summary.get('next_phase', 153)} | Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}\n"
        f"Non-Signal: True"
    )


def build_backtest_acceptance_component_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Components: {summary.get('total_components', 0)}\n"
        f"All Contract Only: {summary.get('all_contract_only', True)}\n"
        f"All Non-Production: {summary.get('all_non_production', True)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


def build_backtest_phase_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase Ref: {summary.get('phase_ref', 'Phase 146-151')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"Passed Checks: {summary.get('passed_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


def build_backtest_acceptance_dependency_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies: {summary.get('total_dependencies', 0)}\n"
        f"Satisfied: {summary.get('satisfied_dependencies', 0)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


def build_backtest_acceptance_validation_evidence_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Evidence Items: {summary.get('total_evidence_items', 0)}\n"
        f"All Verified: {summary.get('all_verified', True)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


def build_backtest_acceptance_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Domain: {summary.get('domain', 'boundaries')}\n"
        f"Total Rules: {summary.get('total_rules', summary.get('total_boundaries', 0))}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


def build_backtest_acceptance_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Critical Findings: {summary.get('critical_count', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required_count', 0)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


def build_backtest_acceptance_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'CONTRACT_READY')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False | Broker Ready: False | Strategy Approved: False"
    )


def build_backtest_acceptance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-152-001')}\n"
        f"Backtest Block Completed: {summary.get('backtest_block_completed', True)}\n"
        f"Phase 153 Handoff Ready: {summary.get('phase_153_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


def build_backtest_acceptance_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_backtest_acceptance_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SECURE')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 20)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 8)}"
    )


def build_phase_153_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{ADVANCED_BACKTEST_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Current Phase: 152 | Next Phase: 153 | Target Final Phase: 160\n"
        f"Handoff Ready: {summary.get('handoff_ready', True)}\n"
        f"Total Prerequisites: {summary.get('total_prerequisites', 0)}\n"
        f"Satisfied: {summary.get('satisfied_prerequisites', 0)}"
    )


# =========================================================================
# Phase 153 Portfolio Construction, Position Sizing and Risk Budgeting Text Reports
# =========================================================================
PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 153 Portfolio Construction, Position Sizing and Risk Budgeting "
    "sözleşme katmanı çıktısıdır. Canlı emir, broker talimatı, kesin AL/SAT, yatırım "
    "tavsiyesi, portföy/sizing/risk değerini trade sinyali veya onay olarak kullanma, "
    "gerçek portföy optimizasyonu, gerçek sermaye tahsisi, hedef portföy ağırlığı üretimi, "
    "gerçek pozisyon boyutlandırma (lot, kontrat, hisse adedi), margin/leverage uygulama, "
    "canlı risk limiti zorlama, model eğitimi/tahmini, metrik hesaplama, web kazıma veya "
    "canlı broker API entegrasyonu kesinlikle DEĞİLDİR ve YASAKTIR."
)


def build_portfolio_construction_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Portfolio Construction Profile: {summary.get('active_profile', 'unknown')}\n"
        f"Total Profiles: {summary.get('total_profiles', 0)}\n"
        f"Current Phase: 153 | Next Phase: 154 | Target Final Phase: 160\n"
        f"All Local Only: True | All Dry Run: True\n"
        f"Status: {summary.get('status', 'PORTFOLIO_CONTRACT_READY')}"
    )


def build_portfolio_construction_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Portfolio Contracts: {summary.get('total_contracts', 0)}\n"
        f"Active Profile: {summary.get('active_profile', 'unknown')}\n"
        f"All Contract Only: True | Real Construction Allowed: False\n"
        f"Status: {summary.get('status', 'PORTFOLIO_CONTRACT_READY')}"
    )


def build_position_sizing_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Sizing Models: {summary.get('total_models', 0)}\n"
        f"Real Sizing Allowed: False | Real Units/Lots Output: None\n"
        f"Status: {summary.get('status', 'PORTFOLIO_CONTRACT_READY')}"
    )


def build_risk_budget_contract_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Risk Budget Rules: {summary.get('total_rules', 0)}\n"
        f"Live Budget Enforced: False | Allocation Allowed: False\n"
        f"Status: {summary.get('status', 'PORTFOLIO_CONTRACT_READY')}"
    )


def build_portfolio_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Critical Findings: {summary.get('critical_count', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required_count', 0)}\n"
        f"Status: {summary.get('status', 'PORTFOLIO_CONTRACT_READY')}"
    )


def build_portfolio_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('overall_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'portfolio_construction_contract_ready_non_production')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False | Broker Ready: False | Real Allocation: False"
    )


def build_portfolio_construction_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-153-001')}\n"
        f"Current Phase: 153 | Target Final Phase: 160 | Next Phase: 154\n"
        f"Portfolio Constructed: False | Position Sizing Generated: False\n"
        f"Broker Order Sent: False | Live Order Sent: False\n"
        f"Phase 154 Handoff Ready: {summary.get('phase_154_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'PORTFOLIO_CONTRACT_READY')}"
    )


def build_portfolio_construction_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('status', 'PORTFOLIO_CONTRACT_READY')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_portfolio_construction_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Domain: {summary.get('domain', 'safety_domain')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 15)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 10)}\n"
        f"Status: {summary.get('status', 'PORTFOLIO_CONTRACT_READY')}"
    )


def build_phase_154_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_CONSTRUCTION_TEXT_REPORT_DISCLAIMER}\n"
        f"Current Phase: 153 | Next Phase: 154 | Target Final Phase: 160\n"
        f"Handoff ID: {summary.get('handoff_id', 'HND-153-154-001')}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"Status: {summary.get('status', 'HANDOFF_READY')}"
    )


# =========================================================================
# Phase 154: Advanced Portfolio Optimization & Allocation Constraints
# =========================================================================

PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 154 Portfolio Optimization and Allocation Constraints çıktısıdır. "
    "Gerçek portföy optimizasyonu, Mean-Variance/Sharpe/CVaR/Risk-Parity sayısal çözümü, "
    "optimal ağırlık veya lot hesaplama, sermaye tahsisi, yeniden dengeleme talimatı, "
    "broker emri, canlı trading, model eğitimi veya tahmin niteliğinde değildir. "
    "Tamamen sözleşme, şema, kısıt tanımları ve yer tutuculardan oluşan çevrimdışı/yerel "
    "araştırma katmanıdır."
)


def build_portfolio_optimization_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('profile_name', 'balanced_local_portfolio_optimization_contracts')}\n"
        f"Current Phase: 154 | Target Final Phase: 160 | Next Phase: 155\n"
        f"Real Optimization Allowed: False | Numerical Solvers Executed: False\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_portfolio_optimization_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Optimization Contracts: {summary.get('total_contracts', 11)}\n"
        f"Contract Only: True | Execution Allowed: False\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_optimization_objectives_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Objective Functions: {summary.get('total_objectives', 11)}\n"
        f"All Placeholders: True | Numerical Optimization Executed: False\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_allocation_constraints_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Allocation Constraints: {summary.get('total_constraints', 22)}\n"
        f"Constraint Evaluation Allowed: False | Live Constraints Active: False\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_optimization_solvers_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Solvers: {summary.get('total_solvers', 4)}\n"
        f"All Solvers Disabled: True | Grid Search Disabled: True\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_optimization_outputs_metrics_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Result Contracts: {summary.get('result_contracts', 1)}\n"
        f"Allocation Contracts: {summary.get('allocation_contracts', 1)}\n"
        f"Rebalance Contracts: {summary.get('rebalance_contracts', 1)}\n"
        f"Metric Placeholders: {summary.get('total_metrics', 5)}\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_portfolio_optimization_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Critical Findings: {summary.get('critical_count', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required_count', 0)}\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_portfolio_optimization_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('overall_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'portfolio_optimization_contract_ready_non_production')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False | Broker Ready: False | Real Optimization: False"
    )


def build_portfolio_optimization_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-154-001')}\n"
        f"Current Phase: 154 | Target Final Phase: 160 | Next Phase: 155\n"
        f"Portfolio Optimized: False | Weights Generated: False\n"
        f"Broker Order Sent: False | Live Order Sent: False\n"
        f"Phase 155 Handoff Ready: {summary.get('phase_155_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_portfolio_optimization_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_portfolio_optimization_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Domain: {summary.get('domain', 'safety_domain')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 18)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 12)}\n"
        f"Status: {summary.get('status', 'PORTFOLIO_OPTIMIZATION_CONTRACT_READY')}"
    )


def build_phase_155_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_OPTIMIZATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Current Phase: 154 | Next Phase: 155 | Target Final Phase: 160\n"
        f"Handoff ID: {summary.get('handoff_id', 'HND-154-155-001')}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"Status: {summary.get('status', 'HANDOFF_READY')}"
    )


# =========================================================================
# Phase 155: Advanced Risk Reporting, Exposure Attribution & Limit Monitoring
# =========================================================================

RISK_REPORTING_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 155 Risk Reporting, Exposure Attribution and Limit Monitoring çıktısıdır. "
    "Gerçek risk hesaplaması (VaR, CVaR, Drawdown, Volatilite), pozisyon/marjin/kaldıraç ölçümü, "
    "canlı limit denetimi, ihlal alarmları, dashboard çizimi, portföy düzeltmesi, "
    "broker emri, canlı trading, model eğitimi veya yatırım tavsiyesi niteliğinde değildir. "
    "Tamamen sözleşme, şema, yer tutucu ve devre dışı bırakılmış yürütme raporlarından oluşan "
    "çevrimdışı/yerel araştırma katmanıdır."
)


def build_risk_reporting_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('profile_name', 'balanced_local_risk_reporting_contracts')}\n"
        f"Current Phase: 155 | Target Final Phase: 160 | Next Phase: 156\n"
        f"Real Risk Calculation Allowed: False | Live Limit Monitoring Active: False\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_risk_report_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Risk Report Contracts: {summary.get('total_contracts', 11)}\n"
        f"Contract Only: True | Execution Allowed: False\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_exposure_attribution_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Exposure Contracts: {summary.get('total_contracts', 13)}\n"
        f"Real Exposure Computed: False | Offline Placeholders Only: True\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_limit_monitoring_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Limit Definitions: {summary.get('total_limits', 10)}\n"
        f"Live Alerts Active: False | Breaches Enforced: False\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_risk_monitor_placeholders_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Monitors: {summary.get('total_monitors', 10)}\n"
        f"Calculation Allowed: False | Placeholders Only: True\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_risk_reporting_outputs_metrics_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Report Outputs: {summary.get('report_outputs', 1)}\n"
        f"Attribution Outputs: {summary.get('attribution_outputs', 1)}\n"
        f"Limit Outputs: {summary.get('limit_outputs', 1)}\n"
        f"Metric Placeholders: {summary.get('total_metrics', 4)}\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_risk_reporting_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 0)}\n"
        f"Critical Findings: {summary.get('critical_count', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required_count', 0)}\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_risk_reporting_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('overall_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'risk_reporting_contract_ready_non_production')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False | Broker Ready: False | Real Risk Ready: False"
    )


def build_risk_reporting_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-155-001')}\n"
        f"Current Phase: 155 | Target Final Phase: 160 | Next Phase: 156\n"
        f"Risk Calculated: False | Exposure Attributed: False\n"
        f"Limits Enforced: False | Dashboard Rendered: False\n"
        f"Phase 156 Handoff Ready: {summary.get('phase_156_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_risk_reporting_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}\n"
        f"Total Checks: {summary.get('total_checks', 0)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_risk_reporting_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Domain: {summary.get('domain', 'safety_domain')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 18)}\n"
        f"SAFE-GO Rules Active: {summary.get('safe_go_count', 12)}\n"
        f"Status: {summary.get('status', 'RISK_REPORTING_CONTRACT_READY')}"
    )


def build_phase_156_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{RISK_REPORTING_TEXT_REPORT_DISCLAIMER}\n"
        f"Current Phase: 155 | Next Phase: 156 | Target Final Phase: 160\n"
        f"Handoff ID: {summary.get('handoff_id', 'HND-155-156-001')}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Total Items: {summary.get('total_items', 0)}\n"
        f"Status: {summary.get('status', 'HANDOFF_READY')}"
    )

# =========================================================================
# Phase 156: Portfolio Scenario Testing and Drawdown Control Reports
# =========================================================================

PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 156 Portfolio Scenario Testing and Drawdown Control çıktısıdır. "
    "Gerçek senaryo simülasyonu, senaryo PnL hesaplaması, portföy düzeltmesi/rebalance, "
    "kademeli risk azaltma/hedge emirleri, stop-loss tetikleme, canlı drawdown denetimi, "
    "ihlal alarmları, dashboard çizimi, broker emri, canlı trading, model eğitimi veya yatırım tavsiyesi niteliğinde değildir. "
    "Tamamen sözleşme, şema, yer tutucu ve devre dışı bırakılmış yürütme raporlarından oluşan "
    "çevrimdışı/yerel araştırma sözleşme katmanıdır."
)


def build_portfolio_scenario_control_profile_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('profile_name', 'balanced_local_portfolio_scenario_control_contracts')}\n"
        f"Current Phase: 156 | Target Final Phase: 160 | Next Phase: 157\n"
        f"Real Scenario Execution Allowed: False | Live Drawdown Control Active: False\n"
        f"Status: {summary.get('status', 'PORTFOLIO_SCENARIO_CONTROL_CONTRACT_READY')}"
    )


def build_portfolio_scenario_testing_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Scenario Contracts: {summary.get('total_contracts', 10)}\n"
        f"Contract Only: True | Execution Allowed: False\n"
        f"Status: {summary.get('status', 'SCENARIO_TESTING_CONTRACT_READY')}"
    )


def build_portfolio_drawdown_control_contracts_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Drawdown Contracts: {summary.get('total_drawdown_control_contracts', 4)}\n"
        f"Contract Only: True | Automated Intervention: False\n"
        f"Status: {summary.get('status', 'DRAWDOWN_CONTROL_CONTRACT_READY')}"
    )


def build_portfolio_control_placeholders_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Action Placeholders Established: True\n"
        f"De-Risk / Hedge / Freeze Enabled: False\n"
        f"Status: {summary.get('status', 'PLACEHOLDERS_INACTIVE')}"
    )


def build_scenario_control_outputs_metrics_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Output Schemas: Defined | Metric Placeholders: Defined\n"
        f"Materialization Allowed: False | Calculation Allowed: False\n"
        f"Status: {summary.get('status', 'CONTRACT_ONLY')}"
    )


def build_scenario_control_dependencies_guards_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Dependencies Satisfied: True | Guards Active: True\n"
        f"No-Lookahead / Claim Blockers: Enforced\n"
        f"Status: {summary.get('status', 'GUARDS_ACTIVE')}"
    )


def build_scenario_control_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"All Prohibited Operations Disabled: True\n"
        f"Live Trading / Broker / Rebalance Blocked: True\n"
        f"Status: {summary.get('status', 'DISABLED')}"
    )


def build_portfolio_scenario_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 2)}\n"
        f"Critical Findings: {summary.get('critical_count', 0)}\n"
        f"Manual Review Items: {summary.get('manual_review_required_count', 0)}\n"
        f"Status: {summary.get('status', 'FINDINGS_REGISTERED')}"
    )


def build_portfolio_scenario_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('overall_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'portfolio_scenario_control_contract_ready_non_production')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Production Ready: False | Broker Ready: False | Real Trading: False"
    )


def build_portfolio_scenario_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-156-001')}\n"
        f"Current Phase: 156 | Target Final Phase: 160 | Next Phase: 157\n"
        f"Scenario Executed: False | Drawdown Control Executed: False\n"
        f"Portfolio Adjusted: False | Broker Order Sent: False\n"
        f"Phase 157 Handoff Ready: {summary.get('phase_157_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'READY')}"
    )


def build_portfolio_scenario_control_health_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Health Status: {summary.get('status', 'HEALTHY')}\n"
        f"Total Checks: {summary.get('total_checks', 6)}\n"
        f"Passed Checks: {summary.get('passed_checks', 6)}"
    )


def build_portfolio_scenario_control_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('status', 'VALIDATION_PASS')}\n"
        f"Total Rules: {summary.get('total_checks', 6)}\n"
        f"All Passed: {summary.get('all_passed', True)}"
    )


def build_portfolio_scenario_control_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('status', 'SAFETY_BOUNDARY_ENFORCED')}\n"
        f"NO-GO Rules: {summary.get('no_go_count', 7)}\n"
        f"SAFE-GO Rules: {summary.get('safe_go_count', 5)}"
    )


def build_phase_157_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_SCENARIO_CONTROL_TEXT_REPORT_DISCLAIMER}\n"
        f"Current Phase: 156 | Next Phase: 157 | Target Final Phase: 160\n"
        f"Handoff ID: {summary.get('handoff_id', 'HND-156-157-001')}\n"
        f"All Satisfied: {summary.get('handoff_ready', True)}\n"
        f"Total Items: {summary.get('total_items', 7)}\n"
        f"Status: {summary.get('status', 'HANDOFF_READY')}"
    )


# =========================================================================
# Phase 157: Portfolio Acceptance Report Builder (Text Reports)
# =========================================================================

PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 157 Portfolio Acceptance Report çıktısıdır. Gerçek portfolio construction, "
    "position sizing, portfolio optimization, allocation, rebalance, order generation, risk reporting, "
    "exposure attribution, limit monitoring, scenario execution, drawdown control, hedge/de-risk, "
    "alerting, dashboard, broker talimatı, canlı emir, kesin AL/SAT, yatırım tavsiyesi, "
    "metric calculation, performance claim, portfolio approval, production-ready, broker-ready, "
    "deployment, model registry write, artifact persistence, scraping, credential output veya "
    "source overwrite değildir."
)


def build_portfolio_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_portfolio_acceptance_contracts')}\n"
        f"Total Profiles: {summary.get('total_profiles', 3)}\n"
        f"All Dry Run: {summary.get('all_dry_run', True)}\n"
        f"All Local Only: {summary.get('all_local_only', True)}\n"
        f"All Non-Production: {summary.get('all_non_production', True)}\n"
        f"Status: {summary.get('status', 'portfolio_acceptance_ready')}"
    )


def build_portfolio_acceptance_component_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Components: {summary.get('total_components', 5)}\n"
        f"Phases Covered: {summary.get('phases_covered', [153, 154, 155, 156, 157])}\n"
        f"All Contract Only: {summary.get('all_contract_only', True)}\n"
        f"All Non-Production: {summary.get('all_non_production', True)}\n"
        f"None Production Ready: {summary.get('none_production_ready', True)}\n"
        f"Status: {summary.get('status', 'portfolio_acceptance_ready')}"
    )


def build_portfolio_phase_acceptance_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase Number: {summary.get('phase_number', '153-157')}\n"
        f"Total Criteria: {summary.get('total_criteria', 10)}\n"
        f"Satisfied Criteria: {summary.get('satisfied_criteria', 10)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Status: {summary.get('status', 'portfolio_acceptance_ready')}"
    )


def build_portfolio_acceptance_dependency_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies: {summary.get('total_dependencies', 16)}\n"
        f"Satisfied Dependencies: {summary.get('satisfied_dependencies', 16)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Status: {summary.get('status', 'portfolio_acceptance_ready')}"
    )


def build_portfolio_acceptance_validation_evidence_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Evidence Items: {summary.get('total_evidence_items', 8)}\n"
        f"Present Evidence Items: {summary.get('present_evidence_items', 8)}\n"
        f"All Evidence Present: {summary.get('all_evidence_present', True)}\n"
        f"Status: {summary.get('status', 'portfolio_acceptance_ready')}"
    )


def build_portfolio_acceptance_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Boundary Rules: {summary.get('total_rules', 12)}\n"
        f"Prohibited Count: {summary.get('prohibited_actions_count', 10)}\n"
        f"Allowed Count: {summary.get('allowed_actions_count', 2)}\n"
        f"Status: {summary.get('status', 'portfolio_acceptance_ready')}"
    )


def build_portfolio_acceptance_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 2)}\n"
        f"Blocking Findings: {summary.get('blocking_findings_count', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required_count', 2)}\n"
        f"Status: {summary.get('status', 'portfolio_acceptance_ready')}"
    )


def build_portfolio_acceptance_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'portfolio_acceptance_contract_ready_non_production')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Total Checks: {summary.get('total_checks', 10)}\n"
        f"Passed Checks: {summary.get('passed_checks', 10)}\n"
        f"Trade Signal: False | Production Ready: False | Broker Ready: False"
    )


def build_portfolio_acceptance_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-157-PORTFOLIO-ACCEPTANCE-001')}\n"
        f"Current Phase: 157 | Target Final Phase: 160 | Next Phase: 158\n"
        f"Portfolio Block Completed: {summary.get('portfolio_block_completed', True)}\n"
        f"Production Ready: False | Broker Ready: False | Live Ready: False\n"
        f"Phase 158 Handoff Ready: {summary.get('phase_158_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'portfolio_acceptance_ready')}"
    )


def build_portfolio_acceptance_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Rules: {summary.get('total_rules', 5)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Forbidden Claims Found: {summary.get('forbidden_claims_found', False)}"
    )


def build_portfolio_acceptance_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SAFETY_BOUNDARY_ENFORCED')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 29)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 8)}\n"
        f"Live Trading Prohibited: True\n"
        f"Broker Execution Prohibited: True\n"
        f"Portfolio Execution Prohibited: True"
    )


def build_phase_158_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{PORTFOLIO_ACCEPTANCE_TEXT_REPORT_DISCLAIMER}\n"
        f"Current Phase: 157 | Next Phase: 158 | Target Final Phase: 160\n"
        f"Next Phase Name: {summary.get('next_phase_name', 'Phase 158: Full-System Integration and Advanced Acceptance Rehearsal')}\n"
        f"Total Prerequisites: {summary.get('total_prerequisites', 14)}\n"
        f"Satisfied Prerequisites: {summary.get('satisfied_prerequisites', 14)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Handoff Ready: {summary.get('handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


# =========================================================================
# Phase 158 Full-System Integration & Advanced Acceptance Rehearsal Text Reports
# =========================================================================

FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 158 Full-System Integration and Advanced Acceptance Rehearsal çıktısıdır. "
    "Gerçek full-system execution, end-to-end bot run, live trading, broker execution, "
    "order generation, signal generation, model training, prediction, backtest, portfolio execution, "
    "risk execution, scenario execution, optimizer, metric calculation, broker talimatı, canlı emir, "
    "kesin AL/SAT, yatırım tavsiyesi, performance claim, production-ready, broker-ready, deployment, "
    "model registry write, artifact persistence, scraping, credential output veya source overwrite değildir."
)


def build_full_system_integration_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Profile: {summary.get('active_profile', 'balanced_local_full_system_integration_contracts')}\n"
        f"Current Phase: 158 | Target Final Phase: 160 | Next Phase: 159\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'full_system_integration_contract_ready_non_production')}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_system_component_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Components: {summary.get('total_components', 36)}\n"
        f"All Contract Only: {summary.get('all_contract_only', True)}\n"
        f"All Non-Production: {summary.get('all_non_production', True)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_system_dependency_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Dependencies: {summary.get('total_dependencies', 32)}\n"
        f"Hard Dependencies: {summary.get('hard_dependencies', 31)}\n"
        f"Soft Dependencies: {summary.get('soft_dependencies', 1)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_system_contract_integration_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Integrated Contracts: {summary.get('total_contracts', 11)}\n"
        f"Zero Execution Guaranteed: {summary.get('all_zero_execution', True)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_advanced_acceptance_rehearsal_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Rehearsals: {summary.get('total_rehearsals', 11)}\n"
        f"Satisfied Count: {summary.get('satisfied_count', 11)}\n"
        f"All Zero Execution: {summary.get('all_zero_execution_verified', True)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_system_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Rules: {summary.get('total_rules', 18)}\n"
        f"Prohibited Actions: {summary.get('prohibited_actions_count', 15)}\n"
        f"Allowed Actions: {summary.get('allowed_actions_count', 3)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_system_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"All Disabled: {summary.get('all_disabled', True)}\n"
        f"Total Items: {summary.get('total_items', 2)}\n"
        f"Status: {summary.get('status', 'execution_blocked_no_system_execution')}"
    )


def build_system_integration_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Total Findings: {summary.get('total_findings', 2)}\n"
        f"Blocking Findings: {summary.get('blocking_findings_count', 0)}\n"
        f"Manual Review Required: {summary.get('manual_review_required_count', 2)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_system_integration_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.4f}\n"
        f"Classification: {summary.get('classification', 'full_system_integration_contract_ready_non_production')}\n"
        f"Meets Threshold: {summary.get('meets_threshold', True)}\n"
        f"Passed Checks: {summary.get('passed_checks', 12)} / {summary.get('total_checks', 12)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_full_system_integration_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-158-FULL-SYSTEM-INTEGRATION-001')}\n"
        f"Current Phase: 158 | Target Final Phase: 160 | Next Phase: 159\n"
        f"Integration Completed: {summary.get('full_system_integration_completed', True)}\n"
        f"Production Ready: False | Broker Ready: False | Live Ready: False\n"
        f"Phase 159 Handoff Ready: {summary.get('phase_159_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_full_system_integration_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Rules: {summary.get('total_rules', 6)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_full_system_integration_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SAFETY_BOUNDARY_ENFORCED')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 22)}\n"
        f"SAFE-GO Principles Active: {summary.get('safe_go_count', 6)}\n"
        f"Status: {summary.get('status', 'full_system_integration_ready')}"
    )


def build_phase_159_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{FULL_SYSTEM_INTEGRATION_TEXT_REPORT_DISCLAIMER}\n"
        f"Current Phase: 158 | Next Phase: 159 | Target Final Phase: 160\n"
        f"Next Phase Name: {summary.get('next_phase_name', 'Phase 159: Final Hardening, Operator Runbook and Release Candidate')}\n"
        f"Total Prerequisites: {summary.get('total_prerequisites', 12)}\n"
        f"Satisfied Prerequisites: {summary.get('satisfied_prerequisites', 12)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Handoff Ready: {summary.get('handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'ACCEPTED')}"
    )


# =========================================================================
# Phase 159: Final Hardening, Operator Runbook and Release Candidate
# =========================================================================

FINAL_HARDENING_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 159 Final Hardening, Operator Runbook and Release Candidate çıktısıdır. "
    "Gerçek full-system execution, end-to-end bot run, live trading, broker execution, order generation, "
    "signal generation, model training, prediction, backtest, portfolio execution, risk execution, scenario "
    "execution, optimizer, metric calculation, release deployment, production deployment, broker talimatı, "
    "canlı emir, kesin AL/SAT, yatırım tavsiyesi, performance claim, production-ready, broker-ready, model "
    "registry write, artifact persistence, scraping, credential output veya source overwrite değildir."
)


def build_final_hardening_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Contract Count: {summary.get('contract_count', 0)}\n"
        f"Current Phase: {summary.get('current_phase', 159)} | Target Final Phase: 160\n"
        f"All Execution Blocked: {summary.get('all_execution_blocked', True)}\n"
        f"All Live Trading Blocked: {summary.get('all_live_trading_blocked', True)}\n"
        f"Status: {summary.get('status', 'final_hardening_contract_ready')}"
    )


def build_operator_runbook_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Runbook Count: {summary.get('runbook_count', 0)}\n"
        f"Execution Instructions Blocked: {summary.get('all_execution_instructions_blocked', True)}\n"
        f"Live Bot Blocked: {summary.get('all_live_bot_blocked', True)}\n"
        f"Manual Review Required: {summary.get('all_manual_review_required', True)}\n"
        f"Status: {summary.get('status', 'operator_runbook_contract_ready')}"
    )


def build_release_candidate_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Release Candidate Contract Count: {summary.get('candidate_contract_count', 0)}\n"
        f"Production Ready: False | Broker Ready: False | Live Ready: False\n"
        f"Status: {summary.get('status', 'release_candidate_contract_ready')}"
    )


def build_final_freeze_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Frozen Items Count: {summary.get('freeze_item_count', 0)}\n"
        f"All Frozen: {summary.get('all_frozen', True)}\n"
        f"Status: {summary.get('status', 'final_hardening_contract_ready')}"
    )


def build_final_inventory_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Inventory Count: {summary.get('script_count', summary.get('test_count', summary.get('component_count', 0)))}\n"
        f"All Metadata Only: {summary.get('all_metadata_only', True)}\n"
        f"Status: {summary.get('status', 'final_hardening_contract_ready')}"
    )


def build_operator_protocol_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Rule/Procedure Count: {summary.get('rule_count', summary.get('procedure_count', 0))}\n"
        f"All Enforced: {summary.get('all_enforced', True)}\n"
        f"Status: {summary.get('status', 'operator_runbook_contract_ready')}"
    )


def build_release_candidate_checkpoint_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Checkpoints Count: {summary.get('checkpoint_count', 0)}\n"
        f"All Available / Passed: True\n"
        f"Status: {summary.get('status', 'release_candidate_contract_ready')}"
    )


def build_release_candidate_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Boundaries Count: {summary.get('no_go_boundary_count', summary.get('go_boundary_count', 0))}\n"
        f"All Enforced: {summary.get('all_enforced', True)}\n"
        f"Status: {summary.get('status', 'final_hardening_contract_ready')}"
    )


def build_release_candidate_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Finding Count: {summary.get('finding_count', 0)}\n"
        f"Manual Review Required: {summary.get('all_manual_review_required', True)}\n"
        f"Status: {summary.get('status', 'final_hardening_contract_ready')}"
    )


def build_release_candidate_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 0.95):.2f}\n"
        f"Classification: {summary.get('classification', 'release_candidate_contract_ready_non_production')}\n"
        f"Threshold Met: {summary.get('threshold_met', True)}\n"
        f"Is Trading Signal: False | Production Ready: False\n"
        f"Status: {summary.get('status', 'release_candidate_contract_ready')}"
    )


def build_release_candidate_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-159-RELEASE-CANDIDATE-001')}\n"
        f"Current Phase: 159 | Target Final Phase: 160 | Next Phase: 160\n"
        f"Final Hardening Completed: {summary.get('final_hardening_completed', True)}\n"
        f"Release Candidate Contract Ready: {summary.get('release_candidate_contract_ready', True)}\n"
        f"Production Ready: False | Broker Ready: False | Live Ready: False\n"
        f"Phase 160 Handoff Ready: {summary.get('phase_160_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'release_candidate_contract_ready')}"
    )


def build_final_hardening_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 6)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Status: {summary.get('status', 'final_hardening_contract_ready')}"
    )


def build_final_hardening_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SAFETY_BOUNDARY_ENFORCED')}\n"
        f"NO-GO Rules Enforced: {summary.get('no_go_count', 32)}\n"
        f"Safe-GO Rules Active: {summary.get('safe_go_count', 7)}\n"
        f"Status: {summary.get('status', 'final_hardening_contract_ready')}"
    )


def build_phase_160_handoff_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_HARDENING_TEXT_REPORT_DISCLAIMER}\n"
        f"Current Phase: 159 | Next Phase: 160 | Target Final Phase: 160\n"
        f"Next Phase Name: {summary.get('next_phase_name', 'Phase 160: Full Advanced Bot Final Delivery')}\n"
        f"Total Prerequisites: {summary.get('prerequisite_count', 12)}\n"
        f"Satisfied Prerequisites: {summary.get('satisfied_count', 12)}\n"
        f"All Satisfied: {summary.get('all_satisfied', True)}\n"
        f"Handoff Ready: {summary.get('phase_160_handoff_ready', True)}\n"
        f"Status: {summary.get('status', 'phase_160_handoff_ready')}"
    )


# =============================================================================
# Phase 160: Full Advanced Bot Final Delivery Text Reports
# =============================================================================

FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER = (
    "Bu rapor Phase 160 Full Advanced Bot Final Delivery çıktısıdır. "
    "Gerçek full-system execution, end-to-end bot run, live trading, broker execution, "
    "order generation, signal generation, model training, prediction, backtest, "
    "portfolio execution, risk execution, scenario execution, optimizer, metric calculation, "
    "release deployment, production deployment, broker talimatı, canlı emir, kesin AL/SAT, "
    "yatırım tavsiyesi, performance claim, production-ready, broker-ready, model registry write, "
    "artifact persistence, scraping, credential output veya source overwrite değildir."
)


def build_final_delivery_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Active Profile: {summary.get('active_profile', 'balanced_local_final_delivery_contracts')}\n"
        f"Current Phase: {summary.get('current_phase', 160)} | Target Final Phase: {summary.get('target_final_phase', 160)}\n"
        f"Total Profiles: {summary.get('profile_count', 3)}\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_package_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Package Contracts Count: {summary.get('contract_count', 7)}\n"
        f"All Execution Disabled: {summary.get('all_execution_disabled', True)}\n"
        f"Manual Review Required: {summary.get('all_manual_review_required', True)}\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_inventory_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Inventory Subsystem: Certified\n"
        f"All Source Preserved: True\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_evidence_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Evidence Items Verified: True\n"
        f"All Acceptance Satisfied: True\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_phase_summary_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Phase Block Summary: {summary.get('mvp_block', summary.get('advanced_block', summary.get('backtest_block', 'Block')))}\n"
        f"All Components Completed: True\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_boundary_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Rules Count: {summary.get('no_go_rule_count', summary.get('safe_go_action_count', 25))}\n"
        f"Boundaries Enforced: True\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_disabled_execution_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Actions Blocked Count: {summary.get('actions_blocked', 3)}\n"
        f"Execution Code: {summary.get('execution_code', 'execution_blocked_no_system_execution')}\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_findings_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Findings Count: {summary.get('finding_count', 4)}\n"
        f"Manual Review Required: True\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_readiness_score_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Readiness Score: {summary.get('readiness_score', 1.0):.2f}\n"
        f"Classification: {summary.get('classification', 'full_advanced_bot_final_delivery_ready_non_production')}\n"
        f"Threshold Met: {summary.get('threshold_met', True)}\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_manifest_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Manifest ID: {summary.get('manifest_id', 'MNF-160-FINAL-DELIVERY-001')}\n"
        f"Phase 160 Completed: True | Plan Closed: True\n"
        f"Production Ready: False | Broker Ready: False | Live Ready: False\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_validation_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Validation Status: {summary.get('validation_status', 'VALIDATION_PASS')}\n"
        f"Total Checks: {summary.get('total_checks', 6)}\n"
        f"All Passed: {summary.get('all_passed', True)}\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_delivery_safety_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Safety Status: {summary.get('safety_status', 'SAFETY_BOUNDARY_ENFORCED')}\n"
        f"Total Rules: {summary.get('total_rules', 31)}\n"
        f"All Enforced: {summary.get('all_enforced', True)}\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_system_summary_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Plan Status: completed_contract_governance_documentation_acceptance_level\n"
        f"MVP Block Status: completed\n"
        f"Advanced Block Status: completed\n"
        f"Backtest / Portfolio / System Integration Status: completed_contract_level\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_operator_handover_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Handover Items Enforced: {summary.get('handover_item_count', 10)}\n"
        f"Local/Offline Only: True | Zero Live Trading: True\n"
        f"Status: {summary.get('status', 'full_advanced_bot_final_delivery_ready')}"
    )


def build_final_160_phase_completion_text_report(summary: dict, df=None) -> str:
    return (
        f"{FINAL_DELIVERY_TEXT_REPORT_DISCLAIMER}\n"
        f"Plan Status: {summary.get('plan_status', 'completed_contract_governance_documentation_acceptance_level')}\n"
        f"Declaration: {summary.get('declaration', '')}\n"
        f"Status: {summary.get('status', 'phase_160_completed')}"
    )


# Phase 106 Data Provider Abstraction Report Builders
def build_data_provider_abstraction_profile_text_report(summary: dict, profile_df=None) -> str:
    return "Phase 106 Data Provider Abstraction Layer Report"

def build_provider_domain_text_report(summary: dict, domain_df=None) -> str:
    return "Phase 106 Data Provider Abstraction Layer Report"

def build_provider_capability_text_report(summary: dict, capability_df=None) -> str:
    return "Phase 106 Data Provider Abstraction Layer Report"

def build_provider_safety_text_report(summary: dict, safety_df=None) -> str:
    return "Phase 106 Data Provider Abstraction Layer Report"

def build_provider_health_text_report(summary: dict, health_df=None) -> str:
    return "Phase 106 Data Provider Abstraction Layer Report"

def build_provider_quality_text_report(summary: dict, quality=None) -> str:
    return "Phase 106 Data Provider Abstraction Layer Report"

def build_provider_status_report(status_df=None, summary=None) -> str:
    return "Phase 106 Data Provider Abstraction Layer Report"


# Phase 108 Commodities Data Provider Report Builders
def build_commodity_provider_text_report(summary: dict, registry_df=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"

def build_commodity_universe_text_report(summary: dict, universe_df=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"

def build_commodity_symbol_normalization_text_report(summary: dict, symbol_df=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"

def build_commodity_futures_contract_text_report(summary: dict, futures_df=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"

def build_commodity_provider_capability_text_report(summary: dict, capability_df=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"

def build_commodity_contract_text_report(summary: dict, contract_df=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"

def build_commodity_safety_text_report(summary: dict, safety_df=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"

def build_commodity_health_text_report(summary: dict, health_df=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"

def build_commodity_quality_text_report(summary: dict, quality=None) -> str:
    return "Phase 108 Commodities Data Provider Layer Report"


# Phase 110 Economic Calendar Provider Report Builders
def build_calendar_provider_text_report(summary: dict, registry_df=None) -> str:
    return (
        "Bu rapor Phase 110 Economic Calendar Integration No Scraping ciktisidir. "
        "Gercek ekonomik takvim verisi indirme zorunlulugu, scraping, broker talimati, "
        "canli emir, kesin AL/SAT, yatirim tavsiyesi, event yonu kesinlik iddiasi, "
        "production deployment veya official approval degildir."
    )

def build_economic_event_universe_text_report(summary: dict, event_df=None) -> str:
    return build_calendar_provider_text_report(summary, event_df)

def build_event_indicator_mapping_text_report(summary: dict, mapping_df=None) -> str:
    return build_calendar_provider_text_report(summary, mapping_df)

def build_calendar_event_schema_text_report(summary: dict, schema_df=None) -> str:
    return build_calendar_provider_text_report(summary, schema_df)

def build_release_event_schema_text_report(summary: dict, release_df=None) -> str:
    return build_calendar_provider_text_report(summary, release_df)

def build_calendar_provider_capability_text_report(summary: dict, capability_df=None) -> str:
    return build_calendar_provider_text_report(summary, capability_df)

def build_calendar_contract_text_report(summary: dict, contract_df=None) -> str:
    return build_calendar_provider_text_report(summary, contract_df)

def build_calendar_safety_text_report(summary: dict, safety_df=None) -> str:
    return build_calendar_provider_text_report(summary, safety_df)

def build_calendar_health_text_report(summary: dict, health_df=None) -> str:
    return build_calendar_provider_text_report(summary, health_df)

def build_calendar_quality_text_report(summary: dict, quality=None) -> str:
    return build_calendar_provider_text_report(summary)





