with open("commodity_fx_signal_bot/tests/test_packaging_pipeline.py", "r") as f:
    t = f.read()

t = t.replace('dl = DataLake()', 'dl = DataLake(tmp_path)')

with open("commodity_fx_signal_bot/tests/test_packaging_pipeline.py", "w") as f:
    f.write(t)
