with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "a") as f:
    f.write("""

## Position Sizing Candidate Layer (Simülasyon Katmanı)

Risk Candidates
→ Sizing Context Loader
→ Risk Unit Calculator
→ ATR / Volatility Adjusted Sizing
→ Budget Model
→ Exposure Limits
→ SizingCandidatePool
→ Future Backtest / Paper Trade / Portfolio Simulation
""")

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "a") as f:
    f.write("""

## Phase 24: Pozisyon Boyutu Simülasyon Adayları, Volatiliteye Göre Teorik Risk Birimi ve Portföy Risk Bütçesi
- Sizing profile sistemi eklendi.
- Sizing label registry eklendi.
- Sizing models eklendi.
- Risk unit hesaplama eklendi.
- ATR tabanlı teorik sizing eklendi.
- Volatilite adjustment eklendi.
- Teorik budget model eklendi.
- Exposure limit proxy eklendi.
- Sizing filters eklendi.
- SizingCandidate dataclass eklendi.
- SizingCandidatePool eklendi.
- Sizing quality report eklendi.
- SizingPipeline eklendi.
- DataLake sizing_candidates/sizing_pool desteği aldı.
- Sizing preview/batch/status scriptleri eklendi.
- Testler genişletildi.
""")
