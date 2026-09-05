from pathlib import Path
import pytest
import scripts.run_feature_engine_profile_registry as s1
import scripts.run_feature_input_contracts as s2
import scripts.run_indicator_catalog_registry as s3
import scripts.run_feature_schema_registry as s4
import scripts.run_basic_feature_computations as s5
import scripts.run_feature_metadata_registry as s6
import scripts.run_feature_engine_health_check as s7
import scripts.run_feature_engine_validation_report as s8
import scripts.run_feature_engine_status as s9


def test_advanced_feature_engine_scripts_contract(capsys):
    # Execute each script's main function to verify CLI contract
    s1.main()
    out1 = capsys.readouterr().out
    assert "PHASE 116: FEATURE ENGINE PROFILE & DOMAIN REGISTRY" in out1

    s2.main()
    out2 = capsys.readouterr().out
    assert "PHASE 116: CANONICAL FEATURE INPUT CONTRACTS REGISTRY" in out2

    s3.main()
    out3 = capsys.readouterr().out
    assert "PHASE 116: INDICATOR CATALOG REGISTRY" in out3

    s4.main()
    out4 = capsys.readouterr().out
    assert "PHASE 116: CANONICAL FEATURE & FACTOR SCHEMA REGISTRY" in out4

    s5.main()
    out5 = capsys.readouterr().out
    assert "PHASE 116: BASIC FEATURE COMPUTATION REHEARSAL" in out5

    s6.main()
    out6 = capsys.readouterr().out
    assert "PHASE 116: FEATURE METADATA & ROLLING WINDOW CONTRACTS" in out6

    s7.main()
    out7 = capsys.readouterr().out
    assert "PHASE 116: FEATURE ENGINE HEALTH CHECK" in out7

    s8.main()
    out8 = capsys.readouterr().out
    assert "PHASE 116: FEATURE ENGINE VALIDATION & SAFETY REPORT" in out8

    s9.main()
    out9 = capsys.readouterr().out
    assert "PHASE 116: ADVANCED INDICATOR/FEATURE/FACTOR ENGINE STATUS" in out9
