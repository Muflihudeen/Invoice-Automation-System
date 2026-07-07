import sqlite3
import pandas as pd
from config import DATABASE

def export_csv():

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "SELECT * FROM invoices",
        conn
    )

    df.to_csv(
        "exports/invoices.csv",
        index=False
    )

    conn.close()

    print("CSV exported successfully!")

def export_excel():

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "SELECT * FROM invoices",
        conn
    )

    df.to_excel(
        "exports/invoices.xlsx",
        index=False
    )

    conn.close()

    print("Excel exported successfully!")
