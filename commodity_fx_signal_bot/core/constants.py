"""
Project-wide constants.
"""

# Intervals
INTERVAL_1H = "1h"
INTERVAL_1D = "1d"
INTERVAL_1W = "1wk"

# Column names
COL_OPEN = "open"
COL_HIGH = "high"
COL_LOW = "low"
COL_CLOSE = "close"
COL_ADJ_CLOSE = "adj_close"
COL_VOLUME = "volume"

# Expected OHLCV columns
REQUIRED_COLUMNS = [COL_OPEN, COL_HIGH, COL_LOW, COL_CLOSE, COL_ADJ_CLOSE, COL_VOLUME]
