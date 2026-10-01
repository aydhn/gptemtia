import time
import pandas as pd
from signals.signal_scoring import SignalScorer
from signals.signal_config import get_default_signal_scoring_profile

def create_large_events_df(n_rows=5000):
    timestamps = pd.date_range(start="2023-01-01", periods=n_rows, freq="h")

    # We want many unique candidate_type and directional_bias combinations or just
    # many rows per timestamp
    # Lets make sure each timestamp has a few different biases/candidate types

    repeated_timestamps = list(timestamps) * 5
    types = ["trend_following", "mean_reversion", "breakout", "trend_following", "mean_reversion"] * n_rows
    biases = ["bullish", "bearish", "bullish", "bearish", "bullish"] * n_rows

    df = pd.DataFrame({
        "timestamp": repeated_timestamps,
        "candidate_type": types,
        "directional_bias": biases,
        "is_warning": [False] * len(repeated_timestamps),
        "is_context": [False] * len(repeated_timestamps),
        "event_name": ["ema_cross"] * len(repeated_timestamps),
        "event_group": ["trend"] * len(repeated_timestamps),
        "normalized_strength": [1.0] * len(repeated_timestamps),
    })

    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df

def run_benchmark():
    prof = get_default_signal_scoring_profile()
    scorer = SignalScorer(prof)
    events_df = create_large_events_df(1000)
    context_frames = {}

    start_time = time.time()
    cands, summary = scorer.score_timestamps("GC=F", "1d", events_df, context_frames)
    end_time = time.time()

    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Generated candidates: {summary['generated_candidates']}")

if __name__ == "__main__":
    run_benchmark()
