from typing import Dict, List, Optional, Tuple

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from meta_research.meta_config import MetaResearchProfile
from meta_research.meta_models import ResearchEvidence, build_evidence_id
from ml.feature_store import FeatureStore


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
