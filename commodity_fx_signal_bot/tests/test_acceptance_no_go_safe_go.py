from pathlib import Path
import pandas as pd
from local_acceptance.acceptance_no_go_safe_go import (
    build_acceptance_no_go_register,
    build_acceptance_safe_go_register,
    build_acceptance_no_go_safe_go_summary
)
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_no_go_safe_go():
    p = get_default_local_acceptance_profile()
    n_df, _ = build_acceptance_no_go_register(Path("."), p)
    s_df, _ = build_acceptance_safe_go_register(Path("."), p)
    assert not n_df.empty
    assert not s_df.empty
    sm_df, _ = build_acceptance_no_go_safe_go_summary(n_df, s_df, p)
    assert not sm_df.empty
