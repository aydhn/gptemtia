import re

# Update README.md
with open("commodity_fx_signal_bot/README.md", "r") as f:
    content = f.read()

new_readme_section = """
## Offline ML Baseline Training ve Model Evaluation (Phase 30)

Bu faz canlı prediction değildir. Model training sadece offline/research amaçlıdır.
- Dummy, Logistic Regression, Random Forest ve HistGradientBoosting baseline modelleri desteklenir.
- Chronological CV kullanılır; random shuffle yoktur.
- Preprocessing train set üzerinde fit edilir, validation/test sadece transform edilir.
- Model registry deploy sistemi değildir.
- `registered_candidate` canlı model onayı değildir.
- Evaluation metrikleri gelecek performans garantisi değildir.
- Model çıktısı canlı sinyal veya yatırım tavsiyesi değildir.

**Komutlar:**
```bash
python -m scripts.run_ml_training_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_model_evaluation_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_training_batch --limit 10 --timeframe 1d
python -m scripts.run_ml_model_registry_status
python -m scripts.run_ml_model_artifact_status
```
"""
content = content + "\n" + new_readme_section
with open("commodity_fx_signal_bot/README.md", "w") as f:
    f.write(content)

# Update ARCHITECTURE.md
with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    content = f.read()

new_arch_section = """
### Phase 30: ML Training & Evaluation Layer
ML Supervised Dataset
→ Feature/Target Schema
→ BasicPreprocessor
→ BaselineModels
→ Chronological CV
→ MLModelTrainer
→ ModelEvaluator
→ ModelArtifacts
→ ModelRegistry
→ Future Prediction Engine / Model Monitoring / Paper Trade Research
"""
content = content + "\n" + new_arch_section
with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
    f.write(content)

# Update PHASE_LOG.md
with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "r") as f:
    content = f.read()

new_log_section = """
### Phase 30: İLK ML MODEL TRAINING İSKELETİ, BASELINE MODELLER, CROSS-VALIDATION, MODEL REGISTRY
- ML training profile sistemi eklendi.
- Model label registry eklendi.
- Feature/target schema snapshot eklendi.
- BasicPreprocessor eklendi.
- Baseline model factory eklendi.
- Chronological CV modülü eklendi.
- MLModelTrainer eklendi.
- ModelEvaluator eklendi.
- Model artifact save/load eklendi.
- ModelRegistry taslağı eklendi.
- Model quality report eklendi.
- MLTrainingPipeline eklendi.
- DataLake model evaluation/CV/registry/artifact desteği aldı.
- ML training preview/batch/status scriptleri eklendi.
- Testler genişletildi.
"""
content = content + "\n" + new_log_section
with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
    f.write(content)
