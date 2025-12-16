import pandas as pd
from sqlalchemy import create_engine

# 1. Read CSV
df = pd.read_csv(
    r"C:\Users\katri\OneDrive\Desktop\atm_cash_management_modified.csv",
    encoding="utf-8"
)

print("Rows in CSV:", len(df))

# 2. MySQL connection
engine = create_engine(
    "mysql+mysqlconnector://username:password@localhost:3306/atm_optimization"
)

# 3. Load into MySQL
df.to_sql(
    "atm_raw",
    engine,
    if_exists="replace",   # replaces table safely
    index=False
)

print("Data loaded into MySQL successfully")
