import os
from pathlib import Path
import re

def append_to_file(path_str: str, text: str):
    p = Path(path_str)
    if p.exists():
        content = p.read_text(encoding="utf-8")
        if text.strip().split("\\n")[0] not in content:
            p.write_text(content + "\\n\\n" + text, encoding="utf-8")
            print(f"Updated {path_str}")
    else:
        print(f"Not found: {path_str}")

def update_docs():
    # README
    readme_text = """## Local Performance Budgeting and Offline Efficiency Planning

Final local performance budget gercek benchmark degildir.
Lightweight runtime profile production profiling degildir.
Resource-footprint rehearsal gercek CPU/memory profiler degildir.
Maintenance cost estimate resmi maliyet veya is gucu plani degildir.
Offline efficiency planning otomatik optimizasyon uygulamaz.
Retention/rotation guide dosya silmez veya tasimaz.
Performance readiness score production capacity approval degildir.
Ciktilar data/lake/local_performance ve reports/output/local_performance altinda olusur.

Komutlar:
python -m scripts.run_performance_domain_registry
python -m scripts.run_final_local_performance_budget
python -m scripts.run_resource_footprint_rehearsal
python -m scripts.run_maintenance_cost_estimate
python -m scripts.run_offline_efficiency_plan
python -m scripts.run_performance_quality_report
python -m scripts.run_performance_status
"""
    # Wait, README is at project root.
    append_to_file("README.md", readme_text)
    
    arch_text = """-> PerformanceProfileRegistry -> PerformanceDomainRegistry -> FinalLocalPerformanceBudget -> LightweightRuntimeProfile -> ResourceFootprintRehearsal -> CPU/Memory/DiskEstimates -> GrowthEstimates -> Script/Test/PipelineRuntimeEstimates -> MaintenanceCostEstimate -> MaintenanceEffortMatrix -> OperatorTimeBudget -> LocalMachineSuitability -> OfflineEfficiencyPlanning -> EfficiencyCandidates -> LightweightModeRecommendations -> HeavyOutputWarnings -> RetentionRehearsal -> PerformanceNoGoSafeGo -> PerformanceExceptions -> PerformanceGaps -> PerformanceRisks -> PerformanceReadinessScoring -> PerformanceValidation -> PerformanceQuality -> Local Performance Outputs"""
    append_to_file("commodity_fx_signal_bot/docs/ARCHITECTURE.md", arch_text)

    phase_text = """### Phase 83: Local Performance Budgeting
- Local performance profile sistemi eklendi.
- Performance label registry eklendi.
- PerformanceDomain, ResourceEstimateItem, vb eklendi.
- Performance domain registry eklendi.
- Final local performance budget eklendi.
- Lightweight runtime profile eklendi.
- Resource-footprint rehearsal report eklendi.
- CPU/memory/disk usage estimate registry eklendi.
- Report/DataLake/generated-docs growth estimate eklendi.
- Script/test/pipeline runtime estimate registry eklendi.
- Maintenance cost estimate eklendi.
- Local machine suitability checklist eklendi.
- Offline efficiency planning guide eklendi.
- Efficiency candidate registry eklendi.
- Heavy-output warning registry eklendi.
- Storage retention eklendi.
- Performance no-go/safe-go summary eklendi.
- Performance exception/gap/risk registerlari eklendi.
- Performance readiness score report eklendi.
- Performance validation ve quality report eklendi.
- LocalPerformancePipeline eklendi.
- DataLake local performance kayit destegi aldi.
- Local performance scriptleri eklendi.
- Testler genisletildi."""
    append_to_file("commodity_fx_signal_bot/docs/PHASE_LOG.md", phase_text)
    
    manual_text = """## Local Performance
- Final local performance budget nasil okunur? Budget dosyalarina bakin, gercek benchmark degildir.
- Lightweight runtime profile ne yapar? Hizli calisma modlarini listeler.
- Resource-footprint rehearsal gercek benchmark degildir.
- Maintenance cost estimate nasil yorumlanir? Gozden gecirme eforu olarak.
- Offline efficiency planning guide nasil kullanilir? Manuel optimizasyon icin.
- Retention/rotation rehberleri neden dosya silmez? Sadece tavsiyedir.
- Gercek benchmark, load/stress test, production profiling, cloud cost approval, canli emir, broker execution, deployment, yatirim performansi iddiasi ve yatirim tavsiyesi degildir."""
    
    append_to_file("commodity_fx_signal_bot/docs/OPERATOR_MANUAL.md", manual_text)
    append_to_file("commodity_fx_signal_bot/docs/ANALYST_HANDBOOK.md", manual_text)
    append_to_file("commodity_fx_signal_bot/docs/CODEX_AGENT_GUIDE.md", manual_text)
    append_to_file("commodity_fx_signal_bot/docs/SAFE_USAGE_GUIDE.md", manual_text)
    append_to_file("commodity_fx_signal_bot/docs/INSTALLATION.md", manual_text)
    append_to_file("commodity_fx_signal_bot/docs/CONFIGURATION.md", manual_text)

if __name__ == "__main__":
    update_docs()
