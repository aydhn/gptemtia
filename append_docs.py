import re

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "a") as f:
    f.write("""
## Sizing & Level Generation Flow
Sizing Candidates
→ Level Context Loader
→ ATR Levels
→ Structure Levels
→ Volatility Adjusted Levels
→ Target Ladder
→ Reward/Risk Evaluation
→ StopTargetLevelCandidatePool
→ Future Backtest / Paper Trade / Exit Simulation
""")

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "a") as f:
    f.write("""
### Phase 25
- Level profile sistemi eklendi.
- Level label registry eklendi.
- Level models eklendi.
- ATR tabanlı teorik stop/target adayları eklendi.
- Structure/swing/breakout referans seviyeleri eklendi.
- Volatiliteye göre level adjustment eklendi.
- Target ladder eklendi.
- Invalidation zone candidate eklendi.
- Reward/risk hesaplama eklendi.
- Level filters eklendi.
- StopTargetLevelCandidate dataclass eklendi.
- StopTargetLevelCandidatePool eklendi.
- Level quality report eklendi.
- LevelPipeline eklendi.
- DataLake level_candidates/level_pool desteği aldı.
- Level preview/batch/status scriptleri eklendi.
- Testler genişletildi.
""")
