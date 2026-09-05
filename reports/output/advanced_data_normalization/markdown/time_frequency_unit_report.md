# Phase 113 — Time, Frequency & Unit Normalization Report

> [!IMPORTANT]
> **YASAL UYARI VE GÜVENLİK SINIRI**:
> Bu çıktı Phase 113 Data Normalization Layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, normalized data’yı trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.


## Zaman, Frekans ve Birim Standartlaştırması
- **Kanonik Zaman Dilimi**: UTC (ISO 8601)
- **Kaynak Korundu**: True
- **Birim Değer Dönüşümü**: Ertelendi (Yalnızca sözlük standartlaştırıldı)

| canonical_timezone | iso_format | local_note_timezone | policy | source_preserved | current_phase |
| --- | --- | --- | --- | --- | --- |
| UTC | %Y-%m-%dT%H:%M:%SZ | Europe/Istanbul | Her zaman UTC kanonik saklanır; yerel saatler yalnızca rapor gösterimi içindir. | True | 113 |
