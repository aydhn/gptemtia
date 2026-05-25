def patch_architecture():
    path = "commodity_fx_signal_bot/docs/ARCHITECTURE.md"
    with open(path, "r") as f:
        content = f.read()

    new_section = """
## Performance Profiling Flow
Offline Scripts / Command Registry / DataLake / Reports / Knowledge Index
→ RuntimeProfiler
→ MemoryProfiler
→ CPU/GPU Awareness
→ ResourceBudget
→ CacheRegistry
→ CacheStrategy
→ CacheInventory
→ BatchPlanner
→ Checkpointing
→ LargeRunStability
→ BottleneckDetection
→ OptimizationRecommendations
→ PerformanceQuality
→ Performance Reports
"""
    if "## Performance Profiling Flow" not in content:
        content += new_section
        with open(path, "w") as f:
            f.write(content)

def patch_phase_log():
    path = "commodity_fx_signal_bot/docs/PHASE_LOG.md"
    with open(path, "r") as f:
        content = f.read()

    new_log = """
### Phase 52
- Performance profile sistemi eklendi.
- Performance label registry eklendi.
- RuntimeProfileRecord, MemoryProfileRecord, ResourceBudget, CacheRecord ve BatchPlan modelleri eklendi.
- Runtime profiler eklendi.
- Memory profiler eklendi.
- CPU/GPU awareness eklendi.
- Resource budget raporları eklendi.
- Cache registry, cache strategy ve cache inventory eklendi.
- Batch planner eklendi.
- Checkpoint manifest ve resume plan eklendi.
- Large-run stability checklist eklendi.
- Bottleneck detection eklendi.
- Safe optimization recommendations eklendi.
- Performance quality report eklendi.
- PerformancePipeline eklendi.
- DataLake performance kayıt desteği aldı.
- Performance scriptleri eklendi.
- Testler genişletildi.
"""
    if "### Phase 52" not in content:
        content += new_log
        with open(path, "w") as f:
            f.write(content)

patch_architecture()
patch_phase_log()
