with open("commodity_fx_signal_bot/README.md", "r") as f:
    content = f.read()

meta_research_section = """
## Meta Research and Consensus Engine

Bu proje bir meta-research/kanıt ağırlıklandırma katmanı içerir (Phase 45).
Bu katman; teknik analiz, backtest, ML, sentetik endeks, makro rejim ve faktör araştırmalarından gelen verileri ağırlıklandırır ve araştırma kalitesine/güvenilirliğine göre düzenler.
Önemli Uyarı:
- Meta research canlı sinyal motoru değildir.
- Consensus score yatırım tavsiyesi değildir.
- Strong positive/negative consensus AL/SAT anlamına gelmez.
- Evidence weighting kaynak güvenilirliğine ve kaliteye göre araştırma skorlarını birleştirir.
- Conflict detection kaynaklar arası çelişkiyi gösterir.
- Quality-adjusted ranking sadece araştırma önceliklendirmesidir.
- Çıktılar `data/lake/meta_research` ve `reports/output/meta_research` altında oluşur.

Komutlar:
```bash
python -m scripts.run_meta_research_report --timeframe 1d --limit 20
python -m scripts.run_meta_consensus_report --timeframe 1d --limit 20
python -m scripts.run_evidence_conflict_report --timeframe 1d --limit 20
python -m scripts.run_quality_adjusted_ranking_report --timeframe 1d --limit 30
python -m scripts.run_meta_symbol_snapshot --symbol GC=F --timeframe 1d
python -m scripts.run_meta_research_status
```
"""

if "Meta Research and Consensus Engine" not in content:
    content = content + "\n" + meta_research_section
    with open("commodity_fx_signal_bot/README.md", "w") as f:
        f.write(content)

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    content = f.read()

meta_flow = """
## Meta Research Pipeline (Phase 45)

Technical / Strategy / Risk-Level / Backtest / Validation / ML / Paper / Research Reports / Synthetic Index / Portfolio / Regime / Factor
-> EvidenceCollector
-> EvidenceNormalizer
-> SourceRegistry
-> ReliabilityScoring
-> ConsensusEngine
-> ConflictDetection
-> UncertaintyAggregation
-> EnsembleScoring
-> QualityAdjustment
-> MetaRanking
-> MetaSnapshot
-> MetaQuality
-> Meta Research Reports
"""
if "Meta Research Pipeline (Phase 45)" not in content:
    content = content + "\n" + meta_flow
    with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
        f.write(content)

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "r") as f:
    content = f.read()

phase45_log = """
## Phase 45
- Meta research profile sistemi eklendi.
- Meta label registry eklendi.
- ResearchEvidence, ConsensusResult ve MetaResearchSnapshot modelleri eklendi.
- Evidence source registry eklendi.
- Evidence collector eklendi.
- Evidence normalizer eklendi.
- Source reliability scoring eklendi.
- Consensus engine eklendi.
- Conflict detection eklendi.
- Uncertainty aggregation eklendi.
- Ensemble scoring eklendi.
- Quality adjustment eklendi.
- Meta ranking eklendi.
- Meta snapshot eklendi.
- Meta quality report eklendi.
- MetaResearchPipeline eklendi.
- DataLake meta research kayıt desteği aldı.
- Meta research scriptleri eklendi.
- Testler genişletildi.
"""
if "Phase 45" not in content:
    content = content + "\n" + phase45_log
    with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
        f.write(content)
