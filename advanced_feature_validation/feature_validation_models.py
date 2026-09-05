"""Data models and entities for Phase 121 Feature Validation Layer.

Defines schemas for profiles, domains, rules, findings, integrity manifests, and scores.
Strictly non-signal and research-only.
"""

from dataclasses import asdict, dataclass, field
import hashlib
import re
from typing import Any, Dict, List


@dataclass
class FeatureValidationProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    dry_run: bool
    non_signal: bool
    no_leakage_required: bool
    status_label: str
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureValidationDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureValidationRule:
    rule_id: str
    rule_name: str
    validation_family: str = "general"
    severity_label: str = "validation_medium"
    description: str = ""
    required_inputs: List[str] = field(default_factory=list)
    forbidden_patterns: List[str] = field(default_factory=list)
    non_signal_required: bool = True
    manual_review_required: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


from advanced_feature_validation.feature_validation_config import FeatureValidationProfile


@dataclass
class FeatureValidationFinding:
    finding_id: str
    rule_id: str
    finding_type: str
    feature_or_matrix_name: str = ""
    severity_label: str = "validation_medium"
    status_label: str = "validation_manual_review_required"
    message: str = ""
    recommendation: str = ""
    column_name: str = ""
    severity: str = "HIGH"
    current_phase: int = 121
    destructive_action_allowed: bool = False
    manual_review_required: bool = True

    def __post_init__(self):
        if not self.feature_or_matrix_name and self.column_name:
            self.feature_or_matrix_name = self.column_name
        if not self.column_name and self.feature_or_matrix_name:
            self.column_name = self.feature_or_matrix_name
        if self.severity and not self.severity_label:
            self.severity_label = f"validation_{self.severity.lower()}"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureMatrixIntegrityManifest:
    matrix_name: str
    manifest_id: str = "mani_default"
    row_count: int = 0
    feature_count: int = 0
    total_rows: int = 0
    total_columns: int = 0
    forbidden_column_count: int = 0
    duplicate_feature_count: int = 0
    future_leakage_risk_count: int = 0
    missingness_warning_count: int = 0
    current_phase: int = 121
    checksum: str = "sha256_mock_manifest"
    non_signal: bool = True
    contains_target_or_prediction: bool = False
    contains_full_article_text: bool = False
    source_preserved: bool = True
    manual_review_required: bool = True

    def __post_init__(self):
        if self.total_rows and not self.row_count:
            self.row_count = self.total_rows
        if not self.total_rows and self.row_count:
            self.total_rows = self.row_count
        if self.total_columns and not self.feature_count:
            self.feature_count = self.total_columns
        if not self.total_columns and self.feature_count:
            self.total_columns = self.feature_count

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureValidationScore:
    score_id: str
    matrix_name: str
    validation_score: float
    status_label: str
    critical_findings: int
    high_findings: int
    medium_findings: int
    manual_review_count: int
    official_approval: bool = False
    production_ready: bool = False
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureValidationScoreResult:
    overall_score: float
    lookahead_score: float = 1.0
    forbidden_column_score: float = 1.0
    integrity_score: float = 1.0
    numeric_sanity_score: float = 1.0
    completeness_score: float = 1.0
    is_passing: bool = True
    current_phase: int = 121

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)



def _slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_]+", "_", text.strip().lower())
    return re.sub(r"_+", "_", cleaned).strip("_")


def build_feature_validation_profile_id(profile_name: str) -> str:
    slug = _slugify(profile_name)
    return f"val_prof_{slug}"


def build_feature_validation_domain_id(domain_label: str) -> str:
    slug = _slugify(domain_label)
    return f"val_dom_{slug}"


def build_feature_validation_rule_id(rule_name: str, validation_family: str) -> str:
    slug_rule = _slugify(rule_name)
    slug_fam = _slugify(validation_family)
    return f"val_rule_{slug_fam}_{slug_rule}"


def build_feature_validation_finding_id(rule_id: str, feature_or_matrix_name: str) -> str:
    seed = f"{rule_id}:{feature_or_matrix_name}".encode("utf-8")
    short_hash = hashlib.sha256(seed).hexdigest()[:8]
    slug_name = _slugify(feature_or_matrix_name)[:20]
    return f"find_{slug_name}_{short_hash}"


def build_feature_matrix_integrity_manifest_id(matrix_name: str) -> str:
    slug = _slugify(matrix_name)
    seed = matrix_name.encode("utf-8")
    short_hash = hashlib.sha256(seed).hexdigest()[:8]
    return f"mani_{slug}_{short_hash}"


def build_feature_validation_score_id(matrix_name: str) -> str:
    slug = _slugify(matrix_name)
    return f"val_score_{slug}"
