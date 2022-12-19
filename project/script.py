import pandas as pd
import glob
import os
import csv
files = os.path.join("example*.csv")
files = glob.glob(files)
print("Resultant CSV after joining all CSV files at a particular location...")
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_csv('Combined_files.csv')