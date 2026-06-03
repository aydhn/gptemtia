with open("commodity_fx_signal_bot/portable_packaging/packaging_pipeline.py", "r") as f:
    t = f.read()

# ProjectPaths doesn't take project_root in __init__
t = t.replace('paths = ProjectPaths(self.project_root)', 'paths = ProjectPaths()')

with open("commodity_fx_signal_bot/portable_packaging/packaging_pipeline.py", "w") as f:
    f.write(t)
