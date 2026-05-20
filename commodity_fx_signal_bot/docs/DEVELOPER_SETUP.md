# Developer Setup Guide

## Amaç
Bu kılavuz, projeyi yerel ortamınızda güvenle ve tutarlı bir şekilde çalıştırmanız için gereken adımları içerir. Bu proje bir offline research botudur.

## Güvenlik Sınırları
Bu sistem **ASLA** canlı emir üretmez ve gerçek bir broker'a bağlanmaz. Yapacağınız geliştirmeler sadece araştırma, sinyal hesaplama ve simülasyon amaçlıdır.

## Python Sürümü
Gereken minimum sürüm **3.10**'dur.

## Sanal Ortam Kurulumu
Linux / macOS:
`python -m v` `env .venv`
`source .venv/bin/activate`

Windows:
`python -m v` `env .venv`
`.venv\Scripts\activate`

## Bağımlılık Kurulumu
`python -m pip install -r requirements.txt`
`python -m pip install -r requirements-dev.txt`

## .env Hazırlığı
`cp .env.example .env`
İlgili alanları doldurun.

## İlk Healthcheck
`python -m scripts.run_system_healthcheck`

## İlk Security Audit
`python -m scripts.run_security_audit`

## İlk Dry-Run Workflow
`python -m scripts.run_daily_research_workflow --timeframe 1d`

## İlk Paper Preview
`python -m scripts.run_paper_trading_preview`

## Telegram Dry-Run Test
`python -m scripts.run_telegram_report --dry-run`

## Testleri Çalıştırma
`python -m pytest`

## Sık Kurulum Hataları
Tüm kurulum hataları için `docs/TROUBLESHOOTING.md` dosyasına bakabilirsiniz.
