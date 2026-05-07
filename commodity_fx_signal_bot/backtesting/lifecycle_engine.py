import pandas as pd
from backtesting.backtest_config import BacktestProfile
from backtesting.execution_simulator import ExecutionSimulator
from backtesting.backtest_models import SimulatedTrade, build_trade_id
from backtesting.candidate_adapter import infer_candidate_direction


class TradeLifecycleEngine:
    def __init__(
        self,
        profile: BacktestProfile,
        execution_simulator: ExecutionSimulator | None = None,
    ):
        self.profile = profile
        self.execution = execution_simulator or ExecutionSimulator(profile)

    def simulate_candidate_lifecycle(
        self,
        symbol: str,
        timeframe: str,
        candidate_row: pd.Series,
        price_df: pd.DataFrame,
    ) -> tuple[SimulatedTrade, dict]:
        signal_ts = candidate_row.name
        bias = candidate_row.get("directional_bias", "")
        direction = infer_candidate_direction(candidate_row)

        stop_level = candidate_row.get("theoretical_stop_level")
        target_level = candidate_row.get("theoretical_target_level")
        units = candidate_row.get("theoretical_units", 1.0)
        notional = candidate_row.get("theoretical_notional", 0.0)

        trade_id = build_trade_id(
            symbol, timeframe, str(candidate_row.get("candidate_id", signal_ts))
        )

        warnings = []

        # 1. Entry
        entry_res = self.execution.simulate_entry(price_df, signal_ts, bias)
        if entry_res["status"] != "success":
            trade = SimulatedTrade(
                symbol=symbol,
                timeframe=timeframe,
                trade_id=trade_id,
                source_level_id=str(candidate_row.get("candidate_id", "")),
                source_sizing_id="",
                source_risk_id="",
                strategy_family="unknown",
                directional_bias=bias,
                entry_timestamp=None,
                entry_price=None,
                exit_timestamp=None,
                exit_price=None,
                theoretical_stop_level=stop_level,
                theoretical_target_level=target_level,
                theoretical_units=units,
                adjusted_theoretical_units=units,
                theoretical_notional=notional,
                gross_pnl=None,
                fee_cost=0.0,
                slippage_cost=0.0,
                net_pnl=None,
                return_pct=None,
                holding_bars=0,
                lifecycle_status="simulated_rejected",
                entry_reason="risk_rejected",
                exit_reason="unknown_exit_reason",
                result_label="rejected",
                warnings=["Entry rejected: " + entry_res.get("reason", "")],
            )
            return trade, {"status": "rejected"}

        entry_ts = entry_res["entry_timestamp"]
        entry_price = entry_res["entry_price"]

        entry_loc = price_df.index.get_loc(entry_ts)

        # 2. Lifecycle
        exit_ts = None
        exit_price = None
        exit_reason = ""
        holding_bars = 0

        for i in range(entry_loc, len(price_df)):
            current_bar_ts = price_df.index[i]
            current_bar = price_df.iloc[i]

            holding_bars = i - entry_loc

            if holding_bars == 0 and not self.profile.allow_same_bar_exit:
                continue

            if holding_bars >= self.profile.max_holding_bars:
                exit_ts = current_bar_ts
                exit_price = current_bar["close"]
                exit_reason = "max_holding_period"
                break

            touch_res = self.check_stop_target_touch(
                current_bar, bias, stop_level, target_level
            )
            if touch_res["touched"]:
                exit_ts = current_bar_ts
                exit_reason = touch_res["reason"]
                if "ambiguity" in touch_res and touch_res["ambiguity"]:
                    warnings.append(f"Intrabar ambiguity at {current_bar_ts}")

                # Assume exact touch for price
                exit_price = (
                    stop_level
                    if exit_reason == "stop_touch_simulated"
                    else target_level
                )
                break

        if exit_ts is None:
            # End of data
            exit_ts = price_df.index[-1]
            exit_price = price_df.iloc[-1]["close"]
            exit_reason = "end_of_data"
            holding_bars = len(price_df) - 1 - entry_loc
            result_label = "open_at_end"

        # 3. PnL & Costs
        if direction == "long":
            gross_pnl = (exit_price - entry_price) * units
        elif direction == "short":
            gross_pnl = (entry_price - exit_price) * units
        else:
            gross_pnl = 0.0

        costs_entry = self.execution.apply_transaction_costs(
            entry_price, units, notional
        )
        costs_exit = self.execution.apply_transaction_costs(exit_price, units, notional)

        total_fee = costs_entry["fee"] + costs_exit["fee"]
        total_slippage = costs_entry["slippage"] + costs_exit["slippage"]

        net_pnl = gross_pnl - total_fee - total_slippage

        if notional > 0:
            return_pct = net_pnl / notional
        else:
            return_pct = 0.0

        if exit_reason != "end_of_data":
            if net_pnl > 0:
                result_label = "win"
            elif net_pnl < 0:
                result_label = "loss"
            else:
                result_label = "breakeven"

        trade = SimulatedTrade(
            symbol=symbol,
            timeframe=timeframe,
            trade_id=trade_id,
            source_level_id=str(candidate_row.get("candidate_id", "")),
            source_sizing_id="",
            source_risk_id="",
            strategy_family="unknown",
            directional_bias=bias,
            entry_timestamp=str(entry_ts),
            entry_price=entry_price,
            exit_timestamp=str(exit_ts),
            exit_price=exit_price,
            theoretical_stop_level=stop_level,
            theoretical_target_level=target_level,
            theoretical_units=units,
            adjusted_theoretical_units=units,
            theoretical_notional=notional,
            gross_pnl=gross_pnl,
            fee_cost=total_fee,
            slippage_cost=total_slippage,
            net_pnl=net_pnl,
            return_pct=return_pct,
            holding_bars=holding_bars,
            lifecycle_status="simulated_closed",
            entry_reason=entry_res.get("reason", "candidate_entry"),
            exit_reason=exit_reason,
            result_label=result_label,
            warnings=warnings,
        )

        return trade, {"status": "success"}

    def check_stop_target_touch(
        self,
        bar: pd.Series,
        directional_bias: str,
        stop_level: float | None,
        target_level: float | None,
    ) -> dict:
        if stop_level is None or target_level is None:
            return {"touched": False}

        high = bar["high"]
        low = bar["low"]

        stop_touched = False
        target_touched = False

        if directional_bias == "long_bias_candidate":
            if low <= stop_level:
                stop_touched = True
            if high >= target_level:
                target_touched = True
        elif directional_bias == "short_bias_candidate":
            if high >= stop_level:
                stop_touched = True
            if low <= target_level:
                target_touched = True

        if stop_touched and target_touched:
            reason = self.resolve_intrabar_ambiguity(
                bar, directional_bias, stop_level, target_level
            )
            return {"touched": True, "reason": reason, "ambiguity": True}
        elif stop_touched:
            return {
                "touched": True,
                "reason": "stop_touch_simulated",
                "ambiguity": False,
            }
        elif target_touched:
            return {
                "touched": True,
                "reason": "target_touch_simulated",
                "ambiguity": False,
            }

        return {"touched": False}

    def resolve_intrabar_ambiguity(
        self,
        bar: pd.Series,
        directional_bias: str,
        stop_level: float | None,
        target_level: float | None,
    ) -> str:
        # Conservative assumption: always assume stop was hit first
        return "stop_touch_simulated"
