# Data Sources

This document describes the data sources used by the Commodity & FX Signal Bot.

## Symbol Reliability Checks
During Phase 3, we introduced a systematic way to check and grade the reliability of data for each symbol.
The `UniverseAnalyzer` fetches data for a symbol and grades it from `A` to `F` (or `SYNTHETIC`) based on factors like:
- Successful fetch
- Enough rows
- No missing close prices
- No duplicate indices
- No negative prices
- No high/low inversion
- Valid last close price

## Yahoo Finance (yfinance)
- Used for most Commodities and Forex pairs.
- **Yahoo Missing Data Risk:** Sometimes Yahoo might drop a symbol or temporarily have missing data. The reliability scan will flag this and lower the score.
- **Alias Fallback:** If the primary symbol fails, the system will attempt to fetch data using aliases defined in the `SymbolSpec`. Using an alias reduces the reliability score by 5 points.
- **Futures Data Limitations:** Yahoo may not provide continuous contracts seamlessly, so roll dates and gaps are common.
- **FX Volume:** Volume data for Forex pairs is often missing or zero on Yahoo Finance.

## EVDS (TCMB)
- Used for Turkish macroeconomic indicators (e.g., Inflation, Interest rates).

## FRED (St. Louis Fed)
- Used for US macroeconomic indicators (e.g., CPI, Interest rates).

## Synthetic Symbols
- Symbols marked with `data_source="synthetic"` (e.g., Benchmarks) are not fetched from external providers like Yahoo. They are generated internally or bypassed to maintain perfect reliability scores ("SYNTHETIC" grade).

## Timeframes & Resampling (Phase 4)
- **Intraday Limitations:** Yahoo/yfinance often limits how far back 1m, 2m, or 5m data can go. Thus, the minimum reliable timeframe starts around 15m or 1h.
- **Derived Timeframes:** The 4h timeframe is generated as a `derived` timeframe by fetching 1h data from the provider and up-sampling it within the `DataPipeline` using pandas.
- **Backtest vs Signal:** Timeframes are categorized to show if they are `recommended_for_signal` (like 1h, 4h, 1d) avoiding micro timeframes that break logic in low-frequency bots.

## Lokal Veri Gölü (Data Lake)

Phase 5 ile birlikte sisteme eklenen yerel veri gölü özellikleri şunları içerir:

- **Lokal Cache ile Data Lake Farkı:** Geçici `cache` yalnızca istekleri hızlandırmak içinken, `data lake` kalıcı bir depo ve gelecekteki test/strateji algoritmaları için ana kaynaktır. Veri kalitesi (quality grade) lake içerisine işlenir.
- **Veri Tekrar İndirmeyi Azaltma:** İndirme geçmişi (DownloadJournal) tutularak, aynı gün veya periyot içinde gereksiz Yahoo/EVDS hit'lerinin önüne geçilir.
- **Yahoo Veri Sınırlamaları:** Sık istek atmanın sınırlarını bildiğimiz için limitlenmiş (örn. `max_download_failures_per_run=20`) bir indirme süreci (`DownloadManager`) kullanılır.
- **Macro/Synthetic Semboller:** Bu varlık sınıfları OHLCV modeline her zaman tam uymadığından (`synthetic` hiç inmez, `macro` ise sadece farklı bir pipeline'da iner), normal OHLCV indirme turundan dışlanmıştır (`skip_synthetic_downloads`).
- **Data Quality Grade:** İndirilen veriler A ile F arasında derecelendirilir. Eksik veriler, negatif fiyatlar veya düşük satır sayıları notu düşürür ve sonrasında `run_data_lake_repair` aracı bu bozuk notlu dosyaları hedef alır.

## Data Quality & Integrity (Phase 6)

- **Ücretsiz Veride Kalite Riski:** Yahoo Finance gibi ücretsiz veri sağlayıcılar eksik veriler, boşluklar (gaps), hatalı fiyatlamalar (outliers) barındırabilir. Bu, algoritmaların yanlış kararlar vermesine neden olabilir.
- **Eksik Veri ve Boşluklar (Gaps):** Zaman serilerinde bazı mumların eksik olması, hareketli ortalamalar veya gecikmeli indikatörlerin hatalı hesaplanmasına yol açar. Gaps tespiti bu tür sorunların raporlanmasını sağlar.
- **Outlier Verinin Gerçek Piyasa Olayı Olabileceği:** Fiyatların aniden aşırı sapması her zaman veri sağlayıcısının hatası değildir (örneğin; flaş çöküşler, önemli makroekonomik duyurular). Bu yüzden Phase 6'da outlier'lar silinmez, sadece analiz edilmesi için işaretlenir (flagging).
- **Otomatik Düzeltme Riskleri:** Çok büyük veri boşluklarını veya outlier'ları varsayımsal değerlerle doldurmak (interpolation/forward fill) sentetik ve gerçekdışı bir piyasa resmi oluşturur. Sadece çok küçük (1-2 barlık) boşluklar güvenle doldurulabilir.
- **Ham Veri / İşlenmiş Veri Ayrımı:** Sağlayıcıdan gelen ham veri gölde (`lake/ohlcv`) olduğu gibi saklanır. Temizleme ve kalite kontrol işlemlerinden geçen veri ise ayrı bir dizine (`lake/processed/ohlcv`) kaydedilir. Böylece ham verinin orjinalliği her zaman korunur ve istenildiği an farklı temizlik algoritmalarıyla yeni baştan işlenebilir.
