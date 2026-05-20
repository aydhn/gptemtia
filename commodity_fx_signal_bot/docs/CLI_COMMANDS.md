# CLI Commands Catalog

Projeyi yönetmek, verileri indirmek, stratejileri test etmek ve diagnostik raporlar üretmek için kullanılan CLI komutları.

## Komut Grupları
- Data komutları
- Feature komutları
- Candidate komutları
- Risk/Sizing/Level komutları
- Backtest/Performance komutları
- Validation komutları
- ML komutları
- Paper komutları
- Notification komutları
- Orchestration komutları
- Observability komutları
- Security komutları
- Devtools komutları

## Dry-run ve --run farkı
Sistemdeki komutlar varsayılan olarak `dry-run` mantığında çalışır. Herhangi bir notification göndermek için özel flag (örn: `--send`) gerekebilir.
ÖNEMLİ: Sistem ASLA canlı emir atmaz. O yüzden `--run` flag'leri bile sadece lokal dosya üretimi ve telegram mesajı atılmasını yönetir.

Lütfen komut detayları için `python -m scripts.run_cli_catalog` çalıştırıp güncel CLI listesini `reports/` altından okuyun.
