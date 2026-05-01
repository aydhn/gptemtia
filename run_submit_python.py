import sys
# Make sure we don't import anything that shadows submit
try:
    with open("success.txt", "w") as f:
        f.write("Done")
except Exception:
    pass
