# GLOBAL PROJECT POLICY — LOCAL PAPER SIGNALS AND REAL-DATA BACKTESTS ARE ALLOWED

**Belge Durumu:** Aktif / Bağlayıcı Politika  
**Kapsam:** Tüm Modüller, Dokümantasyon, Kod Tabanı ve Geliştirici/Ajan Yönergeleri  
**Son Güncelleme:** 2026-09-17  

---

## 1. Kesin Yasak Olan Eylemler (Strictly Forbidden)

Aşağıdaki eylemler ve bileşenler bu projede koşulsuz olarak **YASAKTIR**:
1. **Gerçek Borsa / Broker Bağlantısı:** Gerçek broker/borsa API uç noktalarına bağlanmak, emir iletim adaptörleri açmak.
2. **Gerçek Emir Gönderimi:** Herhangi bir piyasaya canlı alım/satım/iptal emri iletmek.
3. **Gerçek Para ile Canlı İşlem:** Gerçek sermaye, canlı bakiye veya finansal hesaplar üzerinden canlı işlem yapmak.
4. **Broker API Key / Secret Kullanımı:** Gerçek işlem yetkisine sahip broker/borsa API anahtarı, gizli anahtar veya yetkilendirme belirteci kullanmak veya kodda/repoda barındırmak.
5. **Production Deployment:** Canlı finansal sisteme veya regüle piyasa üretim ortamına dağıtım yapmak.
6. **Yatırım Tavsiyesi Dili:** "Kesin kazanç", "al tavsiyesi", "sat tavsiyesi", "finansal tavsiye", "yatırım danışmanlığı" niteliğinde ifadeler kullanmak.
7. **Kâr Garantisi / Kesin Sonuç İddiası:** Herhangi bir modelin veya stratejinin kâr garantisi sunduğunu veya gelecekte kesin sonuç vereceğini iddia etmek.
8. **Scraping:** Web sitelerinden izinsiz HTML scraping, bot/browser automation ile veri kazıma veya telifli haber tam metinlerini izinsiz çekmek.
9. **Lookahead Bias / Future Leak:** Gelecekteki verinin eğitim, özellik çıkarımı veya backtest esnasında bugüne sızması (`shift(-k)`, gelecek pencereleri).

---

## 2. İzinli ve Hedeflenen Kapsam (Allowed & Targeted)

Aşağıdaki işlevler sistemin ana geliştirme hedefleri arasında olup **TAMAMEN İZİNLİDİR**:
1. **Gerçek Tarihsel Piyasa Verisiyle Backtest:** Lokal, offline veya güvenli veri sağlayıcı önbelleği (cache) üzerinden temin edilen gerçek tarihsel verilerle backtest yürütülmesi.
2. **Local Paper Trading Engine:** Tamamen yerel ortamda çalışan, gerçek broker ile hiçbir bağlantısı olmayan simülasyon motoru.
3. **Sanal Portföy & Muhasebe:** Sanal bakiye, sanal pozisyon defteri, sanal emir üretimi, sanal gerçekleşme (virtual fills) ve sanal PnL hesaplaması.
4. **Telegram Research / Paper-Trading Sinyalleri:** Telegram üzerinden araştırma ve kağıt üstü işlem (paper-trade) amacıyla sinyal iletimi.
5. **Açıklanabilir Sinyal Metadata:** Sinyal skoru, model güveni (confidence), risk skoru, rejim etiketi (regime label) ve strateji gerekçesi (strategy reason) sunulması.
6. **İleri Düzey Doğrulama & Dayanıklılık:** Walk-forward validasyon, örneklem dışı (Out-of-Sample / OOS) testler, benchmark kıyaslamaları, işlem maliyeti (transaction cost), kayma (slippage) ve Monte Carlo / robustness stres testleri.
7. **Local ML Training / Inference:** Yalnızca araştırma ve paper-trade bağlamında yerel makine öğrenmesi modellerinin (CPU/GPU) eğitilmesi ve tahmin/çıkarım yapması.
8. **Local Optimization:** Yalnızca araştırma, backtest ve paper-trade parametre tuning bağlamında yerel optimizasyon çalışmaları.

---

## 3. Terminoloji ve Mesajlaşma Standartları

- **Sinyal Üretimi:** "AL/SAT sinyali" üretilebilir ve raporlanabilir.
- **Yasal ve Fonksiyonel Ayrım:** Bu sinyaller bir “yatırım tavsiyesi”, “kesin al/sat talimatı”, “garantili işlem”, “gerçek emir” veya “broker talimatı” DEĞİLDİR.
- **Telegram Mesaj Formatı:** Telegram mesajlarında ve bildirimlerde operasyonel netlik için:
  - `PAPER BUY`
  - `PAPER SELL`
  - `PAPER EXIT`
  - `WATCH`
  - `HOLD`
  standart terminolojisi tercih edilmelidir.
- **Etiketleme Zorunluluğu:** Her sinyal çıktısında ve Telegram mesajında belirgin bir biçimde `[LOCAL PAPER-TRADE / RESEARCH-ONLY]` etiketi ve sorumluluk reddi (disclaimer) yer almalıdır.

---

## 4. Paper Trade Motoru Tanımı

- **İşlevsellik:** Paper trade engine bağımsız bir yerel süreçtir. Gerçek broker emri göndermez.
- **Kapsam:** Yalnızca lokal pozisyon defteri, sanal nakit bakiyesi, sanal limit/market emirleri, gerçekçi kayma ve komisyon içeren sanal gerçekleşme ve sanal kâr/zarar (PnL) üretir.
- **Prensip:** Bir "Paper Order", hiçbir koşulda gerçek bir finansal emir değildir.

---

## 5. Backtest Standartları ve Metodolojik Güvenceler

- **Veri Gerçekçiliği:** Backtestler gerçek tarihsel piyasa verisiyle icra edilmelidir; sentetik ve yapay varsayımlar tek başına yeterli kabul edilmez.
- **Performans Yanılgısı:** Geçmiş backtest sonuçları gelecekteki performansın garantisi veya taahhüdü değildir.
- **Metodolojik Kontroller:** Aşağıdaki riskler açıkça kontrol edilmeli, loglanmalı ve guard kontrolleriyle denetlenmelidir:
  - Lookahead bias & data leakage,
  - Target leakage,
  - Survivorship bias (hayatta kalma yanlılığı),
  - Data snooping & multiple testing yanılgısı,
  - Aşırı öğrenme (overfitting),
  - Gerçekçi spread, komisyon ve slippage maliyetleri.

---

## 6. Geçmiş Faz İfadelerinin Yorumlanması (Historical Clause Interpretation)

Önceki fazlarda ve dokümanlarda geçen:
- `signal_generation_disabled`
- `prediction_disabled`
- `backtest_execution_disabled`
- `training_disabled`
- `broker_ready_disabled`
- `live_trading_disabled`

gibi ifadeler ve raporlama bayrakları, **YALNIZCA VE SADECE** canlı broker bağlantısı, gerçek para ile işlem, üretim ortamı dağıtımı veya yatırım tavsiyesi bağlamında anlaşılmalıdır.

Bu ifadeler; **yerel araştırma (local research), gerçek verili backtest simülasyonları, yerel model eğitimi/çıkarımı (local ML inference), Telegram paper sinyalleri ve yerel paper trade motorunun çalışmasını YASAKLAMAZ**.

---

## 7. Git İş Akışı, Master Branch ve Her Faz Sonu Senkronizasyon Kuralı (Mandatory Git Sync Policy)

Bu kural, projede çalışan **TÜM YAPAY ZEKA ARAÇLARI, AJANLAR VE GELİŞTİRİCİLER** için bağlayıcıdır:
1. **Daima `master` Branch:** Tüm geliştirmeler, hata düzeltmeleri ve fazlar doğrudan `master` branch üzerinde gerçekleştirilir. Yan/ayrı branch açılmayacaktır.
2. **Her Faz Sonu Zorunlu Commit + Push:** Tamamlanan her fazın ve mantıksal geliştirme bloğunun ardından derhal `git add .`, anlamlı bir `git commit` ve doğrudan `git push origin master` yapılacaktır.
3. **Senkronizasyon ve Temiz Çalışma:** `origin/master` = `yerel master` olmalı, repo asla "dirty" (uncommitted/untracked) bırakılmamalıdır. Her iki taraf daima tam hizalı tutulacaktır.

