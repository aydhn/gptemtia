# Commodity & FX Signal Bot

A zero-budget, paper-trading Python bot for Commodity and FX signals using free data sources (Yahoo Finance, EVDS, FRED) and Telegram for notifications.

**Note:** This bot does NOT execute live trades, nor does it connect to broker APIs for live execution.

## Setup
1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`

## Execution and Scripts

- `python main.py`: Run the main application (work in progress).

### Phase 3 Commands
- `python -m scripts.run_universe_preview`: Preview the current symbol universe configuration.
- `python -m scripts.run_universe_audit`: Validates the universe and generates a universe manifest in `reports/output`.
- `python -m scripts.run_symbol_reliability_scan --limit 20 --interval 1d --period 1y`: Runs a reliability scan on the universe to check data fetching capability and quality.
- `python -m scripts.run_symbol_reliability_scan --asset-class metals --interval 1d --period 2y`: Runs a reliability scan filtered by asset class.

## Concepts (Phase 3)

- **Reliability Score:** A score from 0 to 100 representing the quality of the downloaded data. Deductions occur for missing prices, errors, duplicate indices, short datasets, etc.
- **Grade System:** Translates the score to a letter grade (A, B, C, D, F) or "SYNTHETIC" for benchmarks that don't need network fetching.
- **Alias Use:** If a primary symbol fails, the pipeline will try its aliases. Doing so costs 5 points on the reliability score.
- **Synthetic Benchmarks:** These symbols represent logical constructs (like an equal-weight portfolio) and do not fetch data from Yahoo.

**Important:** Phase 3 still does not generate trading strategies. It focuses on preparing a clean, graded, and tradeable symbol universe for the following phases.

## Concepts (Phase 4)

- **Timeframes:** The bot targets low-frequency signals using 1h, 4h (derived), 1d, 1wk. 1m/2m are generally excluded to avoid unreliable historical data from Yahoo and frequent API hits.
- **Market Sessions:** Approximate open/close times and weekend checking are added (e.g., Forex is 24/5 while Crypto trades 24/7). This stops unnecessary fetches.
- **Scan Profiles:** Determines how frequently to run. The default `balanced_swing` profile checks every hour using 4h, 1d, 1wk timeframes.
- **Scan Scheduler:** Uses profiles and market session logic to build a "scan plan" telling the bot which symbols to process during the current cycle.

### Phase 4 Commands
- `python -m scripts.run_timeframe_compatibility_audit`: Audits timeframe config, market calendars, and generates a realistic scan plan in `reports/output`.

## Lokal Veri Gölü (Phase 5)

Açıkla:
- **Neden data lake var?** Çevrimiçi veri kaynaklarından (Yahoo vs.) sürekli veri çekmek yerine veriyi kendi ortamımızda saklayarak bant genişliğinden ve süreden tasarruf ederiz. Tekrarlanan ve hatalı denemeleri önleriz.
- **Veriler nereye kaydedilir?** `data/lake/ohlcv/{data_source}/{sub_class}/{symbol}/` altında saklanır.
- **Parquet neden kullanılır?** CSV'ye göre çok daha hızlıdır ve diskte daha az yer kaplar. Pandas ile uyumludur.
- **Manifest nedir?** Veri gölünün o anki fotoğrafını (hangi dosyalar var, boyutları, kaliteleri) özetleyen bir CSV ve JSON listesidir.
- **Download journal nedir?** Her veri indirme denemesinin (başarılı ya da başarısız) kaydedildiği günlüktür. Hata tespitini kolaylaştırır.
- **Repair script ne işe yarar?** Eksik veya "D/F" notuna sahip zayıf kalitedeki veri dosyalarını otomatik tespit edip onarmak için kullanılır.

Komutlar:
- `python -m scripts.run_data_lake_update --limit 10 --period 1y`
- `python -m scripts.run_data_lake_update --asset-class metals --period 2y`
- `python -m scripts.run_data_lake_status`
- `python -m scripts.run_data_lake_repair --dry-run`

## Veri Kalitesi ve Temiz Veri Katmanı (Phase 6)

Veri sağlığı, stratejilerin ve backtestlerin doğruluğu için kritik öneme sahiptir. Bu katman, veri gölündeki ham verileri sistematik olarak denetler, temizler ve işlenmiş (processed) veri olarak ayrı bir alanda saklar.

**Önemli Kavramlar:**
- **Raw Veri:** Data sağlayıcılardan (Yahoo vb.) indirilen ve olduğu gibi saklanan ham veri. Data gölünde orijinali asla değiştirilmez (ezilmez).
- **Processed Veri:** Temizlik işlemlerinden geçmiş, indeksleri düzeltilmiş, küçük gapleri doldurulmuş ve kalitesi artırılmış veridir. İndikatörler, stratejiler, ML ve backtest motorları tarafından kullanılır.
- **Ham Veri Neden Ezilmez?** Ham veriyi değiştirmek, orijinal hata kaynağını kaybetmeye yol açar ve gelecekte farklı temizlik stratejileri uygulamayı zorlaştırır.
- **Outlier Neden Otomatik Silinmez?** Aşırı fiyat hareketleri (outlier'lar) veri hatası olabileceği gibi gerçek bir piyasa dalgalanması (crash/rally) da olabilir. Bu nedenle outlier'lar otomatik silinmez, işaretlenir ve raporlanır.
- **Gap Nedir?** Ardışık iki zaman damgası arasındaki beklenen süreden çok daha büyük olan boşluktur. Veri kaybını ifade eder.
- **Quality Grade:** Verinin sağlık durumunu A'dan F'ye kadar derecelendirir. Düşük not alan veriler problemlidir ve kullanılmadan önce onarılmalıdır.

**Çalıştırma Komutları:**

Veri Gölü Kalite Denetimi:
```bash
python -m scripts.run_data_quality_audit
python -m scripts.run_data_quality_audit --limit 10
```

Veri Temizleme ve İşlenmiş (Processed) Veri Üretimi:
```bash
python -m scripts.run_data_cleaning --limit 10
python -m scripts.run_data_cleaning --symbol GC=F --timeframe 1d
```

İşlenmiş Veri Gölü Durum Raporu:
```bash
python -m scripts.run_processed_data_status
```


## Phase 7: Teknik İndikatör ve Feature Katmanı
Bu faz strateji üretmez, aksine gelecekteki stratejiler ve makine öğrenmesi katmanı için gerekli olan teknik özellikleri (features) temiz ve profesyonel bir yapıda hesaplar.
- Processed veri (işlenmiş temiz veri) kullanılması tercih edilir.
- Warmup (ısınma periyodu) ve hesaplanamayan değerlerden doğan NaN'lar normal kabul edilir ve raporlanır.
- Özellik dosyaları (features) `data/lake/features/technical` altında ayrı olarak saklanır, orijinal veri bozulmaz.
- İndikatör hesaplamaları için `ta` kütüphanesi ve built-in Pandas/NumPy yöntemleri birlikte kullanılır.
- İleride eklenecek olan FX Volume indikatörlerinde volume sıfır/NaN çıktılarının sistemi çökertmemesi garanti altına alınmıştır.
- Ichimoku gibi forward-shift içeren indikatörlerde ML veri kaçağı (leakage) riski bulunur, dikkat edilmelidir.

**Kullanım Komutları:**
```bash
python -m scripts.run_indicator_preview --symbol GC=F --timeframe 1d
python -m scripts.run_indicator_batch_build --limit 10
python -m scripts.run_indicator_status
```

## Phase 9: Trend Feature ve Trend Event Katmanı

Bu faz nihai al/sat stratejisi değildir.
Trend eventleri sadece aday olaylardır (ön sinyal).
SMA, EMA, WMA, HMA, MACD, ADX, DMI, Aroon, Ichimoku gibi trend göstergeleri kullanılır.

**Compact ve Full Trend Feature Set Farkı:**
- **Compact:** Daha az kolonla sadece en kritik trend özelliklerini (SMA 20/50/200, MACD, temel ADX/Aroon vb.) üretir. Backtest ve ML için daha hafiftir.
- **Full:** Belirtilen indikatörlerin birçok farklı parametre setiyle olan kombinasyonlarını ve ek olarak Ichimoku Cloud'u içerir.

**Uyarı:** Ichimoku ve forward-shift içeren yapıların (Chikou Span) leakage (gelecekten bilgi sızdırma) riski vardır; strateji/ML tarafında dikkatle kullanılmalıdır.

Event kolonları (örn. `event_ma_stack_bullish`, `event_macd_hist_positive_shift`) ileride strateji ve backtest motoru tarafından kullanılacaktır. Trend eventleri tek başına işlem kararı değildir.

**Kullanım Komutları:**
```bash
python -m scripts.run_trend_feature_preview --symbol GC=F --timeframe 1d
python -m scripts.run_trend_event_preview --symbol GC=F --timeframe 1d
python -m scripts.run_trend_batch_build --limit 10
python -m scripts.run_trend_status
```

## Phase 10: Volatilite Feature ve Volatilite Event Katmanı

- Bu faz nihai al/sat stratejisi değildir.
- Volatilite eventleri sadece aday olaylardır.
- ATR, Bollinger, Keltner, Donchian, Historical Volatility, Parkinson, Garman-Klass, gap/range gibi ölçümler kullanılır.
- Compact ve full volatility feature set farkı mevcuttur.
- Event kolonları ileride strateji, risk yönetimi ve backtest motoru tarafından kullanılacaktır.
- Volatilite eventleri tek başına işlem kararı değildir.
- Volatilite sıkışması yön söylemez; sadece potansiyel hareket hazırlığına işaret eder.

**Kullanım Komutları:**
```bash
python -m scripts.run_volatility_feature_preview --symbol GC=F --timeframe 1d
python -m scripts.run_volatility_event_preview --symbol GC=F --timeframe 1d
python -m scripts.run_volatility_batch_build --limit 10
python -m scripts.run_volatility_status
```


## Hacim/Likidite Feature ve Volume Event Katmanı
Bu faz nihai al/sat stratejisi değildir.
Volume eventleri sadece aday olaylardır.
OBV, MFI, CMF, Volume Z-score, Relative Volume, Accumulation/Distribution, PVT, liquidity proxy gibi ölçümler kullanılır.
Compact ve full volume feature set farkı.
Forex tarafında volume verisi çoğu zaman güvenilir olmayabilir.
Volume unusable ise eventler bastırılabilir.
Event kolonları ileride strateji, risk yönetimi ve backtest motoru tarafından kullanılacaktır.
Volume eventleri tek başına işlem kararı değildir.

Komutları ekle:
python -m scripts.run_volume_feature_preview --symbol GC=F --timeframe 1d
python -m scripts.run_volume_event_preview --symbol GC=F --timeframe 1d
python -m scripts.run_volume_batch_build --limit 10
python -m scripts.run_volume_status


## Mean Reversion Feature ve Ortalamaya Dönüş Event Katmanı

- Bu faz nihai al/sat stratejisi değildir.
- Mean reversion eventleri sadece aday olaylardır.
- Z-score, SMA/EMA distance, percentile rank, Bollinger reentry, overextension ve snapback pressure kullanılır.
- Compact ve full mean reversion feature set farkı mevcuttur.
- Güçlü trendlerde mean reversion adayları risklidir.
- Event kolonları ileride strateji, rejim filtresi, risk yönetimi ve backtest motoru tarafından kullanılacaktır.
- Mean reversion eventleri tek başına işlem kararı değildir.

Komutlar:
```bash
python -m scripts.run_mean_reversion_feature_preview --symbol GC=F --timeframe 1d
python -m scripts.run_mean_reversion_event_preview --symbol GC=F --timeframe 1d
python -m scripts.run_mean_reversion_batch_build --limit 10
python -m scripts.run_mean_reversion_status
```

## Price Action Feature ve Fiyat Davranışı Event Katmanı (Phase 13)

- Bu faz nihai al/sat stratejisi değildir.
- Price action eventleri sadece aday olaylardır.
- Mum gövdesi, fitil, range, close location, gap, inside/outside bar, breakout ve false breakout ölçülür.
- Compact ve full price action feature set farkı bulunmaktadır.
- Gap ve breakout eventleri tek başına işlem kararı değildir.
- Event kolonları ileride strateji, rejim filtresi, risk yönetimi ve backtest motoru tarafından kullanılacaktır.
- Emtia ve FX tarafında gap davranışı farklı yorumlanmalıdır.

Komutlar:
```bash
python -m scripts.run_price_action_feature_preview --symbol GC=F --timeframe 1d
python -m scripts.run_price_action_event_preview --symbol GC=F --timeframe 1d
python -m scripts.run_price_action_batch_build --limit 10
python -m scripts.run_price_action_status
```

### Divergence / Uyumsuzluk Feature ve Event Katmanı
Bu faz nihai al/sat stratejisi değildir. Divergence eventleri sadece aday olaylardır.
Regular bullish/bearish ve hidden bullish/bearish divergence desteklenir.
RSI, MACD histogram, ROC, OBV, MFI, CMF gibi kolonlar kullanılabilir.
Divergence için önce momentum/trend/volume feature dosyalarının üretilmesi önerilir.
Pivot confirmation lag vardır. Pivot hesaplama yanlış kullanılırsa lookahead/leakage riski oluşturabilir.
Divergence tek başına işlem kararı değildir.

Komutlar:
```bash
python -m scripts.run_divergence_feature_preview --symbol GC=F --timeframe 1d
python -m scripts.run_divergence_event_preview --symbol GC=F --timeframe 1d
python -m scripts.run_divergence_batch_build --limit 10
python -m scripts.run_divergence_status
```

## Çoklu Zaman Dilimi / MTF Analiz Katmanı

Bu faz nihai al/sat stratejisi değildir.
MTF eventleri sadece bağlam/adayı olaylardır.
Üst zaman dilimi trend/volatilite/momentum bağlamı alt zaman dilimi analizine taşınır.
MTF alignment sırasında future leakage riski vardır; sistem strict no-lookahead yaklaşımı kullanır.
Context stale olabilir; stale context ayrıca raporlanır.
Eksik feature setleri sistemi çökertmez ama raporlanır.
MTF feature üretmeden önce ilgili timeframe’lerde momentum/trend/volatility/price_action/divergence feature dosyalarının üretilmesi önerilir.

Komutlar:
python -m scripts.run_mtf_alignment_preview --symbol GC=F --profile daily_swing
python -m scripts.run_mtf_event_preview --symbol GC=F --profile daily_swing
python -m scripts.run_mtf_batch_build --limit 10 --profile daily_swing
python -m scripts.run_mtf_status

## Makro Rejim, Enflasyon ve Benchmark Katmanı (Phase 17)

Bu faz nihai al/sat stratejisi üretmez. Makro veriler işlem sinyali değil, bağlam ve kıyaslama katmanıdır.
- Türkiye enflasyonu için EVDS, ABD CPI için FRED entegre edilmiştir.
- API key yoksa sistem çökmez, düzgün bir şekilde uyarı üretir.
- USDTRY, altın, emtia sepeti ve CPI benchmarkları performans kıyaslaması içindir.
- Reel getiri hesapları ileride strateji performans analizinde kullanılacaktır.
- Web scraping kesinlikle yoktur.

**Örnek Komutlar:**
```bash
python -m scripts.run_macro_data_update
python -m scripts.run_macro_feature_preview
python -m scripts.run_macro_benchmark_preview
python -m scripts.run_macro_batch_build
python -m scripts.run_macro_status
```


## Varlık Sınıfı Davranış Profilleri ve Grup Analizi (Phase 18)

Bu proje, her varlık sınıfının farklı davranış karakterlerini analiz ederek sistem için önemli bir "bağlam" oluşturur. **Önemli: Bu analizler nihai AL/SAT veya LONG/SHORT sinyali üretmez.** Asset profile ve group analizi sadece sonraki aşamalardaki strateji ve risk filtreleri için hazırlıktır.

### Davranış Profili Prensipleri
- **Metaller, Enerji, Tarım, Softs, Livestock, TL Forex, Majör Forex ve Çapraz Forex** için ayrı profiller tanımlanmıştır.
- **Forex Hacim Güvenilirliği:** Birçok forex kaynağında hacim verisi yoktur veya yanıltıcıdır. Forex profillerinde `volume_reliability` düşük kabul edilir.
- Grup indeksleri, üyeler arası korelasyon (nedensellik değil, ilişki gösterir), ve grup ayrışması (dispersion) özellik setlerine dahil edilmiştir.
- Her sembolün kendi grubuna karşı (Relative Strength) ve makro verilere (USDTRY, Altın vb.) karşı göreceli durumu hesaplanır.
- Üretilen event'ler ("leader_candidate", "high_dispersion_context" vb.) sadece uyarı veya bağlam amacı taşır.

### Asset Profile Scriptleri

```bash
# Tek bir sembolün davranış profilini ve güncel eventlerini göster
python -m scripts.run_asset_profile_preview --symbol GC=F --timeframe 1d

# Tüm grup için event önizlemesi (ör. metaller)
python -m scripts.run_asset_group_event_preview --asset-class metals --timeframe 1d

# Toplu şekilde feature pipeline'ı çalıştır
python -m scripts.run_asset_profile_batch_build --limit 10 --timeframe 1d

# Data lake içindeki asset profile ve group feature dosyalarının durumunu kontrol et
python -m scripts.run_asset_profile_status
```

## Sinyal Aday Skorlama ve Candidate Pool Katmanı

- Bu faz nihai al/sat stratejisi değildir.
- Sistem eventleri normalize eder, skorlar ve aday havuzuna alır.
- Candidate score emir değildir.
- Directional bias emir değildir.
- Passed pre-filter canlı işlem izni değildir.
- Bu katman ileride strateji, backtest, paper trade ve Telegram rapor sistemine veri sağlayacaktır.
- Missing event/context grupları kalite skorunu etkiler.
- Conflict score yüksekse aday zayıflatılır.

### Komutlar
```bash
python -m scripts.run_signal_candidate_preview --symbol GC=F --timeframe 1d
python -m scripts.run_signal_batch_build --limit 10 --timeframe 1d
python -m scripts.run_signal_pool_preview --timeframe 1d --top 20
python -m scripts.run_signal_status
```


## Yönsel Ön Karar / Decision Candidate Katmanı
Bu katman signal candidate havuzundan yönsel bias, conflict, neutral/no-trade ve strategy readiness ayrıştırması yapar.

- Bu faz nihai al/sat stratejisi değildir.
- `long_bias_candidate` gerçek long emri değildir.
- `short_bias_candidate` gerçek short emri değildir.
- `no_trade_candidate` sadece kalite/çelişki nedeniyle adayın strateji motoruna aktarılmamasını gösterir.
- Decision score emir değildir.
- `passed_decision_filters` canlı işlem izni değildir.
- Bu katman ileride strateji motoru, backtest, paper trade ve Telegram raporlama için kullanılacaktır.
- Conflict ve neutral filtreleri düşük kaliteli adayları ayrıştırır.

### Komutlar
```bash
python -m scripts.run_decision_candidate_preview --symbol GC=F --timeframe 1d
python -m scripts.run_decision_batch_build --limit 10 --timeframe 1d
python -m scripts.run_decision_pool_preview --timeframe 1d --top 20
python -m scripts.run_decision_status
```

## Risk Ön Kontrol / Pre-Trade Risk Candidate Katmanı

- Bu faz nihai risk motoru değildir.
- Risk approval candidate gerçek işlem onayı değildir.
- Risk rejection candidate gerçek emir iptali değildir.
- Risk watchlist candidate sadece izleme/raporlama bağlamıdır.
- Stop-loss, take-profit, position sizing ve leverage bu fazda yoktur.
- Risk skorları 0 düşük risk, 1 yüksek risk olarak yorumlanır.
- Risk readiness score 1 iyi, 0 zayıf olarak yorumlanır.
- Bu katman ileride backtest, position sizing, paper trade ve Telegram rapor sistemine veri sağlayacaktır.

```bash
python -m scripts.run_risk_precheck_preview --symbol GC=F --timeframe 1d
python -m scripts.run_risk_batch_build --limit 10 --timeframe 1d
python -m scripts.run_risk_pool_preview --timeframe 1d --top 20
python -m scripts.run_risk_status
```


## Teorik Position Sizing Candidate Katmanı

- Bu faz gerçek position sizing motoru değildir.
- theoretical_units gerçek lot/adet/kontrat değildir.
- theoretical_notional gerçek portföy emri değildir.
- sizing_approved_candidate gerçek işlem onayı değildir.
- sizing_rejected_candidate gerçek emir iptali değildir.
- Bu katman ATR, volatilite, risk readiness ve teorik risk bütçesine göre simülasyon amaçlı sizing adayları üretir.
- Gerçek stop-loss, take-profit, leverage, broker emri, paper trade ve canlı işlem yoktur.
- Bu katman ileride backtest ve paper trade simülasyonlarının temel girdilerinden biri olacaktır.

**Komutlar:**
```bash
python -m scripts.run_sizing_candidate_preview --symbol GC=F --timeframe 1d
python -m scripts.run_sizing_batch_build --limit 10 --timeframe 1d
python -m scripts.run_sizing_pool_preview --timeframe 1d --top 20
python -m scripts.run_sizing_status
```


## Teorik Stop/Target Level Candidate Katmanı

Bu faz gerçek stop-loss/take-profit motoru değildir.
theoretical_stop_level gerçek stop-loss emri değildir.
theoretical_target_level gerçek take-profit emri değildir.
invalidation_zone gerçek stop veya pozisyon kapatma talimatı değildir.
reward_risk gerçek trade planı değil simülasyon metriğidir.
Level candidate katmanı ATR, structure, volatility adjustment ve reward/risk hesapları üretir.
Gerçek emir, broker, paper trade, pozisyon açma/kapama yoktur.
Bu katman ileride backtest ve paper trade simülasyonlarının seviye girdilerinden biri olacaktır.

Komutları ekle:
```bash
python -m scripts.run_level_candidate_preview --symbol GC=F --timeframe 1d
python -m scripts.run_reward_risk_preview --symbol GC=F --timeframe 1d
python -m scripts.run_level_batch_build --limit 10 --timeframe 1d
python -m scripts.run_level_status
```


## Backtest Motoru İskeleti ve Trade Lifecycle Simülasyonu

- Bu faz canlı işlem değildir.
- Backtest sonuçları gerçek performans iddiası değildir.
- Entry/exit/stop/target ifadeleri tarihsel simülasyon objeleridir.
- Lookahead guard kullanılır.
- Entry varsayılan olarak sonraki bar open ile simüle edilir.
- Same-bar exit default kapalıdır.
- Intrabar stop/target ambiguity konservatif varsayımla çözülür.
- Fee/slippage simülasyon varsayımlarıdır.
- Bu katman ileride daha gelişmiş performans analizi, optimizer ve paper trade için temel sağlar.

Komutlar:
```bash
python -m scripts.run_backtest_preview --symbol GC=F --timeframe 1d
python -m scripts.run_backtest_batch --limit 10 --timeframe 1d
python -m scripts.run_backtest_trade_ledger_preview --symbol GC=F --timeframe 1d
python -m scripts.run_backtest_status
```


## Gelişmiş Backtest Performans Analizi ve Benchmark Kıyaslama

- Bu faz canlı işlem değildir.
- Performans metrikleri tarihsel simülasyon çıktısıdır.
- Sharpe, Sortino, Calmar, profit factor, max drawdown, expectancy gibi metrikler üretilir.
- Strateji simülasyonu USDTRY, altın, emtia sepeti, TR CPI ve US CPI ile kıyaslanabilir.
- Enflasyon karşısında reel getiri analizi yapılır.
- Benchmark kıyasları yatırım tavsiyesi değildir.
- Az trade sayısı, eksik benchmark, yetersiz veri gibi durumlarda quality warning üretilir.

**Çalıştırma Komutları:**
```bash
python -m scripts.run_performance_report_preview --symbol GC=F --timeframe 1d
python -m scripts.run_benchmark_comparison_preview --symbol GC=F --timeframe 1d
python -m scripts.run_inflation_adjusted_performance --symbol GC=F --timeframe 1d
python -m scripts.run_performance_batch --limit 10 --timeframe 1d
python -m scripts.run_performance_status
```


## Walk-Forward Validation, Parameter Sensitivity ve Optimizer Candidate Katmanı

DİKKAT:
- Bu faz canlı optimizer değildir.
- Walk-forward sonuçları tarihsel validasyon çıktısıdır.
- In-sample/out-of-sample ayrımı yapılır.
- Parameter sensitivity yüksekse overfitting riski artabilir.
- `optimizer_candidate_passed` etiketi gerçek canlı strateji seçimi değildir.
- Robustness score garanti değildir.
- Overfitting risk score araştırma uyarısıdır.
- Bu katman ileride daha güvenilir optimizer, model selection ve paper trade hazırlığı için temel sağlar.

Komutlar:
```bash
python -m scripts.run_walk_forward_preview --symbol GC=F --timeframe 1d
python -m scripts.run_parameter_sensitivity_preview --symbol GC=F --timeframe 1d
python -m scripts.run_optimizer_candidate_preview --symbol GC=F --timeframe 1d
python -m scripts.run_validation_batch --limit 10 --timeframe 1d
python -m scripts.run_validation_status
```

## ML Dataset Hazırlığı ve Target Engineering (Phase 29)

Bu proje aynı zamanda gelecekteki Machine Learning model eğitimleri için bir altyapı sunar. Bu faz model eğitimi değildir, sadece ML için leakage-safe (geleceğe sızmasız) feature matrix ve target frame üretir.

Özellikler:
- Forward return, direction class, future volatility, future drawdown ve candidate outcome targetları desteklenir.
- Target kolonları feature olarak kullanılamaz.
- Chronological split kullanılır; random split/shuffle yoktur.
- Purging ve embargo desteklenir.
- Leakage audit raporu üretilir.

*Not: "Dataset ready candidate" durumu, model hazır veya canlı sinyal anlamına gelmez.*

Komutlar:
```bash
python -m scripts.run_ml_dataset_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_target_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_dataset_batch_build --limit 10 --timeframe 1d
python -m scripts.run_ml_dataset_status
```


## Offline ML Baseline Training ve Model Evaluation (Phase 30)

Bu faz canlı prediction değildir. Model training sadece offline/research amaçlıdır.
- Dummy, Logistic Regression, Random Forest ve HistGradientBoosting baseline modelleri desteklenir.
- Chronological CV kullanılır; random shuffle yoktur.
- Preprocessing train set üzerinde fit edilir, validation/test sadece transform edilir.
- Model registry deploy sistemi değildir.
- `registered_candidate` canlı model onayı değildir.
- Evaluation metrikleri gelecek performans garantisi değildir.
- Model çıktısı canlı sinyal veya yatırım tavsiyesi değildir.

**Komutlar:**
```bash
python -m scripts.run_ml_training_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_model_evaluation_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_training_batch --limit 10 --timeframe 1d
python -m scripts.run_ml_model_registry_status
python -m scripts.run_ml_model_artifact_status
```
