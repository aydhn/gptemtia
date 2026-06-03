# Reproducible Setup Guide

## Amaç ve Kapsam
Bu rehber, projenin taşınabilir offline kopyasını kurmanızı sağlar.

## Güvenlik Sınırları
- Canlı emir, broker entegrasyonu, model deploy işlemleri YOKTUR.

## Setup Steps
1. Sanal ortamı oluşturun (python -m venv venv).
2. Requirements minimal veya frozen dosyasından kurulum yapın (pip install -r requirements_minimal.txt).
3. Config template üzerinden kendi yapılandırmanızı oluşturun (cp .env.example .env).
4. Install verification scriptini çalıştırın (python -m scripts.run_install_verification).

## Troubleshooting
Eğer kurulumda sorun yaşarsanız missing module veya versiyon çakışmalarını kontrol edin.
