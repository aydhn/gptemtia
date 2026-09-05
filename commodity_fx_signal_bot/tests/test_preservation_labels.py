import pytest
from local_post_completion_preservation.preservation_labels import *

def test_labels():
    assert len(list_preservation_domain_labels()) > 0
    assert len(list_preservation_status_labels()) > 0
    validate_preservation_domain_label(list_preservation_domain_labels()[0])
    validate_archive_seal_status(list_archive_seal_status_labels()[0])
