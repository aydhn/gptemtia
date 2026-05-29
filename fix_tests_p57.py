import os

with open('commodity_fx_signal_bot/tests/test_golden_outputs.py', 'r') as f:
    content = f.read()
content = content.replace('assert df.iloc[0]["synthetic_only"] is True', 'assert bool(df.iloc[0]["synthetic_only"]) is True')
with open('commodity_fx_signal_bot/tests/test_golden_outputs.py', 'w') as f:
    f.write(content)

with open('commodity_fx_signal_bot/scenario_regression/snapshot_compare.py', 'r') as f:
    content = f.read()
# In test numeric_diff_score = 0.0, if 0.0 <= 1e-8, it returns snapshot_numeric_diff_within_tolerance.
# We want it to be identical. Let's fix classify_snapshot_diff to return identical if score == 0
content = content.replace(
"""        if numeric_diff_score <= profile.numeric_tolerance:
            if not row_count_changed:
                return "snapshot_numeric_diff_within_tolerance"
""",
"""        if numeric_diff_score == 0.0:
            if not row_count_changed and text_similarity_score in [1.0, None]:
                return "snapshot_identical"
        if numeric_diff_score <= profile.numeric_tolerance:
            if not row_count_changed:
                return "snapshot_numeric_diff_within_tolerance"
"""
)
with open('commodity_fx_signal_bot/scenario_regression/snapshot_compare.py', 'w') as f:
    f.write(content)
