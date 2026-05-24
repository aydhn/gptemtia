import pandas as pd
from datetime import datetime, timezone
from research_planning.planning_models import RoadmapHealthSnapshot, build_roadmap_snapshot_id

def calculate_roadmap_health_score(backlog_df: pd.DataFrame, debt_summary: dict, opportunity_summary: dict) -> float:
    # Health score calculation
    if backlog_df.empty:
        return 1.0 # Empty backlog means no debt, healthy

    # High debt lowers health
    debt_items = debt_summary.get("total_debt_items", 0)
    total_items = len(backlog_df)

    if total_items == 0:
        return 1.0

    debt_ratio = debt_items / total_items
    health = max(0.0, 1.0 - debt_ratio)

    return min(1.0, health)

def infer_roadmap_status(score: float, high_priority_count: int, blocked_count: int) -> str:
    if blocked_count > 5:
        return "blocked_research_roadmap"
    if high_priority_count > 20:
        return "overloaded_research_roadmap"
    if score >= 0.7:
        return "healthy_research_roadmap"
    if score >= 0.4:
        return "manageable_research_roadmap"
    return "unknown_research_roadmap"

def build_roadmap_health_snapshot(backlog_df: pd.DataFrame, debt_summary: dict, opportunity_summary: dict) -> RoadmapHealthSnapshot:
    created_at = datetime.now(timezone.utc).isoformat()

    backlog_count = len(backlog_df) if not backlog_df.empty else 0
    high_priority_count = 0
    blocked_count = 0

    if not backlog_df.empty:
        if "priority_label" in backlog_df.columns:
            high_priority_count = len(backlog_df[backlog_df["priority_label"].isin(["critical_research_priority", "high_research_priority"])])
        if "status" in backlog_df.columns:
            blocked_count = len(backlog_df[backlog_df["status"] == "task_blocked"])

    debt_score = 0.5 # Default fallback
    if "total_debt_items" in debt_summary and backlog_count > 0:
        debt_score = min(1.0, debt_summary["total_debt_items"] / backlog_count)

    opp_score = 0.5
    if "total_opportunities" in opportunity_summary:
        opp_score = min(1.0, opportunity_summary["total_opportunities"] / 10.0) # Assume 10+ is max

    health_score = calculate_roadmap_health_score(backlog_df, debt_summary, opportunity_summary)

    return RoadmapHealthSnapshot(
        snapshot_id=build_roadmap_snapshot_id(created_at),
        created_at_utc=created_at,
        backlog_count=backlog_count,
        high_priority_count=high_priority_count,
        blocked_count=blocked_count,
        research_debt_score=debt_score,
        opportunity_score=opp_score,
        roadmap_health_score=health_score,
        roadmap_status=infer_roadmap_status(health_score, high_priority_count, blocked_count),
        warnings=["Not a production readiness indicator"]
    )

def build_roadmap_health_table(snapshots: list[RoadmapHealthSnapshot]) -> pd.DataFrame:
    from research_planning.planning_models import roadmap_health_snapshot_to_dict
    return pd.DataFrame([roadmap_health_snapshot_to_dict(s) for s in snapshots])

def summarize_roadmap_health(snapshot: RoadmapHealthSnapshot) -> dict:
    from research_planning.planning_models import roadmap_health_snapshot_to_dict
    return roadmap_health_snapshot_to_dict(snapshot)
