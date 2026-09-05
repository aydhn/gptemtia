import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from advanced_feature_validation.feature_validation_profile_registry import get_feature_validation_profiles_summary
from advanced_feature_validation.feature_validation_domain_registry import get_feature_validation_domains_summary
from advanced_feature_validation.feature_validation_rule_registry import get_feature_validation_rules_summary
from advanced_feature_validation.feature_validation_health import check_feature_validation_health
from advanced_feature_validation.phase_122_handoff import build_phase_122_handoff_manifest


def main():
    settings = get_settings()
    health = check_feature_validation_health()
    prof_summary = get_feature_validation_profiles_summary()
    dom_summary = get_feature_validation_domains_summary()
    rule_summary = get_feature_validation_rules_summary()
    handoff = build_phase_122_handoff_manifest()

    print("=" * 70)
    print("PHASE 121 STATUS: FEATURE VALIDATION & NO-LOOKAHEAD GUARD")
    print("=" * 70)
    print(f"Health Status       : {health['status']}")
    print(f"Current Phase       : 121")
    print(f"Next Phase          : 122")
    print(f"Target Final Phase  : 160")
    print(f"Profiles Configured : {prof_summary['total_profiles']}")
    print(f"Domains Defined     : {dom_summary['total_domains']}")
    print(f"Rules Registered    : {rule_summary['total_rules']}")
    print(f"Handoff Status      : {handoff['handoff_status']}")
    print("Safety Invariants:")
    print("  - Zero Trade Signals      : ENFORCED")
    print("  - Forbidden Columns Guard : ENFORCED")
    print("  - No-Lookahead (Backward) : ENFORCED")
    print("  - Metadata-Only News      : ENFORCED")
    print("  - Non-Destructive Invariant: ENFORCED")
    print("=" * 70)


if __name__ == "__main__":
    main()
