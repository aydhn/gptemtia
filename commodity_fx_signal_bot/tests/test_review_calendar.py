import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.domain_registry import build_maintenance_domain_registry
from local_maintenance.task_registry import build_maintenance_task_registry
from local_maintenance.review_calendar import build_periodic_review_calendar, build_monthly_review_calendar, build_quarterly_review_calendar

def test_periodic_review_calendar():
    profile = get_default_local_maintenance_profile()
    domain_df, _ = build_maintenance_domain_registry(profile)
    task_df, _ = build_maintenance_task_registry(domain_df, profile)

    cal_df, summary = build_periodic_review_calendar(task_df, profile)
    assert not cal_df.empty
    assert summary["total_items"] > 0
    assert "not an automatic scheduler" in summary["disclaimer"].lower()

def test_monthly_quarterly_calendars():
    profile = get_default_local_maintenance_profile()
    domain_df, _ = build_maintenance_domain_registry(profile)
    task_df, _ = build_maintenance_task_registry(domain_df, profile)

    m_df = build_monthly_review_calendar(task_df, profile)
    q_df = build_quarterly_review_calendar(task_df, profile)
    assert not m_df.empty
    assert not q_df.empty
