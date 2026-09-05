import sys
from advanced_economic_calendar.calendar_pipeline import EconomicCalendarPipeline

if __name__ == "__main__":
    print("Running economic event universe registry script...")
    pipeline = EconomicCalendarPipeline(None, None, None)
    pipeline.build_event_universe_and_mapping(save=False)
    print("Done.")
