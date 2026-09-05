
from local_review_governance.review_report_builder import build_review_disclaimer
def test_report_builder():
    assert "rehearsal" in build_review_disclaimer()
