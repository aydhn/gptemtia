import os

path = "commodity_fx_signal_bot/config/paths.py"
with open(path, "r") as f:
    content = f.read()

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

# Insert these into the ProjectPaths.__init__ method
# Find the end of ProjectPaths.__init__ or just before the end of the file/class
idx = content.find("class ProjectPaths")
if idx != -1:
    init_idx = content.find("def __init__(self", idx)
    if init_idx != -1:
        # Find next method or end of init
        next_def = content.find("def ", init_idx + 10)
        if next_def != -1:
            content = content[:next_def] + new_attrs + "\n    " + content[next_def:]
        else:
            content += new_attrs

with open(path, "w") as f:
    f.write(content)
print("Patched ProjectPaths")
