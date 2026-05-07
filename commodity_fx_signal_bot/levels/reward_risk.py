import math
import pandas as pd
from levels.level_models import safe_price


def calculate_stop_distance(
    price: float | None, stop_level: float | None
) -> float | None:
    price = safe_price(price)
    stop_level = safe_price(stop_level)
    if price is None or stop_level is None:
        return None
    return abs(price - stop_level)


def calculate_target_distance(
    price: float | None, target_level: float | None
) -> float | None:
    price = safe_price(price)
    target_level = safe_price(target_level)
    if price is None or target_level is None:
        return None
    return abs(price - target_level)


def calculate_reward_risk(
    price: float | None,
    stop_level: float | None,
    target_level: float | None,
    directional_bias: str,
) -> float | None:
    # First, validate geometry implicitly by distance sign if we wanted, but we use abs distances and check if geometry is valid
    from levels.level_models import is_valid_level_for_direction

    if not is_valid_level_for_direction(price, stop_level, directional_bias, "stop"):
        return None
    if not is_valid_level_for_direction(
        price, target_level, directional_bias, "target"
    ):
        return None

    stop_dist = calculate_stop_distance(price, stop_level)
    target_dist = calculate_target_distance(price, target_level)

    if stop_dist is None or target_dist is None or stop_dist <= 0:
        return None

    return target_dist / stop_dist


def build_reward_risk_table(
    price: float | None,
    stop_levels: list[float],
    target_levels: list[float],
    directional_bias: str,
) -> pd.DataFrame:
    rows = []

    for s in stop_levels:
        for t in target_levels:
            rr = calculate_reward_risk(price, s, t, directional_bias)
            valid = rr is not None
            s_dist = calculate_stop_distance(price, s) if valid else None
            t_dist = calculate_target_distance(price, t) if valid else None

            rows.append(
                {
                    "stop_level_candidate": s,
                    "target_level_candidate": t,
                    "stop_distance": s_dist,
                    "target_distance": t_dist,
                    "stop_distance_pct": s_dist / price if (valid and price) else None,
                    "target_distance_pct": (
                        t_dist / price if (valid and price) else None
                    ),
                    "reward_risk": rr,
                    "valid": valid,
                    "warnings": (
                        [] if valid else ["Invalid geometry or division by zero"]
                    ),
                }
            )

    return pd.DataFrame(rows)


def select_best_reward_risk_candidate(
    rr_table: pd.DataFrame, min_reward_risk: float = 1.2
) -> dict:
    if rr_table.empty:
        return {
            "stop_level_candidate": None,
            "target_level_candidate": None,
            "reward_risk": None,
            "warnings": ["Empty RR table"],
        }

    valid_table = rr_table[rr_table["valid"] == True]
    if valid_table.empty:
        return {
            "stop_level_candidate": None,
            "target_level_candidate": None,
            "reward_risk": None,
            "warnings": ["No valid RR candidates"],
        }

    # Example logic: Pick closest to preferred reward risk (e.g. max RR if we want, or just > min_reward_risk)
    # Let's just pick the one with max reward_risk that satisfies minimum, or if none, the max one anyway.
    candidates = valid_table[valid_table["reward_risk"] >= min_reward_risk]

    if not candidates.empty:
        best = candidates.sort_values("reward_risk", ascending=False).iloc[0]
    else:
        best = valid_table.sort_values("reward_risk", ascending=False).iloc[0]

    return {
        "stop_level_candidate": best["stop_level_candidate"],
        "target_level_candidate": best["target_level_candidate"],
        "reward_risk": best["reward_risk"],
        "warnings": (
            []
            if best["reward_risk"] >= min_reward_risk
            else [f"Reward/risk {best['reward_risk']} is below min {min_reward_risk}"]
        ),
    }
