
## Portable Packaging
Environment snapshot, requirements export ve install verification işlemleri için Phase 61 scriptlerini kullanın (örn. `run_environment_snapshot.py`, `run_portable_bundle_manifest.py`). Package publish, Docker deploy, cloud deploy, canlı trading ve broker execution KESİNLİKLE YOKTUR.

## Backup/Recovery Dry-Run and Disaster Recovery
- **Project state inventory**: Taranarak proje dosyalarının scope/policy sınıflandırmasını üretir. `python -m scripts.run_project_state_inventory` ile çağrılabilir.
- **Backup manifest**: Politikaları uygulayıp nelerin dahil/hariç edildiğini (ve manifest-only) gösteren referans dosyadır, dosya kopyalamaz.
- **Restore dry-run**: Manifest tabanlı olarak restore adımlarını (ve overwrite uyarılarını) raporlar, dosya değiştirmez/silmez.
- **Disaster recovery manifest**: Offline projeyi yeniden kurma hedeflerini (RPO/RTO) ve planlarını gösterir, production cloud backup onayı değildir.
- **Restore verification**: Kurtarma dry-run planındaki güvenlik (secret protection) ve uyumluluk kontrollerini doğrular.
- **Secrets exclusion**: Her durumda `.env`, `secret` vb dosyalar otomatik exclude edilir, içerikleri okunmaz.
- **Data/report manifest-only**: Büyük klasörler default olarak "manifest-only" dahil edilir (hashlenmez veya kopyalanmaz).
- **Gerçek restore/overwrite/cloud backup olmadığı açık yazılsın**: Backup Recovery tool'ları yalnızca dry-run raporlar üretmek ve sistemin recovery readiness'ını değerlendirmek (audit) içindir. Canlı deploy veya real overwrite için kullanılmaz.
