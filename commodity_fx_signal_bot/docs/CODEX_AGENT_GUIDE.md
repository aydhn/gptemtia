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
