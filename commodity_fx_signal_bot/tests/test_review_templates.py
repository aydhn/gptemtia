import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.review_templates import build_monthly_review_template, build_quarterly_review_template

def test_review_templates():
    profile = get_default_local_maintenance_profile()

    m_temp, _ = build_monthly_review_template(profile)
    q_temp, _ = build_quarterly_review_template(profile)

    assert "Monthly Operator Review Template" in m_temp
    assert "Quarterly Operator Review Template" in q_temp
    assert "audit" in m_temp.lower()
