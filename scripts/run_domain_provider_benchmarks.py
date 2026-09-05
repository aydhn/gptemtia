from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.fx_provider_benchmark import build_fx_provider_benchmark_report
from advanced_provider_benchmark.commodity_provider_benchmark import build_commodity_provider_benchmark_report
from advanced_provider_benchmark.macro_provider_benchmark import build_macro_provider_benchmark_report
from advanced_provider_benchmark.calendar_provider_benchmark import build_calendar_provider_benchmark_report
from advanced_provider_benchmark.news_metadata_provider_benchmark import build_news_metadata_provider_benchmark_report
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_domain_provider_benchmark_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    fx_df, fx_sum = build_fx_provider_benchmark_report(profile)
    com_df, com_sum = build_commodity_provider_benchmark_report(profile)
    mac_df, mac_sum = build_macro_provider_benchmark_report(profile)
    cal_df, cal_sum = build_calendar_provider_benchmark_report(profile)
    news_df, news_sum = build_news_metadata_provider_benchmark_report(profile)

    data_lake.save_fx_provider_benchmark_report(fx_df, fx_sum)
    data_lake.save_commodity_provider_benchmark_report(com_df, com_sum)
    data_lake.save_macro_provider_benchmark_report(mac_df, mac_sum)
    data_lake.save_calendar_provider_benchmark_report(cal_df, cal_sum)
    data_lake.save_news_metadata_provider_benchmark_report(news_df, news_sum)

    out_dir = project_root / "reports" / "output" / "advanced_provider_benchmark"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    domains = [
        ("fx_benchmark_report", fx_df, fx_sum),
        ("commodity_benchmark_report", com_df, com_sum),
        ("macro_benchmark_report", mac_df, mac_sum),
        ("calendar_benchmark_report", cal_df, cal_sum),
        ("news_metadata_benchmark_report", news_df, news_sum),
    ]

    for name, df, s in domains:
        df.to_csv(csv_dir / f"{name}.csv", index=False)
        md_text = build_domain_provider_benchmark_markdown_report(s, df)
        (md_dir / f"{name}.md").write_text(md_text, encoding="utf-8")
        (txt_dir / f"{name}.txt").write_text(md_text, encoding="utf-8")

    print("Domain provider benchmarks built successfully: FX, Commodity, Macro, Calendar, News Metadata.")


if __name__ == "__main__":
    main()
