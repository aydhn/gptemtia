import re
from pathlib import Path

f = Path("README.md")
content = f.read_text()

add = """
### Local Archive Strategy and Long-Horizon Preservation

- **Local archive strategy** cloud backup değildir.
- **Cold storage manifest** dosya yüklemez, taşımaz, sıkıştırmaz. Sadece manual backup işlemleri için talimat ve metadata tutar.
- **Snapshot catalog** dosya kopyalamaz; manifest/index üretir.
- **Retention policy** resmi hukuki kayıt saklama politikası değildir. Offline ortamda neyin saklanıp neyin silinmeyeceğine dair manuel tavsiyelerdir.
- **Archive integrity verification plan** read-only kontrol planıdır.
- **Secret exclusion registry** raw secret içermez ve bu dosyaların arşivlenmesini engellemek için checklist sağlar.
- **Preservation binder** production archive service veya compliance sertifikası değildir. Offline arşivi yöneten operator için referans kitapçığıdır.
- Tüm çıktılar `data/lake/local_archive` ve `reports/output/local_archive` altında oluşur.

Komutlar:
```bash
python -m scripts.run_archive_domain_registry
python -m scripts.run_project_snapshot_catalog
python -m scripts.run_cold_storage_manifest
python -m scripts.run_archive_integrity_plan
python -m scripts.run_preservation_binder
python -m scripts.run_archive_quality_report
python -m scripts.run_archive_status
```
"""

if "Local Archive Strategy and Long-Horizon Preservation" not in content:
    content += add
    f.write_text(content)
    print("README patched")
