import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_orchestration_scripts_can_be_imported():
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


    import scripts.run_pipeline_workflow
    import scripts.run_full_research_workflow
    import scripts.run_daily_research_workflow
    import scripts.run_paper_reporting_workflow
    import scripts.run_failed_jobs_report
    assert True
