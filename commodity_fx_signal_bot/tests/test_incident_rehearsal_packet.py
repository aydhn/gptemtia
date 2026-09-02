from pathlib import Path
from local_incident_response.incident_rehearsal_packet import build_final_local_incident_response_rehearsal_packet
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_final_local_incident_response_rehearsal_packet():
    profile = get_default_local_incident_response_profile()
    text, summary = build_final_local_incident_response_rehearsal_packet(Path("."), profile)
    assert len(text) > 0
    assert "length" in summary
    assert "forensic" not in text.lower() or "değildir" in text.lower()
