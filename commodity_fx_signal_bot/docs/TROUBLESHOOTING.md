# Troubleshooting Guide

## Yaygın Sorunlar ve Çözümleri

- **ModuleNotFoundError / ImportError**
  - **Belirti:** Komutlar import hatası vererek durur.
  - **Sebep:** Sanal ortam aktif değil veya `pip install` yapılmamış.
  - **Çözüm:** PYTHONPATH ayarını kontrol et, requirements.txt kur.

- **pytest collection hatası**
  - **Belirti:** `pytest` testleri bulamaz.
  - **Sebep:** PYTHONPATH bozuk.
  - **Çözüm:** `export PYTHONPATH=. && pytest` ile çalıştır.

- **.env bulunamıyor**
  - **Belirti:** Settings yüklenmez veya token hatası verir.
  - **Sebep:** Kök dizinde `.env` yok.
  - **Çözüm:** `cp .env.example .env` yap.

- **DataLake klasörü yok / Veri dosyası yok**
  - **Belirti:** Parquet okuma hatası, FileNotFound.
  - **Sebep:** Fetch pipeline çalışmamış.
  - **Çözüm:** `python -m scripts.run_data_pipeline` çalıştır.

- **Candidate üretilemiyor / Backtest no trades**
  - **Belirti:** Çıktı csv'leri boş, summary "no trades" der.
  - **Sebep:** Sinyal kriterleri çok sıkı.
  - **Çözüm:** Config üzerinden sinyal parametrelerini gevşet.

- **ML dataset insufficient rows**
  - **Belirti:** "Not enough rows to train" uyarısı.
  - **Sebep:** Geçmiş veri çok az, embargo gap yüksek.
  - **Çözüm:** Daha uzun timeframe indir.

- **Telegram not configured**
  - **Belirti:** Telegram API atlar veya yetki hatası verir.
  - **Sebep:** TELEGRAM_BOT_TOKEN veya CHAT_ID eksik.
  - **Çözüm:** .env dosyasına ekle.

- **Security audit secret warning**
  - **Belirti:** Security audit fail olur.
  - **Sebep:** Loglarda veya kodda şifre, token unutulmuş olabilir.
  - **Çözüm:** Raporu inceleyip maske ekle.
