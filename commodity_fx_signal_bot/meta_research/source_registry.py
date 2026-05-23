from dataclasses import dataclass

import pandas as pd

from meta_research.meta_config import MetaResearchProfile
from meta_research.meta_labels import validate_evidence_source


class SourceConfigError(Exception):
    pass

@dataclass(frozen=True)
class EvidenceSourceDefinition:
    source_label: str
    description: str
    default_weight: float
    reliability_prior: float
    required: bool
    enabled: bool
    notes: str = ""

def build_default_evidence_sources(profile: MetaResearchProfile) -> list[EvidenceSourceDefinition]:
    sources = []

    if profile.include_technical:
        sources.append(EvidenceSourceDefinition(
            source_label="technical_evidence",
            description="Technical summary and signal candidates.",
            default_weight=0.08,
            reliability_prior=0.80,
            required=True,
            enabled=True
        ))
    if profile.include_strategy:
        sources.append(EvidenceSourceDefinition(
            source_label="strategy_evidence",
            description="Strategy candidates and rules.",
            default_weight=0.08,
            reliability_prior=0.75,
            required=False,
            enabled=True
        ))
    if profile.include_risk_level:
        sources.append(EvidenceSourceDefinition(
            source_label="risk_level_evidence",
            description="Risk, sizing, and level candidates.",
            default_weight=0.08,
            reliability_prior=0.85,
            required=False,
            enabled=True
        ))
    if profile.include_backtest:
        sources.append(EvidenceSourceDefinition(
            source_label="backtest_evidence",
            description="Backtest and performance summary.",
            default_weight=0.10,
            reliability_prior=0.70,
            required=False,
            enabled=True
        ))
    if profile.include_validation:
        sources.append(EvidenceSourceDefinition(
            source_label="validation_evidence",
            description="Validation, walk-forward, overfitting.",
            default_weight=0.12,
            reliability_prior=0.75,
            required=False,
            enabled=True
        ))
    if profile.include_ml:
        sources.append(EvidenceSourceDefinition(
            source_label="ml_evidence",
            description="ML prediction and integration context.",
            default_weight=0.10,
            reliability_prior=0.65,
            required=False,
            enabled=True
        ))
    if profile.include_paper:
        sources.append(EvidenceSourceDefinition(
            source_label="paper_evidence",
            description="Paper trading summary.",
            default_weight=0.08,
            reliability_prior=0.80,
            required=False,
            enabled=True
        ))
    if profile.include_factor:
        sources.append(EvidenceSourceDefinition(
            source_label="factor_evidence",
            description="Factor score, rank, IC.",
            default_weight=0.10,
            reliability_prior=0.60,
            required=False,
            enabled=True
        ))
    if profile.include_synthetic_index:
        sources.append(EvidenceSourceDefinition(
            source_label="synthetic_index_evidence",
            description="Synthetic index relative strength and rotation.",
            default_weight=0.06,
            reliability_prior=0.70,
            required=False,
            enabled=True
        ))
    if profile.include_portfolio:
        sources.append(EvidenceSourceDefinition(
            source_label="portfolio_evidence",
            description="Portfolio research and basket exposure.",
            default_weight=0.06,
            reliability_prior=0.70,
            required=False,
            enabled=True
        ))
    if profile.include_regime:
        sources.append(EvidenceSourceDefinition(
            source_label="regime_evidence",
            description="Portfolio regime and stress.",
            default_weight=0.05,
            reliability_prior=0.65,
            required=False,
            enabled=True
        ))

    # Always include quality as contextual evidence if needed, but we check if it is part of another flag.
    # We will add it explicitly since it's in the default weights.
    sources.append(EvidenceSourceDefinition(
        source_label="quality_evidence",
        description="Observability and security quality summary.",
        default_weight=0.05,
        reliability_prior=0.90,
        required=False,
        enabled=True
    ))

    # Optional but in starting weights
    sources.append(EvidenceSourceDefinition(
        source_label="performance_evidence",
        description="Historical performance metrics.",
        default_weight=0.08,
        reliability_prior=0.80,
        required=False,
        enabled=True
    ))
    sources.append(EvidenceSourceDefinition(
        source_label="research_report_evidence",
        description="Symbol research reports.",
        default_weight=0.06,
        reliability_prior=0.70,
        required=False,
        enabled=True
    ))

    validate_evidence_source_definitions(sources)
    return sources

def evidence_sources_to_dataframe(sources: list[EvidenceSourceDefinition]) -> pd.DataFrame:
    data = []
    for s in sources:
        data.append({
            "source_label": s.source_label,
            "description": s.description,
            "default_weight": s.default_weight,
            "reliability_prior": s.reliability_prior,
            "required": s.required,
            "enabled": s.enabled,
            "notes": s.notes
        })
    return pd.DataFrame(data)

def get_source_weight(source_label: str, sources: list[EvidenceSourceDefinition]) -> float:
    for s in sources:
        if s.source_label == source_label:
            return s.default_weight
    return 0.0

def get_source_reliability_prior(source_label: str, sources: list[EvidenceSourceDefinition]) -> float:
    for s in sources:
        if s.source_label == source_label:
            return s.reliability_prior
    return 0.50

def validate_evidence_source_definitions(sources: list[EvidenceSourceDefinition]) -> dict:
    total_weight = sum(s.default_weight for s in sources if s.enabled)
    warnings = []

    for s in sources:
        try:
            validate_evidence_source(s.source_label)
        except Exception as e:
            warnings.append(str(e))

        if not (0 <= s.default_weight <= 1):
            raise SourceConfigError(f"Weight for {s.source_label} must be between 0 and 1")
        if not (0 <= s.reliability_prior <= 1):
            raise SourceConfigError(f"Reliability prior for {s.source_label} must be between 0 and 1")

    return {
        "valid": len(warnings) == 0,
        "total_weight": total_weight,
        "source_count": len(sources),
        "warnings": warnings
    }
