import pandas as pd
import glob
import os
import csv
files = os.path.join("example*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_json('Combined_files.json')