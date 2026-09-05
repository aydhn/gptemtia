import sys
from advanced_economic_calendar.calendar_pipeline import EconomicCalendarPipeline

if __name__ == "__main__":
    print("Running calendar dry run fixture script...")
    pipeline = EconomicCalendarPipeline(None, None, None)
    pipeline.build_calendar_dry_run_fixture(save=False)
    print("Done.")
