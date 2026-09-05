import os

def update_readme():
    path = "README.md"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    addition = """
## Phase 107 FX Data Provider Layer
Phase 107, scraping yapmadan FX/döviz veri sağlayıcı katmanını kurar.
Major/minor/exotic FX pair universe registry oluşturulur.
FX sembol normalizasyonu, quote/OHLCV schema contract, cross-rate requirements ve provider capability map eklenir.
Bu faz gerçek FX provider API entegrasyonu veya gerçek veri indirme fazı değildir.
FX dry-run fixture, manual file placeholder, local cache placeholder, official API placeholder ve licensed provider placeholder eklenir.
Phase 108 Commodities Data Provider Layer geliştirmesi için temel bırakılır.
Final hedef hâlâ Phase 160'tır.
Canlı trading, broker execution, yatırım tavsiyesi, deployment, scraping veya official approval yoktur.

Komutlar:
```bash
python -m scripts.run_fx_provider_profile_registry
python -m scripts.run_fx_pair_universe_registry
python -m scripts.run_fx_provider_registry
python -m scripts.run_fx_provider_contracts
python -m scripts.run_fx_dry_run_fixture
python -m scripts.run_fx_provider_health_check
python -m scripts.run_fx_provider_quality_report
python -m scripts.run_fx_provider_status
```
"""
    if "Phase 107 FX Data Provider Layer" not in content:
        content += "\n" + addition
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def update_roadmap():
    path = "docs/ROADMAP.md"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    addition = """
- 101-105 completed/foundation block ready
- 106 completed/Multi-Provider Data Abstraction ready
- 107 FX Data Provider Layer
- 108 Commodities Data Provider Layer sıradaki faz
- 109 Macro Data Provider Layer
- 110 Economic Calendar Integration No Scraping
- 111 News Metadata Integration No Scraping
- 112 Data Quality Engine
- 113 Data Normalization Layer
- 114 Data Lineage and Provenance
- 115 Data Provider Benchmark Report
"""
    if "107 FX Data Provider Layer" not in content:
        content += "\n" + addition
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def update_phase_log():
    path = "docs/PHASE_LOG.md"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    addition = """
## Phase 107
- FX Provider Profile sistemi eklendi.
- FX provider domain registry eklendi.
- FX pair universe registry eklendi.
- FX currency metadata registry eklendi.
- FX symbol normalization map eklendi.
- FX quote/OHLCV schema contract eklendi.
- FX cross-rate requirement registry eklendi.
- FX provider capability/metadata registry eklendi.
- FX request/response/error schema eklendi.
- FX provider interface ve adapter contract eklendi.
- FX provider registry ve resolver eklendi.
- FX provider preference resolver eklendi.
- FX capability matcher eklendi.
- FX dry-run fixture provider eklendi.
- FX manual file, local cache, official API ve licensed placeholder'ları eklendi.
- FX output validation contract eklendi.
- FX safety boundary eklendi.
- FX health/readiness/validation/quality raporları eklendi.
- Phase 108 commodities provider handoff raporu eklendi.
- Scraping yapılmayacağı sınırı FX katmanında tekrar güçlendirildi.
"""
    if "## Phase 107" not in content:
        content += "\n" + addition
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def update_arch():
    path = "docs/ARCHITECTURE.md"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    addition = """
Phase 106 Multi-Provider Data Abstraction
→ Phase 107 FX Data Provider Layer
→ FX Provider Profile Registry
→ FX Pair Universe Registry
→ FX Currency Metadata
→ FX Symbol Normalization
→ FX Quote Schema
→ FX OHLCV Schema
→ FX Cross-Rate Requirements
→ FX Provider Capability Registry
→ FX Provider Metadata
→ FX Request/Response/Error Schema
→ BaseFXProvider Interface
→ FX Adapter Contract
→ FX Provider Registry
→ FX Provider Resolver
→ FX Dry-Run Fixture Provider
→ FX Placeholder Providers
→ FX Output Validation
→ FX Safety Boundary
→ Phase 108 Commodities Data Provider Layer
"""
    if "Phase 107 FX Data Provider Layer" not in content:
        content += "\n" + addition
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def update_config_doc():
    path = "docs/CONFIGURATION.md"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    addition = """
## Phase 107 FX Configuration
- FX provider profile nasıl seçilir? `DEFAULT_FX_PROVIDER_PROFILE` env vars ile seçilir.
- FX pair universe nasıl yorumlanır? Major, minor, exotic olarak ayrılır. Sinyal değildir.
- major/minor/exotic pair farkları: İşlem hacmi ve likiditeye göre.
- FX symbol normalization nasıl çalışır? Broker/Provider sembollerini `XXX/YYY` canonical formuna getirir.
- FX quote/OHLCV schema ne işe yarar? Çekilecek veri sözleşmesini tanımlar.
- Cross-rate requirements neden kesin fiyat üretmez? Spread ve slippage içerir.
- FX dry-run fixture provider ne işe yarar? Gerçek API çağırmadan sahte veriyle testi sağlar.
- FX official API placeholder neden gerçek API çağrısı değildir? Yalnızca contract ve adapter arayüzü sunar.
- FX licensed provider placeholder neden credential istemez? Çünkü no-scraping ve offline test boundary altındadır.
- no-scraping FX provider preference nasıl uygulanır? Profil özellikleriyle varsayılan yapılır.
- credential output neden yasaktır? Güvenlik (secrets hygiene) gereği.
"""
    if "Phase 107 FX Configuration" not in content:
        content += "\n" + addition
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def update_safe_usage():
    path = "docs/SAFE_USAGE_GUIDE.md"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    addition = """
## Phase 107 FX Provider Safety
- FX katmanında scraping yapılmadığı kesindir.
- HTML scraping/browser automation/paywall bypass/hidden API reverse engineering/rate abuse yasaktır.
- FX provider placeholder'ın gerçek API çağrısı olmadığı ve sinyal üretmediği kesindir.
- FX provider request'in yatırım tavsiyesi veya broker talimatı olmadığı bilinmelidir.
- FX pair registry'nin sinyal olmadığı belirtilir.
- Credential yazdırılmayacağı kurallara bağlıdır.
- Canlı trading/deployment sınırlarının devam ettiği unutulmamalıdır.
"""
    if "Phase 107 FX Provider Safety" not in content:
        content += "\n" + addition
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

update_readme()
update_roadmap()
update_phase_log()
update_arch()
update_config_doc()
update_safe_usage()
