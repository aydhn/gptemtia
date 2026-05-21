from report_exports.report_comparison import (
    compare_research_scores,
    compare_warning_counts,
    compare_archive_records
)

def test_compare_research_scores():
    res = compare_research_scores({"research_score": 0.8}, {"research_score": 0.5})
    assert res["label"] == "improved"

    res = compare_research_scores({"research_score": 0.5}, {"research_score": 0.8})
    assert res["label"] == "deteriorated"

    res = compare_research_scores({"research_score": 0.5}, None)
    assert res["label"] == "insufficient_history"

def test_compare_archive_records():
    curr = {"report_id": "r2", "research_score": 0.8}
    prev = {"report_id": "r1", "research_score": 0.7}
    comp = compare_archive_records(curr, prev)
    assert comp.comparison_label == "improved"
    assert "improved" in comp.comparison_label
