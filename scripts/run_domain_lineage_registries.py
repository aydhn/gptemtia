from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.fx_lineage_registry import build_fx_lineage_registry
from advanced_data_lineage.commodity_lineage_registry import build_commodity_lineage_registry
from advanced_data_lineage.macro_lineage_registry import build_macro_lineage_registry
from advanced_data_lineage.calendar_lineage_registry import build_calendar_lineage_registry
from advanced_data_lineage.news_metadata_lineage_registry import build_news_metadata_lineage_registry


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    fx_df, fx_sum = build_fx_lineage_registry(profile)
    com_df, com_sum = build_commodity_lineage_registry(profile)
    mac_df, mac_sum = build_macro_lineage_registry(profile)
    cal_df, cal_sum = build_calendar_lineage_registry(profile)
    news_df, news_sum = build_news_metadata_lineage_registry(profile)

    data_lake.save_fx_lineage_registry(fx_df, fx_sum)
    data_lake.save_commodity_lineage_registry(com_df, com_sum)
    data_lake.save_macro_lineage_registry(mac_df, mac_sum)
    data_lake.save_calendar_lineage_registry(cal_df, cal_sum)
    data_lake.save_news_metadata_lineage_registry(news_df, news_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    fx_df.to_csv(csv_dir / "fx_lineage_registry.csv", index=False)
    com_df.to_csv(csv_dir / "commodity_lineage_registry.csv", index=False)
    mac_df.to_csv(csv_dir / "macro_lineage_registry.csv", index=False)
    cal_df.to_csv(csv_dir / "calendar_lineage_registry.csv", index=False)
    news_df.to_csv(csv_dir / "news_metadata_lineage_registry.csv", index=False)

    print(f"Domain-specific lineage registries built successfully: FX({len(fx_df)}), Commodity({len(com_df)}), Macro({len(mac_df)}), Calendar({len(cal_df)}), News({len(news_df)}).")


if __name__ == "__main__":
    main()
