# Local Runbook

Günlük lokal çalışma sırası ve workflow zinciri.

## Günlük lokal çalışma sırası
1. **Health/Security/DX Kontrolleri**
   - `make health` (ya da python script)
   - `make security`
   - `make dx`
2. **Veri İndirme ve Ön İşleme**
   - Data pipeline çalıştırılır.
3. **Feature ve Candidate Üretimi**
   - Feature -> Signal -> Decision -> Strategy
4. **ML Research Zinciri (Opsiyonel)**
   - Model train/eval adımları.
5. **Backtest/Performance/Validation Zinciri**
   - Üretilen candidate'ler paper üzerinden backtest edilir.
6. **Paper Simulation Zinciri**
   - Sonuçlar paper defterine yazılır.
7. **Notification Dry-Run**
   - Telegram dry-run.

## Güvenli dry-run workflow
Sistemdeki tüm `--timeframe` komutlarını `1d` gibi küçük zaman aralıklarıyla vererek tüm modülleri dry-run modunda tek tek test edebilirsiniz. Workflow scriptlerini de test amaçlı kullanabilirsiniz.

## Run sonrası kontrol checklist
- Reports klasöründe ilgili csv/txt oluşmuş mu?
- .env dosyanız kazara commit'lenmeye hazır mı (gitignore'da değilse dikkat)?
- Parquet klasörü çok mu büyümüş? (bkz. Maintenance)
