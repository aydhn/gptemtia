from typing import List, Optional

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
