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

## Phase 30: Offline ML Baseline Training ve Model Evaluation

- Bu faz canlı prediction değildir.
- Model training sadece offline/research amaçlıdır.
- Dummy, Logistic Regression, Random Forest ve HistGradientBoosting baseline modelleri desteklenir.
- Chronological CV kullanılır; random shuffle yoktur.
- Preprocessing train set üzerinde fit edilir, validation/test sadece transform edilir.
- Model registry deploy sistemi değildir.
- registered_candidate canlı model onayı değildir.
- Evaluation metrikleri gelecek performans garantisi değildir.
- Model çıktısı canlı sinyal veya yatırım tavsiyesi değildir.

Komutlar:
```bash
python -m scripts.run_ml_training_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_model_evaluation_preview --symbol GC=F --timeframe 1d
python -m scripts.run_ml_training_batch --limit 10 --timeframe 1d
python -m scripts.run_ml_model_registry_status
python -m scripts.run_ml_model_artifact_status
```


## ML Context Integration ve Model-Aware Candidate Scoring
Bu faz canlı ML sinyal motoru değildir.
ML prediction context signal/decision/strategy katmanlarına düşük ağırlıklı bağlam olarak entegre edilir.
Model supportive alignment trade onayı değildir.
Model conflict alignment gerçek emir yasağı değildir.
Model-aware score canlı sinyal değildir.
High uncertainty model etkisini düşürür.
Leakage/model quality fail durumları ML context kalitesini düşürür.
Research-only profile skorlamaya etki etmeden sadece rapor üretir.

Komutlar:
```bash
python -m scripts.run_ml_context_integration_preview --symbol GC=F --timeframe 1d
python -m scripts.run_model_alignment_preview --symbol GC=F --timeframe 1d --layer decision
python -m scripts.run_ml_conflict_filter_preview --symbol GC=F --timeframe 1d --layer decision
python -m scripts.run_ml_integration_batch --limit 10 --timeframe 1d
python -m scripts.run_ml_integration_status
```


## Telegram Raporlama ve Notification Katmanı (Phase 34)
Sistemde sadece raporlama, özetleme ve hata uyarı amaçlı bir Telegram katmanı bulunmaktadır.
- Telegram **yalnızca raporlama** kanalıdır.
- Default olarak Telegram kapalı ve `dry-run` (simülasyon) açıktır.
- Gerçek token/chat_id `.env` üzerinden verilir, repoya yazılmaz.
- Telegram mesajları **canlı sinyal değildir**.
- Paper summary sanal portföy raporudur. Quality alert trade alarmı değildir.
- Günlük digest araştırma ve simülasyon özetidir.
- Dashboard, broker entegrasyonu, gerçek emir, web scraping **kesinlikle yoktur**.

**Komutlar:**
```bash
python -m scripts.run_telegram_test_message
python -m scripts.run_telegram_paper_summary --symbol GC=F --timeframe 1d
python -m scripts.run_telegram_system_status
python -m scripts.run_telegram_daily_digest --timeframe 1d
python -m scripts.run_telegram_quality_alerts --timeframe 1d
python -m scripts.run_notification_status
```

**Güvenli Gönderim Örneği:**
1. Önce dry-run çalıştırın.
2. `.env` içine `TELEGRAM_ENABLED=true`, `TELEGRAM_DRY_RUN=false`, `TELEGRAM_BOT_TOKEN` ve `TELEGRAM_CHAT_ID` değerlerini ekleyin.
3. Sonra ilgili komutu `--send` parametresiyle çalıştırın.
Token bilgileri hiçbir log dosyasına kaydedilmez.


## Observability, Healthcheck, and Self-Diagnostics (Phase 36)

Bu faz canlı monitoring veya broker takip sistemi değildir.
Sistem sağlık raporu, dependency diagnostics, data freshness, artifact integrity ve runtime metrics üretir.
Structured logging JSON/file/console destekler.
Error taxonomy standart hata kodları sağlar.
Self-diagnostics recommended system actions üretir; bunlar trade önerisi değildir.
Secret/token bilgileri loglarda maskelenir.
Health status trade alarmı değildir.

Kullanılabilir Komutlar:
```bash
python -m scripts.run_system_healthcheck
python -m scripts.run_component_healthcheck --timeframe 1d
python -m scripts.run_data_freshness_check --timeframe 1d
python -m scripts.run_artifact_integrity_check
python -m scripts.run_runtime_metrics_report
python -m scripts.run_error_taxonomy_report
python -m scripts.run_self_diagnostics --timeframe 1d
python -m scripts.run_observability_status
```

---

## Proje Amacı
Bu proje emtia ve FX kurları üzerinde çevrimdışı (offline) araştırma yapmak, veri toplamak, teknik ve makro analizler uygulamak ve bu modelleri Telegram üzerinden raporlamak üzere tasarlanmıştır.

## Güvenlik ve Sınırlar
**Bu sistem ASLA canlı emir göndermez. Broker bağlantısı içermez.** Yapılacak bütün işlemler bir paper trading simülasyonu mantığıyla değerlendirilmeli ve asla yatırım tavsiyesi olarak kullanılmamalıdır.

## Bu Sistem Ne Değildir?
- Canlı trading botu değildir.
- Broker emir yönlendiricisi değildir.
- Yatırım tavsiye aracı değildir.

## Kurulum
Lütfen kurulum detayları için `docs/DEVELOPER_SETUP.md` dosyasını okuyun. Kısaca:
`python -m v` `env .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`
`cp .env.example .env`


## Hızlı Başlangıç
Sistemin çalıştığını doğrulamak için:
```bash
python -m scripts.run_system_healthcheck
```

## CLI Komutları
Tüm CLI komutları için `docs/CLI_COMMANDS.md` dosyasına bakınız veya:
```bash
python -m scripts.run_cli_catalog
```

## Dry-Run Workflow
Tam sistemi dry-run olarak (hiçbir aksiyon almadan) çalıştırmak için:
```bash
python -m scripts.run_daily_research_workflow --timeframe 1d
```

## Paper Trading Simülasyonu
Stratejileri test etmek için paper trade simülasyonu kullanılır, kesinlikle live_trade_enabled True yapılamaz.

## Offline ML Research
Tahminleme için scikit-learn modellerini kullanır (bkz `ml/` klasörü).

## Telegram Raporlama
Sinyal ve sonuç raporları Telegram ile gönderilebilir.

## Orchestration
Komutlar `scripts/` klasöründen izole olarak veya `orchestration` altından tek zincirde çağrılır.

## Observability
Loglama ve sistem metrikleri offline incelenebilir. Arka planda çalışan bir daemon yoktur.

## Security Audit
Projenin secret ve dosya güvenliğini test etmek için:
```bash
python -m scripts.run_security_audit
```

## Developer Tools
DX kalitesini korumak için `devtools/` araçları sağlanmıştır:
```bash
python -m scripts.run_dx_quality_report
```

## Testler
Tüm testleri koşturmak için `make test` veya `python -m pytest` kullanabilirsiniz.

## Sorun Giderme
Sık karşılaşılan sorunlar için `docs/TROUBLESHOOTING.md` dosyasına bakabilirsiniz.

## Faz Geçmişi
Gelişim detayları `docs/PHASE_LOG.md` içindedir.

## Lisans / Notlar
Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.

## Research Reports (Phase 39)

The Research Reports module generates user-readable offline research reports in Markdown, CSV, and TXT formats from simulation and analytics data.

**Important Note:** Research reports are strictly offline simulation findings and do not contain or constitute live trading signals, broker orders, or financial advice.

Available scripts:
- `python -m scripts.run_symbol_research_report --symbol GC=F --timeframe 1d`
- `python -m scripts.run_universe_research_report --asset-class metals --timeframe 1d --limit 20`
- `python -m scripts.run_daily_research_digest_report --timeframe 1d`
- `python -m scripts.run_research_ranking_report --timeframe 1d --limit 50`
- `python -m scripts.run_research_report_status`

These will output to `reports/output/research_reports`.

## Regime-Aware Portfolio Research and Stress Tests

- Regime-aware portfolio research gerçek portföy yönetimi değildir.
- Risk-on/risk-off label’ları canlı sinyal değildir.
- Macro scenario sensitivity tahmin değildir.
- Basket stress test gerçek risk limiti değildir.
- Drawdown clustering geçmiş/sanal sepet analizidir.
- Tail risk historical proxy’dir.
- Çıktılar data/lake/portfolio_regime ve reports/output/portfolio_regime altında oluşur.

Komutları:
```bash
python -m scripts.run_regime_portfolio_report --timeframe 1d --limit 20
python -m scripts.run_macro_scenario_sensitivity_report --timeframe 1d --limit 20
python -m scripts.run_basket_stress_test_report --timeframe 1d --limit 20
python -m scripts.run_drawdown_cluster_report --timeframe 1d
python -m scripts.run_risk_regime_exposure_report --timeframe 1d
python -m scripts.run_portfolio_regime_status
```

## Synthetic Benchmarks, Composite Indices and Relative Strength (Phase 43)

The bot includes an offline research infrastructure to generate synthetic benchmarks, composite indices, relative strength rankings, and universe rotation analysis.

**DISCLAIMER**:
- Synthetic benchmarks are not real financial benchmarks.
- Composite indices are not real index or ETF products.
- Relative strength "leader" is not a buy signal.
- "Laggard" label is not a sell signal.
- Universe rotation is not a real rotation execution.
- Outputs are for offline research only and do not constitute investment advice.

Outputs are generated under `data/lake/synthetic_indices` and `reports/output/synthetic_indices`.

Commands:
```bash
python -m scripts.run_synthetic_benchmark_report --timeframe 1d --limit 20
python -m scripts.run_composite_index_report --timeframe 1d --limit 30
python -m scripts.run_relative_strength_report --timeframe 1d --limit 30
python -m scripts.run_universe_rotation_report --timeframe 1d --limit 30
python -m scripts.run_leadership_laggard_report --timeframe 1d --limit 30
python -m scripts.run_synthetic_index_status
```

## Phase 44: Factor Research and Cross-Sectional Analysis

Factor research canlı strateji değildir.
Trend/momentum/value/carry/volatility factor skorları yatırım tavsiyesi değildir.
Carry ve value faktörleri proxy olarak üretilir; gerçek fundamental/carry verisi değildir.
Top-minus-bottom spread gerçek long-short portföy değildir.
Factor-neutral basket gerçek portföy değildir.
IC proxy ve factor decay geçmiş veri araştırma metrikleridir.
Çıktılar data/lake/factor_research ve reports/output/factor_research altında oluşur.

Komutlar:
```bash
python -m scripts.run_factor_research_report --timeframe 1d --limit 20
python -m scripts.run_factor_score_report --timeframe 1d --limit 20
python -m scripts.run_factor_backtest_report --timeframe 1d --limit 20
python -m scripts.run_factor_exposure_report --timeframe 1d --limit 20
python -m scripts.run_factor_neutral_report --timeframe 1d --limit 20
python -m scripts.run_factor_research_status
```


## Meta Research and Consensus Engine

Bu proje bir meta-research/kanıt ağırlıklandırma katmanı içerir (Phase 45).
Bu katman; teknik analiz, backtest, ML, sentetik endeks, makro rejim ve faktör araştırmalarından gelen verileri ağırlıklandırır ve araştırma kalitesine/güvenilirliğine göre düzenler.
Önemli Uyarı:
- Meta research canlı sinyal motoru değildir.
- Consensus score yatırım tavsiyesi değildir.
- Strong positive/negative consensus AL/SAT anlamına gelmez.
- Evidence weighting kaynak güvenilirliğine ve kaliteye göre araştırma skorlarını birleştirir.
- Conflict detection kaynaklar arası çelişkiyi gösterir.
- Quality-adjusted ranking sadece araştırma önceliklendirmesidir.
- Çıktılar `data/lake/meta_research` ve `reports/output/meta_research` altında oluşur.

Komutlar:
```bash
python -m scripts.run_meta_research_report --timeframe 1d --limit 20
python -m scripts.run_meta_consensus_report --timeframe 1d --limit 20
python -m scripts.run_evidence_conflict_report --timeframe 1d --limit 20
python -m scripts.run_quality_adjusted_ranking_report --timeframe 1d --limit 30
python -m scripts.run_meta_symbol_snapshot --symbol GC=F --timeframe 1d
python -m scripts.run_meta_research_status
```

## Phase 46: Experiment Tracking and Research Versioning
This phase adds a professional experiment tracking and versioning layer.
It includes components for:
- Hypothesis registry
- Experiment run manifests
- Research version records (config, environment, git, data snapshots)
- Artifact manifests
- Reproducibility manifests
- Ablation studies
- Baseline vs candidate comparison
- Experiment leaderboard

**Disclaimer**: This is an offline research tool. Experiment tracking does NOT generate live signals, execute trades, deploy models, or provide investment advice.

**Useful Commands:**
```bash
python -m scripts.run_hypothesis_registry_report
python -m scripts.run_experiment_tracking_report --timeframe 1d
python -m scripts.run_research_version_report
python -m scripts.run_ablation_study_report
python -m scripts.run_experiment_comparison_report
python -m scripts.run_experiment_leaderboard
python -m scripts.run_experiment_status
```

## Data Provenance, Lineage and Research Governance (Phase 47)
- Governance katmanı canlı trading governance değildir. Sadece offline research artifact'leri içindir.
- Artifact inventory data/lake ve reports/output dosyalarını tarar.
- Fingerprinting veri/artifact izlenebilirliği içindir.
- Provenance ve lineage graph kaynak/bağımlılık ilişkilerini araştırma bağlamında gösterir.
- Audit trail broker audit veya compliance onayı değildir.
- Dependency tracing approximation olabilir.
- Governance passed production compliance onayı değildir.
- Çıktılar data/lake/governance ve reports/output/governance altında oluşur.

### Governance Commands
```bash
python -m scripts.run_artifact_inventory_report
python -m scripts.run_lineage_graph_report
python -m scripts.run_provenance_report
python -m scripts.run_dependency_trace_report --symbol GC=F --direction upstream
python -m scripts.run_audit_trail_report
python -m scripts.run_research_governance_report
python -m scripts.run_governance_status
```

## Adaptive Research Planning and Backlog (Phase 48)

The project includes an offline research planning layer that generates automated research tasks, priority scores, and next-best-experiment recommendations based on outputs from the governance, validation, observability, and other modules.

- Research planning is not a live scheduler.
- The backlog is a list of research tasks; it does not trigger automatic execution.
- Priority scores are not live trading priorities.
- Next-best-experiment recommendations do not automatically start experiments.
- Research debt indicates maintenance risks, not trade alarms.
- Roadmap health reflects offline research capacity, not production readiness.
- Outputs are saved in `data/lake/research_planning` and `reports/output/research_planning`.

### Generating Planning Reports

```bash
python -m scripts.run_research_backlog_report --timeframe 1d
python -m scripts.run_priority_scoring_report --timeframe 1d
python -m scripts.run_next_best_experiment_report --timeframe 1d
python -m scripts.run_research_debt_report --timeframe 1d
python -m scripts.run_roadmap_health_report --timeframe 1d
python -m scripts.run_research_planning_status
```


## Knowledge Base, Research Memory and Analyst Workspace

The project includes an offline knowledge base and analyst workspace:
- Knowledge base local/offline çalışır.
- Ücretli embedding/API kullanmaz.
- Raporlar, docs, experiment, governance, planning ve meta-research çıktıları indexlenir.
- Retrieval result yatırım tavsiyesi değildir.
- Symbol memory card AL/SAT üretmez.
- Decision journal trade journal değildir.
- Findings digest trade fırsatı listesi değildir.
- Çıktılar `data/lake/knowledge_base` ve `reports/output/knowledge_base` altında oluşur.

### Komutlar:
```bash
python -m scripts.run_knowledge_index_report
python -m scripts.run_research_query --query "GC=F hakkında ne biliyoruz?"
python -m scripts.run_symbol_memory_report --symbol GC=F
python -m scripts.run_decision_journal_report
python -m scripts.run_recent_findings_digest
python -m scripts.run_analyst_workspace_status
```



## Offline Analyst Command Center (Phase 50)

The Offline Analyst Command Center aggregates all offline research, reporting, knowledge base, governance, experiment, and planning layers into safe command catalogs, guided workflows, safe runbooks, dry-run plans, project status, module health, script discovery, phase coverage, and project consolidation reports.

**Important Note:** The Command Center is NOT a live trading terminal.
- Safe command catalogs only list offline report, status, and query commands.
- Guided workflows do not auto-execute commands.
- Runbooks do not contain live execution or deployment instructions.
- Dry-run plans do not run commands; they only produce safe plans.
- Project consolidation is not production readiness.
- Analyst command queries only suggest safe offline commands.
- Outputs are saved under `data/lake/command_center` and `reports/output/command_center`.

**Available Commands:**
```bash
python -m scripts.run_command_catalog_report
python -m scripts.run_guided_workflow_report
python -m scripts.run_safe_runbook_report
python -m scripts.run_project_status_report
python -m scripts.run_project_consolidation_report
python -m scripts.run_analyst_command_query --query "GC=F için hangi raporları çalıştırmalıyım?"
python -m scripts.run_command_center_status
```


## Quality Gates, Local CI Validation and Release Candidate Preparation

The system includes an offline local validation and quality gate layer to ensure the safety and reliability of the codebase without connecting to any live execution system.

Important concepts:
- Quality gates are not production CI pipelines; they run locally and offline.
- A passed quality gate or "ready" release candidate label (`rc_ready_offline`) does NOT represent an approval for live trading, model deployment, or investment advice.
- The static safety scanner actively checks for forbidden patterns, such as live orders, background loops, or data scrapers.
- Smoke tests only execute offline, read-only commands without connecting to brokers or network instances.

Commands for quality checking:
- `python -m scripts.run_local_ci_validation`
- `python -m scripts.run_test_health_report`
- `python -m scripts.run_import_graph_report`
- `python -m scripts.run_repo_hygiene_report`
- `python -m scripts.run_dependency_audit_report`
- `python -m scripts.run_static_safety_scan`
- `python -m scripts.run_smoke_test_report`
- `python -m scripts.run_release_candidate_report`
- `python -m scripts.run_release_quality_gate_status`

Reports are saved to `data/lake/quality_gates` and `reports/output/quality_gates`.

## Performance Profiling, Resource Budgets and Large-Run Stability
- Performance profiling canlı trading latency optimizasyonu değildir.
- Resource budgets local/offline araştırma sınırlarıdır.
- GPU awareness GPU zorunluluğu veya model deployment değildir.
- Cache strategy dosya silmez; sadece policy/invalidation plan üretir.
- Batch plan otomatik execution başlatmaz.
- Checkpoint manifest canlı pozisyon state'i değildir.
- Large-run stability production readiness değildir.
- Çıktılar `data/lake/performance` ve `reports/output/performance` altında oluşur.

### Komutlar
```bash
python -m scripts.run_performance_profile_report
python -m scripts.run_resource_budget_report
python -m scripts.run_cache_strategy_report
python -m scripts.run_large_run_stability_report
python -m scripts.run_runtime_optimization_report
python -m scripts.run_performance_status
```


## Data Retention, Archive Strategy and Local Maintenance

Maintenance katmanı otomatik silme sistemi değildir. Default mod dry-run’dır. Cleanup candidates sadece incelenecek adaylardır.
Archive candidates otomatik taşınmaz. Source code, config, tests ve docs protected kabul edilir.
Retention policies local araştırma çıktıları içindir. Storage lifecycle health production readiness değildir.
Çıktılar `data/lake/maintenance` ve `reports/output/maintenance` altında oluşur.

```bash
python -m scripts.run_storage_inventory_report
python -m scripts.run_retention_policy_report
python -m scripts.run_cleanup_dry_run_report
python -m scripts.run_archive_dry_run_report
python -m scripts.run_storage_lifecycle_report
python -m scripts.run_maintenance_status
```

## Final System Review and Offline Acceptance

The final review layer provides comprehensive audits for architecture, safety, integration, data contracts, reports, documentation, quality gates, and system readiness.
Final review is an offline process and does not imply a production release.
The acceptance score is not an approval for live trading.
The safety audit strictly looks for broker execution, live trading, model deployment, background daemon, and web scraping risks.
The release readiness dry-run is a simulated check and does not perform any package publish or actual deployment.
The risk register lists project quality and safety risks, not financial investment risks.
The gap register lists missing offline components to track for follow-up.
Outputs are saved under `data/lake/final_review` and `reports/output/final_review`.

Commands:
```bash
python -m scripts.run_final_system_review
python -m scripts.run_architecture_audit
python -m scripts.run_safety_audit
python -m scripts.run_offline_acceptance_audit
python -m scripts.run_release_readiness_dry_run
python -m scripts.run_final_consolidation_audit
python -m scripts.run_final_review_status
```


## Scenario Regression, Golden Outputs and Deterministic Replay (Phase 57)

- Scenario regression canlı trading QA değildir.
- Golden output gerçek piyasa performans referansı değildir.
- Snapshot diff yatırım sinyali değildir.
- Deterministic replay yalnız synthetic/offline fixture üzerinde çalışır.
- Demo acceptance production acceptance değildir.
- Varsayılan olarak gerçek piyasa verisi indirilmez.
- Broker/live/deploy/daemon komutları blocked kabul edilir.
- Çıktılar `data/lake/scenario_regression` ve `reports/output/scenario_regression` altında oluşur.

### Komutlar
```bash
python -m scripts.run_scenario_regression_registry
python -m scripts.run_golden_output_report
python -m scripts.run_snapshot_comparison_report
python -m scripts.run_deterministic_replay_report
python -m scripts.run_demo_acceptance_report
python -m scripts.run_scenario_regression_status
```


## Local Analyst UX and Operator Productivity (Phase 58)

The Analyst UX layer improves the daily operational workflow for offline researchers and Codex agents.

- Analyst UX katmanı canlı trading assistant değildir.
- Natural-language-to-safe-command mapping komut çalıştırmaz, sadece güvenli offline öneri üretir.
- Command alias canlı emir alias'ı değildir.
- Prompt pack'ler Codex ajanına güvenli offline geliştirme yönergesi vermek içindir.
- Task board yatırım veya trading task board değildir.
- Query mapping internet araması yapmaz; local docs/runbook/command reference önerir.
- Çıktılar data/lake/analyst_ux ve reports/output/analyst_ux altında oluşur.

Available Commands:
```bash
python -m scripts.run_ux_alias_report
python -m scripts.run_safe_command_suggestions --query "final review durumunu kontrol et"
python -m scripts.run_prompt_pack_report
python -m scripts.run_productivity_checklist
python -m scripts.run_analyst_task_board
python -m scripts.run_operator_productivity_status
```


## Report Summarization, Analyst Briefs and Weekly Offline Review

Sistem, offline araştırma çıktılarını sentezleyerek üst düzey analiz ve özet paketleri sunar. Bu katman harici LLM kullanmaz.
Özetler yatırım tavsiyesi, canlı sinyal veya ticaret aksiyonu üretmez.
Çıktılar `data/lake/report_summarization` ve `reports/output/report_summarization` altında oluşur.

Mevcut raporları üretmek için:
```bash
python -m scripts.run_report_summary_registry
python -m scripts.run_executive_summary_report
python -m scripts.run_analyst_brief_report
python -m scripts.run_weekly_offline_review_pack
python -m scripts.run_research_digest_report
python -m scripts.run_summary_quality_report
python -m scripts.run_briefing_status
```

## Portable Packaging, Environment Snapshot and Install Verification
Bu proje local/offline bir bot altyapısıdır. Portable packaging özellikleri, environment snapshot, dependency inventory, install verification ve portable bundle manifest süreçlerini otomatikleştirir. Bu çıktıların hiçbiri production release, package publish, broker deploy veya canlı yatırım tavsiyesi değildir.

Komutlar:
```bash
python -m scripts.run_environment_snapshot
python -m scripts.run_dependency_inventory
python -m scripts.run_requirements_export
python -m scripts.run_install_verification
python -m scripts.run_portable_bundle_manifest
python -m scripts.run_reproducible_setup_guide
python -m scripts.run_packaging_status
```


## Backup/Restore Dry-Run and Disaster Recovery Planning

**Phase 62 added Backup/Restore Dry-Run & DR Planning to ensure local offline projects state can be safety backed up, without risking destructive overwrites, secret leaks or real deployment/trading triggers.**

- Backup recovery katmanı gerçek backup/restore sistemi değildir; default dry-run manifest üretir.
- Backup manifest dosya kopyalamaz.
- Restore dry-run dosya kopyalamaz, overwrite yapmaz, silmez.
- .env, secret, credential, token ve private key dosyaları excluded kalır.
- data/lake ve reports/output varsayılan olarak manifest-only recovery planında yer alır.
- Disaster recovery manifest production DR garantisi değildir.
- Restore verification gerçek restore garantisi değildir.
- Çıktılar data/lake/backup_recovery ve reports/output/backup_recovery altında oluşur.

### Backup Recovery Commands
```bash
python -m scripts.run_project_state_inventory
python -m scripts.run_backup_manifest_report
python -m scripts.run_backup_dry_run_plan
python -m scripts.run_restore_dry_run_plan
python -m scripts.run_disaster_recovery_manifest
python -m scripts.run_restore_verification_report
python -m scripts.run_backup_recovery_status
```

## Governance Evidence, Control Mapping and Audit Evidence Binder
Bu proje local/offline bir araştırma ortamıdır. Evidence governance katmanı resmi compliance sertifikası değildir.
Policy/control mapping project-local denetlenebilirlik içindir. Evidence binder cloud upload veya external auditor submission yapmaz. Evidence completeness/freshness score resmi uyum skoru değildir. Governance evidence export local manifest/index üretir. Secret/raw credential output yoktur. Çıktılar `data/lake/evidence_governance` ve `reports/output/evidence_governance` altında oluşur.

Komutlar:
```bash
python -m scripts.run_evidence_artifact_inventory
python -m scripts.run_policy_control_mapping
python -m scripts.run_audit_evidence_binder
python -m scripts.run_evidence_traceability_matrix
python -m scripts.run_governance_evidence_export
python -m scripts.run_evidence_quality_report
python -m scripts.run_evidence_status
```

## Research Artifact Metadata, Model Cards and Dataset Cards

Artifact metadata katmani model deployment onayi degildir.
Model cards canli trading veya broker execution icin kullanilamaz.
Dataset cards veri dogrulugu veya canli piyasa uygunlugu garantisi degildir.
Experiment/reproducibility cards gercek performans garantisi degildir.
Scenario/regression cards production readiness degildir.
Non-use policy her artefakt icin canli emir, broker execution, yatirim tavsiyesi ve deployment yasaklarini belirtir.
Ciktilar data/lake/artifact_metadata ve reports/output/artifact_metadata altinda olusur.

Komutlar:
```bash
python -m scripts.run_research_artifact_inventory
python -m scripts.run_model_dataset_cards
python -m scripts.run_experiment_reproducibility_cards
python -m scripts.run_scenario_regression_cards
python -m scripts.run_research_metadata_export
python -m scripts.run_metadata_quality_report
python -m scripts.run_metadata_status
```
