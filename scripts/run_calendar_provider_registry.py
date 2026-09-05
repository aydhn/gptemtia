import sys
from advanced_economic_calendar.calendar_pipeline import EconomicCalendarPipeline

if __name__ == "__main__":
    print("Running calendar provider registry script...")
    pipeline = EconomicCalendarPipeline(None, None, None)
    pipeline.build_calendar_registry_and_resolver(save=False)
    print("Done.")
