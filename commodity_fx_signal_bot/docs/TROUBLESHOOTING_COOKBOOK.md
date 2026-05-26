<!-- AUTO-GENERATED SECTION START -->
# Sorun Giderme (Troubleshooting Cookbook)

> **UYARI / YASAL BİLDİRİM**
> Bu doküman ve açıklanan sistem yalnızca **offline/local araştırma platformu** kullanımını açıklar.
> Bu proje bir canlı alım-satım botu değildir. Gerçek emir göndermez, canlı sinyal üretmez, broker talimatı vermez ve gerçek pozisyon yönetmez.
> Model deployment, production scheduler veya otomatik trade özellikleri içermez.
> Bu projede üretilen hiçbir rapor veya sinyal **yatırım tavsiyesi değildir**.
> Eğitim, araştırma ve kağıt üzerinde test (paper trading) amacıyla geliştirilmiştir.


## Amaç
Yaygın karşılaşılan hataların tespit edilmesi ve çözülmesi için adım adım rehber.

## Kapsam
Ortam kurulum hataları, veri indirme hataları, modül import hataları ve performans sorunları.


## Güvenlik Sınırları (Safety Boundaries)

Sistemin tasarımı gereği aşılmaması gereken sınırlar:
1. **Canlı Emir Yasağı:** Sistem broker API'lerine emir gönderecek kod içermez.
2. **Yatırım Tavsiyesi Yoktur:** Üretilen kararlar kesinlik bildirmez, araştırma hipotezidir.
3. **Daemon/Cron Yasağı:** Sistem sonsuz döngüde veya arka planda sessizce çalışacak şekilde tasarlanmamıştır. Manuel veya kontrollü script execution gerektirir.
4. **Web Dashboard Yok:** Dışarıya açık web sunucusu (Streamlit, Flask vb.) barındırmaz.
5. **Scraping Yasağı:** Selenium, Playwright veya BeautifulSoup ile veri kazıma işlemi yapmaz; sadece resmi/ücretsiz veri API'lerini kullanır.


## Kullanım Örnekleri
- "ModuleNotFoundError" çözümü.
- Yahoo Finance rate limit sorununun aşılması.

## Üretilen Çıktılar
- Hata çözüm logları.


## Kapsam Dışı (Out of Scope)

Aşağıdaki özellikler kasıtlı olarak sisteme **dahil edilmemiştir**:
- Gerçek para ile işlem (Live Trading)
- Otonom (kendi kendine çalışan) üretim dağıtımı (Production Deployment)
- Otomatik alım-satım onayları (Auto Trade Approvals)
- Kar garantisi veya riskten arındırılmış getiri iddiaları


## Sık Hatalar
- Sanal ortamı (virtual environment) aktif etmeden komut çalıştırmak.

## İlgili Komutlar
- `make setup`
- `python -m scripts.run_error_taxonomy_report`

## İlgili Klasörler
- `logs/`

## Uyarılar
Sorun çözülmezse, log detaylarını kontrol edin. Sorunu çözerken production/canlı trade araçları yüklemeyin.

<!-- AUTO-GENERATED SECTION END -->
