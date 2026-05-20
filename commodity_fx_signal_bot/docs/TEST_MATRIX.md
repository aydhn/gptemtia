# Test Matrix

Projeye ait tüm test stratejisi ve yapısını özetler.

## Test Stratejisi
- **Unit Tests**: Çekirdek modüllerin bağımsız testi.
- **Integration Tests**: Modüller arası iletişim (örn: Data -> Feature).
- **Contract Tests**: Developer tool ve DX komutları.
- **Security/Observability Tests**: Hata tolerans ve sızıntı testleri.

## Hızlı test
`python -m pytest -q`

## Tam test
`python -m pytest`

## Script import testleri
Tüm scriptlerin güvenle import edilebildiğinden emin olmak için yazılmıştır.

## Yeni faz eklerken test checklist
- Eski testlerin geçtiğini onayla.
- Yeni eklenen modellerin validatörlerini test et.
- Scriptlerin `argparse` ve `main guard` testlerini DX pipeline'a uydur.
