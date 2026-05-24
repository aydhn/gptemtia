import os
from pathlib import Path

path = "commodity_fx_signal_bot/docs/ARCHITECTURE.md"
if Path(path).exists():
    with open(path, "r") as f:
        content = f.read()

    new_arch = """
### Data Provenance & Governance Flow
DataLake / Reports Output / Experiment Manifests / Research Artifacts
-> ArtifactInventory
-> Fingerprinting
-> ProvenanceRegistry
-> LineageGraph
-> DependencyTracing
-> AuditTrail
-> SourceAttribution
-> FreshnessGovernance
-> IntegrityGovernance
-> ExperimentLineageBridge
-> GovernanceChecklist
-> GovernanceQuality
-> Research Governance Reports
"""
    if "Data Provenance & Governance Flow" not in content:
        content += new_arch
        with open(path, "w") as f:
            f.write(content)
        print("Updated ARCHITECTURE.md")
else:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write("# Architecture\n")
        f.write("""
### Data Provenance & Governance Flow
DataLake / Reports Output / Experiment Manifests / Research Artifacts
-> ArtifactInventory
-> Fingerprinting
-> ProvenanceRegistry
-> LineageGraph
-> DependencyTracing
-> AuditTrail
-> SourceAttribution
-> FreshnessGovernance
-> IntegrityGovernance
-> ExperimentLineageBridge
-> GovernanceChecklist
-> GovernanceQuality
-> Research Governance Reports
""")
    print("Created ARCHITECTURE.md")

path2 = "commodity_fx_signal_bot/docs/PHASE_LOG.md"
if Path(path2).exists():
    with open(path2, "r") as f:
        content2 = f.read()
else:
    Path(path2).parent.mkdir(parents=True, exist_ok=True)
    content2 = "# Phase Log\n"

new_phase = """
## Phase 47: Data Provenance, Lineage and Research Governance
- Governance profile sistemi eklendi.
- Governance label registry eklendi.
- ArtifactRecord, ProvenanceRecord, LineageNode, LineageEdge ve AuditTrailRecord modelleri eklendi.
- Artifact inventory builder eklendi.
- Fingerprinting modülü eklendi.
- Provenance registry eklendi.
- Lineage graph eklendi.
- Dependency tracing eklendi.
- Audit trail eklendi.
- Source attribution eklendi.
- Freshness governance eklendi.
- Integrity governance eklendi.
- Experiment lineage bridge eklendi.
- Governance checklist eklendi.
- Governance quality report eklendi.
- GovernancePipeline eklendi.
- DataLake governance kayıt desteği aldı.
- Governance scriptleri eklendi.
- Testler genişletildi.
"""

if "Phase 47" not in content2:
    content2 += new_phase
    with open(path2, "w") as f:
        f.write(content2)
    print("Updated PHASE_LOG.md")
