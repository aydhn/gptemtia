import re
import os

readme_path = "commodity_fx_signal_bot/README.md"
with open(readme_path, "r") as f:
    readme_content = f.read()

readme_addition = """
## Research Artifact Metadata, Model Cards and Dataset Cards

Artifact metadata katmani model deployment onayi degildir.
Model cards canli trading veya broker execution icin kullanilamaz.
Dataset cards veri dogrulugu veya canli piyasa uygunlugu garantisi degildir.
Experiment/reproducibility cards gercek performans garantisi degildir.
Scenario/regression cards production readiness degildir.
Non-use policy her artefakt icin canli emir, broker execution, yatirim tavsiyesi ve deployment yasaklarini belirtir.
Ciktilar data/lake/artifact_metadata ve reports/output/artifact_metadata altinda olusur.

Komutlar:
```bash
python -m scripts.run_research_artifact_inventory
python -m scripts.run_model_dataset_cards
python -m scripts.run_experiment_reproducibility_cards
python -m scripts.run_scenario_regression_cards
python -m scripts.run_research_metadata_export
python -m scripts.run_metadata_quality_report
python -m scripts.run_metadata_status
```
"""
if "Research Artifact Metadata, Model Cards and Dataset Cards" not in readme_content:
    readme_content += readme_addition
    with open(readme_path, "w") as f:
        f.write(readme_content)

arch_path = "commodity_fx_signal_bot/docs/ARCHITECTURE.md"
if os.path.exists(arch_path):
    with open(arch_path, "r") as f:
        arch_content = f.read()

    arch_addition = """
### Artifact Metadata Flow
Research Artifacts -> ResearchArtifactInventory -> ModelCards/DatasetCards/ExperimentCards/ReproducibilityCards -> BacktestCards/ScenarioCards/RegressionCards/FeatureSetCards/SyntheticDataCards/ResearchReportCards -> LineageCards/LimitationCards/IntendedUseCards/NonUsePolicyCards -> MetadataScoring/MetadataValidation/MetadataQuality/MetadataExport -> Artifact Metadata Outputs
"""
    if "Artifact Metadata Flow" not in arch_content:
        arch_content += arch_addition
        with open(arch_path, "w") as f:
            f.write(arch_content)

log_path = "commodity_fx_signal_bot/docs/PHASE_LOG.md"
if os.path.exists(log_path):
    with open(log_path, "r") as f:
        log_content = f.read()

    log_addition = """
### Phase 65: Local Model Cards, Dataset Cards, Experiment Cards, Reproducibility Cards ve Research Artifact Metadata Layer
- Artifact metadata profile sistemi eklendi.
- Metadata label registry eklendi.
- ResearchArtifact, ArtifactCard, ReproducibilityChecklistItem ve MetadataExportRecord modelleri eklendi.
- Research artifact inventory, model cards, dataset cards, experiment cards, vb. eklendi.
- Lineage, limitation, intended use, non-use policy kartlari eklendi.
- Metadata completeness/freshness scoring eklendi.
- Metadata validation ve quality report eklendi.
- ArtifactMetadataPipeline eklendi.
- Scriptler ve testler eklendi.
"""
    if "Phase 65:" not in log_content:
        log_content += log_addition
        with open(log_path, "w") as f:
            f.write(log_content)

operator_path = "commodity_fx_signal_bot/docs/OPERATOR_MANUAL.md"
if os.path.exists(operator_path):
    with open(operator_path, "a") as f:
         f.write("\n## Artifact Metadata\nModel card okuma rehberi, dataset card kullanim amaci, non-use policy onemi. Canli emir, broker execution, yatirim tavsiyesi, resmi sertifika ve deployment olmadigi acik yazilsin.\n")
