from local_dr.dr_models import (
    DRDomain, TabletopScenario, RestoreDrillSimulation, FailureMode, DRFinding,
    build_dr_domain_id, build_tabletop_scenario_id, build_restore_drill_id,
    build_failure_mode_id, build_dr_finding_id,
    dr_domain_to_dict, tabletop_scenario_to_dict, restore_drill_simulation_to_dict,
    failure_mode_to_dict, dr_finding_to_dict
)

def test_dr_models():
    dom = DRDomain(domain_id=build_dr_domain_id("Archive Restore DR"), domain_label="archive_restore_dr", description="Desc", criticality="high")
    assert dom.domain_id == "dom_archive_restore_dr"
    assert dr_domain_to_dict(dom) == {"domain_id": "dom_archive_restore_dr", "domain_label": "archive_restore_dr", "description": "Desc", "criticality": "high"}

    scen = TabletopScenario(scenario_id=build_tabletop_scenario_id("Data Loss", "archive_restore_dr"), domain_label="archive_restore_dr", scenario_name="Data Loss", status="defined", details="Details")
    assert scen.scenario_id == "scen_archive_restore_dr_data_loss"
    assert tabletop_scenario_to_dict(scen) == {"scenario_id": "scen_archive_restore_dr_data_loss", "domain_label": "archive_restore_dr", "scenario_name": "Data Loss", "status": "defined", "details": "Details"}

    drill = RestoreDrillSimulation(drill_id=build_restore_drill_id("Basic Drill", "archive_restore_dr"), domain_label="archive_restore_dr", drill_name="Basic Drill", status="pending", paths_checked=[])
    assert drill.drill_id == "drill_archive_restore_dr_basic_drill"
    assert restore_drill_simulation_to_dict(drill) == {"drill_id": "drill_archive_restore_dr_basic_drill", "domain_label": "archive_restore_dr", "drill_name": "Basic Drill", "status": "pending", "paths_checked": []}

    fail = FailureMode(failure_id=build_failure_mode_id("archive_restore_dr", "Corruption"), domain_label="archive_restore_dr", failure_name="Corruption", severity="high")
    assert fail.failure_id == "fail_archive_restore_dr_corruption"
    assert failure_mode_to_dict(fail) == {"failure_id": "fail_archive_restore_dr_corruption", "domain_label": "archive_restore_dr", "failure_name": "Corruption", "severity": "high"}

    finding = DRFinding(finding_id=build_dr_finding_id("archive_restore_dr", "Issue Found"), domain_label="archive_restore_dr", title="Issue Found", description="Desc")
    assert finding.finding_id == "find_archive_restore_dr_issue_found"
    assert dr_finding_to_dict(finding) == {"finding_id": "find_archive_restore_dr_issue_found", "domain_label": "archive_restore_dr", "title": "Issue Found", "description": "Desc"}
