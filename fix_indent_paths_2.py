import re

with open('commodity_fx_signal_bot/config/paths.py', 'r') as f:
    content = f.read()

content = content.replace("        LAKE_SCENARIO_REGRESSION_DIR,\n", "        LAKE_SCENARIO_REGRESSION_DIR,\n")
# Wait, let's just make sure all of them are exactly 8 spaces
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

lines = content.split('\n')
for i, line in enumerate(lines):
    if line.strip() == "LAKE_SCENARIO_REGRESSION_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_REGISTRY_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_REPLAY_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_DRIFT_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_FAILURES_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "LAKE_SCENARIO_REGRESSION_QUALITY_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "REPORTS_SCENARIO_REGRESSION_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "REPORTS_SCENARIO_REGRESSION_CSV_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "REPORTS_SCENARIO_REGRESSION_TXT_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "REPORTS_SCENARIO_REGRESSION_JSON_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    if line.strip() == "DOCS_SCENARIO_REGRESSION_DIR," and not line.startswith("        "):
        lines[i] = "        " + line.strip()

with open('commodity_fx_signal_bot/config/paths.py', 'w') as f:
    f.write('\n'.join(lines))
