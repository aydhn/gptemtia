<!-- AUTO-GENERATED SECTION START -->
# Operatör El Kitabı (Operator Manual)

> **UYARI / YASAL BİLDİRİM**
> Bu doküman ve açıklanan sistem yalnızca **offline/local araştırma platformu** kullanımını açıklar.
> Bu proje bir canlı alım-satım botu değildir. Gerçek emir göndermez, canlı sinyal üretmez, broker talimatı vermez ve gerçek pozisyon yönetmez.
> Model deployment, production scheduler veya otomatik trade özellikleri içermez.
> Bu projede üretilen hiçbir rapor veya sinyal **yatırım tavsiyesi değildir**.
> Eğitim, araştırma ve kağıt üzerinde test (paper trading) amacıyla geliştirilmiştir.


## Amaç
Bu kılavuz, sistemi çalıştıran, bakımını yapan ve rutin görevleri (veri güncelleme, raporlama, log takibi) yürüten teknik operatörler içindir.

## Kapsam
Veri pipeline'ı, hata ayıklama (troubleshooting), log yönetimi, sistem sağlığı kontrolleri ve Command Center kullanımı.


## Güvenlik Sınırları (Safety Boundaries)

Sistemin tasarımı gereği aşılmaması gereken sınırlar:
1. **Canlı Emir Yasağı:** Sistem broker API'lerine emir gönderecek kod içermez.
2. **Yatırım Tavsiyesi Yoktur:** Üretilen kararlar kesinlik bildirmez, araştırma hipotezidir.
3. **Daemon/Cron Yasağı:** Sistem sonsuz döngüde veya arka planda sessizce çalışacak şekilde tasarlanmamıştır. Manuel veya kontrollü script execution gerektirir.
4. **Web Dashboard Yok:** Dışarıya açık web sunucusu (Streamlit, Flask vb.) barındırmaz.
5. **Scraping Yasağı:** Selenium, Playwright veya BeautifulSoup ile veri kazıma işlemi yapmaz; sadece resmi/ücretsiz veri API'lerini kullanır.



## Local Timeline ve Change History (Phase 67)
- **Project event registry nasıl okunur?**: `reports/output/local_timeline/markdown/project_event_registry_report.md` dosyası, proje genelindeki dosya değişikliklerini kronolojik bir bakışla sunar. Gerçek zamanlı bir production monitoring aracı değil, sadece bir snapshot'tır.
- **Phase chronology ne yapar/ne yapmaz?**: Phase bazlı event sayısını çıkarır. Biten fazların tam mükemmelliğini garantilemez.
- **Artifact evolution nasıl yorumlanır?**: Sistemdeki dosyaların yenilik (freshness) durumunu gösterir. "Stale" artifact bir hata değil, manuel gözden geçirme uyarısıdır.
- **Cloud event service, broker event, canlı emir, yatırım tavsiyesi ve production monitoring** işlevleri bulunmaz.

## Kullanım Örnekleri
- `make dx` ile developer experience toollarını çalıştırma.
- Sağlık durumunu kontrol etme (`run_system_healthcheck.py`).

## Üretilen Çıktılar
- Observability metrikleri
- DataLake manifestoları


## Kapsam Dışı (Out of Scope)

Aşağıdaki özellikler kasıtlı olarak sisteme **dahil edilmemiştir**:
- Gerçek para ile işlem (Live Trading)
- Otonom (kendi kendine çalışan) üretim dağıtımı (Production Deployment)
- Otomatik alım-satım onayları (Auto Trade Approvals)
- Kar garantisi veya riskten arındırılmış getiri iddiaları


## Sık Hatalar
- Disk dolması nedeniyle DataLake hataları.
- API limitlerine (rate limit) takılma.

## İlgili Komutlar
- `python -m scripts.run_system_healthcheck`
- `python -m scripts.run_observability_status`

## İlgili Klasörler
- `logs/`
- `data/lake/`

## Uyarılar
Sistemi üretim ortamı gibi değil, bir laboratuvar ortamı gibi yönetin.

<!-- AUTO-GENERATED SECTION END -->



## Controlled Scenarios and Demos

To safely explore the system's capabilities without using real data or issuing real trades, you can run offline scenarios:
- **Generate Synthetic Data**: `python -m scripts.run_sample_data_builder`
- **View Scenarios**: `python -m scripts.run_scenario_registry_report`
- **Follow Demo Workflows**: `python -m scripts.run_demo_workflow_report`
- **Simulate Execution**: `python -m scripts.run_scenario_dry_run`
- **Read Case Studies**: `python -m scripts.run_case_study_report`

**IMPORTANT**: These tools do NOT perform live trading, broker integrations, or produce investment advice. They only simulate the offline research workflow.


### Scenario Regression & Replay (Phase 57)
- **Golden Output:** Sadece synthetic/offline datalardan üretilen test beklentisidir. Kesinlikle gerçek piyasa performansı veya referansı değildir.
- **Snapshot Comparison:** Çıktıların zamana veya versiyona göre değişip değişmediğini kontrol eder. Snapshot farklılıkları bir yatırım sinyali veya trading stratejisi değildir.
- **Deterministic Replay:** Sadece sentetik fixutre üzerinde kurulu deterministik bir test ortamıdır. Gerçek piyasa olaylarını doğrulamaz.
- **Demo Acceptance:** Çıktıların belirli kurallara (örn. no-live-trading kuralı) uyduğunu offline olarak doğrular. Production acceptance değildir.
- **Regression Failure:** Sadece test ortamındaki veya pipeline çıktılarındaki yapısal bozulmaları gösterir, yatırım veya portföy riski değildir.


### Local Analyst UX & Operator Productivity (Phase 58)
- **Command Aliases:** How to read aliases (`alias_name` maps to a safe offline `command`).
- **Safe Command Suggestions:** When you ask "how to check status", the system suggests offline commands. These are NEVER executed automatically.
- **Natural Language Mapping:** Queries map to local offline documentation and runbooks. No web search is performed.
- **Prompt Packs:** Pre-packaged safe instructions to give to Codex agents.
- **Task Board:** An offline checklist of pending system validations. NOT a trading or investment task board.
- **Safety:** It is strictly prohibited to execute live trades, broker commands, real portfolio actions, or receive investment advice via these tools.


## Report Summarization
Sistem offline araştırma süreçlerinden elde edilen bulguları özetler:
- **Executive Summary:** Yatırım kararı özeti değildir. Offline kalite durumunu aktarır.
- **Analyst Brief:** Gerçek piyasa sinyali değildir. Odaklanılması gereken modülleri öne çıkarır.
- **Weekly Offline Review:** Piyasa strateji raporu değildir. Proje durum özetidir.
- **Symbol Brief:** AL/SAT üretmez, tavsiye barındırmaz.
- **Follow-up Tasks:** Safe/offline görevleridir. Kesinlikle live komut içermezler.
Bu katman harici LLM kullanmaz ve sadece local rule-based özetleme yapar.

## Portable Packaging
Environment snapshot, requirements export ve install verification işlemleri için Phase 61 scriptlerini kullanın (örn. `run_environment_snapshot.py`, `run_portable_bundle_manifest.py`). Package publish, Docker deploy, cloud deploy, canlı trading ve broker execution KESİNLİKLE YOKTUR.

## Backup/Recovery Dry-Run and Disaster Recovery
- **Project state inventory**: Taranarak proje dosyalarının scope/policy sınıflandırmasını üretir. `python -m scripts.run_project_state_inventory` ile çağrılabilir.
- **Backup manifest**: Politikaları uygulayıp nelerin dahil/hariç edildiğini (ve manifest-only) gösteren referans dosyadır, dosya kopyalamaz.
- **Restore dry-run**: Manifest tabanlı olarak restore adımlarını (ve overwrite uyarılarını) raporlar, dosya değiştirmez/silmez.
- **Disaster recovery manifest**: Offline projeyi yeniden kurma hedeflerini (RPO/RTO) ve planlarını gösterir, production cloud backup onayı değildir.
- **Restore verification**: Kurtarma dry-run planındaki güvenlik (secret protection) ve uyumluluk kontrollerini doğrular.
- **Secrets exclusion**: Her durumda `.env`, `secret` vb dosyalar otomatik exclude edilir, içerikleri okunmaz.
- **Data/report manifest-only**: Büyük klasörler default olarak "manifest-only" dahil edilir (hashlenmez veya kopyalanmaz).
- **Gerçek restore/overwrite/cloud backup olmadığı açık yazılsın**: Backup Recovery tool'ları yalnızca dry-run raporlar üretmek ve sistemin recovery readiness'ını değerlendirmek (audit) içindir. Canlı deploy veya real overwrite için kullanılmaz.

## Evidence Governance and Audit Binder
Projedeki tüm safety, backup, packaging ve quality çıktılarını bir denetim paketinde toplamak için Phase 64 scriptlerini kullanın (örn. `run_audit_evidence_binder.py`, `run_evidence_traceability_matrix.py`). Policy/control mappingleri, traceability matrixleri ve evidence score'ları resmi/hukuki bir uyum sertifikasyonu (SOC2, ISO vb.) teşkil etmez, tamamen offline/local denetlenebilirlik amacını taşır.

## Artifact Metadata
Model card okuma rehberi, dataset card kullanim amaci, non-use policy onemi. Canli emir, broker execution, yatirim tavsiyesi, resmi sertifika ve deployment olmadigi acik yazilsin.

## Local Knowledge Graph (Phase 66)
- **Node/Edge Registry**: Lists all extracted artifacts and their relationships. Use to understand how components link together offline.
- **Artifact Relationship Graph**: Maps dependencies without external cloud/DB usage. Does not execute code.
- **Relationship Query**: Use for searching internal linkages (e.g. which report relates to which policy). Cannot generate investment advice or live commands.
- **Semantic Keyword/TF-IDF Index**: Local text index only. External vector DBs are strictly disabled.
- **Graph Centrality**: Purely structural metric. Does not denote investment opportunity or trading significance.
- **Graph Gap/Orphan/Stale Report**: Useful for internal consistency audits. Not an indicator of live market risks.
- **Notice**: No live trading, broker execution, external vector DB, cloud upload, or investment advice is provided by the Knowledge Graph tools.

### Local Consistency Engine Guide
- **Consistency check registry**: Tüm config, docs, reports, metadata, timeline vb. arasındaki kuralları listeler.
- **Cross-layer consistency matrix**: Farklı proje katmanları arasındaki uyumun snapshot'ını verir.
- **Contradiction detection**: Metinlerde "canlı emir yok" ile "canlı trade" gibi çelişen ifadeleri tespit eder.
- **Missing/broken reference report**: Bozuk yolları ve bulunamayan referansları raporlar.
- **Stale reconciliation plan**: Auto-fix değildir. Zamanı geçmiş artifactlar için manuel düzeltme tavsiyeleri verir.
- **System coherence score**: Production readiness veya canlı sistem onayı değildir. Offline projenin uyumunu yansıtır.
ÖNEMLİ: Canlı emir, broker execution, otomatik düzeltme, cloud upload ve yatırım tavsiyesi yeteneği YOKTUR.
