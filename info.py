import pandas as pd

FOLDER = "datasets/DABB Dataset Original/telemetry_"

DATASET_DATE = "2026-06-26"

CSV_PATH = f"{FOLDER}{DATASET_DATE}.csv"

df = pd.read_csv(CSV_PATH)

print("INFO: \n")
print(df.info())
