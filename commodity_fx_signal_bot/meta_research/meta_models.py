from dataclasses import asdict, dataclass


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
