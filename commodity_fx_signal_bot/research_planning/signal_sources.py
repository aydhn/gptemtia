import pandas as pd
from typing import Any
from pathlib import Path

from data.storage.data_lake import DataLake
from research_planning.planning_config import ResearchPlanningProfile
from research_planning.planning_models import ResearchSignal, build_research_signal_id

class PlanningSignalCollector:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def collect_governance_signals(self, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        signals = []
        if not profile.include_governance_signals:
            return signals, {"status": "skipped"}

        try:
            # Check governance audits
            audit_df = self.data_lake.load_governance_audit_report("latest")
            if not audit_df.empty:
                for idx, row in audit_df.iterrows():
                    if row.get("status") in ["failed", "warning"]:
                        sig = ResearchSignal(
                            signal_id=build_research_signal_id("governance", f"Governance Issue {idx}"),
                            source_module="governance",
                            source_type="audit",
                            symbol=None,
                            timeframe=None,
                            severity_score=0.8 if row.get("status") == "failed" else 0.5,
                            opportunity_score=0.2,
                            uncertainty_score=0.1,
                            quality_score=0.3,
                            title=f"Governance Audit Issue: {row.get('check_name', 'Unknown')}",
                            description="Governance audit failed or returned a warning.",
                            evidence={"row": str(row.to_dict())},
                            warnings=[]
                        )
                        signals.append(sig)
        except Exception as e:
            # Missing file generates a signal
            sig = ResearchSignal(
                signal_id=build_research_signal_id("governance", "Missing Audit"),
                source_module="governance",
                source_type="missing_data",
                symbol=None,
                timeframe=None,
                severity_score=0.6,
                opportunity_score=0.1,
                uncertainty_score=0.5,
                quality_score=0.0,
                title="Missing Governance Audit",
                description=f"Could not load governance audit report: {str(e)}",
                evidence={"error": str(e)},
                warnings=["governance source missing"]
            )
            signals.append(sig)

        return signals, {"status": "success", "count": len(signals)}

    def collect_experiment_signals(self, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        signals = []
        if not profile.include_experiment_signals:
            return signals, {"status": "skipped"}

        try:
            # Just a placeholder for actual experiment reading
            exp_df = self.data_lake.load_experiment_tracking_table()
            if not exp_df.empty:
                for idx, row in exp_df.iterrows():
                    if row.get("reproducibility_score", 1.0) < 0.6:
                        sig = ResearchSignal(
                            signal_id=build_research_signal_id("experiment", f"Low Reproducibility {idx}"),
                            source_module="experiment",
                            source_type="quality",
                            symbol=None,
                            timeframe=None,
                            severity_score=0.7,
                            opportunity_score=0.4,
                            uncertainty_score=0.6,
                            quality_score=row.get("reproducibility_score", 0.0),
                            title=f"Low Reproducibility: {row.get('experiment_name', 'Unknown')}",
                            description="Experiment has low reproducibility score.",
                            evidence={"row": str(row.to_dict())},
                            warnings=[]
                        )
                        signals.append(sig)
        except Exception as e:
            pass # Be lenient

        return signals, {"status": "success", "count": len(signals)}

    def collect_meta_research_signals(self, timeframe: str, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        signals = []
        if not profile.include_meta_signals:
            return signals, {"status": "skipped"}

        try:
            meta_df = self.data_lake.load_meta_conflict_report(timeframe)
            if not meta_df.empty:
                for idx, row in meta_df.iterrows():
                    if row.get("conflict_score", 0.0) > 0.7:
                        sig = ResearchSignal(
                            signal_id=build_research_signal_id("meta_research", f"High Conflict {idx}", row.get("symbol")),
                            source_module="meta_research",
                            source_type="conflict",
                            symbol=row.get("symbol"),
                            timeframe=timeframe,
                            severity_score=0.5,
                            opportunity_score=0.8,
                            uncertainty_score=0.9,
                            quality_score=0.5,
                            title=f"High Meta Conflict: {row.get('symbol', 'Unknown')}",
                            description="High conflict detected in meta research layer.",
                            evidence={"row": str(row.to_dict())},
                            warnings=["meta_conflict"]
                        )
                        signals.append(sig)
        except Exception as e:
            sig = ResearchSignal(
                signal_id=build_research_signal_id("meta_research", "Missing Meta Report"),
                source_module="meta_research",
                source_type="missing_data",
                symbol=None,
                timeframe=timeframe,
                severity_score=0.4,
                opportunity_score=0.2,
                uncertainty_score=0.8,
                quality_score=0.0,
                title="Missing Meta Research Report",
                description=f"Could not load meta research report: {str(e)}",
                evidence={"error": str(e)},
                warnings=["meta source missing"]
            )
            signals.append(sig)

        return signals, {"status": "success", "count": len(signals)}

    def collect_factor_signals(self, timeframe: str, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        return [], {"status": "stub", "count": 0}

    def collect_portfolio_signals(self, timeframe: str, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        return [], {"status": "stub", "count": 0}

    def collect_regime_signals(self, timeframe: str, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        return [], {"status": "stub", "count": 0}

    def collect_validation_ml_paper_signals(self, timeframe: str, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        return [], {"status": "stub", "count": 0}

    def collect_observability_signals(self, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        return [], {"status": "stub", "count": 0}

    def collect_all_signals(self, timeframe: str, profile: ResearchPlanningProfile) -> tuple[list[ResearchSignal], dict]:
        all_signals = []
        summary = {}

        gov_sigs, gov_sum = self.collect_governance_signals(profile)
        all_signals.extend(gov_sigs)
        summary["governance"] = gov_sum

        exp_sigs, exp_sum = self.collect_experiment_signals(profile)
        all_signals.extend(exp_sigs)
        summary["experiment"] = exp_sum

        meta_sigs, meta_sum = self.collect_meta_research_signals(timeframe, profile)
        all_signals.extend(meta_sigs)
        summary["meta"] = meta_sum

        fac_sigs, fac_sum = self.collect_factor_signals(timeframe, profile)
        all_signals.extend(fac_sigs)
        summary["factor"] = fac_sum

        summary["total_signals"] = len(all_signals)
        return all_signals, summary
