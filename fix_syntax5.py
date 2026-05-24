path = "commodity_fx_signal_bot/config/paths.py"
with open(path, "r") as f:
    content = f.read()

# Fix indentation error on line 698
lines = content.split('\n')
for i, line in enumerate(lines):
    if "self.DATA_LAKE_GOVERNANCE_DIR = " in line:
        print(f"Line {i}: {line}")
        # Need to fix indent

new_lines = []
for line in lines:
    if line.startswith("        self.DATA_LAKE_GOVERNANCE_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_INVENTORY_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_FINGERPRINTS_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_PROVENANCE_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_LINEAGE_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_DEPENDENCIES_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_AUDIT_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_SOURCE_ATTRIBUTION_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_CHECKLISTS_DIR = ") or \
       line.startswith("        self.DATA_LAKE_GOVERNANCE_QUALITY_DIR = ") or \
       line.startswith("        self.REPORTS_GOVERNANCE_DIR = ") or \
       line.startswith("        self.REPORTS_GOVERNANCE_CSV_DIR = ") or \
       line.startswith("        self.REPORTS_GOVERNANCE_MARKDOWN_DIR = ") or \
       line.startswith("        self.REPORTS_GOVERNANCE_TXT_DIR = ") or \
       line.startswith("        self.REPORTS_GOVERNANCE_JSON_DIR = ") or \
       line.startswith("        # Phase 47: Governance"):
        pass
    else:
        new_lines.append(line)

content = "\n".join(new_lines)

# Re-insert properly indented
new_attrs = """
        # Phase 47: Governance
        self.DATA_LAKE_GOVERNANCE_DIR = DATA_LAKE_GOVERNANCE_DIR
        self.DATA_LAKE_GOVERNANCE_INVENTORY_DIR = DATA_LAKE_GOVERNANCE_INVENTORY_DIR
        self.DATA_LAKE_GOVERNANCE_FINGERPRINTS_DIR = DATA_LAKE_GOVERNANCE_FINGERPRINTS_DIR
        self.DATA_LAKE_GOVERNANCE_PROVENANCE_DIR = DATA_LAKE_GOVERNANCE_PROVENANCE_DIR
        self.DATA_LAKE_GOVERNANCE_LINEAGE_DIR = DATA_LAKE_GOVERNANCE_LINEAGE_DIR
        self.DATA_LAKE_GOVERNANCE_DEPENDENCIES_DIR = DATA_LAKE_GOVERNANCE_DEPENDENCIES_DIR
        self.DATA_LAKE_GOVERNANCE_AUDIT_DIR = DATA_LAKE_GOVERNANCE_AUDIT_DIR
        self.DATA_LAKE_GOVERNANCE_SOURCE_ATTRIBUTION_DIR = DATA_LAKE_GOVERNANCE_SOURCE_ATTRIBUTION_DIR
        self.DATA_LAKE_GOVERNANCE_CHECKLISTS_DIR = DATA_LAKE_GOVERNANCE_CHECKLISTS_DIR
        self.DATA_LAKE_GOVERNANCE_QUALITY_DIR = DATA_LAKE_GOVERNANCE_QUALITY_DIR

        self.REPORTS_GOVERNANCE_DIR = REPORTS_GOVERNANCE_DIR
        self.REPORTS_GOVERNANCE_CSV_DIR = REPORTS_GOVERNANCE_CSV_DIR
        self.REPORTS_GOVERNANCE_MARKDOWN_DIR = REPORTS_GOVERNANCE_MARKDOWN_DIR
        self.REPORTS_GOVERNANCE_TXT_DIR = REPORTS_GOVERNANCE_TXT_DIR
        self.REPORTS_GOVERNANCE_JSON_DIR = REPORTS_GOVERNANCE_JSON_DIR
"""

idx = content.find("self.factor_research_reports_txt = REPORTS_FACTOR_RESEARCH_TXT_DIR")
if idx != -1:
    end_of_line = content.find("\n", idx)
    content = content[:end_of_line+1] + new_attrs + content[end_of_line+1:]

with open(path, "w") as f:
    f.write(content)
print("Fixed indent in paths.py")
