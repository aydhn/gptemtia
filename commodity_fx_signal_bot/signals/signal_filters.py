from signals.signal_candidate import SignalCandidate


def filter_candidates_by_score(
    candidates: list[SignalCandidate], min_score: float
) -> list[SignalCandidate]:
    return [c for c in candidates if c.candidate_score >= min_score]


def filter_candidates_by_quality(
    candidates: list[SignalCandidate], min_quality: float
) -> list[SignalCandidate]:
    return [c for c in candidates if c.quality_score >= min_quality]


def filter_candidates_by_conflict(
    candidates: list[SignalCandidate], max_conflict: float
) -> list[SignalCandidate]:
    return [c for c in candidates if c.conflict_score <= max_conflict]


def filter_candidates_by_direction(
    candidates: list[SignalCandidate], directional_bias: str
) -> list[SignalCandidate]:
    return [c for c in candidates if c.directional_bias == directional_bias]


def filter_recent_candidates(
    candidates: list[SignalCandidate], max_age_bars: int = 5
) -> list[SignalCandidate]:
    # A real implementation would compare candidate timestamps to the current run timestamp
    # For now we'll just return all or a sliced tail
    return candidates[-max_age_bars:] if len(candidates) > max_age_bars else candidates


def rank_candidates(
    candidates: list[SignalCandidate], top_n: int | None = None
) -> list[SignalCandidate]:
    ranked = sorted(candidates, key=lambda c: c.candidate_score, reverse=True)
    if top_n is not None:
        return ranked[:top_n]
    return ranked
