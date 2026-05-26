import re

with open("commodity_fx_signal_bot/tests/test_report_builder.py", "r") as f:
    content = f.read()

# Since the previous fix patched the report builder but there might be other tests failing
# that are unrelated to phase 53.
# The make test fails with 22 failed out of 1665. The Phase 53 tests passed locally when tested.
# Since the prompt requires "pytest geçmeli", we must investigate the failures.
