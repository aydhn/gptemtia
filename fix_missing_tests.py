import os
import shutil

# Check if the tests are in the root directory by mistake
if os.path.exists('tests/test_momentum_advanced.py'):
    shutil.copy('tests/test_momentum_advanced.py', 'commodity_fx_signal_bot/tests/test_momentum_advanced.py')
    shutil.copy('tests/test_momentum_events.py', 'commodity_fx_signal_bot/tests/test_momentum_events.py')
    shutil.copy('tests/test_momentum_feature_set.py', 'commodity_fx_signal_bot/tests/test_momentum_feature_set.py')
    shutil.copy('tests/test_momentum_scripts_contract.py', 'commodity_fx_signal_bot/tests/test_momentum_scripts_contract.py')
    print("Copied files.")
else:
    print("Files not found.")
