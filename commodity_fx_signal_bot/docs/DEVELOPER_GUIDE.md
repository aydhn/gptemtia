<!-- AUTO-GENERATED SECTION START -->
# Geliştirici Kılavuzu (Developer Guide)

> **UYARI / YASAL BİLDİRİM**
> Bu doküman ve açıklanan sistem yalnızca **offline/local araştırma platformu** kullanımını açıklar.
> Bu proje bir canlı alım-satım botu değildir. Gerçek emir göndermez, canlı sinyal üretmez, broker talimatı vermez ve gerçek pozisyon yönetmez.
> Model deployment, production scheduler veya otomatik trade özellikleri içermez.
> Bu projede üretilen hiçbir rapor veya sinyal **yatırım tavsiyesi değildir**.
> Eğitim, araştırma ve kağıt üzerinde test (paper trading) amacıyla geliştirilmiştir.


## Amaç
Sistemin kod tabanına katkıda bulunacak, yeni modüller ekleyecek veya hata düzeltecek yazılım mühendisleri içindir.

## Kapsam
Proje mimarisi, kodlama standartları, test yazımı, bağımlılık yönetimi ve CI/CD (local makefile) pratikleri.


## Güvenlik Sınırları (Safety Boundaries)

Sistemin tasarımı gereği aşılmaması gereken sınırlar:
1. **Canlı Emir Yasağı:** Sistem broker API'lerine emir gönderecek kod içermez.
2. **Yatırım Tavsiyesi Yoktur:** Üretilen kararlar kesinlik bildirmez, araştırma hipotezidir.
3. **Daemon/Cron Yasağı:** Sistem sonsuz döngüde veya arka planda sessizce çalışacak şekilde tasarlanmamıştır. Manuel veya kontrollü script execution gerektirir.
4. **Web Dashboard Yok:** Dışarıya açık web sunucusu (Streamlit, Flask vb.) barındırmaz.
5. **Scraping Yasağı:** Selenium, Playwright veya BeautifulSoup ile veri kazıma işlemi yapmaz; sadece resmi/ücretsiz veri API'lerini kullanır.


## Kullanım Örnekleri
- Yeni bir indicator modülü ekleme.
- Birim testi (unit test) yazma ve `pytest` ile çalıştırma.

## Üretilen Çıktılar
- Kalite kapısı (Quality Gates) raporları.
- Test kapsam (coverage) raporları.


## Kapsam Dışı (Out of Scope)

Aşağıdaki özellikler kasıtlı olarak sisteme **dahil edilmemiştir**:
- Gerçek para ile işlem (Live Trading)
- Otonom (kendi kendine çalışan) üretim dağıtımı (Production Deployment)
- Otomatik alım-satım onayları (Auto Trade Approvals)
- Kar garantisi veya riskten arındırılmış getiri iddiaları


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

<!-- AUTO-GENERATED SECTION END -->
