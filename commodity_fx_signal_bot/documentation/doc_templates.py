def build_standard_disclaimer() -> str:
    return """
> **UYARI / YASAL BİLDİRİM**
> Bu doküman ve açıklanan sistem yalnızca **offline/local araştırma platformu** kullanımını açıklar.
> Bu proje bir canlı alım-satım botu değildir. Gerçek emir göndermez, canlı sinyal üretmez, broker talimatı vermez ve gerçek pozisyon yönetmez.
> Model deployment, production scheduler veya otomatik trade özellikleri içermez.
> Bu projede üretilen hiçbir rapor veya sinyal **yatırım tavsiyesi değildir**.
> Eğitim, araştırma ve kağıt üzerinde test (paper trading) amacıyla geliştirilmiştir.
"""

def build_safety_boundaries_section() -> str:
    return """
## Güvenlik Sınırları (Safety Boundaries)

Sistemin tasarımı gereği aşılmaması gereken sınırlar:
1. **Canlı Emir Yasağı:** Sistem broker API'lerine emir gönderecek kod içermez.
2. **Yatırım Tavsiyesi Yoktur:** Üretilen kararlar kesinlik bildirmez, araştırma hipotezidir.
3. **Daemon/Cron Yasağı:** Sistem sonsuz döngüde veya arka planda sessizce çalışacak şekilde tasarlanmamıştır. Manuel veya kontrollü script execution gerektirir.
4. **Web Dashboard Yok:** Dışarıya açık web sunucusu (Streamlit, Flask vb.) barındırmaz.
5. **Scraping Yasağı:** Selenium, Playwright veya BeautifulSoup ile veri kazıma işlemi yapmaz; sadece resmi/ücretsiz veri API'lerini kullanır.
"""

def build_common_not_in_scope_section() -> str:
    return """
## Kapsam Dışı (Out of Scope)

Aşağıdaki özellikler kasıtlı olarak sisteme **dahil edilmemiştir**:
- Gerçek para ile işlem (Live Trading)
- Otonom (kendi kendine çalışan) üretim dağıtımı (Production Deployment)
- Otomatik alım-satım onayları (Auto Trade Approvals)
- Kar garantisi veya riskten arındırılmış getiri iddiaları
"""

def build_user_guide_template() -> str:
    return f"""# Kullanıcı Kılavuzu (User Guide)
{build_standard_disclaimer()}

## Amaç
Bu kılavuz, Emtia-Döviz offline araştırma platformunun son kullanıcılar (araştırmacılar) tarafından temel düzeyde nasıl çalıştırılacağını ve raporların nasıl okunacağını açıklar.

## Kapsam
Sistemin kurulumu, konfigürasyonu, veri çekilmesi, raporların üretilmesi ve Telegram bildirimlerinin alınması adımlarını kapsar.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- Sistem durumunu kontrol etme
- Günlük araştırma döngüsünü çalıştırma
- Üretilen Markdown raporlarını okuma

## Üretilen Çıktılar
- `reports/output/` dizininde üretilen araştırma raporları.
- Telegram üzerinden alınan özet bildirimler.

{build_common_not_in_scope_section()}

## Sık Hatalar
- Yanlış dizinden çalıştırma
- Eksik `.env` ayarları

## İlgili Komutlar
- `make setup`
- `python main.py`

## İlgili Klasörler
- `reports/output/`
- `docs/`

## Uyarılar
Daima offline ortamda, paper-trading modunda çalıştığınızı unutmayın.
"""

def build_operator_manual_template() -> str:
    return f"""# Operatör El Kitabı (Operator Manual)
{build_standard_disclaimer()}

## Amaç
Bu kılavuz, sistemi çalıştıran, bakımını yapan ve rutin görevleri (veri güncelleme, raporlama, log takibi) yürüten teknik operatörler içindir.

## Kapsam
Veri pipeline'ı, hata ayıklama (troubleshooting), log yönetimi, sistem sağlığı kontrolleri ve Command Center kullanımı.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- `make dx` ile developer experience toollarını çalıştırma.
- Sağlık durumunu kontrol etme (`run_system_healthcheck.py`).

## Üretilen Çıktılar
- Observability metrikleri
- DataLake manifestoları

{build_common_not_in_scope_section()}

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
"""

def build_analyst_handbook_template() -> str:
    return f"""# Analist El Kitabı (Analyst Handbook)
{build_standard_disclaimer()}

## Amaç
Bu kılavuz, üretilen finansal sinyal adaylarını, rejim raporlarını ve korelasyon matrislerini inceleyen analistler içindir.

## Kapsam
Modellerin, rejim filtrelerinin, sentetik endekslerin ve faktör araştırmalarının metodolojisi ve nasıl yorumlanacağı.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- Backtest sonuçlarının (Sharpe, Max Drawdown) incelenmesi.
- Feature önem sırasının (feature importance) değerlendirilmesi.

## Üretilen Çıktılar
- Performans metrikleri
- ML model değerlendirme raporları

{build_common_not_in_scope_section()}

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
"""

def build_developer_guide_template() -> str:
    return f"""# Geliştirici Kılavuzu (Developer Guide)
{build_standard_disclaimer()}

## Amaç
Sistemin kod tabanına katkıda bulunacak, yeni modüller ekleyecek veya hata düzeltecek yazılım mühendisleri içindir.

## Kapsam
Proje mimarisi, kodlama standartları, test yazımı, bağımlılık yönetimi ve CI/CD (local makefile) pratikleri.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- Yeni bir indicator modülü ekleme.
- Birim testi (unit test) yazma ve `pytest` ile çalıştırma.

## Üretilen Çıktılar
- Kalite kapısı (Quality Gates) raporları.
- Test kapsam (coverage) raporları.

{build_common_not_in_scope_section()}

## Sık Hatalar
- Type hint (tip belirteci) kullanmamak.
- Modüller arası dairesel bağımlılık (circular dependency) yaratmak.

## İlgili Komutlar
- `make test`
- `make typecheck`
- `make lint`

## İlgili Klasörler
- `tests/`
- `core/`

## Uyarılar
Güvenlik sınırlarını aşacak (örneğin broker API ekleyecek) PR'lar reddedilecektir.
"""

def build_codex_agent_guide_template() -> str:
    return f"""# Codex Agent Kılavuzu (Codex Agent Guide)
{build_standard_disclaimer()}

## Amaç
Yapay zeka asistanlarının (Codex vb.) kod tabanını anlarken, refactor ederken veya dokümante ederken uyması gereken katı kuralları tanımlar.

## Kapsam
Yapay zeka ile kod geliştirme prosedürleri, `AGENTS.md` kurallarına uyum ve güvenlik bariyerleri.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- Yeni modül eklemeden önce mimari uyumluluk kontrolü.
- Hata ayıklarken sistem günlüklerinin okunması.

## Üretilen Çıktılar
- Yamanmış (patched) dosyalar.
- Geliştirilmiş dokümantasyon.

{build_common_not_in_scope_section()}

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
"""

def build_safe_usage_guide_template() -> str:
    return f"""# Güvenli Kullanım Kılavuzu (Safe Usage Guide)
{build_standard_disclaimer()}

## Amaç
Kullanıcıların, operatörlerin ve geliştiricilerin sistemi tehlikeye atmadan, güvenlik sınırları içinde nasıl kullanacaklarını tanımlar.

## Kapsam
API anahtarlarının korunması, logların maskelenmesi, canlı işlem yasağı denetimleri.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- `.env` dosyasında anahtarların saklanması (git commit edilmemesi).
- Loglarda PII (Personal Identifiable Information) ve secret'ların maskelendiğinin kontrolü.

## Üretilen Çıktılar
- Güvenlik denetim (Security/Observability) raporları.

{build_common_not_in_scope_section()}

## Sık Hatalar
- `.env` dosyasını public repoya yüklemek.

## İlgili Komutlar
- `python -m scripts.run_observability_status`

## İlgili Klasörler
- `security/`
- `observability/`

## Uyarılar
API anahtarlarınızı kimseyle paylaşmayın.
"""

def build_troubleshooting_template() -> str:
    return f"""# Sorun Giderme (Troubleshooting Cookbook)
{build_standard_disclaimer()}

## Amaç
Yaygın karşılaşılan hataların tespit edilmesi ve çözülmesi için adım adım rehber.

## Kapsam
Ortam kurulum hataları, veri indirme hataları, modül import hataları ve performans sorunları.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- "ModuleNotFoundError" çözümü.
- Yahoo Finance rate limit sorununun aşılması.

## Üretilen Çıktılar
- Hata çözüm logları.

{build_common_not_in_scope_section()}

## Sık Hatalar
- Sanal ortamı (virtual environment) aktif etmeden komut çalıştırmak.

## İlgili Komutlar
- `make setup`
- `python -m scripts.run_error_taxonomy_report`

## İlgili Klasörler
- `logs/`

## Uyarılar
Sorun çözülmezse, log detaylarını kontrol edin. Sorunu çözerken production/canlı trade araçları yüklemeyin.
"""

def build_faq_template() -> str:
    return f"""# Sıkça Sorulan Sorular (FAQ)
{build_standard_disclaimer()}

## Amaç
Kullanıcıların genel sorularını hızlıca yanıtlamak.

## Kapsam
Genel sorular ve yanıtlar.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- S: Bu bot gerçek işlem yapar mı? C: Hayır, sadece offline araştırma yapar.
- S: Telegram'a nasıl bağlarım? C: `.env` dosyasına bot token ekleyerek.

## Üretilen Çıktılar
Yok.

{build_common_not_in_scope_section()}

## Sık Hatalar
- Gerçek işlem beklentisine girmek.

## İlgili Komutlar
- Yok.

## İlgili Klasörler
- `docs/`

## Uyarılar
Lütfen `README.md` dosyasını dikkatle okuyun.
"""

def build_glossary_template() -> str:
    return f"""# Sözlük (Glossary)
{build_standard_disclaimer()}

## Amaç
Projede geçen finansal ve teknik terimlerin açıklanması.

## Kapsam
Sinyal adayları, indikatörler, rejimler vb. terimler.

{build_safety_boundaries_section()}

## Kullanım Örnekleri
- **Sinyal Adayı (Signal Candidate):** Karar verilmemiş, araştırma amaçlı yön belirteci.
- **Offline Araştırma:** Verilerin önceden indirilip, piyasa saatleri dışında incelenmesi.

## Üretilen Çıktılar
Yok.

{build_common_not_in_scope_section()}

## Sık Hatalar
Yok.

## İlgili Komutlar
Yok.

## İlgili Klasörler
Yok.

## Uyarılar
Bu terimler akademik/araştırma bağlamında tanımlanmıştır.
"""
