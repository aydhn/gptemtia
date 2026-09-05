from dataclasses import dataclass, asdict, field
from typing import List, Dict, Any


@dataclass
class DataLineageProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    dry_run: bool
    non_destructive: bool
    status_label: str
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DataLineageDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProvenanceSource:
    source_id: str
    source_name: str
    source_type: str
    provider_name: str
    dataset_type: str
    license_note: str
    retrieval_mode: str
    no_scraping_policy: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SourceReference:
    reference_id: str
    source_id: str
    reference_type: str
    reference_value: str
    canonical_reference: str
    metadata_only: bool
    contains_credentials: bool
    contains_full_text: bool
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProviderProvenance:
    provenance_id: str
    provider_name: str
    provider_type: str
    source_id: str
    capability_ref: str
    license_note: str
    credential_policy: str
    no_scraping_policy: str
    confidence_label: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DatasetProvenance:
    provenance_id: str
    dataset_name: str
    dataset_type: str
    provider_name: str
    source_reference_id: str
    schema_id: str
    retrieval_mode: str
    original_ref: str
    normalized_ref: str
    source_preserved: bool
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SchemaProvenance:
    provenance_id: str
    dataset_type: str
    schema_name: str
    schema_version: str
    source_schema_ref: str
    canonical_schema_ref: str
    mapping_note: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TransformationProvenance:
    provenance_id: str
    dataset_type: str
    transformation_rule: str
    source_field: str
    target_field: str
    original_value_repr: str
    normalized_value_repr: str
    source_preserved: bool
    destructive_action_allowed: bool
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AuditTrailEvent:
    audit_id: str
    event_type: str
    dataset_type: str
    provider_name: str
    source_id: str
    related_record_id: str
    event_note: str
    destructive_action_allowed: bool
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class LineageFinding:
    finding_id: str
    finding_type: str
    dataset_type: str
    provider_name: str
    source_id: str
    severity_label: str
    status_label: str
    message: str
    recommendation: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TraceabilityScore:
    score_id: str
    entity_name: str
    entity_type: str
    dataset_type: str
    provider_name: str
    score: float
    status_label: str
    missing_links: int
    manual_review_count: int
    notes: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def build_data_lineage_profile_id(profile_name: str) -> str:
    slug = profile_name.lower().replace(" ", "_").replace("-", "_")
    return f"lineage_profile_{slug}"


def build_data_lineage_domain_id(domain_label: str) -> str:
    slug = domain_label.lower().replace(" ", "_").replace("-", "_")
    return f"lineage_domain_{slug}"


def build_provenance_source_id(source_name: str, provider_name: str) -> str:
    s_slug = source_name.lower().replace(" ", "_").replace("-", "_")
    p_slug = provider_name.lower().replace(" ", "_").replace("-", "_")
    return f"prov_src_{p_slug}_{s_slug}"


def build_source_reference_id(source_id: str, reference_type: str) -> str:
    r_slug = reference_type.lower().replace(" ", "_").replace("-", "_")
    return f"ref_{source_id}_{r_slug}"


def build_provider_provenance_id(provider_name: str) -> str:
    p_slug = provider_name.lower().replace(" ", "_").replace("-", "_")
    return f"prov_rec_{p_slug}"


def build_dataset_provenance_id(dataset_name: str, provider_name: str) -> str:
    d_slug = dataset_name.lower().replace(" ", "_").replace("-", "_")
    p_slug = provider_name.lower().replace(" ", "_").replace("-", "_")
    return f"ds_prov_{p_slug}_{d_slug}"


def build_schema_provenance_id(dataset_type: str, schema_version: str) -> str:
    d_slug = dataset_type.lower().replace(" ", "_").replace("-", "_")
    v_slug = schema_version.lower().replace(".", "_").replace("-", "_")
    return f"schema_prov_{d_slug}_{v_slug}"


def build_transformation_provenance_id(dataset_type: str, source_field: str, target_field: str) -> str:
    d_slug = dataset_type.lower().replace(" ", "_").replace("-", "_")
    sf_slug = source_field.lower().replace(" ", "_").replace(",", "_").replace("/", "_")
    tf_slug = target_field.lower().replace(" ", "_").replace(",", "_").replace("/", "_")
    return f"trans_prov_{d_slug}_{sf_slug}_to_{tf_slug}"


def build_audit_trail_event_id(event_type: str, related_record_id: str) -> str:
    e_slug = event_type.lower().replace(" ", "_").replace("-", "_")
    r_slug = related_record_id.lower().replace(" ", "_").replace("-", "_")
    return f"audit_{e_slug}_{r_slug}"


def build_lineage_finding_id(finding_type: str, dataset_type: str, provider_name: str) -> str:
    f_slug = finding_type.lower().replace(" ", "_").replace("-", "_")
    d_slug = dataset_type.lower().replace(" ", "_").replace("-", "_")
    p_slug = provider_name.lower().replace(" ", "_").replace("-", "_")
    return f"finding_{f_slug}_{d_slug}_{p_slug}"


def build_traceability_score_id(entity_name: str, entity_type: str) -> str:
    e_slug = entity_name.lower().replace(" ", "_").replace("-", "_").replace("/", "_")
    t_slug = entity_type.lower().replace(" ", "_").replace("-", "_")
    return f"trace_score_{t_slug}_{e_slug}"
