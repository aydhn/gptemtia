<!-- AUTO-GENERATED SECTION START -->
# Analist El Kitabı (Analyst Handbook)

> **UYARI / YASAL BİLDİRİM**
> Bu doküman ve açıklanan sistem yalnızca **offline/local araştırma platformu** kullanımını açıklar.
> Bu proje bir canlı alım-satım botu değildir. Gerçek emir göndermez, canlı sinyal üretmez, broker talimatı vermez ve gerçek pozisyon yönetmez.
> Model deployment, production scheduler veya otomatik trade özellikleri içermez.
> Bu projede üretilen hiçbir rapor veya sinyal **yatırım tavsiyesi değildir**.
> Eğitim, araştırma ve kağıt üzerinde test (paper trading) amacıyla geliştirilmiştir.


## Amaç
Bu kılavuz, üretilen finansal sinyal adaylarını, rejim raporlarını ve korelasyon matrislerini inceleyen analistler içindir.

## Kapsam
Modellerin, rejim filtrelerinin, sentetik endekslerin ve faktör araştırmalarının metodolojisi ve nasıl yorumlanacağı.


## Güvenlik Sınırları (Safety Boundaries)

Sistemin tasarımı gereği aşılmaması gereken sınırlar:
1. **Canlı Emir Yasağı:** Sistem broker API'lerine emir gönderecek kod içermez.
2. **Yatırım Tavsiyesi Yoktur:** Üretilen kararlar kesinlik bildirmez, araştırma hipotezidir.
3. **Daemon/Cron Yasağı:** Sistem sonsuz döngüde veya arka planda sessizce çalışacak şekilde tasarlanmamıştır. Manuel veya kontrollü script execution gerektirir.
4. **Web Dashboard Yok:** Dışarıya açık web sunucusu (Streamlit, Flask vb.) barındırmaz.
5. **Scraping Yasağı:** Selenium, Playwright veya BeautifulSoup ile veri kazıma işlemi yapmaz; sadece resmi/ücretsiz veri API'lerini kullanır.



## Local Timeline ve Change History (Phase 67)
- **Change history digest neden trading journal değildir?**: Bu sistem proje dosyalarındaki değişiklikleri listeler; gerçek piyasa emirlerini veya işlem kayıtlarını (trade journal) listelemez.
- **Timeline query nasıl kullanılır?**: `python -m scripts.run_timeline_query --query "Phase 60 sonrası hangi çıktılar oluştu?"` komutuyla offline timeline arayüzüne soru sorabilirsiniz. Yatırım tavsiyesi veya işlem sorgusu kabul edilmez.
- **Stale artifact warning nasıl okunur?**: Bir doküman veya rapor uzun süredir güncellenmediyse uyarılır. Modeller için bu, yeniden eğitim ihtiyacını düşündürebilir ancak otomatik aksiyon almaz.
- **Cloud event service, broker event, canlı emir, yatırım tavsiyesi ve production monitoring** işlevleri bulunmaz.

## Kullanım Örnekleri
- Backtest sonuçlarının (Sharpe, Max Drawdown) incelenmesi.
- Feature önem sırasının (feature importance) değerlendirilmesi.

## Üretilen Çıktılar
- Performans metrikleri
- ML model değerlendirme raporları


## Kapsam Dışı (Out of Scope)

Aşağıdaki özellikler kasıtlı olarak sisteme **dahil edilmemiştir**:
- Gerçek para ile işlem (Live Trading)
- Otonom (kendi kendine çalışan) üretim dağıtımı (Production Deployment)
- Otomatik alım-satım onayları (Auto Trade Approvals)
- Kar garantisi veya riskten arındırılmış getiri iddiaları


## Sık Hatalar
- Overfitting (aşırı öğrenme) ihtimalinin göz ardı edilmesi.
- Sinyal adaylarının kesin "AL/SAT" emri olarak yorumlanması.

## İlgili Komutlar
- `python -m scripts.run_backtest_report`
- `python -m scripts.run_model_evaluation`

## İlgili Klasörler
- `reports/output/ml/`
- `reports/output/backtest/`

## Uyarılar
Sinyal adayları kesin karar değildir; bir sonraki analiz katmanı için girdidir.

<!-- AUTO-GENERATED SECTION END -->


## Report Summarization
Sistem offline araştırma süreçlerinden elde edilen bulguları özetler:
- **Executive Summary:** Yatırım kararı özeti değildir. Offline kalite durumunu aktarır.
- **Analyst Brief:** Gerçek piyasa sinyali değildir. Odaklanılması gereken modülleri öne çıkarır.
- **Weekly Offline Review:** Piyasa strateji raporu değildir. Proje durum özetidir.
- **Symbol Brief:** AL/SAT üretmez, tavsiye barındırmaz.
- **Follow-up Tasks:** Safe/offline görevleridir. Kesinlikle live komut içermezler.
Bu katman harici LLM kullanmaz ve sadece local rule-based özetleme yapar.

## Evidence Governance and Audit Binder
Projedeki tüm safety, backup, packaging ve quality çıktılarını bir denetim paketinde toplamak için Phase 64 scriptlerini kullanın (örn. `run_audit_evidence_binder.py`, `run_evidence_traceability_matrix.py`). Policy/control mappingleri, traceability matrixleri ve evidence score'ları resmi/hukuki bir uyum sertifikasyonu (SOC2, ISO vb.) teşkil etmez, tamamen offline/local denetlenebilirlik amacını taşır.

## Artifact Metadata
Model card okuma rehberi, dataset card kullanim amaci, non-use policy onemi. Canli emir, broker execution, yatirim tavsiyesi, resmi sertifika ve deployment olmadigi acik yazilsin.

## Local Knowledge Graph (Phase 66)
- **Node/Edge Registry**: Lists all extracted artifacts and their relationships. Use to understand how components link together offline.
- **Artifact Relationship Graph**: Maps dependencies without external cloud/DB usage. Does not execute code.
- **Relationship Query**: Use for searching internal linkages (e.g. which report relates to which policy). Cannot generate investment advice or live commands.
- **Semantic Keyword/TF-IDF Index**: Local text index only. External vector DBs are strictly disabled.
- **Graph Centrality**: Purely structural metric. Does not denote investment opportunity or trading significance.
- **Graph Gap/Orphan/Stale Report**: Useful for internal consistency audits. Not an indicator of live market risks.
- **Notice**: No live trading, broker execution, external vector DB, cloud upload, or investment advice is provided by the Knowledge Graph tools.
