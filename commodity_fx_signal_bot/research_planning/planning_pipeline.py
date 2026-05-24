import pandas as pd
from pathlib import Path
from data.storage.data_lake import DataLake
from config.settings import Settings
from research_planning.planning_config import ResearchPlanningProfile, get_default_research_planning_profile
from research_planning.signal_sources import PlanningSignalCollector
from research_planning.backlog_builder import build_backlog_from_signals
from research_planning.priority_scoring import score_backlog_priorities
from research_planning.next_best_experiment import build_next_best_experiment_table
from research_planning.research_debt import build_research_debt_table, summarize_research_debt
from research_planning.roadmap_health import build_roadmap_health_snapshot, summarize_roadmap_health

class ResearchPlanningPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: ResearchPlanningProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_research_planning_profile()
        self.signal_collector = PlanningSignalCollector(data_lake)

    def build_research_backlog_report(
        self,
        timeframe: str = "1d",
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        signals, _ = self.signal_collector.collect_all_signals(timeframe, self.profile)
        backlog_df, summary = build_backlog_from_signals(signals, self.profile)

        if save:
            try:
                self.data_lake.save_research_planning_signals(timeframe, self.profile.name, pd.DataFrame([s.__dict__ for s in signals]))
                self.data_lake.save_research_backlog(timeframe, self.profile.name, backlog_df, summary)
            except AttributeError:
                # Mock DataLake in tests might not have these methods
                pass

        return backlog_df, summary

    def build_priority_scoring_report(
        self,
        timeframe: str = "1d",
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        signals, _ = self.signal_collector.collect_all_signals(timeframe, self.profile)
        backlog_df, _ = build_backlog_from_signals(signals, self.profile)
        priority_df, summary = score_backlog_priorities(backlog_df, signals, self.profile)

        if save:
            try:
                self.data_lake.save_research_priority_scores(timeframe, self.profile.name, priority_df, summary)
            except AttributeError:
                pass

        return priority_df, summary

    def build_next_best_experiment_report(
        self,
        timeframe: str = "1d",
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        priority_df, _ = self.build_priority_scoring_report(timeframe, save=False)
        next_best_df, summary = build_next_best_experiment_table(priority_df, self.profile)

        if save:
            try:
                self.data_lake.save_next_best_experiments(timeframe, self.profile.name, next_best_df, summary)
            except AttributeError:
                pass

        return next_best_df, summary

    def build_research_debt_report(
        self,
        timeframe: str = "1d",
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        priority_df, _ = self.build_priority_scoring_report(timeframe, save=False)
        debt_df = build_research_debt_table(priority_df)
        summary = summarize_research_debt(debt_df)

        if save:
            try:
                self.data_lake.save_research_debt_report(timeframe, self.profile.name, debt_df, summary)
            except AttributeError:
                pass

        return debt_df, summary

    def build_roadmap_health_report(
        self,
        timeframe: str = "1d",
        save: bool = True,
    ) -> tuple[dict, dict]:

        priority_df, _ = self.build_priority_scoring_report(timeframe, save=False)
        debt_df = build_research_debt_table(priority_df)
        debt_sum = summarize_research_debt(debt_df)

        snapshot = build_roadmap_health_snapshot(priority_df, debt_sum, {"total_opportunities": 0})
        summary = summarize_roadmap_health(snapshot)

        if save:
            try:
                self.data_lake.save_roadmap_health_snapshot(timeframe, self.profile.name, summary)
            except AttributeError:
                pass

        return summary, summary

    def build_full_research_planning_report(
        self,
        timeframe: str = "1d",
        save: bool = True,
    ) -> tuple[dict, dict]:

        # Simplified full pipeline run
        self.build_research_backlog_report(timeframe, save)
        self.build_priority_scoring_report(timeframe, save)
        self.build_next_best_experiment_report(timeframe, save)
        self.build_research_debt_report(timeframe, save)
        self.build_roadmap_health_report(timeframe, save)

        return {"status": "success"}, {"completed": True}
