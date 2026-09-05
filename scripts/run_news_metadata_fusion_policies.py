import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_fusion.news_metadata_only_fusion_policies import (
    get_news_metadata_only_policies,
    get_news_metadata_only_policies_summary,
)
from advanced_feature_fusion.fusion_timestamp_alignment_policies import (
    get_timestamp_alignment_policies,
    get_timestamp_alignment_policies_summary,
)
from advanced_feature_fusion.fusion_asof_join_policies import (
    get_asof_join_policies,
    get_asof_join_policies_summary,
)


def main():
    data_lake = DataLake()

    news_policies = get_news_metadata_only_policies()
    news_summary = get_news_metadata_only_policies_summary()

    ts_policies = get_timestamp_alignment_policies()
    ts_summary = get_timestamp_alignment_policies_summary()

    asof_policies = get_asof_join_policies()
    asof_summary = get_asof_join_policies_summary()

    data_lake.save_news_metadata_only_fusion_policies(news_policies)
    data_lake.save_fusion_timestamp_alignment_policies(ts_policies)
    data_lake.save_fusion_asof_join_policies(asof_policies)

    print("=" * 70)
    print("PHASE 120: NEWS METADATA-ONLY & JOIN ALIGNMENT POLICIES")
    print("=" * 70)
    print(f"News Metadata Policies : {news_summary['policy_count']}")
    print(f"Zero Full-Text Mandate : {news_summary['full_article_prohibited']}")
    print(f"Zero Scraping Mandate  : {news_summary['scraping_prohibited']}")
    print(f"Timestamp Policies     : {ts_summary['policy_count']}")
    print(f"AsOf Join Direction    : {asof_summary['join_direction']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
