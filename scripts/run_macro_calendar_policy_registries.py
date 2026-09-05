import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_fusion.macro_release_lag_policies import (
    get_macro_release_lag_policies,
    get_macro_release_lag_policies_summary,
)
from advanced_feature_fusion.calendar_event_window_policies import (
    get_calendar_event_window_policies,
    get_calendar_event_window_policies_summary,
)


def main():
    data_lake = DataLake()

    lag_policies = get_macro_release_lag_policies()
    lag_summary = get_macro_release_lag_policies_summary()

    window_policies = get_calendar_event_window_policies()
    window_summary = get_calendar_event_window_policies_summary()

    data_lake.save_macro_release_lag_policies(lag_policies)
    data_lake.save_calendar_event_window_policies(window_policies)

    print("=" * 70)
    print("PHASE 120: MACRO RELEASE LAG & CALENDAR EVENT WINDOW POLICIES")
    print("=" * 70)
    print(f"Lag Policies Count   : {lag_summary['policy_count']}")
    print(f"No-Lookahead Mandate : {lag_summary['no_lookahead_mandate']}")
    print(f"Window Policies Count: {window_summary['policy_count']}")
    print(f"Window Sizing Rules  : Pre={window_summary['default_pre_window_hours']}h, Post={window_summary['default_post_window_hours']}h")
    print("=" * 70)


if __name__ == "__main__":
    main()
