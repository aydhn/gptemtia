import re
import os

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

insert_str = """
    # Phase 22: Strategy Rule Settings
    strategy_rules_enabled: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_RULES_ENABLED", "true").lower() == "true"
    )
    strategy_rule_engine_enabled: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_RULE_ENGINE_ENABLED", "true").lower() == "true"
    )
    default_strategy_rule_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_STRATEGY_RULE_PROFILE", "balanced_rule_evaluation")
    )
    default_strategy_rule_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_STRATEGY_RULE_TIMEFRAME", "1d")
    )
    rule_min_match_score: float = field(
        default_factory=lambda: float(os.getenv("RULE_MIN_MATCH_SCORE", "0.45"))
    )
    rule_min_confidence: float = field(
        default_factory=lambda: float(os.getenv("RULE_MIN_CONFIDENCE", "0.50"))
    )
    rule_min_quality_score: float = field(
        default_factory=lambda: float(os.getenv("RULE_MIN_QUALITY_SCORE", "0.50"))
    )
    rule_max_conflict_score: float = field(
        default_factory=lambda: float(os.getenv("RULE_MAX_CONFLICT_SCORE", "0.65"))
    )
    rule_min_readiness_score: float = field(
        default_factory=lambda: float(os.getenv("RULE_MIN_READINESS_SCORE", "0.45"))
    )
    rule_require_strategy_candidate_passed: bool = field(
        default_factory=lambda: os.getenv("RULE_REQUIRE_STRATEGY_CANDIDATE_PASSED", "true").lower() == "true"
    )
    rule_require_decision_candidate_passed: bool = field(
        default_factory=lambda: os.getenv("RULE_REQUIRE_DECISION_CANDIDATE_PASSED", "false").lower() == "true"
    )
    rule_allow_wait_candidates: bool = field(
        default_factory=lambda: os.getenv("RULE_ALLOW_WAIT_CANDIDATES", "true").lower() == "true"
    )
    rule_allow_invalidation_candidates: bool = field(
        default_factory=lambda: os.getenv("RULE_ALLOW_INVALIDATION_CANDIDATES", "true").lower() == "true"
    )
    save_strategy_rule_candidates: bool = field(
        default_factory=lambda: os.getenv("SAVE_STRATEGY_RULE_CANDIDATES", "true").lower() == "true"
    )
    save_entry_exit_candidates: bool = field(
        default_factory=lambda: os.getenv("SAVE_ENTRY_EXIT_CANDIDATES", "true").lower() == "true"
    )
    save_strategy_rule_pool: bool = field(
        default_factory=lambda: os.getenv("SAVE_STRATEGY_RULE_POOL", "true").lower() == "true"
    )
"""

if "strategy_rules_enabled" not in content:
    content = content.replace('save_strategy_pool: bool = field(\n        default_factory=lambda: os.getenv("SAVE_STRATEGY_POOL", "true").lower()\n        == "true"\n    )', 'save_strategy_pool: bool = field(\n        default_factory=lambda: os.getenv("SAVE_STRATEGY_POOL", "true").lower()\n        == "true"\n    )' + insert_str)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/.env.example", "r") as f:
    env_content = f.read()

env_insert_str = """
STRATEGY_RULES_ENABLED=true
STRATEGY_RULE_ENGINE_ENABLED=true
DEFAULT_STRATEGY_RULE_PROFILE=balanced_rule_evaluation
DEFAULT_STRATEGY_RULE_TIMEFRAME=1d
RULE_MIN_MATCH_SCORE=0.45
RULE_MIN_CONFIDENCE=0.50
RULE_MIN_QUALITY_SCORE=0.50
RULE_MAX_CONFLICT_SCORE=0.65
RULE_MIN_READINESS_SCORE=0.45
RULE_REQUIRE_STRATEGY_CANDIDATE_PASSED=true
RULE_REQUIRE_DECISION_CANDIDATE_PASSED=false
RULE_ALLOW_WAIT_CANDIDATES=true
RULE_ALLOW_INVALIDATION_CANDIDATES=true
SAVE_STRATEGY_RULE_CANDIDATES=true
SAVE_ENTRY_EXIT_CANDIDATES=true
SAVE_STRATEGY_RULE_POOL=true
"""
if "STRATEGY_RULES_ENABLED" not in env_content:
    env_content += env_insert_str

with open("commodity_fx_signal_bot/.env.example", "w") as f:
    f.write(env_content)
