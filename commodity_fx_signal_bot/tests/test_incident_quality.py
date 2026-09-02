from local_incident_response.incident_quality import check_for_forbidden_terms_in_incident

def test_check_for_forbidden_terms_in_incident():
    res = check_for_forbidden_terms_in_incident("real trade")
    assert not res["passed"]
    
    res = check_for_forbidden_terms_in_incident("bu rapor yatırım tavsiyesi değildir")
    assert res["passed"]
