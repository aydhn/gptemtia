def patch_readme():
    path = "commodity_fx_signal_bot/README.md"
    with open(path, "r") as f:
        content = f.read()

    new_section = """
## Performance Profiling, Resource Budgets and Large-Run Stability
- Performance profiling canlı trading latency optimizasyonu değildir.
- Resource budgets local/offline araştırma sınırlarıdır.
- GPU awareness GPU zorunluluğu veya model deployment değildir.
- Cache strategy dosya silmez; sadece policy/invalidation plan üretir.
- Batch plan otomatik execution başlatmaz.
- Checkpoint manifest canlı pozisyon state'i değildir.
- Large-run stability production readiness değildir.
- Çıktılar `data/lake/performance` ve `reports/output/performance` altında oluşur.

### Komutlar
```bash
python -m scripts.run_performance_profile_report
python -m scripts.run_resource_budget_report
python -m scripts.run_cache_strategy_report
python -m scripts.run_large_run_stability_report
python -m scripts.run_runtime_optimization_report
python -m scripts.run_performance_status
```
"""
    if "## Performance Profiling" not in content:
        content += new_section
        with open(path, "w") as f:
            f.write(content)

patch_readme()
