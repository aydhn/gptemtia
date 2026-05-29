import re

with open('commodity_fx_signal_bot/config/paths.py', 'r') as f:
    content = f.read()

# Let's remove the orphaned variables at the bottom and insert them correctly at module scope.
# The error was caused by placing variables in the global scope but indented, causing an unexpected indent.
new_content = []
for line in content.split('\n'):
    if line.strip() in [
        "LAKE_SCENARIO_REGRESSION_DIR,", "LAKE_SCENARIO_REGRESSION_REGISTRY_DIR,",
        "LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR,", "LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR,",
        "LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR,", "LAKE_SCENARIO_REGRESSION_REPLAY_DIR,",
        "LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR,", "LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR,",
        "LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR,", "LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR,",
        "LAKE_SCENARIO_REGRESSION_DRIFT_DIR,", "LAKE_SCENARIO_REGRESSION_FAILURES_DIR,",
        "LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR,", "LAKE_SCENARIO_REGRESSION_QUALITY_DIR,",
        "REPORTS_SCENARIO_REGRESSION_DIR,", "REPORTS_SCENARIO_REGRESSION_CSV_DIR,",
        "REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR,", "REPORTS_SCENARIO_REGRESSION_TXT_DIR,",
        "REPORTS_SCENARIO_REGRESSION_JSON_DIR,", "DOCS_SCENARIO_REGRESSION_DIR,"
    ]:
        continue # delete all of them from everywhere
    new_content.append(line)

fixed_content = '\n'.join(new_content)

# add them properly in ensure_project_directories
insert_idx = fixed_content.find("LAKE_COMMAND_CENTER_QUALITY_DIR,")
insert_idx = fixed_content.find("\n", insert_idx) + 1

new_dirs = """        LAKE_SCENARIO_REGRESSION_DIR,
        LAKE_SCENARIO_REGRESSION_REGISTRY_DIR,
        LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR,
        LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR,
        LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR,
        LAKE_SCENARIO_REGRESSION_REPLAY_DIR,
        LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR,
        LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR,
        LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR,
        LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR,
        LAKE_SCENARIO_REGRESSION_DRIFT_DIR,
        LAKE_SCENARIO_REGRESSION_FAILURES_DIR,
        LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR,
        LAKE_SCENARIO_REGRESSION_QUALITY_DIR,
        REPORTS_SCENARIO_REGRESSION_DIR,
        REPORTS_SCENARIO_REGRESSION_CSV_DIR,
        REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR,
        REPORTS_SCENARIO_REGRESSION_TXT_DIR,
        REPORTS_SCENARIO_REGRESSION_JSON_DIR,
        DOCS_SCENARIO_REGRESSION_DIR,
"""
fixed_content = fixed_content[:insert_idx] + new_dirs + fixed_content[insert_idx:]

with open('commodity_fx_signal_bot/config/paths.py', 'w') as f:
    f.write(fixed_content)
