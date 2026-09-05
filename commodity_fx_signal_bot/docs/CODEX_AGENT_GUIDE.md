<!-- AUTO-GENERATED SECTION START -->
# Codex Agent Kılavuzu (Codex Agent Guide)

> **UYARI / YASAL BİLDİRİM**
> Bu doküman ve açıklanan sistem yalnızca **offline/local araştırma platformu** kullanımını açıklar.
> Bu proje bir canlı alım-satım botu değildir. Gerçek emir göndermez, canlı sinyal üretmez, broker talimatı vermez ve gerçek pozisyon yönetmez.
> Model deployment, production scheduler veya otomatik trade özellikleri içermez.
> Bu projede üretilen hiçbir rapor veya sinyal **yatırım tavsiyesi değildir**.
> Eğitim, araştırma ve kağıt üzerinde test (paper trading) amacıyla geliştirilmiştir.


## Amaç
Yapay zeka asistanlarının (Codex vb.) kod tabanını anlarken, refactor ederken veya dokümante ederken uyması gereken katı kuralları tanımlar.

## Kapsam
Yapay zeka ile kod geliştirme prosedürleri, `AGENTS.md` kurallarına uyum ve güvenlik bariyerleri.


## Güvenlik Sınırları (Safety Boundaries)

Sistemin tasarımı gereği aşılmaması gereken sınırlar:
1. **Canlı Emir Yasağı:** Sistem broker API'lerine emir gönderecek kod içermez.
2. **Yatırım Tavsiyesi Yoktur:** Üretilen kararlar kesinlik bildirmez, araştırma hipotezidir.
3. **Daemon/Cron Yasağı:** Sistem sonsuz döngüde veya arka planda sessizce çalışacak şekilde tasarlanmamıştır. Manuel veya kontrollü script execution gerektirir.
4. **Web Dashboard Yok:** Dışarıya açık web sunucusu (Streamlit, Flask vb.) barındırmaz.
5. **Scraping Yasağı:** Selenium, Playwright veya BeautifulSoup ile veri kazıma işlemi yapmaz; sadece resmi/ücretsiz veri API'lerini kullanır.



## Local Timeline ve Change History (Phase 67)
- **Local Timeline Limits**: Local timeline engine Git geçmişi veya resmi audit trail değildir.
- **Kesinlikle Yasaktır**: Cloud event service bağlantısı yapmak, timeline üzerinden canlı broker eventleri izlemek, production monitoring kurmak, veya export edilen timeline'ı trading journal olarak okumak yasaktır.
- Timeline sadece proje artifactlerindeki değişimi ve dosyaların freshness oranını offline kontrol etmek içindir.

## Kullanım Örnekleri
- Yeni modül eklemeden önce mimari uyumluluk kontrolü.
- Hata ayıklarken sistem günlüklerinin okunması.

## Üretilen Çıktılar
- Yamanmış (patched) dosyalar.
- Geliştirilmiş dokümantasyon.


## Kapsam Dışı (Out of Scope)

Aşağıdaki özellikler kasıtlı olarak sisteme **dahil edilmemiştir**:
- Gerçek para ile işlem (Live Trading)
- Otonom (kendi kendine çalışan) üretim dağıtımı (Production Deployment)
- Otomatik alım-satım onayları (Auto Trade Approvals)
- Kar garantisi veya riskten arındırılmış getiri iddiaları


## Sık Hatalar
- Live trading yeteneği eklemeye çalışmak.
- Arka planda çalışan (daemon) süreçler önermek.
- HTML scraping araçları (Selenium vb.) kurmaya çalışmak.

## İlgili Komutlar
- `cat AGENTS.md`

## İlgili Klasörler
- Tüm proje dizini.

## Uyarılar
AI Ajanları her zaman kullanıcının "canlı işlem yapılmayacak" talimatına itaat etmelidir.

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

## Local Long-Term Operations
- **Long-term operations binder nasıl okunur?** Bu belge lokal bakım işlemlerinin bir provasıdır.
- **Review calendars nasıl yorumlanır?** Sadece manuel hatırlatma ve inceleme önerileridir, entegre takvim değildir.
- **Lifecycle maintenance workbook neden official lifecycle policy değildir?** Offline/local bir projedir ve regülatif bağlayıcılığı yoktur.
- **Deprecation rehearsal neden gerçek kaldırma/migration değildir?** Dosya silinmez, taşınmaz, değiştirilmez; sadece raporlanır.
- **v1.x roadmap governance neden official roadmap commitment değildir?** Planlama provasıdır, kesin sürüm garantisi sunmaz.
- **Feature intake ve change-control rehearsal nasıl kullanılır?** Sistemin gelişimini lokal bağlamda teorik olarak denetlemek için kullanılır.
- **ÖNEMLİ:** Gerçek operations plan, package publish, Docker push, Git tag, cloud upload, deployment, legal/compliance sign-off, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.

## Local Project Completion
- System closure dossier nasıl okunur? -> Sadece rehearsal.
- Terminal handoff pack nasıl kullanılır? -> Gerçek devir değildir.
- Knowledge freeze rehearsal neden gerçek freeze/git tag değildir? -> Offline dokümantasyon snapshottır.
- Last-mile audit binder neden official audit değildir? -> Sadece local proof.
- Completion readiness packet neden production approval değildir? -> Gerçek sign-off içermez.
- Final handoff checklistleri nasıl yorumlanır? -> Rehearsal only.
- Gerçek project closure, official completion approval, package publish, Docker push, Git tag, cloud upload, deployment, legal/compliance sign-off, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.


## Local Post-Completion Preservation
- **Archive seal rehearsal nasıl okunur?**: data/lake/local_post_completion_preservation/archive_seal/ altındaki rehearsal raporu incelenir. Bu dosya gerçek seal değildir.
- **Immutable README rehearsal neden gerçek immutable lock değildir?**: Hiçbir chmod, file lock uygulanmaz; sadece deneme amaçlı okuma dosyasıdır.
- **Evidence vault index nasıl yorumlanır?**: Projedeki kritik verilerin listesidir, ancak legal/audit bir evidence vault değildir.
- **Final knowledge capsule nasıl kullanılır?**: Projenin genel durumunu ve kritik okuma noktalarını sunar; official freeze değildir.
- **Preservation binder neden official preservation policy değildir?**: Offline/local deneme amaçlı bir dosya olup, gerçek policy onayı içermez.
- **Fingerprint rehearsal neden official artifact seal değildir?**: Kriptografik hash'ler üretir ancak legal signoff eksiktir.
- **ÖNEMLİ**: Gerçek archive seal, chmod, Git tag, release publish, package publish, deployment, legal/compliance sign-off, canlı emir, broker execution ve yatırım tavsiyesi yoktur!


## Local Project Atlas (Phase 93)
- Meta-index, projenin okunabilir listesidir, official knowledge index değildir.
- Universal navigation map, başlangıç noktalarını gösterir, official SOP değildir.
- Cross-phase lookup engine, klasör içi anahtar kelime eşleştirmesidir, enterprise search değildir.
- Offline semantic table of contents, başlıkların statik hiyerarşisidir, vector/embedding search değildir.
- Terminal project atlas projenin haritasıdır.
- Gerçek cloud index, vector DB, embedding API, external LLM, package publish, deployment, canlı emir, broker execution ve yatırım tavsiyesi yoktur.

## Local Review Governance
- **Human-review cockpit:** Sadece text/markdown tabanli offline review aracidir, gercek bir dashboard veya GUI/TUI degildir.
- **Manual approval ledger:** Gercek bir approval workflow, e-signature veya sign-off sistemi degildir; rehearsal amacli uretilmistir.
- **Expert review workbook:** Sadece offline dokumantasyon uretir, resmi expert sign-off, legal approval veya compliance onayi vermez.
- **Offline reviewer console:** Sadece komut/rapor ciktilarini listeler, bir konsol uzerinden islem calistirmaz, dashboard degildir.
- **Review governance binder:** Legal/compliance/production approval icermez, yatırım tavsiyesi verilmez.
- Hicbir sekilde package publish, deployment, Docker push, Git tag, bulut yukleme, canli emir, broker execution desteklenmez ve yatirim tavsiyesi degildir.

## Local Distribution Packaging
- Distribution bundle rehearsal nasil okunur? 
- Portable docs bundle nasil kullanilir?
- Offline release folder manifest neden gercek release degildir?
- Terminal handover ZIP-map neden gercek ZIP/archive uretmez?
- Packaging governance binder nasil yorumlanir?
- Inclusion/exclusion matrices ve source/output/command maps nasil okunur?
- Gercek ZIP/archive, installer, binary artifact, package publish, deployment, canli emir, broker execution ve yatirim tavsiyesi olmadigi acik yazilsin.
