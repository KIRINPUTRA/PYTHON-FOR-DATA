# Renames .jpg (& .png) files in dir
# to YYYYMMDD_hhmmss.jpg (or .png)
# based on birthtime.

from datetime import datetime
import os, sys

dir = sys.argv[1]

for fname in os.listdir(dir):
    if (fname[-4:].lower() == '.jpg' or fname[-4:].lower() == '.png'):
        print("Processing %s" % fname)
        Fname = os.path.join(dir, fname)
        btime_raw = os.stat(Fname).st_birthtime
        btime = datetime.fromtimestamp(btime_raw).strftime("%Y%m%d_%I%M%S")
        newname = os.path.join(dir, btime + fname[-4:])
        os.rename(Fname, newname)
print("All done")
