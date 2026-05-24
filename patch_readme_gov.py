import os

path = "commodity_fx_signal_bot/README.md"
with open(path, "r") as f:
    content = f.read()

new_section = """
## Data Provenance, Lineage and Research Governance (Phase 47)
- Governance katmanı canlı trading governance değildir. Sadece offline research artifact'leri içindir.
- Artifact inventory data/lake ve reports/output dosyalarını tarar.
- Fingerprinting veri/artifact izlenebilirliği içindir.
- Provenance ve lineage graph kaynak/bağımlılık ilişkilerini araştırma bağlamında gösterir.
- Audit trail broker audit veya compliance onayı değildir.
- Dependency tracing approximation olabilir.
- Governance passed production compliance onayı değildir.
- Çıktılar data/lake/governance ve reports/output/governance altında oluşur.

### Governance Commands
```bash
python -m scripts.run_artifact_inventory_report
python -m scripts.run_lineage_graph_report
python -m scripts.run_provenance_report
python -m scripts.run_dependency_trace_report --symbol GC=F --direction upstream
python -m scripts.run_audit_trail_report
python -m scripts.run_research_governance_report
python -m scripts.run_governance_status
```
"""

if "Data Provenance, Lineage and Research Governance" not in content:
    content += new_section
    with open(path, "w") as f:
        f.write(content)
    print("Updated README.md")
