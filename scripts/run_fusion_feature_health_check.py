import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_feature_fusion.fusion_feature_health import check_fusion_feature_health


def main():
    health = check_fusion_feature_health()

    print("=" * 70)
    print("PHASE 120: FUSION FEATURE HEALTH CHECK")
    print("=" * 70)
    print(f"Overall Status : {health['status']}")
    print(f"Current Phase  : {health['phase']}")
    print(f"Next Phase     : {health['next_phase']}")
    print(f"Timestamp      : {health['timestamp']}")
    print("Subsystem Checks:")
    for k, v in health["checks"].items():
        print(f"  - {k}: {v}")
    print("=" * 70)

    if health["status"] != "HEALTHY":
        sys.exit(1)


if __name__ == "__main__":
    main()
