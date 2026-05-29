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
