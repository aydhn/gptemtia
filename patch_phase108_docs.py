import os
from pathlib import Path

def append_to_file(filepath: str, text: str, check_text: str):
    p = Path(filepath)
    if not p.exists(): return
    content = p.read_text(encoding="utf-8")
    if check_text not in content:
        p.write_text(content + "\n" + text, encoding="utf-8")
        print(f"Patched {filepath}")

def patch_readme():
    text = """
## Phase 108 Commodities Data Provider Layer

Phase 108, scraping yapmadan emtia veri sağlayıcı katmanını kurar.
Precious metals, energy, industrial metals ve agriculture emtia evreni oluşturulur.
XAU/XAG bu fazda commodity symbol olarak ele alınır, FX currency gibi ele alınmaz.
Commodity symbol normalization, spot/OHLCV schema, futures contract metadata, continuous contract requirements ve roll-adjustment requirements eklenir.
Bu faz gerçek commodity provider API entegrasyonu veya gerçek veri indirme fazı değildir.
Futures metadata placeholder gerçek futures execution altyapısı değildir.
Commodity dry-run fixture, manual file placeholder, local cache placeholder, official API placeholder ve licensed provider placeholder eklenir.
Phase 109 Macro Data Provider Layer geliştirmesi için temel bırakılır.
Final hedef hâlâ Phase 160’tır.
Canlı trading, broker/futures broker execution, yatırım tavsiyesi, deployment, scraping veya official approval yoktur.

Çalıştırma komutları:
```bash
python -m scripts.run_commodity_provider_profile_registry
python -m scripts.run_commodity_universe_registry
python -m scripts.run_commodity_provider_registry
python -m scripts.run_commodity_provider_contracts
python -m scripts.run_commodity_dry_run_fixture
python -m scripts.run_commodity_provider_health_check
python -m scripts.run_commodity_provider_quality_report
python -m scripts.run_commodity_provider_status
```
"""
    append_to_file("README.md", text, "Phase 108 Commodities Data Provider Layer")

def patch_roadmap():
    text = """
- 101-105 completed/foundation block ready
- 106 completed/Multi-Provider Data Abstraction ready
- 107 completed/FX Data Provider Layer ready
- 108 Commodities Data Provider Layer
- 109 Macro Data Provider Layer sıradaki faz
- 110 Economic Calendar Integration No Scraping
- 111 News Metadata Integration No Scraping
- 112 Data Quality Engine
- 113 Data Normalization Layer
- 114 Data Lineage and Provenance
- 115 Data Provider Benchmark Report
"""
    append_to_file("docs/ROADMAP.md", text, "108 Commodities Data Provider Layer")

def patch_phase_log():
    text = """
### Phase 108
- Commodity Provider Profile sistemi eklendi.
- Commodity provider domain registry eklendi.
- Commodity universe registry eklendi.
- Commodity category registry eklendi.
- Commodity metadata registry eklendi.
- Commodity symbol normalization map eklendi.
- Commodity spot/OHLCV schema contract eklendi.
- Futures contract metadata schema eklendi.
- Continuous contract requirement registry eklendi.
- Roll-adjustment requirement registry eklendi.
- Commodity provider capability/metadata registry eklendi.
- Commodity request/response/error schema eklendi.
- Commodity provider interface ve adapter contract eklendi.
- Commodity provider registry ve resolver eklendi.
- Commodity provider preference resolver eklendi.
- Commodity capability matcher eklendi.
- Commodity dry-run fixture provider eklendi.
- Commodity manual file, local cache, official API ve licensed placeholder’ları eklendi.
- Commodity output validation contract eklendi.
- Commodity safety boundary eklendi.
- Commodity health/readiness/validation/quality raporları eklendi.
- Phase 109 macro provider handoff raporu eklendi.
- Scraping yapılmayacağı sınırı commodities katmanında tekrar güçlendirildi.
"""
    append_to_file("docs/PHASE_LOG.md", text, "Commodity Provider Profile sistemi eklendi")

def patch_architecture():
    text = """
Phase 107 FX Data Provider Layer
→ Phase 108 Commodities Data Provider Layer
→ Commodity Provider Profile Registry
→ Commodity Universe Registry
→ Commodity Category Registry
→ Commodity Metadata
→ Commodity Symbol Normalization
→ Commodity Spot Schema
→ Commodity OHLCV Schema
→ Futures Contract Metadata
→ Continuous Contract Requirements
→ Roll Adjustment Requirements
→ Commodity Provider Capability Registry
→ Commodity Provider Metadata
→ Commodity Request/Response/Error Schema
→ BaseCommodityProvider Interface
→ Commodity Adapter Contract
→ Commodity Provider Registry
→ Commodity Provider Resolver
→ Commodity Dry-Run Fixture Provider
→ Commodity Placeholder Providers
→ Commodity Output Validation
→ Commodity Safety Boundary
→ Phase 109 Macro Data Provider Layer
"""
    append_to_file("docs/ARCHITECTURE.md", text, "Phase 108 Commodities Data Provider Layer")

def patch_configuration():
    text = """
### Phase 108 Commodities Configuration
- Commodity provider profile nasıl seçilir? `settings.py` içinden `default_commodity_provider_profile` ile.
- Commodity universe nasıl yorumlanır? Emtia evreni sinyal değil, tanım listesidir.
- Precious metals / energy / industrial metals / agriculture farkları `CommodityCategory` ile ayrılır.
- XAU/XAG neden FX currency değil commodity olarak tutulur? Çakışmaları önlemek için.
- Commodity symbol normalization nasıl çalışır? Provider-spesifik semboller canonical form'a (`XAU/USD` vs) döner.
- Commodity spot/OHLCV schema ne işe yarar? Çıktı standartlarını belirler.
- Futures contract metadata neden execution değildir? Yalnızca tanımlayıcıdır.
- Continuous contract requirements neden gerçek continuous seri üretmez? Sadece kuralları tanımlar (Phase 113 için).
- Roll-adjustment requirements neden sinyal değildir? Fiyat uyarlamasını tanımlar.
- Commodity dry-run fixture provider ne işe yarar? Gerçek API çağırmadan sistemi test etmeyi sağlar.
- Commodity official API placeholder neden gerçek API çağrısı değildir? Offline geliştirme içindir.
- Commodity licensed provider placeholder neden credential istemez? Güvenlik (no credential output) kuralı gereği.
- no-scraping commodity provider preference nasıl uygulanır? Provider resolver üzerinden uygulanır.
- credential output neden yasaktır? Secrets hygiene kuralı.
"""
    append_to_file("docs/CONFIGURATION.md", text, "Phase 108 Commodities Configuration")

def patch_safe_usage_guide():
    text = """
### Phase 108 Safe Usage
- Commodity katmanında scraping yapılmadığı garanti edilir.
- HTML scraping/browser automation/paywall bypass/hidden API reverse engineering/rate abuse yasaktır.
- Commodity provider placeholder’ın gerçek API çağrısı olmadığı teyit edilmiştir.
- Futures metadata placeholder’ın futures işlem sistemi olmadığı belirtilmiştir.
- Commodity provider request’in yatırım tavsiyesi veya broker/futures broker talimatı olmadığı sabittir.
- Commodity universe registry’nin sinyal olmadığı sabittir.
- Credential yazdırılmayacağı kurallara bağlıdır.
- Canlı trading/deployment sınırlarının devam ettiği onaylanmıştır.
"""
    append_to_file("docs/SAFE_USAGE_GUIDE.md", text, "Phase 108 Safe Usage")

if __name__ == "__main__":
    patch_readme()
    patch_roadmap()
    patch_phase_log()
    patch_architecture()
    patch_configuration()
    patch_safe_usage_guide()
    print("Docs patched.")
