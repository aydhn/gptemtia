def patch_file():
    path = "commodity_fx_signal_bot/data/storage/data_lake.py"
    with open(path, "r") as f:
        content = f.read()

    # The issue is datetime class vs datetime module.
    # Let's just use pd.Timestamp.now().strftime instead to be safe since pandas is available
    content = content.replace("datetime.now().strftime", "pd.Timestamp.now().strftime")

    with open(path, "w") as f:
        f.write(content)

patch_file()
