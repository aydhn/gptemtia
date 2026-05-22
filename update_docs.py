# Update README.md
with open("commodity_fx_signal_bot/README.md", "r") as f:
    readme = f.read()

new_readme_section = """
## Synthetic Benchmarks, Composite Indices and Relative Strength (Phase 43)

The bot includes an offline research infrastructure to generate synthetic benchmarks, composite indices, relative strength rankings, and universe rotation analysis.

**DISCLAIMER**:
- Synthetic benchmarks are not real financial benchmarks.
- Composite indices are not real index or ETF products.
- Relative strength "leader" is not a buy signal.
- "Laggard" label is not a sell signal.
- Universe rotation is not a real rotation execution.
- Outputs are for offline research only and do not constitute investment advice.

Outputs are generated under `data/lake/synthetic_indices` and `reports/output/synthetic_indices`.

Commands:
```bash
python -m scripts.run_synthetic_benchmark_report --timeframe 1d --limit 20
python -m scripts.run_composite_index_report --timeframe 1d --limit 30
python -m scripts.run_relative_strength_report --timeframe 1d --limit 30
python -m scripts.run_universe_rotation_report --timeframe 1d --limit 30
python -m scripts.run_leadership_laggard_report --timeframe 1d --limit 30
python -m scripts.run_synthetic_index_status
```
"""
readme += new_readme_section
with open("commodity_fx_signal_bot/README.md", "w") as f:
    f.write(readme)

# Update docs/ARCHITECTURE.md
with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    arch = f.read()

new_arch_section = """
### Synthetic Indices and Relative Strength Pipeline
Universe Prices / Returns -> IndexUniverse -> BenchmarkDefinitions -> WeightingSchemes -> CompositeIndexBuilder -> RelativeStrength -> RelativeMomentum -> RotationResearch -> LeadershipLaggard -> BenchmarkComparison -> IndexPerformance -> IndexQuality -> Synthetic Index Research Reports
"""
arch += new_arch_section
with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
    f.write(arch)

# Update docs/PHASE_LOG.md
with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "r") as f:
    phase_log = f.read()

new_phase_section = """
## Phase 43: Synthetic Benchmark Baskets & Composite Indices
- Synthetic index profile system added to settings.
- Index label registry created for standardizing index and rotation tags.
- SyntheticIndexDefinition, SyntheticIndexSeries, RelativeStrengthRecord, and RotationRecord models introduced.
- Index universe and weighting schemes modules implemented.
- Benchmark definitions and composite index builder constructed.
- Relative strength and momentum analysis modules added.
- Rotation research and cross-asset leadership/laggard reports implemented.
- Benchmark comparison and index performance modules added.
- Index quality module enforces zero forbidden trade instruction terms (like BUY/SELL/AL/SAT).
- SyntheticIndexPipeline implemented to orchestrate the generation process.
- DataLake and FeatureStore updated to support saving/loading synthetic index research artifacts.
- Six new CLI scripts provided for triggering specific index, momentum, and rotation reports.
- Tests updated to verify pipeline integrity, index definitions, and weighting distributions.
"""
phase_log += new_phase_section
with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
    f.write(phase_log)
