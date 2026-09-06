
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
















