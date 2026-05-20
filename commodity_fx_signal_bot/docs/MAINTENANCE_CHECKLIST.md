# Maintenance Checklist

## Her faz sonrası checklist
- `pytest` tüm testlerin geçtiğinden emin ol.
- `security audit` çalıştır ve secret olmadığından emin ol.
- `system healthcheck` çalıştır.
- `import smoke test` çalıştır.
- `CLI help audit` çalıştır.
- `docs audit` çalıştır.

## Haftalık bakım checklist
- Data/lake backup planını kontrol et (çok büyüyen dosyaları sil).
- Dependency check yap (yeni versiyon var mı).
- Model artifact boyutlarını kontrol et, çok eskileri sil.

## Repo Hygiene ve Secret Checklist
- `.env` gitignore dışında OLMAMALI.
- Model artifact (örnek: `.joblib`) klasörleri `.gitignore` içinde olmalı.

## Release/Tag hazırlık checklist
- Tüm testler pass mi?
- Tüm DX raporları pass mi?
- README.md güncel mi?
- Yeni eklenen bir command için DOCS'ta veya help'te canlı emir ifadesi YOK mu? (Eğer varsa çıkartılmalıdır).
