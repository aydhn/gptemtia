import pandas as pd

from governance.governance_checklist import (
    build_research_governance_checklist,
    evaluate_governance_checklist,
)
from governance.governance_config import get_default_governance_profile


def test_checklist():
    profile = get_default_governance_profile()
    chk = build_research_governance_checklist(profile)
    assert not chk.empty

    inv_df = pd.DataFrame([{"path": "data/lake/test"}])
    eval_df = evaluate_governance_checklist(chk, inv_df, {}, {})
    assert not eval_df.empty
    assert "passed" in eval_df["status"].values
