import os

path = "commodity_fx_signal_bot/ml/feature_store.py"
with open(path, "r") as f:
    content = f.read()

new_methods = """

    # Phase 47 Governance Methods
    def load_artifact_inventory(self):
        return self.data_lake.load_artifact_inventory()

    def load_artifact_fingerprints(self):
        return self.data_lake.load_artifact_fingerprints()

    def load_provenance_records(self):
        return self.data_lake.load_provenance_records()

    def load_lineage_nodes(self):
        return self.data_lake.load_lineage_nodes()

    def load_lineage_edges(self):
        return self.data_lake.load_lineage_edges()

    def load_dependency_trace(self, trace_name: str):
        return self.data_lake.load_dependency_trace(trace_name)

    def load_audit_trail(self):
        return self.data_lake.load_audit_trail()

    def load_source_attribution(self):
        return self.data_lake.load_source_attribution()

    def load_governance_checklist(self):
        return self.data_lake.load_governance_checklist()

    def load_governance_quality(self, profile_name: str | None = None):
        name = profile_name or "balanced_research_governance"
        return self.data_lake.load_governance_quality(name)

    def load_research_governance_report(self, profile_name: str | None = None):
        name = profile_name or "balanced_research_governance"
        return self.data_lake.load_research_governance_report(name)

    def list_available_governance_reports(self):
        return self.data_lake.list_governance_reports().to_dict(orient="records")

"""

if "load_artifact_inventory" not in content:
    # insert at the end of class FeatureStore:

    # Simple way: just append before the end of the file, assuming FeatureStore is the main/last class
    # Actually, it's safer to find a method and insert after

    insert_point = content.rfind("def load_meta_research_metrics")
    if insert_point != -1:
        # find end of method
        next_def = content.find("def ", insert_point + 10)
        if next_def == -1:
            # it's the last method
            content = content + new_methods
        else:
            content = content[:next_def] + new_methods + content[next_def:]

        with open(path, "w") as f:
            f.write(content)
        print("Updated feature_store.py")
    else:
        # Just append to the class
        content += new_methods
        with open(path, "w") as f:
            f.write(content)
        print("Appended to feature_store.py")

else:
    print("Methods already exist in feature_store.py")
