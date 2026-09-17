# gptemtia

**Yerel / Çevrimdışı Emtia ve Döviz (Commodity & FX) Araştırma, Simülasyon ve Sinyal Platformu**

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Branch: master](https://img.shields.io/badge/branch-master-brightgreen.svg)]()
[![Status: Phase 160 Completed](https://img.shields.io/badge/phase-160%2F160%20completed-success.svg)]()
[![Policy: Strict Offline Research](https://img.shields.io/badge/policy-strict%20offline%20research-red.svg)]()

---

## 1. GELİŞTİRİCİ & AJAN ÇALIŞMA KURALLARI (MANDATORY WORKSPACE RULES)

> [!IMPORTANT]
> Projede çalışan tüm yapay zeka ajanları ve geliştiriciler aşağıdaki temel kurallara istisnasız uymak zorundadır:
> 1. **HER ZAMAN master BRANCH:** Tüm geliştirme, hata düzeltmesi, refactoring ve testler doğrudan master branch\'inde yapılır.
> 2. **HER FAZ SONU ZORUNLU COMMIT + PUSH:** Tamamlanan her mantıksal iş bloğunun ardından git add ., anlamlı bir git commit ve doğrudan git push origin master yapılır.
> 3. **ORIGIN/MASTER = YEREL MASTER (%100 SENKRON):** Git çalışma ağacı asla kirli (dirty) bırakılmaz; yerel ile remote daima tam senkron ve hizalı tutulur.

---

## 2. KATİ PROJE POLİTİKASI (GLOBAL_PROJECT_POLICY.md)

Bu proje salt çevrimdışı, yerel araştırma, simülasyon ve eğitim amaçlıdır. Canlı finansal operasyonlar sözleşmelerle engellenmiştir:

- **KESİNLİKLE YASAK:**
  - Canlı borsa/broker/exchange API bağlantısı
  - Canlı piyasaya gerçek emir iletimi ve gerçek para kullanımı
  - Canlı üretim ortamı (production deployment) ve bulut deployment\'ı
  - Yatırım tavsiyesi veya yönlendirici finansal tavsiye dili
  - Web kazıma (scraping), yetkisiz API çağrıları veya tersine mühendislik
  - Lookahead bias (gelecek verisi sızıntısı) ve veri sızıntısı (data leakage)

- **İZİNLİ VE HEDEFLENEN:**
  - Gerçek tarihsel piyasa verisiyle yerel backtest simülasyonları
  - Yerel sanal işlem motoru (Paper Trading: sanal bakiye, sanal emirler, sanal fill, sanal PnL)
  - Telegram araştırma/paper-trade bildirimleri (PAPER BUY, PAPER SELL, PAPER EXIT, WATCH, HOLD)
  - Yerel CPU/GPU Makine Öğrenimi model eğitimi, doğrulama ve çıkarımı
  - Açıklanabilir risk, çoklu-rejim (regime transition) ve Monte Carlo sağlamlık analizleri

---

## 3. PROJE MİMARİSİ VE 160 FAZLIK GELİŞTİRME PLANI

Proje, 160 fazlık kapsamlı kurumsal mimari planını %100 tamamlamıştır (inal_plan_closed=True):

### Blok 1: MVP Katmanı (Phase 1 - 100)
- commodity_fx_signal_bot çekirdek paketi
- Teknik indikatörler, rejim modelleri ve sinyal filtreleri
- Yerel veri gölü (DataLake) ve yerel öznitelik deposu (FeatureStore)
- Yerel kurtarma (DR), denetim izi ve yerel yönetişim kilitleri

### Blok 2: Full Advanced Katmanı (Phase 101 - 160)
- Multi-domain veri sağlayıcı soyutlaması (Emtia, Döviz, Makro, Ekonomik Takvim, Haber Metadata)
- Cross-asset özellik hizalama ve çoklu rejim matrisleri
- GPU hızlandırmalı ML çalışma zamanı (PyTorch / Scikit-Learn)
- Model drift izleme, kalibrasyon belirsizliği ve açıklanabilirlik (SHAP/LIME yerel)
- Yürütme maliyeti modelleri (slippage, spread, turnover) ve Walk-Forward doğrulama
- Portföy optimizasyonu, risk bütçeleme ve Monte Carlo stres testleri
- Nihai dondurma, denetim mühürleri ve Operatör El Kitabı

---

## 4. DİZİN YAPISI

`	ext
c:\Projelerim\gptemtia\
├── .cursorrules                       # Cursor ajan kural yapılandırması
├── .env.example                       # Çevre değişkenleri güvenli şablonu
├── .gitignore                         # Git yok sayma kuralları
├── .windsurfrules                     # Windsurf ajan kuralları
├── AGENTS.md                          # Zorunlu Git ve çalışma kuralları
├── CLAUDE.md                          # Claude rehberi
├── GEMINI.md                          # Gemini çalışma prensipleri
├── GLOBAL_PROJECT_POLICY.md           # Temel proje ilkeleri ve güvenlik sınırları
├── README.md                          # Bu doküman
├── main.py                            # Ana çalıştırma giriş noktası
│
├── advanced_*/                        # 50+ Gelişmiş modül (Veri, ML, Rejim, Portföy, vb.)
│   ├── advanced_data_providers/       # Sağlayıcı soyutlama katmanı
│   ├── advanced_commodity_providers/  # Emtia veri sözleşmeleri ve evreni
│   ├── advanced_fx_providers/         # Döviz çifti sözleşmeleri
│   ├── advanced_feature_engine/       # Öznitelik hesaplama motoru
│   ├── advanced_regime_matrix/        # Piyasa rejimi matrisi
│   ├── advanced_gpu_ml_runtime/       # GPU/CPU ML yürütme katmanı
│   ├── advanced_realistic_backtest/   # Gerçekçi backtest simülasyonu
│   ├── advanced_monte_carlo_robustness/ # Monte Carlo stres analizleri
│   └── advanced_final_delivery/       # Phase 160 nihai teslimat ve kapanış
│
├── commodity_fx_signal_bot/           # MVP temel bot paketi ve yerel operasyonlar
├── config/                            # Proje ayarları (settings.py, paths.py)
├── data/                              # Yerel veri gölü (data/lake/) ve ham girdiler
├── docs/                              # Dokümantasyon kütüphanesi (15+ rehber)
│   ├── PHASE_LOG.md                   # 160 fazın eksiksiz geçmiş günlüğü
│   ├── ARCHITECTURE.md                # Detaylı sistem mimarisi
│   ├── OPERATOR_MANUAL.md             # Operatör kılavuzu
│   ├── ANALYST_HANDBOOK.md            # Analist el kitabı
│   └── SAFE_USAGE_GUIDE.md            # Güvenli kullanım rehberi
├── ml/                                # Model kayıtları ve feature store entegrasyonu
├── reports/                           # Rapor motoru (report_builder.py) ve çıktılar
├── scripts/                           # 600+ Operasyonel CLI çalıştırma betiği
└── tests/                             # 2500+ Kapsamlı birim ve entegrasyon testi
`

---

## 5. HIZLI BAŞLANGIÇ & CLI KULLANIMI

Sistem üzerinde operasyonel kontrolleri ve rapor üretimlerini yürütmek için CLI betiklerini çalıştırabilirsiniz:

### 1. Sistem Sağlık Denetimi
`ash
python -m scripts.run_final_delivery_health_check
`

### 2. Nihai Teslimat Doğrulama Raporu
`ash
python -m scripts.run_final_delivery_validation_report
`

### 3. Phase 160 Tamamlanma Raporu
`ash
python -m scripts.run_final_160_phase_completion_report
`

### 4. Birim Testleri Çalıştırma
`ash
# Örnek test çalıştırması
pytest tests/test_advanced_config.py
pytest tests/test_final_delivery_report_builder.py

# Belirli bir fazın testleri
python -m scripts.run_phase_130_tests
python -m scripts.run_phase_150_tests
`

---

## 6. DOKÜMANTASYON REHBERİ

Daha ayrıntılı bilgi için lütfen docs/ dizinindeki belgeleri inceleyiniz:

| Doküman | Açıklama |
| :--- | :--- |
| [docs/PHASE_LOG.md](docs/PHASE_LOG.md) | 160 fazın her birinin detaylı geliştirme ve kabul kayıtları |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Uçtan uca sistem bileşen ve veri akış mimarisi |
| [docs/OPERATOR_MANUAL.md](docs/OPERATOR_MANUAL.md) | Operatörler için çalıştırma, izleme ve güvenlik prosedürleri |
| [docs/ANALYST_HANDBOOK.md](docs/ANALYST_HANDBOOK.md) | Sinyal, rejim ve backtest analistleri rehberi |
| [docs/SAFE_USAGE_GUIDE.md](docs/SAFE_USAGE_GUIDE.md) | Güvenli yerel kullanım sınırları ve No-Go kuralları |
| [docs/CONFIGURATION.md](docs/CONFIGURATION.md) | Profil, ortam değişkenleri ve ayarlar dokümantasyonu |
| [docs/ROADMAP.md](docs/ROADMAP.md) | Sistem yol haritası ve gelecek vizyonu |
| [GLOBAL_PROJECT_POLICY.md](GLOBAL_PROJECT_POLICY.md) | Proje güvenlik ve etik ilkeleri |
