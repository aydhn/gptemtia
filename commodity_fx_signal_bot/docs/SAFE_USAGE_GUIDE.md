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


## Secrets Hygiene
- **.env vs .env.example:** Real secrets live in `.env` (which is ignored). `.env.example` must only contain placeholders.
- **Reporting:** Secret values are never written to reports to prevent leaks.
- **Masked Findings:** Findings display masked representations (e.g. `abc****xyz`) for safe review.
- **Credential Boundary:** Checks ensure secrets don't bleed into source code, tests, docs, or reports.
- **Private Data Scanner:** Flags potential personal data (emails, phones) but is not a substitute for formal compliance.
- **Backup/Packaging:** Manifests are checked to ensure sensitive files like `.env` are excluded.
- **No Automatic Operations:** The tool will not automatically delete files, overwrite secrets, or integrate with cloud vaults.
