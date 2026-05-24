import os

path = "commodity_fx_signal_bot/reports/report_builder.py"
with open(path, "r") as f:
    content = f.read()

# We need to un-indent the functions from ReportBuilder class to the module level
lines = content.split('\n')
new_lines = []
for line in lines:
    if line.startswith("    def build_artifact_inventory_text_report") or \
       line.startswith("    def build_lineage_graph_text_report") or \
       line.startswith("    def build_provenance_text_report") or \
       line.startswith("    def build_dependency_trace_text_report") or \
       line.startswith("    def build_audit_trail_text_report") or \
       line.startswith("    def build_research_governance_text_report") or \
       line.startswith("    def build_governance_status_report"):
        new_lines.append(line[4:].replace("(self, ", "("))
    elif line.startswith("    ") and "report = " in line or "rep = " in line or "rep += " in line or "for " in line or "return " in line:
        pass # need a better way
