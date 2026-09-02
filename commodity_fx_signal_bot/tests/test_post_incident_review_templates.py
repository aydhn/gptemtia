from local_incident_response.post_incident_review_templates import build_post_incident_review_template_library
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_post_incident_review_template_library():
    profile = get_default_local_incident_response_profile()
    df, summary = build_post_incident_review_template_library(profile)
    assert not df.empty
