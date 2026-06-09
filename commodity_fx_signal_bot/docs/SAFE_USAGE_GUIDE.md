<!-- AUTO-GENERATED SECTION START -->
# Güvenli Kullanım Kılavuzu (Safe Usage Guide)

> **UYARI / YASAL BİLDİRİM**
> Bu doküman ve açıklanan sistem yalnızca **offline/local araştırma platformu** kullanımını açıklar.
> Bu proje bir canlı alım-satım botu değildir. Gerçek emir göndermez, canlı sinyal üretmez, broker talimatı vermez ve gerçek pozisyon yönetmez.
> Model deployment, production scheduler veya otomatik trade özellikleri içermez.
> Bu projede üretilen hiçbir rapor veya sinyal **yatırım tavsiyesi değildir**.
> Eğitim, araştırma ve kağıt üzerinde test (paper trading) amacıyla geliştirilmiştir.


## Amaç
Kullanıcıların, operatörlerin ve geliştiricilerin sistemi tehlikeye atmadan, güvenlik sınırları içinde nasıl kullanacaklarını tanımlar.

## Kapsam
API anahtarlarının korunması, logların maskelenmesi, canlı işlem yasağı denetimleri.


## Güvenlik Sınırları (Safety Boundaries)

Sistemin tasarımı gereği aşılmaması gereken sınırlar:
1. **Canlı Emir Yasağı:** Sistem broker API'lerine emir gönderecek kod içermez.
2. **Yatırım Tavsiyesi Yoktur:** Üretilen kararlar kesinlik bildirmez, araştırma hipotezidir.
3. **Daemon/Cron Yasağı:** Sistem sonsuz döngüde veya arka planda sessizce çalışacak şekilde tasarlanmamıştır. Manuel veya kontrollü script execution gerektirir.
4. **Web Dashboard Yok:** Dışarıya açık web sunucusu (Streamlit, Flask vb.) barındırmaz.
5. **Scraping Yasağı:** Selenium, Playwright veya BeautifulSoup ile veri kazıma işlemi yapmaz; sadece resmi/ücretsiz veri API'lerini kullanır.


## Kullanım Örnekleri
- `.env` dosyasında anahtarların saklanması (git commit edilmemesi).
- Loglarda PII (Personal Identifiable Information) ve secret'ların maskelendiğinin kontrolü.

## Üretilen Çıktılar
- Güvenlik denetim (Security/Observability) raporları.


## Kapsam Dışı (Out of Scope)

Aşağıdaki özellikler kasıtlı olarak sisteme **dahil edilmemiştir**:
- Gerçek para ile işlem (Live Trading)
- Otonom (kendi kendine çalışan) üretim dağıtımı (Production Deployment)
- Otomatik alım-satım onayları (Auto Trade Approvals)
- Kar garantisi veya riskten arındırılmış getiri iddiaları


## Sık Hatalar
- `.env` dosyasını public repoya yüklemek.

## İlgili Komutlar
- `python -m scripts.run_observability_status`

## İlgili Klasörler
- `security/`
- `observability/`

## Uyarılar
API anahtarlarınızı kimseyle paylaşmayın.

<!-- AUTO-GENERATED SECTION END -->

## Evidence Governance and Audit Binder
Projedeki tüm safety, backup, packaging ve quality çıktılarını bir denetim paketinde toplamak için Phase 64 scriptlerini kullanın (örn. `run_audit_evidence_binder.py`, `run_evidence_traceability_matrix.py`). Policy/control mappingleri, traceability matrixleri ve evidence score'ları resmi/hukuki bir uyum sertifikasyonu (SOC2, ISO vb.) teşkil etmez, tamamen offline/local denetlenebilirlik amacını taşır.
