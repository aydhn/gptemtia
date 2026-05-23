#!/bin/bash
cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/meta_config.py
from dataclasses import dataclass
from config.settings import Settings

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class MetaResearchProfile:
    name: str
    description: str
    min_sources: int = 3
    min_evidence_quality: float = 0.40
    conflict_threshold: float = 0.35
    high_agreement_threshold: float = 0.70
    uncertainty_penalty_enabled: bool = True
    quality_penalty_enabled: bool = True
    missing_source_penalty_enabled: bool = True
    include_technical: bool = True
    include_strategy: bool = True
    include_risk_level: bool = True
    include_backtest: bool = True
    include_validation: bool = True
    include_ml: bool = True
    include_paper: bool = True
    include_factor: bool = True
    include_synthetic_index: bool = True
    include_portfolio: bool = True
    include_regime: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_META_RESEARCH_PROFILES = [
    MetaResearchProfile(
        name="balanced_meta_research",
        description="Balanced meta research configuration.",
        min_sources=3,
        min_evidence_quality=0.40,
        conflict_threshold=0.35,
        high_agreement_threshold=0.70,
        notes="Genel amaçlı multi-source meta research ve consensus profili."
    ),
    MetaResearchProfile(
        name="strict_meta_research",
        description="Strict meta research configuration.",
        min_sources=5,
        min_evidence_quality=0.55,
        conflict_threshold=0.25,
        high_agreement_threshold=0.75,
        uncertainty_penalty_enabled=True,
        quality_penalty_enabled=True,
        missing_source_penalty_enabled=True,
        min_quality_score=0.55,
        notes="Daha sıkı kalite, kaynak sayısı ve çelişki toleransı kullanan profil."
    ),
    MetaResearchProfile(
        name="technical_factor_meta_research",
        description="Technical and factor meta research configuration.",
        include_technical=True,
        include_strategy=True,
        include_risk_level=True,
        include_backtest=False,
        include_validation=False,
        include_ml=False,
        include_paper=False,
        include_factor=True,
        include_synthetic_index=True,
        include_portfolio=False,
        include_regime=False,
        notes="Teknik, strateji, sentetik index ve factor araştırmasını birleştirir."
    ),
    MetaResearchProfile(
        name="ml_validation_meta_research",
        description="ML and validation meta research configuration.",
        include_technical=False,
        include_strategy=False,
        include_risk_level=False,
        include_backtest=True,
        include_validation=True,
        include_ml=True,
        include_paper=True,
        include_factor=False,
        include_synthetic_index=False,
        include_portfolio=False,
        include_regime=False,
        notes="Backtest, validation, ML ve paper çıktılarından konsensüs üretir."
    )
]

def list_meta_research_profiles(enabled_only: bool = True) -> list[MetaResearchProfile]:
    if enabled_only:
        return [p for p in _META_RESEARCH_PROFILES if p.enabled]
    return _META_RESEARCH_PROFILES

def get_meta_research_profile(name: str) -> MetaResearchProfile:
    for profile in _META_RESEARCH_PROFILES:
        if profile.name == name:
            return profile
    raise ConfigError(f"Unknown meta research profile: {name}")

def get_default_meta_research_profile() -> MetaResearchProfile:
    settings = Settings()
    return get_meta_research_profile(settings.default_meta_research_profile)

def validate_meta_research_profiles() -> None:
    for profile in _META_RESEARCH_PROFILES:
        if profile.min_sources <= 0:
            raise ConfigError(f"Profile {profile.name} min_sources must be positive")
        if not (0 <= profile.min_evidence_quality <= 1):
            raise ConfigError(f"Profile {profile.name} min_evidence_quality must be between 0 and 1")
        if not (0 <= profile.conflict_threshold <= 1):
            raise ConfigError(f"Profile {profile.name} conflict_threshold must be between 0 and 1")
        if not (0 <= profile.high_agreement_threshold <= 1):
            raise ConfigError(f"Profile {profile.name} high_agreement_threshold must be between 0 and 1")
        if not (0 <= profile.min_quality_score <= 1):
            raise ConfigError(f"Profile {profile.name} min_quality_score must be between 0 and 1")

        include_flags = [
            profile.include_technical,
            profile.include_strategy,
            profile.include_risk_level,
            profile.include_backtest,
            profile.include_validation,
            profile.include_ml,
            profile.include_paper,
            profile.include_factor,
            profile.include_synthetic_index,
            profile.include_portfolio,
            profile.include_regime
        ]
        if not any(include_flags):
            raise ConfigError(f"Profile {profile.name} must have at least one include flag set to True")
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/meta_labels.py
class LabelError(Exception):
    pass

EVIDENCE_SOURCE_LABELS = [
    "technical_evidence",
    "strategy_evidence",
    "risk_level_evidence",
    "backtest_evidence",
    "performance_evidence",
    "validation_evidence",
    "ml_evidence",
    "paper_evidence",
    "research_report_evidence",
    "synthetic_index_evidence",
    "portfolio_evidence",
    "regime_evidence",
    "factor_evidence",
    "quality_evidence",
    "unknown_evidence"
]

EVIDENCE_DIRECTION_LABELS = [
    "supportive_evidence",
    "conflicting_evidence",
    "neutral_evidence",
    "uncertain_evidence",
    "missing_evidence",
    "unknown_evidence_direction"
]

CONSENSUS_LABELS = [
    "strong_positive_consensus",
    "moderate_positive_consensus",
    "neutral_consensus",
    "mixed_consensus",
    "moderate_negative_consensus",
    "strong_negative_consensus",
    "insufficient_consensus_data",
    "unknown_consensus"
]

CONFIDENCE_LABELS = [
    "high_confidence_research",
    "medium_confidence_research",
    "low_confidence_research",
    "unreliable_research",
    "unknown_confidence"
]

def list_evidence_source_labels() -> list[str]:
    return EVIDENCE_SOURCE_LABELS

def list_evidence_direction_labels() -> list[str]:
    return EVIDENCE_DIRECTION_LABELS

def list_consensus_labels() -> list[str]:
    return CONSENSUS_LABELS

def list_confidence_labels() -> list[str]:
    return CONFIDENCE_LABELS

def validate_evidence_source(label: str) -> None:
    if label not in EVIDENCE_SOURCE_LABELS:
        raise LabelError(f"Invalid evidence source label: {label}")

def validate_evidence_direction(label: str) -> None:
    if label not in EVIDENCE_DIRECTION_LABELS:
        raise LabelError(f"Invalid evidence direction label: {label}")

def validate_consensus_label(label: str) -> None:
    if label not in CONSENSUS_LABELS:
        raise LabelError(f"Invalid consensus label: {label}")

def validate_confidence_label(label: str) -> None:
    if label not in CONFIDENCE_LABELS:
        raise LabelError(f"Invalid confidence label: {label}")
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/meta_models.py
from dataclasses import dataclass, asdict

@dataclass
class ResearchEvidence:
    evidence_id: str
    symbol: str
    timeframe: str
    source_label: str
    evidence_direction: str
    raw_score: float | None
    normalized_score: float | None
    confidence_score: float | None
    quality_score: float | None
    uncertainty_score: float | None
    source_timestamp: str | None
    summary: dict
    warnings: list[str]

@dataclass
class ConsensusResult:
    symbol: str
    timeframe: str
    evidence_count: int
    available_source_count: int
    consensus_score: float | None
    confidence_score: float | None
    uncertainty_score: float | None
    conflict_score: float | None
    consensus_label: str
    confidence_label: str
    supportive_count: int
    conflicting_count: int
    neutral_count: int
    missing_count: int
    warnings: list[str]

@dataclass
class MetaResearchSnapshot:
    symbol: str
    timeframe: str
    asset_class: str | None
    consensus: ConsensusResult
    evidence: list[ResearchEvidence]
    ensemble_score: float | None
    quality_adjusted_score: float | None
    final_research_label: str
    warnings: list[str]

def build_evidence_id(symbol: str, timeframe: str, source_label: str) -> str:
    return f"{symbol}_{timeframe}_{source_label}"

def build_meta_snapshot_id(symbol: str, timeframe: str) -> str:
    return f"{symbol}_{timeframe}_snapshot"

def clamp_meta_score(value: float | None) -> float | None:
    if value is None:
        return None
    return max(0.0, min(1.0, value))

def research_evidence_to_dict(evidence: ResearchEvidence) -> dict:
    d = asdict(evidence)
    d["raw_score"] = clamp_meta_score(d.get("raw_score"))
    d["normalized_score"] = clamp_meta_score(d.get("normalized_score"))
    d["confidence_score"] = clamp_meta_score(d.get("confidence_score"))
    d["quality_score"] = clamp_meta_score(d.get("quality_score"))
    d["uncertainty_score"] = clamp_meta_score(d.get("uncertainty_score"))
    return d

def consensus_result_to_dict(result: ConsensusResult) -> dict:
    d = asdict(result)
    d["consensus_score"] = clamp_meta_score(d.get("consensus_score"))
    d["confidence_score"] = clamp_meta_score(d.get("confidence_score"))
    d["uncertainty_score"] = clamp_meta_score(d.get("uncertainty_score"))
    d["conflict_score"] = clamp_meta_score(d.get("conflict_score"))
    return d

def meta_research_snapshot_to_dict(snapshot: MetaResearchSnapshot) -> dict:
    d = asdict(snapshot)
    d["consensus"] = consensus_result_to_dict(snapshot.consensus)
    d["evidence"] = [research_evidence_to_dict(e) for e in snapshot.evidence]
    d["ensemble_score"] = clamp_meta_score(d.get("ensemble_score"))
    d["quality_adjusted_score"] = clamp_meta_score(d.get("quality_adjusted_score"))
    return d
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/source_registry.py
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
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/evidence_collector.py
import pandas as pd
from typing import Optional, Tuple, List, Dict
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore
from meta_research.meta_models import ResearchEvidence, build_evidence_id
from meta_research.meta_config import MetaResearchProfile

class EvidenceCollector:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake
        self.feature_store = FeatureStore(data_lake)

    def collect_symbol_evidence(
        self,
        spec: SymbolSpec,
        timeframe: str,
        profile: MetaResearchProfile,
    ) -> Tuple[List[ResearchEvidence], dict]:
        evidence_list = []
        warnings = []

        def _build_missing(source_label: str) -> ResearchEvidence:
            return ResearchEvidence(
                evidence_id=build_evidence_id(spec.symbol, timeframe, source_label),
                symbol=spec.symbol,
                timeframe=timeframe,
                source_label=source_label,
                evidence_direction="missing_evidence",
                raw_score=None,
                normalized_score=None,
                confidence_score=None,
                quality_score=None,
                uncertainty_score=None,
                source_timestamp=None,
                summary={"status": "missing"},
                warnings=["Source data not found"]
            )

        sources_to_check = []
        if profile.include_technical: sources_to_check.append("technical_evidence")
        if profile.include_strategy: sources_to_check.append("strategy_evidence")
        if profile.include_risk_level: sources_to_check.append("risk_level_evidence")
        if profile.include_backtest: sources_to_check.append("backtest_evidence")
        if profile.include_validation: sources_to_check.append("validation_evidence")
        if profile.include_ml: sources_to_check.append("ml_evidence")
        if profile.include_paper: sources_to_check.append("paper_evidence")
        if profile.include_factor: sources_to_check.append("factor_evidence")
        if profile.include_synthetic_index: sources_to_check.append("synthetic_index_evidence")
        if profile.include_portfolio: sources_to_check.append("portfolio_evidence")
        if profile.include_regime: sources_to_check.append("regime_evidence")

        for source in sources_to_check:
            evidence_list.append(_build_missing(source))
            warnings.append(f"Missing actual data fetch for {source}")

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "collected_count": len(evidence_list),
            "missing_count": len(sources_to_check),
            "warnings": warnings
        }

        return evidence_list, summary

    def collect_universe_evidence(
        self,
        specs: List[SymbolSpec],
        timeframe: str,
        profile: MetaResearchProfile,
        limit: Optional[int] = None,
    ) -> Tuple[Dict[str, List[ResearchEvidence]], dict]:

        evidence_map = {}
        warnings = []
        processed_count = 0

        for spec in specs:
            if limit and processed_count >= limit:
                break

            try:
                ev_list, _ = self.collect_symbol_evidence(spec, timeframe, profile)
                evidence_map[spec.symbol] = ev_list
                processed_count += 1
            except Exception as e:
                warnings.append(f"Failed to collect evidence for {spec.symbol}: {e}")

        summary = {
            "processed_count": processed_count,
            "total_specs": len(specs),
            "timeframe": timeframe,
            "warnings": warnings
        }

        return evidence_map, summary
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/evidence_normalizer.py
from typing import Optional, List
from meta_research.meta_models import ResearchEvidence, clamp_meta_score

def normalize_raw_score(value: Optional[float], source_label: str) -> Optional[float]:
    if value is None:
        return None
    return clamp_meta_score(value)

def infer_evidence_direction(normalized_score: Optional[float], uncertainty_score: Optional[float] = None) -> str:
    if normalized_score is None:
        return "missing_evidence"

    if uncertainty_score is not None and uncertainty_score > 0.8:
        return "uncertain_evidence"

    if normalized_score >= 0.60:
        return "supportive_evidence"
    elif normalized_score <= 0.40:
        return "conflicting_evidence"
    else:
        return "neutral_evidence"

def normalize_confidence_score(value: Optional[float]) -> Optional[float]:
    return clamp_meta_score(value)

def normalize_quality_score(value: Optional[float]) -> Optional[float]:
    return clamp_meta_score(value)

def normalize_uncertainty_score(value: Optional[float]) -> Optional[float]:
    return clamp_meta_score(value)

def normalize_evidence(evidence: ResearchEvidence) -> ResearchEvidence:
    if evidence.raw_score is None and evidence.normalized_score is None:
        evidence.evidence_direction = "missing_evidence"
        return evidence

    if evidence.normalized_score is None:
        evidence.normalized_score = normalize_raw_score(evidence.raw_score, evidence.source_label)

    evidence.normalized_score = clamp_meta_score(evidence.normalized_score)
    evidence.confidence_score = normalize_confidence_score(evidence.confidence_score)
    evidence.quality_score = normalize_quality_score(evidence.quality_score)
    evidence.uncertainty_score = normalize_uncertainty_score(evidence.uncertainty_score)

    evidence.evidence_direction = infer_evidence_direction(
        evidence.normalized_score,
        evidence.uncertainty_score
    )

    return evidence

def normalize_evidence_list(evidence_list: List[ResearchEvidence]) -> List[ResearchEvidence]:
    return [normalize_evidence(e) for e in evidence_list]
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/reliability_scoring.py
import pandas as pd
from typing import List, Dict
from meta_research.meta_models import ResearchEvidence
from meta_research.source_registry import EvidenceSourceDefinition

def calculate_source_reliability(evidence: ResearchEvidence, prior: float = 0.50) -> float:
    if evidence.evidence_direction == "missing_evidence":
        return 0.0

    reliability = prior

    if evidence.quality_score is not None:
        quality_adj = (evidence.quality_score - 0.5) * 0.2
        reliability += quality_adj

    if evidence.confidence_score is not None:
        confidence_adj = (evidence.confidence_score - 0.5) * 0.2
        reliability += confidence_adj

    if evidence.uncertainty_score is not None:
        reliability -= (evidence.uncertainty_score * 0.3)

    if evidence.warnings and len(evidence.warnings) > 0:
        reliability -= 0.1 * min(len(evidence.warnings), 3)

    return max(0.0, min(1.0, reliability))

def calculate_evidence_effective_weight(evidence: ResearchEvidence, source_weight: float, source_reliability: float) -> float:
    if evidence.evidence_direction == "missing_evidence" or evidence.normalized_score is None:
        return 0.0
    return source_weight * source_reliability

def build_source_reliability_table(
    evidence_map: Dict[str, List[ResearchEvidence]],
    sources: List[EvidenceSourceDefinition]
) -> pd.DataFrame:
    rows = []

    source_priors = {s.source_label: s.reliability_prior for s in sources}
    source_weights = {s.source_label: s.default_weight for s in sources}

    for symbol, ev_list in evidence_map.items():
        for ev in ev_list:
            prior = source_priors.get(ev.source_label, 0.50)
            weight = source_weights.get(ev.source_label, 0.0)

            rel = calculate_source_reliability(ev, prior)
            eff_weight = calculate_evidence_effective_weight(ev, weight, rel)

            rows.append({
                "symbol": symbol,
                "timeframe": ev.timeframe,
                "source_label": ev.source_label,
                "prior_reliability": prior,
                "calculated_reliability": rel,
                "base_weight": weight,
                "effective_weight": eff_weight,
                "missing": ev.evidence_direction == "missing_evidence"
            })

    if not rows:
        return pd.DataFrame()

    return pd.DataFrame(rows)

def summarize_source_reliability(reliability_df: pd.DataFrame) -> dict:
    if reliability_df.empty:
        return {"avg_reliability": 0.0, "sources": 0}

    avg_rel = reliability_df["calculated_reliability"].mean()
    zero_rel = (reliability_df["calculated_reliability"] == 0.0).sum()

    return {
        "avg_reliability": float(avg_rel),
        "zero_reliability_count": int(zero_rel),
        "total_evidence_rows": len(reliability_df)
    }
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/consensus_engine.py
import pandas as pd
from typing import List, Dict
from meta_research.meta_models import ResearchEvidence, ConsensusResult, clamp_meta_score
from meta_research.meta_config import MetaResearchProfile
from meta_research.source_registry import EvidenceSourceDefinition
from meta_research.reliability_scoring import calculate_source_reliability, calculate_evidence_effective_weight

def calculate_weighted_consensus_score(
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition]
) -> dict:

    source_priors = {s.source_label: s.reliability_prior for s in sources}
    source_weights = {s.source_label: s.default_weight for s in sources}

    total_effective_weight = 0.0
    weighted_score_sum = 0.0

    supportive = 0
    conflicting = 0
    neutral = 0
    missing = 0

    for ev in evidence_list:
        if ev.evidence_direction == "missing_evidence" or ev.normalized_score is None:
            missing += 1
            continue

        prior = source_priors.get(ev.source_label, 0.50)
        weight = source_weights.get(ev.source_label, 0.0)

        rel = calculate_source_reliability(ev, prior)
        eff_weight = calculate_evidence_effective_weight(ev, weight, rel)

        total_effective_weight += eff_weight
        weighted_score_sum += (ev.normalized_score * eff_weight)

        if ev.evidence_direction == "supportive_evidence":
            supportive += 1
        elif ev.evidence_direction == "conflicting_evidence":
            conflicting += 1
        else:
            neutral += 1

    if total_effective_weight > 0:
        consensus_score = weighted_score_sum / total_effective_weight
    else:
        consensus_score = None

    return {
        "consensus_score": clamp_meta_score(consensus_score),
        "total_effective_weight": total_effective_weight,
        "supportive_count": supportive,
        "conflicting_count": conflicting,
        "neutral_count": neutral,
        "missing_count": missing,
        "available_source_count": supportive + conflicting + neutral
    }

def infer_consensus_label(
    consensus_score: float | None,
    conflict_score: float | None,
    available_source_count: int,
    profile: MetaResearchProfile
) -> str:

    if consensus_score is None or available_source_count < profile.min_sources:
        return "insufficient_consensus_data"

    if conflict_score is not None and conflict_score > profile.conflict_threshold:
        return "mixed_consensus"

    if consensus_score >= profile.high_agreement_threshold:
        return "strong_positive_consensus"
    elif consensus_score >= 0.60:
        return "moderate_positive_consensus"
    elif consensus_score <= (1.0 - profile.high_agreement_threshold):
        return "strong_negative_consensus"
    elif consensus_score <= 0.40:
        return "moderate_negative_consensus"
    else:
        return "neutral_consensus"

def infer_confidence_label(confidence_score: float | None) -> str:
    if confidence_score is None:
        return "unknown_confidence"
    if confidence_score >= 0.70:
        return "high_confidence_research"
    elif confidence_score >= 0.40:
        return "medium_confidence_research"
    elif confidence_score >= 0.20:
        return "low_confidence_research"
    else:
        return "unreliable_research"

def build_consensus_result(
    symbol: str,
    timeframe: str,
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> ConsensusResult:

    metrics = calculate_weighted_consensus_score(evidence_list, sources)

    conf_scores = [e.confidence_score for e in evidence_list if e.confidence_score is not None]
    agg_conf = sum(conf_scores) / len(conf_scores) if conf_scores else None

    unc_scores = [e.uncertainty_score for e in evidence_list if e.uncertainty_score is not None]
    agg_unc = sum(unc_scores) / len(unc_scores) if unc_scores else None

    total_active = metrics["supportive_count"] + metrics["conflicting_count"]
    if total_active > 0:
        minority = min(metrics["supportive_count"], metrics["conflicting_count"])
        conflict_score = minority / total_active
    else:
        conflict_score = 0.0

    cons_label = infer_consensus_label(
        metrics["consensus_score"],
        conflict_score,
        metrics["available_source_count"],
        profile
    )

    conf_label = infer_confidence_label(agg_conf)

    warnings = []
    if metrics["available_source_count"] < profile.min_sources:
        warnings.append(f"Available sources ({metrics['available_source_count']}) below minimum ({profile.min_sources})")

    return ConsensusResult(
        symbol=symbol,
        timeframe=timeframe,
        evidence_count=len(evidence_list),
        available_source_count=metrics["available_source_count"],
        consensus_score=metrics["consensus_score"],
        confidence_score=clamp_meta_score(agg_conf),
        uncertainty_score=clamp_meta_score(agg_unc),
        conflict_score=clamp_meta_score(conflict_score),
        consensus_label=cons_label,
        confidence_label=conf_label,
        supportive_count=metrics["supportive_count"],
        conflicting_count=metrics["conflicting_count"],
        neutral_count=metrics["neutral_count"],
        missing_count=metrics["missing_count"],
        warnings=warnings
    )

def build_consensus_table(
    evidence_map: Dict[str, List[ResearchEvidence]],
    timeframe: str,
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> pd.DataFrame:

    rows = []
    for symbol, ev_list in evidence_map.items():
        res = build_consensus_result(symbol, timeframe, ev_list, sources, profile)
        rows.append({
            "symbol": res.symbol,
            "timeframe": res.timeframe,
            "consensus_score": res.consensus_score,
            "confidence_score": res.confidence_score,
            "conflict_score": res.conflict_score,
            "consensus_label": res.consensus_label,
            "confidence_label": res.confidence_label,
            "available_sources": res.available_source_count,
            "supportive": res.supportive_count,
            "conflicting": res.conflicting_count,
            "warning_count": len(res.warnings)
        })

    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/conflict_detection.py
import pandas as pd
from typing import List, Dict, Tuple
from meta_research.meta_models import ResearchEvidence
from meta_research.meta_config import MetaResearchProfile

def calculate_pairwise_evidence_disagreement(evidence_list: List[ResearchEvidence]) -> pd.DataFrame:
    rows = []
    valid_ev = [e for e in evidence_list if e.normalized_score is not None]

    for i, e1 in enumerate(valid_ev):
        for j, e2 in enumerate(valid_ev):
            if i < j:
                diff = abs(e1.normalized_score - e2.normalized_score)
                rows.append({
                    "source_1": e1.source_label,
                    "score_1": e1.normalized_score,
                    "source_2": e2.source_label,
                    "score_2": e2.normalized_score,
                    "disagreement": diff
                })

    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)

def calculate_conflict_score(evidence_list: List[ResearchEvidence]) -> float:
    df = calculate_pairwise_evidence_disagreement(evidence_list)
    if df.empty:
        return 0.0
    avg_diff = df["disagreement"].mean()
    return float(min(1.0, avg_diff * 1.5))

def identify_major_conflicts(evidence_list: List[ResearchEvidence], threshold: float = 0.35) -> List[dict]:
    df = calculate_pairwise_evidence_disagreement(evidence_list)
    conflicts = []
    if df.empty:
        return conflicts

    major = df[df["disagreement"] > threshold]
    for _, row in major.iterrows():
        conflicts.append({
            "source_1": row["source_1"],
            "source_2": row["source_2"],
            "disagreement": float(row["disagreement"])
        })
    return conflicts

def build_agreement_matrix(evidence_map: Dict[str, List[ResearchEvidence]]) -> pd.DataFrame:
    all_rows = []
    for symbol, ev_list in evidence_map.items():
        df = calculate_pairwise_evidence_disagreement(ev_list)
        if not df.empty:
            df["symbol"] = symbol
            all_rows.append(df)

    if not all_rows:
        return pd.DataFrame()

    combined = pd.concat(all_rows, ignore_index=True)
    matrix = combined.groupby(["source_1", "source_2"])["disagreement"].mean().reset_index()
    pivot = matrix.pivot(index="source_1", columns="source_2", values="disagreement")
    return pivot

def build_conflict_detection_report(
    evidence_map: Dict[str, List[ResearchEvidence]],
    profile: MetaResearchProfile
) -> Tuple[pd.DataFrame, dict]:

    rows = []
    total_conflicts = 0

    for symbol, ev_list in evidence_map.items():
        score = calculate_conflict_score(ev_list)
        major = identify_major_conflicts(ev_list, profile.conflict_threshold)

        total_conflicts += len(major)

        rows.append({
            "symbol": symbol,
            "conflict_score": score,
            "major_conflict_count": len(major),
            "has_critical_conflict": score > profile.conflict_threshold,
            "conflict_details": str([f"{c['source_1']} vs {c['source_2']}" for c in major]) if major else ""
        })

    df = pd.DataFrame(rows) if rows else pd.DataFrame()

    summary = {
        "symbols_analyzed": len(evidence_map),
        "total_major_conflicts": total_conflicts,
        "avg_conflict_score": float(df["conflict_score"].mean()) if not df.empty else 0.0
    }

    return df, summary
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/uncertainty_aggregation.py
import pandas as pd
from typing import List, Dict
from meta_research.meta_models import ResearchEvidence, clamp_meta_score

def calculate_evidence_uncertainty(evidence: ResearchEvidence) -> float:
    base_unc = evidence.uncertainty_score if evidence.uncertainty_score is not None else 0.5

    if evidence.quality_score is not None and evidence.quality_score < 0.4:
        base_unc += 0.2

    if evidence.evidence_direction == "missing_evidence":
        base_unc = 1.0

    return clamp_meta_score(base_unc)

def calculate_aggregate_uncertainty(evidence_list: List[ResearchEvidence]) -> float:
    if not evidence_list:
        return 1.0

    unc_scores = [calculate_evidence_uncertainty(e) for e in evidence_list]
    avg_unc = sum(unc_scores) / len(unc_scores)

    missing = sum(1 for e in evidence_list if e.evidence_direction == "missing_evidence")
    missing_ratio = missing / len(evidence_list)

    final_unc = avg_unc + (missing_ratio * 0.5)

    return clamp_meta_score(final_unc)

def apply_uncertainty_penalty(score: float | None, uncertainty: float | None, enabled: bool = True) -> float | None:
    if score is None:
        return None
    if not enabled or uncertainty is None or uncertainty <= 0.2:
        return score

    dist_to_neutral = score - 0.5
    penalty_factor = 1.0 - (uncertainty * 0.5)

    adjusted = 0.5 + (dist_to_neutral * penalty_factor)
    return clamp_meta_score(adjusted)

def build_uncertainty_penalty_table(evidence_map: Dict[str, List[ResearchEvidence]]) -> pd.DataFrame:
    rows = []
    for symbol, ev_list in evidence_map.items():
        unc = calculate_aggregate_uncertainty(ev_list)
        missing_count = sum(1 for e in ev_list if e.evidence_direction == "missing_evidence")

        rows.append({
            "symbol": symbol,
            "aggregate_uncertainty": unc,
            "missing_source_count": missing_count,
            "high_uncertainty": unc > 0.6
        })

    return pd.DataFrame(rows) if rows else pd.DataFrame()

def summarize_uncertainty(uncertainty_df: pd.DataFrame) -> dict:
    if uncertainty_df.empty:
        return {"avg_uncertainty": 0.0, "high_uncertainty_symbols": 0}

    return {
        "avg_uncertainty": float(uncertainty_df["aggregate_uncertainty"].mean()),
        "high_uncertainty_symbols": int(uncertainty_df["high_uncertainty"].sum())
    }
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/ensemble_scoring.py
import pandas as pd
from typing import List, Dict
from meta_research.meta_models import ResearchEvidence, clamp_meta_score
from meta_research.meta_config import MetaResearchProfile
from meta_research.source_registry import EvidenceSourceDefinition
from meta_research.consensus_engine import calculate_weighted_consensus_score

def calculate_model_factor_strategy_ensemble(
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> dict:

    scores = {
        "technical_score": None,
        "strategy_score": None,
        "risk_level_score": None,
        "backtest_score": None,
        "validation_score": None,
        "ml_score": None,
        "paper_score": None,
        "factor_score": None,
        "synthetic_index_score": None,
        "portfolio_score": None,
        "regime_score": None,
        "quality_score": None
    }

    for ev in evidence_list:
        if ev.normalized_score is not None:
            key = ev.source_label.replace("_evidence", "_score")
            if key in scores:
                scores[key] = ev.normalized_score

    metrics = calculate_weighted_consensus_score(evidence_list, sources)

    scores["ensemble_score"] = metrics["consensus_score"]
    return scores

def build_ensemble_score_table(
    evidence_map: Dict[str, List[ResearchEvidence]],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> pd.DataFrame:

    rows = []
    for symbol, ev_list in evidence_map.items():
        res = calculate_model_factor_strategy_ensemble(ev_list, sources, profile)
        res["symbol"] = symbol
        rows.append(res)

    return pd.DataFrame(rows) if rows else pd.DataFrame()

def summarize_ensemble_scores(ensemble_df: pd.DataFrame) -> dict:
    if ensemble_df.empty:
        return {"avg_ensemble_score": 0.0, "high_ensemble_count": 0}

    high_count = (ensemble_df["ensemble_score"] > 0.7).sum() if "ensemble_score" in ensemble_df else 0

    return {
        "avg_ensemble_score": float(ensemble_df["ensemble_score"].mean()) if "ensemble_score" in ensemble_df else 0.0,
        "high_ensemble_count": int(high_count)
    }
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/quality_adjustment.py
import pandas as pd
from typing import List, Dict
from meta_research.meta_models import ResearchEvidence, clamp_meta_score
from meta_research.meta_config import MetaResearchProfile
from meta_research.source_registry import EvidenceSourceDefinition
from meta_research.uncertainty_aggregation import calculate_aggregate_uncertainty, apply_uncertainty_penalty

def calculate_quality_penalty(evidence_list: List[ResearchEvidence]) -> float:
    if not evidence_list:
        return 0.5

    qual_scores = [e.quality_score for e in evidence_list if e.quality_score is not None]
    if not qual_scores:
        return 0.3

    avg_qual = sum(qual_scores) / len(qual_scores)
    if avg_qual < 0.6:
        return (0.6 - avg_qual) * 0.8
    return 0.0

def calculate_missing_source_penalty(
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> float:
    missing = sum(1 for e in evidence_list if e.evidence_direction == "missing_evidence")
    expected = sum(1 for s in sources if s.enabled)

    if expected == 0:
        return 0.0

    missing_ratio = missing / expected
    return min(0.4, missing_ratio * 0.5)

def apply_quality_adjustments(
    ensemble_score: float | None,
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> dict:

    if ensemble_score is None:
        return {
            "base_score": None,
            "uncertainty_penalty": 0.0,
            "quality_penalty": 0.0,
            "missing_source_penalty": 0.0,
            "conflict_penalty": 0.0,
            "quality_adjusted_score": None
        }

    unc = calculate_aggregate_uncertainty(evidence_list)

    adj_score_unc = apply_uncertainty_penalty(
        ensemble_score, unc, profile.uncertainty_penalty_enabled
    )
    if adj_score_unc is None:
        adj_score_unc = ensemble_score
    unc_penalty = abs(ensemble_score - adj_score_unc)

    qual_penalty = 0.0
    if profile.quality_penalty_enabled:
        qual_penalty = calculate_quality_penalty(evidence_list)

    missing_penalty = 0.0
    if profile.missing_source_penalty_enabled:
        missing_penalty = calculate_missing_source_penalty(evidence_list, sources, profile)

    current_dist = adj_score_unc - 0.5
    total_penalty_ratio = min(1.0, qual_penalty + missing_penalty)

    final_dist = current_dist * (1.0 - total_penalty_ratio)
    quality_adjusted_score = clamp_meta_score(0.5 + final_dist)

    return {
        "base_score": ensemble_score,
        "uncertainty_penalty": unc_penalty,
        "quality_penalty": qual_penalty,
        "missing_source_penalty": missing_penalty,
        "conflict_penalty": 0.0,
        "quality_adjusted_score": quality_adjusted_score
    }

def build_quality_adjustment_table(
    evidence_map: Dict[str, List[ResearchEvidence]],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> pd.DataFrame:
    from meta_research.consensus_engine import calculate_weighted_consensus_score

    rows = []
    for symbol, ev_list in evidence_map.items():
        metrics = calculate_weighted_consensus_score(ev_list, sources)
        adj = apply_quality_adjustments(metrics["consensus_score"], ev_list, sources, profile)
        adj["symbol"] = symbol
        rows.append(adj)

    return pd.DataFrame(rows) if rows else pd.DataFrame()
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/meta_ranking.py
import pandas as pd
from typing import Dict

def build_quality_adjusted_ranking(
    consensus_df: pd.DataFrame,
    ensemble_df: pd.DataFrame,
    adjustment_df: pd.DataFrame
) -> pd.DataFrame:

    if consensus_df.empty or ensemble_df.empty or adjustment_df.empty:
        return pd.DataFrame()

    merged = pd.merge(
        consensus_df,
        ensemble_df[["symbol", "ensemble_score"]],
        on="symbol",
        how="left"
    )

    merged = pd.merge(
        merged,
        adjustment_df[["symbol", "quality_adjusted_score"]],
        on="symbol",
        how="left"
    )

    merged = merged.sort_values(by="quality_adjusted_score", ascending=False).reset_index(drop=True)
    merged["rank"] = merged.index + 1

    merged = assign_meta_rank_labels(merged)

    if "asset_class" not in merged:
        merged["asset_class"] = "unknown"
    if "uncertainty_score" not in merged:
        merged["uncertainty_score"] = 0.5
    if "missing_source_count" not in merged:
        merged["missing_source_count"] = 0

    return merged

def assign_meta_rank_labels(ranking_df: pd.DataFrame) -> pd.DataFrame:
    if "quality_adjusted_score" not in ranking_df:
        return ranking_df

    def _label(score):
        if pd.isna(score):
            return "insufficient_data_alignment"
        if score >= 0.70:
            return "high_research_alignment"
        elif score >= 0.60:
            return "moderate_research_alignment"
        elif score <= 0.30:
            return "weak_research_alignment"
        elif score <= 0.40:
            return "mixed_research_alignment"
        else:
            return "neutral_research_alignment"

    ranking_df["meta_rank_label"] = ranking_df["quality_adjusted_score"].apply(_label)
    return ranking_df

def summarize_meta_ranking(ranking_df: pd.DataFrame) -> dict:
    if ranking_df.empty:
        return {"ranked_symbols": 0, "high_alignment_count": 0, "weak_alignment_count": 0}

    high_alignment = (ranking_df["meta_rank_label"] == "high_research_alignment").sum()
    weak_alignment = (ranking_df["meta_rank_label"] == "weak_research_alignment").sum()

    return {
        "ranked_symbols": len(ranking_df),
        "high_alignment_count": int(high_alignment),
        "weak_alignment_count": int(weak_alignment)
    }
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/meta_snapshot.py
import pandas as pd
from typing import List
from config.symbols import SymbolSpec
from meta_research.meta_models import ResearchEvidence, ConsensusResult, MetaResearchSnapshot, clamp_meta_score

def build_meta_research_snapshot(
    spec: SymbolSpec,
    timeframe: str,
    evidence_list: List[ResearchEvidence],
    consensus: ConsensusResult,
    ensemble_score: float | None,
    quality_adjusted_score: float | None
) -> MetaResearchSnapshot:

    if quality_adjusted_score is None:
        final_label = "unknown"
    elif quality_adjusted_score >= 0.70:
        final_label = "high_research_alignment"
    elif quality_adjusted_score >= 0.60:
        final_label = "moderate_research_alignment"
    elif quality_adjusted_score <= 0.30:
        final_label = "weak_research_alignment"
    elif quality_adjusted_score <= 0.40:
        final_label = "mixed_research_alignment"
    else:
        final_label = "neutral_research_alignment"

    return MetaResearchSnapshot(
        symbol=spec.symbol,
        timeframe=timeframe,
        asset_class=spec.asset_class,
        consensus=consensus,
        evidence=evidence_list,
        ensemble_score=clamp_meta_score(ensemble_score),
        quality_adjusted_score=clamp_meta_score(quality_adjusted_score),
        final_research_label=final_label,
        warnings=consensus.warnings.copy()
    )

def build_symbol_snapshot_table(snapshots: List[MetaResearchSnapshot]) -> pd.DataFrame:
    rows = []
    for s in snapshots:
        rows.append({
            "symbol": s.symbol,
            "timeframe": s.timeframe,
            "asset_class": s.asset_class,
            "consensus_score": s.consensus.consensus_score,
            "ensemble_score": s.ensemble_score,
            "quality_adjusted_score": s.quality_adjusted_score,
            "final_research_label": s.final_research_label
        })
    return pd.DataFrame(rows) if rows else pd.DataFrame()

def summarize_symbol_snapshot(snapshot: MetaResearchSnapshot) -> dict:
    return {
        "symbol": snapshot.symbol,
        "timeframe": snapshot.timeframe,
        "evidence_count": snapshot.consensus.evidence_count,
        "available_sources": snapshot.consensus.available_source_count,
        "final_label": snapshot.final_research_label
    }

def build_snapshot_narrative(snapshot: MetaResearchSnapshot) -> str:
    supportive = [e.source_label for e in snapshot.evidence if e.evidence_direction == "supportive_evidence"]
    conflicting = [e.source_label for e in snapshot.evidence if e.evidence_direction == "conflicting_evidence"]
    missing = [e.source_label for e in snapshot.evidence if e.evidence_direction == "missing_evidence"]

    lines = []
    lines.append(f"Meta Research Snapshot for {snapshot.symbol} ({snapshot.timeframe})")
    lines.append("-" * 50)
    lines.append(f"Consensus Score: {snapshot.consensus.consensus_score}")
    lines.append(f"Quality Adjusted Score: {snapshot.quality_adjusted_score}")
    lines.append(f"Research Alignment: {snapshot.final_research_label}")
    lines.append(f"Total Evaluated Sources: {snapshot.consensus.available_source_count}")
    lines.append("")
    lines.append("Key Supportive Sources:")
    lines.append(", ".join(supportive) if supportive else "None")
    lines.append("")
    lines.append("Key Conflicting Sources:")
    lines.append(", ".join(conflicting) if conflicting else "None")
    lines.append("")
    lines.append("Missing Sources:")
    lines.append(", ".join(missing) if missing else "None")
    lines.append("")
    if snapshot.warnings:
        lines.append("Warnings:")
        for w in snapshot.warnings:
            lines.append(f"- {w}")
    lines.append("")
    lines.append("DISCLAIMER: This narrative is a summary of offline meta-research. "
                 "It is not a live trading signal, order instruction, or investment advice.")

    return "\n".join(lines)
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/meta_quality.py
import pandas as pd
from typing import Optional
from meta_research.meta_config import MetaResearchProfile

FORBIDDEN_TERMS = [
    "AL ", " SAT ", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT",
    "GERÇEK EMİR", "BROKER ORDER", "LIVE ORDER", "LIVE_ORDER"
]

def check_for_forbidden_trade_terms_in_meta_research(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[dict] = None
) -> dict:

    found_terms = set()

    def _check_string(s: str):
        if not isinstance(s, str):
            return
        s_upper = s.upper()
        for term in FORBIDDEN_TERMS:
            if term in s_upper:
                found_terms.add(term)

    if text:
        _check_string(text)

    if summary:
        _check_string(str(summary))

    if df is not None and not df.empty:
        for col in df.columns:
            _check_string(str(col))
        for col in df.select_dtypes(include=['object', 'string']).columns:
            for val in df[col].dropna():
                _check_string(str(val))

    return {
        "passed": len(found_terms) == 0,
        "found_terms": list(found_terms)
    }

def check_evidence_table_quality(evidence_df: pd.DataFrame, profile: MetaResearchProfile) -> dict:
    if evidence_df.empty:
        return {"passed": False, "warnings": ["Evidence table is empty"]}

    warnings = []
    if "evidence_direction" not in evidence_df.columns:
        warnings.append("Missing 'evidence_direction' column")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_consensus_table_quality(consensus_df: pd.DataFrame) -> dict:
    if consensus_df.empty:
        return {"passed": False, "warnings": ["Consensus table is empty"]}
    return {"passed": True, "warnings": []}

def check_ensemble_table_quality(ensemble_df: pd.DataFrame) -> dict:
    if ensemble_df.empty:
        return {"passed": False, "warnings": ["Ensemble table is empty"]}
    return {"passed": True, "warnings": []}

def check_conflict_report_quality(conflict_df: Optional[pd.DataFrame] = None) -> dict:
    if conflict_df is None or conflict_df.empty:
        return {"passed": False, "warnings": ["Conflict table is empty"]}
    return {"passed": True, "warnings": []}

def check_meta_ranking_quality(ranking_df: pd.DataFrame) -> dict:
    if ranking_df.empty:
        return {"passed": False, "warnings": ["Ranking table is empty"]}
    return {"passed": True, "warnings": []}

def build_meta_quality_report(
    summary: dict,
    evidence_df: Optional[pd.DataFrame] = None,
    consensus_df: Optional[pd.DataFrame] = None,
    ranking_df: Optional[pd.DataFrame] = None
) -> dict:

    term_check = check_for_forbidden_trade_terms_in_meta_research(
        text=str(summary), df=evidence_df
    )
    if consensus_df is not None:
        c_check = check_for_forbidden_trade_terms_in_meta_research(df=consensus_df)
        term_check["found_terms"].extend(c_check["found_terms"])

    if ranking_df is not None:
        r_check = check_for_forbidden_trade_terms_in_meta_research(df=ranking_df)
        term_check["found_terms"].extend(r_check["found_terms"])

    unique_terms = list(set(term_check["found_terms"]))

    return {
        "evidence_valid": evidence_df is not None and not evidence_df.empty,
        "consensus_valid": consensus_df is not None and not consensus_df.empty,
        "ranking_valid": ranking_df is not None and not ranking_df.empty,
        "disclaimer_required": True,
        "forbidden_trade_terms_found": len(unique_terms) > 0,
        "found_terms": unique_terms,
        "passed": len(unique_terms) == 0,
        "warnings": [f"Forbidden term found: {t}" for t in unique_terms]
    }
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/meta_report_builder.py
import pandas as pd
from typing import Dict
from meta_research.meta_config import MetaResearchProfile
from meta_research.meta_models import MetaResearchSnapshot
from meta_research.meta_snapshot import build_snapshot_narrative

def build_meta_disclaimer() -> str:
    return (
        "*** DISCLAIMER ***\n"
        "Bu çıktı offline meta-research/kanıt ağırlıklandırma raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, otomatik trade onayı veya "
        "yatırım tavsiyesi değildir. Yalnızca offline araştırma kanıtlarını birleştirir."
    )

def _build_generic_markdown(title: str, summary: dict, df: pd.DataFrame | None, profile: MetaResearchProfile) -> str:
    lines = [
        f"# {title}",
        "",
        "## Configuration",
        f"- Profile: {profile.name}",
        f"- Timeframe: {summary.get('timeframe', 'Unknown')}",
        ""
    ]

    lines.append("## Summary")
    for k, v in summary.items():
        if k != "timeframe":
            lines.append(f"- {k}: {v}")
    lines.append("")

    if df is not None and not df.empty:
        lines.append("## Data Table")
        if len(df) > 50:
            lines.append("*(Showing top 50 rows)*")
            lines.append(df.head(50).to_markdown(index=False))
        else:
            lines.append(df.to_markdown(index=False))
        lines.append("")

    lines.append(build_meta_disclaimer())
    return "\n".join(lines)

def build_meta_research_markdown_report(summary: dict, tables: Dict[str, pd.DataFrame], profile: MetaResearchProfile) -> str:
    df = tables.get("consensus", None)
    return _build_generic_markdown("Meta Research Report", summary, df, profile)

def build_meta_consensus_markdown_report(summary: dict, consensus_df: pd.DataFrame, profile: MetaResearchProfile) -> str:
    return _build_generic_markdown("Meta Consensus Report", summary, consensus_df, profile)

def build_evidence_conflict_markdown_report(summary: dict, conflict_df: pd.DataFrame, profile: MetaResearchProfile) -> str:
    return _build_generic_markdown("Evidence Conflict Report", summary, conflict_df, profile)

def build_quality_adjusted_ranking_markdown_report(summary: dict, ranking_df: pd.DataFrame, profile: MetaResearchProfile) -> str:
    return _build_generic_markdown("Quality Adjusted Ranking Report", summary, ranking_df, profile)

def build_meta_symbol_snapshot_markdown(snapshot: MetaResearchSnapshot, profile: MetaResearchProfile) -> str:
    narrative = build_snapshot_narrative(snapshot)

    lines = [
        f"# Meta Research Snapshot: {snapshot.symbol}",
        f"**Timeframe**: {snapshot.timeframe}",
        f"**Profile**: {profile.name}",
        "",
        "## Narrative Summary",
        narrative,
        "",
        build_meta_disclaimer()
    ]
    return "\n".join(lines)
INNER_EOF

cat << 'INNER_EOF' > commodity_fx_signal_bot/meta_research/meta_pipeline.py
import pandas as pd
from typing import List, Tuple, Dict, Optional
from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from meta_research.meta_config import MetaResearchProfile, get_default_meta_research_profile
from meta_research.meta_models import MetaResearchSnapshot
from meta_research.source_registry import build_default_evidence_sources
from meta_research.evidence_collector import EvidenceCollector
from meta_research.evidence_normalizer import normalize_evidence_list
from meta_research.reliability_scoring import build_source_reliability_table
from meta_research.consensus_engine import build_consensus_table, build_consensus_result
from meta_research.conflict_detection import build_conflict_detection_report
from meta_research.uncertainty_aggregation import build_uncertainty_penalty_table
from meta_research.ensemble_scoring import build_ensemble_score_table
from meta_research.quality_adjustment import build_quality_adjustment_table, apply_quality_adjustments
from meta_research.meta_ranking import build_quality_adjusted_ranking
from meta_research.meta_snapshot import build_meta_research_snapshot
from meta_research.meta_quality import build_meta_quality_report
from meta_research.meta_report_builder import build_meta_research_markdown_report
import traceback

class MetaResearchPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[MetaResearchProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_meta_research_profile()
        self.collector = EvidenceCollector(self.data_lake)
        self.sources = build_default_evidence_sources(self.profile)

    def build_meta_research_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[MetaResearchProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[Dict, Dict]:

        prof = profile or self.profile

        evidence_map, collect_sum = self.collector.collect_universe_evidence(specs, timeframe, prof, limit)

        normalized_map = {}
        for sym, ev_list in evidence_map.items():
            normalized_map[sym] = normalize_evidence_list(ev_list)

        reliability_df = build_source_reliability_table(normalized_map, self.sources)
        consensus_df = build_consensus_table(normalized_map, timeframe, self.sources, prof)
        conflict_df, conflict_sum = build_conflict_detection_report(normalized_map, prof)
        uncertainty_df = build_uncertainty_penalty_table(normalized_map)
        ensemble_df = build_ensemble_score_table(normalized_map, self.sources, prof)
        adjustment_df = build_quality_adjustment_table(normalized_map, self.sources, prof)

        ranking_df = build_quality_adjusted_ranking(consensus_df, ensemble_df, adjustment_df)

        quality = build_meta_quality_report(
            summary={"timeframe": timeframe, "symbols": len(specs)},
            evidence_df=reliability_df,
            consensus_df=consensus_df,
            ranking_df=ranking_df
        )

        summary = {
            "timeframe": timeframe,
            "processed_symbols": len(normalized_map),
            "sources_checked": len(self.sources),
            "conflicts": conflict_sum.get("total_major_conflicts", 0),
            "quality_passed": quality["passed"]
        }

        if save:
            try:
                if hasattr(self.data_lake, "save_meta_consensus_table"):
                    self.data_lake.save_meta_consensus_table(timeframe, prof.name, consensus_df)
                    self.data_lake.save_meta_conflict_report(timeframe, prof.name, conflict_df)
                    self.data_lake.save_meta_quality_adjusted_ranking(timeframe, prof.name, ranking_df)

                    report_md = build_meta_research_markdown_report(summary, {"consensus": consensus_df}, prof)
                    self.data_lake.save_meta_research_report(timeframe, prof.name, summary, report_md)
            except Exception as e:
                print(f"Warning: Failed to save meta research outputs: {e}")

        return summary, {"consensus": consensus_df, "ranking": ranking_df, "quality": quality}

    def build_meta_consensus_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[MetaResearchProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:

        prof = profile or self.profile
        evidence_map, _ = self.collector.collect_universe_evidence(specs, timeframe, prof, limit)
        for sym, ev_list in evidence_map.items():
            evidence_map[sym] = normalize_evidence_list(ev_list)

        df = build_consensus_table(evidence_map, timeframe, self.sources, prof)
        summary = {"timeframe": timeframe, "symbols": len(df)}

        if save and hasattr(self.data_lake, "save_meta_consensus_table"):
            self.data_lake.save_meta_consensus_table(timeframe, prof.name, df)

        return df, summary

    def build_evidence_conflict_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[MetaResearchProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:

        prof = profile or self.profile
        evidence_map, _ = self.collector.collect_universe_evidence(specs, timeframe, prof, limit)
        for sym, ev_list in evidence_map.items():
            evidence_map[sym] = normalize_evidence_list(ev_list)

        df, summary = build_conflict_detection_report(evidence_map, prof)
        summary["timeframe"] = timeframe

        if save and hasattr(self.data_lake, "save_meta_conflict_report"):
            self.data_lake.save_meta_conflict_report(timeframe, prof.name, df)

        return df, summary

    def build_quality_adjusted_ranking_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[MetaResearchProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:

        prof = profile or self.profile
        _, tables = self.build_meta_research_report(specs, timeframe, prof, limit, save=False)
        df = tables.get("ranking", pd.DataFrame())
        summary = {"timeframe": timeframe, "ranked_symbols": len(df)}

        if save and hasattr(self.data_lake, "save_meta_quality_adjusted_ranking"):
            self.data_lake.save_meta_quality_adjusted_ranking(timeframe, prof.name, df)

        return df, summary

    def build_symbol_snapshot(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: Optional[MetaResearchProfile] = None,
        save: bool = True,
    ) -> Tuple[MetaResearchSnapshot, Dict]:

        prof = profile or self.profile
        ev_list, _ = self.collector.collect_symbol_evidence(spec, timeframe, prof)
        ev_list = normalize_evidence_list(ev_list)

        consensus = build_consensus_result(spec.symbol, timeframe, ev_list, self.sources, prof)

        adj = apply_quality_adjustments(consensus.consensus_score, ev_list, self.sources, prof)

        snapshot = build_meta_research_snapshot(
            spec, timeframe, ev_list, consensus,
            ensemble_score=consensus.consensus_score,
            quality_adjusted_score=adj["quality_adjusted_score"]
        )

        summary = {"timeframe": timeframe, "symbol": spec.symbol}

        if save and hasattr(self.data_lake, "save_meta_symbol_snapshot"):
            from meta_research.meta_models import meta_research_snapshot_to_dict
            self.data_lake.save_meta_symbol_snapshot(spec.symbol, timeframe, prof.name, meta_research_snapshot_to_dict(snapshot))

        return snapshot, summary
INNER_EOF
