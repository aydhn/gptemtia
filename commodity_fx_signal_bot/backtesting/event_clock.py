import pandas as pd
import logging

logger = logging.getLogger(__name__)


class EventClock:
    def __init__(self, index: pd.DatetimeIndex):
        if not index.is_monotonic_increasing:
            logger.warning("EventClock index is not monotonic increasing.")
        if index.has_duplicates:
            logger.warning("EventClock index has duplicates.")
        self.index = index
        self._pos = -1
        self._len = len(index)

    def __iter__(self):
        self._pos = -1
        return self

    def __next__(self) -> pd.Timestamp:
        self._pos += 1
        if self._pos >= self._len:
            raise StopIteration
        return self.index[self._pos]

    def current(self) -> pd.Timestamp | None:
        if 0 <= self._pos < self._len:
            return self.index[self._pos]
        return None

    def next_timestamp(self) -> pd.Timestamp | None:
        if self._pos + 1 < self._len:
            return self.index[self._pos + 1]
        return None

    def previous_timestamp(self) -> pd.Timestamp | None:
        if self._pos - 1 >= 0:
            return self.index[self._pos - 1]
        return None

    def position(self) -> int:
        return self._pos

    def get_timestamp_at_offset(
        self, current_ts: pd.Timestamp, offset: int
    ) -> pd.Timestamp | None:
        try:
            loc = self.index.get_loc(current_ts)
            target_pos = loc + offset
            if 0 <= target_pos < self._len:
                return self.index[target_pos]
            return None
        except KeyError:
            return None
