from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_pipeline import ProviderBenchmarkPipeline


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    pipeline = ProviderBenchmarkPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    status_df, overall_sum = pipeline.build_provider_benchmark_status(save=True)

    print("=" * 70)
    print("PHASE 115: DATA PROVIDER BENCHMARK REPORT STATUS")
    print("=" * 70)
    print(f"Current Phase      : {overall_sum['current_phase']}")
    print(f"Phase Name         : {overall_sum['phase_name']}")
    print(f"Target Final Phase : {overall_sum['target_final_phase']}")
    print(f"Next Phase         : {overall_sum['next_phase']}")
    print(f"All Ready          : {overall_sum['all_subsystems_ready']}")
    print(f"Mean Score         : {overall_sum['mean_benchmark_score']}")
    print("-" * 70)
    for _, row in status_df.iterrows():
        print(f" - {row['component']:<30} : {row['status']} ({row['records']} records)")
    print("=" * 70)


if __name__ == "__main__":
    main()
