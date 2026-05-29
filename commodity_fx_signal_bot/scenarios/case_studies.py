"""
Synthetic case studies for demonstration purposes.
"""

import pandas as pd
from typing import List

from scenarios.scenario_config import ScenarioProfile
from scenarios.scenario_models import CaseStudy, build_case_study_id


def _build_case_study(title: str, label: str, obj: str, steps: list, learning: str) -> CaseStudy:
    cid = build_case_study_id(title, label)
    return CaseStudy(
        case_study_id=cid,
        title=title,
        case_study_label=label,
        scenario_ids=[],
        objective=obj,
        steps=steps,
        expected_learning=learning,
        warnings=["Bu case study synthetic/offline araştırma gösterimidir. Yatırım tavsiyesi içermez."]
    )


def build_trend_regime_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Trend Regime Identification",
        "trend_regime_case_study",
        "Demonstrate offline trend regime classification on synthetic data.",
        [
            {"step": 1, "action": "Load synthetic OHLCV data"},
            {"step": 2, "action": "Calculate EMA crossovers"},
            {"step": 3, "action": "Apply regime logic (trend_up/trend_down)"}
        ],
        "Understand how offline indicators classify market phases without live data."
    )


def build_inflation_comparison_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Inflation and FX Comparison",
        "inflation_comparison_case_study",
        "Compare synthetic inflation with synthetic FX rates.",
        [
            {"step": 1, "action": "Load synthetic macro data"},
            {"step": 2, "action": "Load synthetic FX data"},
            {"step": 3, "action": "Calculate offline correlation"}
        ],
        "Understand offline data alignment between macro and price data."
    )


def build_factor_conflict_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Factor Conflict Resolution",
        "factor_conflict_case_study",
        "Show offline behavior when momentum and mean-reversion conflict.",
        [
            {"step": 1, "action": "Generate conflicting synthetic signals"},
            {"step": 2, "action": "Apply meta-research conflict resolution"},
            {"step": 3, "action": "Observe final candidate weight reduction"}
        ],
        "Understand how conflicting indicators safely reduce confidence offline."
    )


def build_governance_gap_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Provenance Tracking",
        "governance_gap_case_study",
        "Demonstrate finding missing provenance in offline artifacts.",
        [
            {"step": 1, "action": "Create synthetic artifact without checksum"},
            {"step": 2, "action": "Run offline governance check"},
            {"step": 3, "action": "Observe warning generation"}
        ],
        "Understand offline governance and artifact safety."
    )


def build_experiment_ablation_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Model Ablation",
        "experiment_ablation_case_study",
        "Demonstrate dropping a feature to test its impact offline.",
        [
            {"step": 1, "action": "Run synthetic baseline model"},
            {"step": 2, "action": "Drop 'RSI' feature"},
            {"step": 3, "action": "Compare offline validation scores"}
        ],
        "Understand offline feature importance testing without live trading."
    )


def build_knowledge_query_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Symbol Knowledge Query",
        "knowledge_query_case_study",
        "Query the offline knowledge base for symbol context.",
        [
            {"step": 1, "action": "Build offline index"},
            {"step": 2, "action": "Query 'GC=F' characteristics"}
        ],
        "Understand how the system uses local markdown for context."
    )


def build_planning_backlog_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Backlog Prioritization",
        "planning_backlog_case_study",
        "Demonstrate how technical debt is prioritized.",
        [
            {"step": 1, "action": "Load synthetic backlog"},
            {"step": 2, "action": "Run prioritization script"}
        ],
        "Understand the offline planning mechanism."
    )


def build_maintenance_cleanup_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Cache Cleanup",
        "maintenance_cleanup_case_study",
        "Show offline maintenance safely identifying old caches.",
        [
            {"step": 1, "action": "Create old synthetic cache files"},
            {"step": 2, "action": "Run maintenance dry-run"}
        ],
        "Understand safe file operations in dry-run mode."
    )


def build_final_review_case_study(profile: ScenarioProfile) -> CaseStudy:
    return _build_case_study(
        "Safety Audit",
        "final_review_case_study",
        "Demonstrate the final safety review catching forbidden terms.",
        [
            {"step": 1, "action": "Create synthetic file with 'LIVE_ORDER'"},
            {"step": 2, "action": "Run final review audit"},
            {"step": 3, "action": "Observe failure"}
        ],
        "Understand the strict safety boundaries preventing live trading."
    )


def build_default_case_studies(profile: ScenarioProfile) -> List[CaseStudy]:
    """Builds all default synthetic case studies."""
    return [
        build_trend_regime_case_study(profile),
        build_inflation_comparison_case_study(profile),
        build_factor_conflict_case_study(profile),
        build_governance_gap_case_study(profile),
        build_experiment_ablation_case_study(profile),
        build_knowledge_query_case_study(profile),
        build_planning_backlog_case_study(profile),
        build_maintenance_cleanup_case_study(profile),
        build_final_review_case_study(profile)
    ]


def case_studies_to_dataframe(case_studies: List[CaseStudy]) -> pd.DataFrame:
    """Converts a list of CaseStudy objects to a DataFrame."""
    if not case_studies:
        return pd.DataFrame()
    return pd.DataFrame([cs.__dict__ for cs in case_studies])
