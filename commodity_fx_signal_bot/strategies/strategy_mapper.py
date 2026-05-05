import pandas as pd

from strategies.strategy_config import StrategySelectionProfile
from strategies.strategy_family import get_compatible_families_for_decision
from strategies.strategy_rules import calculate_strategy_family_fit


class CandidateToStrategyMapper:
    def __init__(self, profile: StrategySelectionProfile):
        self.profile = profile

    def map_decision_to_families(
        self, decision_row: pd.Series
    ) -> tuple[list[str], dict]:
        decision_label = decision_row.get("decision_label", "unknown")
        candidate_type = decision_row.get("candidate_type", "unknown")

        compatible_families = get_compatible_families_for_decision(
            decision_label, candidate_type
        )
        enabled = self.profile.enabled_strategy_families
        filtered_families = [f for f in compatible_families if f in enabled]

        if not filtered_families:
            if "no_trade" in enabled and decision_label in (
                "no_trade_candidate",
                "conflict_candidate",
                "insufficient_quality_candidate",
            ):
                filtered_families = ["no_trade"]
            elif "watchlist" in enabled:
                filtered_families = ["watchlist"]
            else:
                filtered_families = ["unknown"]

        summary = {
            "decision_label": decision_label,
            "candidate_type": candidate_type,
            "raw_families": compatible_families,
            "filtered_families": filtered_families,
        }

        return filtered_families, summary

    def build_family_fit_table(
        self, decision_row: pd.Series, context_snapshot: dict
    ) -> tuple[pd.DataFrame, dict]:
        families, map_summary = self.map_decision_to_families(decision_row)

        fit_results = []
        for family in families:
            if family in ("no_trade", "watchlist", "unknown"):
                fit_results.append(
                    {
                        "family": family,
                        "decision_fit": 0.0,
                        "regime_fit": 0.0,
                        "mtf_fit": 0.0,
                        "asset_profile_fit": 0.0,
                        "macro_fit": 0.0,
                        "conflict_penalty": 0.0,
                        "selection_score": (
                            1.0 if family in ("no_trade", "watchlist") else 0.0
                        ),
                        "fit_score": (
                            1.0 if family in ("no_trade", "watchlist") else 0.0
                        ),
                        "block_reasons": [],
                        "warnings": [],
                    }
                )
                continue

            fit = calculate_strategy_family_fit(
                family, decision_row, context_snapshot, self.profile
            )
            fit_results.append(fit)

        df = pd.DataFrame(fit_results)
        return df, map_summary
