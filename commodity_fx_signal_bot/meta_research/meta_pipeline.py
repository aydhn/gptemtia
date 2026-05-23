from typing import Dict, List, Optional, Tuple

import pandas as pd

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from meta_research.conflict_detection import build_conflict_detection_report
from meta_research.consensus_engine import build_consensus_result, build_consensus_table
from meta_research.ensemble_scoring import build_ensemble_score_table
from meta_research.evidence_collector import EvidenceCollector
from meta_research.evidence_normalizer import normalize_evidence_list
from meta_research.meta_config import MetaResearchProfile, get_default_meta_research_profile
from meta_research.meta_models import MetaResearchSnapshot
from meta_research.meta_quality import build_meta_quality_report
from meta_research.meta_ranking import build_quality_adjusted_ranking
from meta_research.meta_report_builder import build_meta_research_markdown_report
from meta_research.meta_snapshot import build_meta_research_snapshot
from meta_research.quality_adjustment import (
    apply_quality_adjustments,
    build_quality_adjustment_table,
)
from meta_research.reliability_scoring import build_source_reliability_table
from meta_research.source_registry import build_default_evidence_sources
from meta_research.uncertainty_aggregation import build_uncertainty_penalty_table


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
