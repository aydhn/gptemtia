# -*- coding: utf-8 -*-
"""Phase 155: Advanced Risk Reporting, Exposure Attribution and Limit Monitoring Package.

Provides local/offline risk report contract layer, exposure attribution templates,
limit monitoring specifications, monitor placeholders, guards, and Phase 156 handoff.
"""

from .risk_reporting_config import (
    RiskReportingProfile,
    get_risk_reporting_profile,
    get_default_risk_reporting_profile,
    list_risk_reporting_profiles,
    validate_risk_reporting_profiles,
)
from .risk_reporting_labels import (
    RISK_REPORT_CONTRACT_READY,
    EXECUTION_CONTRACT_ONLY,
    ALL_DOMAINS,
)
from .risk_reporting_models import (
    RiskReportingProfileItem,
    RiskReportContract,
    ExposureAttributionContract,
    LimitMonitoringContract,
    RiskMetricPlaceholder,
    ExposurePlaceholder,
    LimitMonitoringPlaceholder,
    RiskReportingGuardItem,
    RiskReportingDisabledExecutionItem,
    RiskReportingFinding,
    RiskReportingReadinessScore,
    RiskReportingManifest,
    RiskReportingManualReviewItem,
)

__version__ = "155.0.0"
__all__ = [
    "RiskReportingProfile",
    "get_risk_reporting_profile",
    "get_default_risk_reporting_profile",
    "list_risk_reporting_profiles",
    "validate_risk_reporting_profiles",
    "RISK_REPORT_CONTRACT_READY",
    "EXECUTION_CONTRACT_ONLY",
    "ALL_DOMAINS",
    "RiskReportingProfileItem",
    "RiskReportContract",
    "ExposureAttributionContract",
    "LimitMonitoringContract",
    "RiskMetricPlaceholder",
    "ExposurePlaceholder",
    "LimitMonitoringPlaceholder",
    "RiskReportingGuardItem",
    "RiskReportingDisabledExecutionItem",
    "RiskReportingFinding",
    "RiskReportingReadinessScore",
    "RiskReportingManifest",
    "RiskReportingManualReviewItem",
]
