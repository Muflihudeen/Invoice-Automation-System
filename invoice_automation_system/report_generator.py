import sqlite3
from config import DATABASE
from datetime import datetime

def generate_report():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM invoices")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(total_amount) FROM invoices")
    amount = cursor.fetchone()[0]

    if amount is None:
        amount = 0

    cursor.execute(
        "SELECT COUNT(*) FROM invoices WHERE payment_status='Pending'"
    )
    pending = cursor.fetchone()[0]

    report = open("reports/invoice_report.txt", "w")

    report.write("SMART INVOICE REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write(f"Generated: {datetime.now()}\n\n")
    report.write(f"Total Invoices: {total}\n")
    report.write(f"Pending Payments: {pending}\n")
    report.write(f"Total Invoice Amount: {amount}\n")

    report.close()

    conn.close()
