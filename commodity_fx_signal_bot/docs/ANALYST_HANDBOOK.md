<!-- AUTO-GENERATED SECTION START -->
# Analist El Kitabı (Analyst Handbook)

> **UYARI / YASAL BİLDİRİM**
> Bu doküman ve açıklanan sistem yalnızca **offline/local araştırma platformu** kullanımını açıklar.
> Bu proje bir canlı alım-satım botu değildir. Gerçek emir göndermez, canlı sinyal üretmez, broker talimatı vermez ve gerçek pozisyon yönetmez.
> Model deployment, production scheduler veya otomatik trade özellikleri içermez.
> Bu projede üretilen hiçbir rapor veya sinyal **yatırım tavsiyesi değildir**.
> Eğitim, araştırma ve kağıt üzerinde test (paper trading) amacıyla geliştirilmiştir.


## Amaç
Bu kılavuz, üretilen finansal sinyal adaylarını, rejim raporlarını ve korelasyon matrislerini inceleyen analistler içindir.

## Kapsam
Modellerin, rejim filtrelerinin, sentetik endekslerin ve faktör araştırmalarının metodolojisi ve nasıl yorumlanacağı.


## Güvenlik Sınırları (Safety Boundaries)

Sistemin tasarımı gereği aşılmaması gereken sınırlar:
1. **Canlı Emir Yasağı:** Sistem broker API'lerine emir gönderecek kod içermez.
2. **Yatırım Tavsiyesi Yoktur:** Üretilen kararlar kesinlik bildirmez, araştırma hipotezidir.
3. **Daemon/Cron Yasağı:** Sistem sonsuz döngüde veya arka planda sessizce çalışacak şekilde tasarlanmamıştır. Manuel veya kontrollü script execution gerektirir.
4. **Web Dashboard Yok:** Dışarıya açık web sunucusu (Streamlit, Flask vb.) barındırmaz.
5. **Scraping Yasağı:** Selenium, Playwright veya BeautifulSoup ile veri kazıma işlemi yapmaz; sadece resmi/ücretsiz veri API'lerini kullanır.



## Local Timeline ve Change History (Phase 67)
- **Change history digest neden trading journal değildir?**: Bu sistem proje dosyalarındaki değişiklikleri listeler; gerçek piyasa emirlerini veya işlem kayıtlarını (trade journal) listelemez.
- **Timeline query nasıl kullanılır?**: `python -m scripts.run_timeline_query --query "Phase 60 sonrası hangi çıktılar oluştu?"` komutuyla offline timeline arayüzüne soru sorabilirsiniz. Yatırım tavsiyesi veya işlem sorgusu kabul edilmez.
- **Stale artifact warning nasıl okunur?**: Bir doküman veya rapor uzun süredir güncellenmediyse uyarılır. Modeller için bu, yeniden eğitim ihtiyacını düşündürebilir ancak otomatik aksiyon almaz.
- **Cloud event service, broker event, canlı emir, yatırım tavsiyesi ve production monitoring** işlevleri bulunmaz.

## Kullanım Örnekleri
- Backtest sonuçlarının (Sharpe, Max Drawdown) incelenmesi.
- Feature önem sırasının (feature importance) değerlendirilmesi.

## Üretilen Çıktılar
- Performans metrikleri
- ML model değerlendirme raporları


## Kapsam Dışı (Out of Scope)

Aşağıdaki özellikler kasıtlı olarak sisteme **dahil edilmemiştir**:
- Gerçek para ile işlem (Live Trading)
- Otonom (kendi kendine çalışan) üretim dağıtımı (Production Deployment)
- Otomatik alım-satım onayları (Auto Trade Approvals)
- Kar garantisi veya riskten arındırılmış getiri iddiaları


## Sık Hatalar
- Overfitting (aşırı öğrenme) ihtimalinin göz ardı edilmesi.
- Sinyal adaylarının kesin "AL/SAT" emri olarak yorumlanması.

## İlgili Komutlar
- `python -m scripts.run_backtest_report`
- `python -m scripts.run_model_evaluation`

## İlgili Klasörler
- `reports/output/ml/`
- `reports/output/backtest/`

## Uyarılar
Sinyal adayları kesin karar değildir; bir sonraki analiz katmanı için girdidir.

<!-- AUTO-GENERATED SECTION END -->


## Report Summarization
Sistem offline araştırma süreçlerinden elde edilen bulguları özetler:
- **Executive Summary:** Yatırım kararı özeti değildir. Offline kalite durumunu aktarır.
- **Analyst Brief:** Gerçek piyasa sinyali değildir. Odaklanılması gereken modülleri öne çıkarır.
- **Weekly Offline Review:** Piyasa strateji raporu değildir. Proje durum özetidir.
- **Symbol Brief:** AL/SAT üretmez, tavsiye barındırmaz.
- **Follow-up Tasks:** Safe/offline görevleridir. Kesinlikle live komut içermezler.
Bu katman harici LLM kullanmaz ve sadece local rule-based özetleme yapar.

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

## Local Readiness

- Readiness gate production release onayi degildir.
- Safe-go/no-go manuel inceleme amaclidir, canli sinyal uretmez.
- Final operator checklist sadece local dry-run plani sunar.
- Handoff manifest resmi compliance sign-off degildir.
- Kesinlikle canli emir, broker execution, deployment, package publish ve yatirim tavsiyesi icermez.

## Local Maintenance Overview

The local maintenance module is available to help evaluate project sustainability.

- **Maintenance domain registry:** Lists all managed parts of the offline infrastructure.
- **Periodic review calendar:** Gives manual hints for reviewing outputs. It is **NOT** a scheduler.
- **Refresh cadence:** Recommended manual refresh schedules.
- **Dependency aging watch:** Local-only scan (no internet connection) for missing metadata and stale files. Does **NOT** auto-upgrade.
- **Manual review queue:** Summarizes tasks and artifacts that require human review.
- **Sustainability score:** A local metric for project health. It is **NOT** an official SLA.
- **Maintenance runbook:** Documentation on how to operate offline checks, **NOT** automatic operations.
- **DISCLAIMER:** No live orders, no broker executions, no deployment scripts, no auto-upgrades, no cloud uploads, and absolutely no investment advice is generated by this module.

### Local Archive Strategy & Preservation Layer (Phase 71)
- **Archive domain registry nasıl okunur?**: Tüm dosyalar çeşitli local retention domain'lere bölünür.
- **Snapshot catalog ne yapar/ne yapmaz?**: Cloud snapshot değildir, local file inventory'dir.
- **Cold storage manifest neden cloud backup değildir?**: Dosya yüklemez veya taşımaz, operatöre offline USB/drive'a neleri atması gerektiğini gösterir.
- **Retention policy neden resmi compliance değildir?**: Otomatik veri silmez, sadece tavsiye verir.
- **Integrity verification plan nasıl kullanılır?**: Geri yükleme tatbikatında dosyaların bozulup bozulmadığını kontrol eder.
- **Secret exclusion verification nasıl yorumlanır?**: .env gibi dosyaların arşivde HİÇ olmamasını denetler.
- **Preservation binder ne işe yarar?**: Sistemin 5-10 yıl boyunca tekrar ayağa kalkabilmesi için operatöre manual yönergeler veren kitaptır.
- **DİKKAT**: Sistemde cloud upload, auto archive, dosya taşıma/silme, canlı emir, broker execution, deployment ve yatırım tavsiyesi YOKTUR.
\n\n
## Local Disaster-Recovery Tabletop and Restore Drill Simulation

### Nasıl Okunur ve Yorumlanır?
- **DR domain registry**: Sistemin test edilebilir DR alanlarını listeler.
- **Tabletop scenario**: Masa başı tatbikat senaryolarıdır. Gerçek bir incident değildir.
- **Restore drill simulation**: Sadece dosyaların ve kayıtların varlığını kontrol eder, **kesinlikle gerçek bir restore işlemi yapmaz**.
- **Failure-mode playbook**: Olası hatalarda uygulanacak adımları içerir, yıkıcı komut (destructive command) içermez.
- **Recovery command plan**: Sadece okunabilir, durum kontrolü yapan komutları önerir, otomasyon veya kurtarma yapmaz.
- **Resilience score**: Sistemin dayanıklılık tatbikatı skorudur, resmi bir SLA veya recovery garantisi **değildir**.
- **Secret boundary rehearsal**: Şifre veya API key sızıntılarını sadece "var/yok" veya "maskeli" olarak simüle eder, kesinlikle raw secret göstermez veya kaydetmez.

> **ÖNEMLİ UYARI:** 
> Bu araçlar gerçek restore, gerçek backup, cloud DR, auto recovery, dosya taşıma/silme, canlı emir, broker execution, deployment ve yatırım tavsiyesi **İÇERMEZ**.

## Local Training and Onboarding

- **Onboarding Paths:** Hangi rolün hangi konularda eğitim alacağını belirtir.
- **Training Packs:** Operatör, analist ve developer için detaylı kılavuzlar.
- **Guided Walkthrough:** Adım adım çevrimdışı rehberler, read-only/manual öğrenme adımları sağlar.
- **Safe Command Lessons:** Sadece okuma veya dry-run komutlarını öğretir, canlı/broker/deploy/destructive komut içermez.
- **Non-use Policy Training:** Yapılmaması gereken eylemleri net bir şekilde sınırlar.
- **Handover Binder:** Proje devri için tüm gerekli belgeleri ve checklistleri içerir.
- **Training Assessment:** Dry-run olarak bilginizi sınar, resmi bir sertifika değildir.

> **UYARI**: Bu modül canlı emir, broker execution, deployment, yatırım tavsiyesi, cloud upload veya resmi sertifika onaylarını İÇERMEZ. Sistem offline knowledge-transfer aracıdır.

### Local Briefing
- Executive summary pack nasil okunur?
- Non-technical briefing deck source ne yapar/ne yapmaz?
- Decision-context binder nasil kullanilir?
- Safe communication guide neden onemlidir?
- Stakeholder templates nasil kullanilmali?
- Communication risks nasil yorumlanir?
- Yatirim tavsiyesi, canli emir, broker execution, deployment, production release ve resmi karar olmadigi acik yazilsin.

## Local Synthesis (Phase 75)
- **Master index nasıl okunur?** Sadece readonly dosya indeksleridir.
- **Cross-phase final map ne yapar/ne yapmaz?** Bağımlılıkları gösterir, canlı sistem onayı değildir.
- **Project completion dossier nasıl kullanılmalı?** Çevrimdışı ve dokümantasyon amaçlıdır.
- **Final navigation guides nasıl okunmalı?** Sadece yönlendirme sağlar, çalıştırılabilir işlem içermez.
- **Final no-go/safe-go summary neden canlı işlem izni değildir?** Offline kontrol sağlar, canlı işlem izni veremez.
- **Final synthesis quality report nasıl yorumlanır?** Proje kalitesini gösterir, yatırım tavsiyesi değildir.
*Not: Bu sistemde yatırım tavsiyesi, canlı emir, broker execution, deployment, production release, resmi completion ve compliance yoktur.*

## Local Hardening
- Dead-code candidate raporu yalnizca adaylari gosterir, silme veya refactor yapmaz.
- Contract freeze catalog resmi API/SLA veya guarantee degildir.
- Documentation freeze snapshot dokumanlari kitlemez, snapshot uretir.
- RC dry-run freeze gercek release candidate degildir, yalnizca hazirlik dry-run idir.
- RC command plan komutlari otomatik calistirmaz, execution plani gosterir.
- Final freeze quality report official compliance veya production release onayi degildir.
- Sistemde production release, package publish, deployment, canli emir, broker execution, otomatik refactor ve yatirim tavsiyesi **yoktur**.

## Local Acceptance
- Final acceptance simulation nasıl okunur? Checklist olarak.
- Independent reviewer pack ne yapar/ne yapmaz? Prova yapar, sertifika vermez.
- Evidence trail nasıl yorumlanır? Local dosya listesi olarak.
- Sign-off rehearsal neden resmi sign-off değildir? Çünkü offline/lokal bir simülasyondur.
- Acceptance readiness score neden production release değildir? Sadece teknik hazırbulunuşluk ölçer.
- No-go/safe-go summary neden canlı işlem izni değildir? Yatırım kararı veya model onayı değildir.
- Resmi audit, compliance, production release, canlı emir, broker execution, deployment ve yatırım tavsiyesi OLMADIĞI AÇIKÇA BİLİNMELİDİR.

### Local Delivery Rehearsal
- Final delivery bundle manifest nasıl okunur? It is a JSON/CSV manifest, no real files are packaged.
- Handoff package index ne yapar/ne yapmaz? Indexes available files for review. Does not move them.
- Portable reviewer archive guide nasıl kullanılır? Provides a sequence for local code review.
- Final local transfer checklist neden resmi teslim onayı değildir? Because it operates strictly locally in dry-run mode.
- Delivery rehearsal binder nasıl yorumlanır? A summary text document of the rehearsal.
- Delivery readiness score neden production handoff değildir? Because no real transfer or deployment is made.
Gerçek transfer, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi yoktur.
\n\n### Local Archival Guidelines
- **Final archival seal rehearsal** nasıl okunur? It's a dry-run local documentation, not a legal seal.
- **Hash catalog ve hash-of-hashes catalog** ne yapar/ne yapmaz? They document state, but do not provide blockchain/timestamp notarization.
- **Local provenance lockfile** neden hukuki lockfile değildir? No legal guarantees or immutable storage.
- **Sensitive file exclusion registry** nasıl yorumlanır? Lists excluded files, doesn't print raw secrets.
- **Custody rehearsal** neden gerçek chain-of-custody değildir? It's a simulation, no legal handoff.
- **Archival readiness score** neden compliance/legal approval değildir? It's purely an internal dry-run readiness metric.
- Immutable lock, chmod, cloud archive, blockchain notarization, legal hold, package publish, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.

### Local Closure Notes (Phase 80)
- Final meta-review `local_closure` klasörü altından okunur.
- Lessons-learned compendium denetim sertifikası değildir.
- Future roadmap backlog implementasyon onayı değildir.
- v1.0 local closure dossier gerçek bir sürüm (release) değildir.
- Closure readiness score production onayı (approval) değildir.
- Handoff-aftercare guide canlı destek anlamına gelmez.
- Gerçek v1 release, production release, official closure, compliance, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.

### Local Reuse
- **Final audit-memory pack nasıl okunur?**: data/lake/local_reuse altından JSON/CSV veya reports/output/local_reuse/markdown altından okunur.
- **Reusable template catalog ne yapar/ne yapmaz?**: Geçmiş mimarileri modeller, kesinlikle official engineering standard değildir.
- **Local knowledge reuse kit nasıl kullanılır?**: Yeni projeler için offline referans olarak. Implementation başlatmaz.
- **v1.1 planning seed neden implementation approval değildir?**: Çünkü sadece fikir/tohumdur. Canlıya alınmaz.
- **Future project starter pack neden yeni proje oluşturmaz?**: Çünkü auto-generation kodu yoktur, sadece dokümantasyondur.
- **Reuse readiness score neden production approval değildir?**: Çünkü production ortamını test etmez.

*Bu sistemde gerçek v1.1 implementation, production release, official standard, compliance, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.*

## Local Simplification (Phase 82)
- Final modular complexity map bir architecture assessment değildir. Sadece fikir verir.
- Optional slimming plan dry-run bir rehearsal'dır. Gerçek refactor yapmaz.
- Consolidation candidates otomatik refactor demek değildir, manuel inceleme gerektirir.
- Repo ergonomics guide okuma kolaylığı sağlamak içindir.
- Maintainability readiness score bir architecture approval değildir.
- Gerçek refactor, dosya silme/taşıma, cleanup execution, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi **yoktur**.
\n\n## Local Performance
- Final local performance budget nasil okunur? Budget dosyalarina bakin, gercek benchmark degildir.
- Lightweight runtime profile ne yapar? Hizli calisma modlarini listeler.
- Resource-footprint rehearsal gercek benchmark degildir.
- Maintenance cost estimate nasil yorumlanir? Gozden gecirme eforu olarak.
- Offline efficiency planning guide nasil kullanilir? Manuel optimizasyon icin.
- Retention/rotation rehberleri neden dosya silmez? Sadece tavsiyedir.
- Gercek benchmark, load/stress test, production profiling, cloud cost approval, canli emir, broker execution, deployment, yatirim performansi iddiasi ve yatirim tavsiyesi degildir.
## Local Usability Review and Operator Navigation
Phase 84:
- Final local usability review gerçek kullanıcı testi değildir.
- Operator friction map telemetry veya analytics değildir.
- Command discoverability guide komut çalıştırmaz.
- Documentation navigation assistant pack harici LLM/API değildir.
- Operator paths canlı operasyon prosedürü değildir.
- Human-in-the-loop checkpoint otomatik onay üretmez.
- Usability readiness score production usability approval değildir.
- Çıktılar data/lake/local_usability ve reports/output/local_usability altında oluşur.

Komutlar:
```bash
python -m scripts.run_usability_domain_registry
python -m scripts.run_final_local_usability_review
python -m scripts.run_command_discoverability_guide
python -m scripts.run_documentation_navigation_assistant
python -m scripts.run_operator_paths
python -m scripts.run_usability_quality_report
python -m scripts.run_usability_status
```

## Local Governance Control Room and Operator Supervision

- **Governance control room packet nasıl okunur?** Control room packet gerçek dashboard veya yönetim sistemi değildir, offline/local provadır.
- **Executive oversight packet nasıl yorumlanır?** Resmi yönetim raporu değildir.
- **Manual approval ledger neden gerçek onay değildir?** Local/offline manuel review provasıdır, onay ve sign-off içermez.
- **Risk committee rehearsal neden gerçek komite değildir?** Formalite ve gözetim adımlarının provasıdır.
- **Operator supervision guide nasıl kullanılır?** Offline dokümantasyon olarak okunur ve uygulanır.
- **Approval/non-approval boundaries nasıl korunur?** Gerçek onay alınmadan ve non-approval boundaries ihlal edilmeden uygulanır.

**ÖNEMLİ:** Gerçek yönetim kararı, compliance sign-off, production approval, canlı emir, broker execution, deployment ve yatırım tavsiyesi olmadığı açık yazılsın.
\n\n## Local Red-Team Rehearsal and Safety Assurance
- **How to read the red-team rehearsal packet?** It is a collection of dry-run safety boundary exercises to demonstrate the project's resilience to misuse.
- **How to interpret the misuse scenario library?** It catalogues theoretical abuse vectors in an abstract format. It does NOT contain real attack or exploit instructions.
- **Why is abuse-case simulation not a real attack?** It only records the expected refusal/boundary logic without actually executing malicious payloads against a live system.
- **Why is the adversarial prompt safety checklist not a jailbreak collection?** It is an abstract list of checks rather than operational payload inputs.
- **Why is the safety assurance summary not a certification?** It is an offline rehearsal report of system safety mechanisms, not an official compliance or production approval.
- **How to use the manual escalation checklist?** Use it to identify inputs that trigger a human review process for safety validation.
- **Disclaimer:** The outputs from this module DO NOT constitute real attacks, exploits, jailbreaks, credential exfiltration, telemetry, dashboard creation, live trading orders, broker execution, model deployment, or investment advice.
\n
## Local Incident Response
- Incident-response rehearsal packet nasıl okunur: Sadece mock offline rehearsal raporudur.
- Safety event register nasıl yorumlanır: Offline event taxonomy ve classification'ı içerir.
- Rollback decision playbook neden gerçek rollback değildir: Sistem konfigürasyonunu veya durumunu geri almaz, sadece onay gerektiren kural listesidir.
- Containment/degraded-mode/recovery rehearsal neden canlı sistemi değiştirmez: Bu playbooklar tamamen dry-run olarak çalışır.
- Post-incident review template nasıl kullanılır: Sadece geçmişe yönelik taslak çıkarır.
- Incident no-go/safe-go sınırları nasıl korunur: Kalite kontrolleri tarafından hard limit olarak izlenir.
- Uyarı: Gerçek incident response, forensic analiz, production recovery, canlı emir, broker execution, deployment ve yatırım tavsiyesi YOKTUR.
