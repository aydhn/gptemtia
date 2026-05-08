with open("commodity_fx_signal_bot/README.md", "r") as f:
    readme = f.read()

readme_add = """
## ML Dataset Hazırlığı ve Target Engineering (Phase 29)

Bu proje aynı zamanda gelecekteki Machine Learning model eğitimleri için bir altyapı sunar. Bu faz model eğitimi değildir, sadece ML için leakage-safe (geleceğe sızmasız) feature matrix ve target frame üretir.

Özellikler:
- Forward return, direction class, future volatility, future drawdown ve candidate outcome targetları desteklenir.
- Target kolonları feature olarak kullanılamaz.
- Chronological split kullanılır; random split/shuffle yoktur.
- Purging ve embargo desteklenir.
- Leakage audit raporu üretilir.

*Not: "Dataset ready candidate" durumu, model hazır veya canlı sinyal anlamına gelmez.*

Komutlar:
```bash
python -m scripts.run_ml_dataset_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_target_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_dataset_batch_build --limit 10 --timeframe 1d
python -m scripts.run_ml_dataset_status
```
"""

if "ML Dataset Hazırlığı ve Target Engineering" not in readme:
    readme += readme_add
    with open("commodity_fx_signal_bot/README.md", "w") as f:
        f.write(readme)

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    arch = f.read()

arch_add = """
### Phase 29: ML Dataset Hazırlık Katmanı
Feature Stores / Candidate Stores / Backtest Outputs
→ FeatureMatrixBuilder
→ TargetEngineering
→ LeakageChecks
→ Chronological / Purged / Embargo Split
→ SupervisedDatasetBuilder
→ DatasetRegistry
→ Future ML Training / Model Registry / Prediction Engine
"""
if "ML Dataset Hazırlık Katmanı" not in arch:
    arch += arch_add
    with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
        f.write(arch)

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "r") as f:
    log = f.read()

log_add = """
### Phase 29: ML DATASET HAZIRLIĞI, SUPERVISED LEARNING TARGET ENGINEERING, FEATURE MATRIX BUILDER VE LEAKAGE-SAFE TRAIN/TEST SPLIT
- ML dataset profile sistemi eklendi.
- Dataset label registry eklendi.
- Target engineering modülü eklendi.
- FeatureMatrixBuilder eklendi.
- SupervisedDatasetBuilder eklendi.
- Leakage audit modülü eklendi.
- Chronological/purged/embargo split modülü eklendi.
- Dataset quality report eklendi.
- Dataset registry metadata eklendi.
- MLDatasetPipeline eklendi.
- DataLake ML feature/target/dataset/split/metadata kayıt desteği aldı.
- ML dataset preview/batch/status scriptleri eklendi.
- Testler genişletildi.
"""
if "Phase 29: ML DATASET HAZIRLIĞI" not in log:
    log += log_add
    with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
        f.write(log)
