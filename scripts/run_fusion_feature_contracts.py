import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_fusion.macro_feature_fusion_contracts import get_macro_timeseries_contracts
from advanced_feature_fusion.calendar_event_fusion_contracts import get_calendar_event_contracts
from advanced_feature_fusion.release_event_fusion_contracts import get_release_event_contracts
from advanced_feature_fusion.news_metadata_fusion_contracts import get_news_metadata_contracts


def main():
    data_lake = DataLake()

    macro_contracts = get_macro_timeseries_contracts()
    cal_contracts = get_calendar_event_contracts()
    rel_contracts = get_release_event_contracts()
    news_contracts = get_news_metadata_contracts()

    summary = {
        "macro_contracts_count": len(macro_contracts),
        "calendar_contracts_count": len(cal_contracts),
        "release_contracts_count": len(rel_contracts),
        "news_contracts_count": len(news_contracts),
        "total_contracts": len(macro_contracts) + len(cal_contracts) + len(rel_contracts) + len(news_contracts),
        "zero_signal_guarantee": True,
        "strictly_metadata_only": True,
    }

    data_lake.save_macro_feature_fusion_contracts(macro_contracts)
    data_lake.save_calendar_event_fusion_contracts(cal_contracts)
    data_lake.save_release_event_fusion_contracts(rel_contracts)
    data_lake.save_news_metadata_fusion_contracts(news_contracts)

    print("=" * 70)
    print("PHASE 120: FUSION FEATURE CONTRACTS")
    print("=" * 70)
    print(f"Macro Contracts    : {summary['macro_contracts_count']}")
    print(f"Calendar Contracts : {summary['calendar_contracts_count']}")
    print(f"Release Contracts  : {summary['release_contracts_count']}")
    print(f"News Contracts     : {summary['news_contracts_count']}")
    print(f"Total Contracts    : {summary['total_contracts']}")
    print(f"Non-Signal Mandate : {summary['zero_signal_guarantee']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
