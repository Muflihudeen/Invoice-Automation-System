import sqlite3
import os
from datetime import datetime
from config import DATABASE

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)


def connect_db():
    return sqlite3.connect(DATABASE)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            invoice_number TEXT PRIMARY KEY,
            vendor_name TEXT,
            customer_name TEXT,
            invoice_date TEXT,
            due_date TEXT,
            tax_amount REAL,
            total_amount REAL,
            currency TEXT,
            payment_status TEXT,
            processing_date TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_invoice(data):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO invoices (
                invoice_number,
                vendor_name,
                customer_name,
                invoice_date,
                due_date,
                tax_amount,
                total_amount,
                currency,
                payment_status,
                processing_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["invoice_number"],
            data["vendor_name"],
            data["customer_name"],
            data["invoice_date"],
            data["due_date"],
            data["tax_amount"],
            data["total_amount"],
            data["currency"],
            data["payment_status"],
            str(datetime.now())
        ))

        conn.commit()
        print("Invoice saved successfully!")

    except sqlite3.IntegrityError:
        print("Duplicate invoice number!")

    finally:
        conn.close()


def view_invoices():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM invoices")
    rows = cursor.fetchall()

    if not rows:
        print("No invoices found.")
    else:
        print("\n===== ALL INVOICES =====")
        for row in rows:
            print(row)

    conn.close()


def search_invoice(invoice_number):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM invoices WHERE invoice_number=?",
        (invoice_number,)
    )

    row = cursor.fetchone()

    if row:
        print("\nInvoice Found:")
        print(row)
    else:
        print("Invoice not found.")

    conn.close()


def delete_invoice(invoice_number):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM invoices WHERE invoice_number=?",
        (invoice_number,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Invoice deleted successfully!")
    else:
        print("Invoice not found.")

    conn.close()


def update_payment_status(invoice_number, new_status):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE invoices
        SET payment_status=?
        WHERE invoice_number=?
    """, (new_status, invoice_number))

    conn.commit()

    if cursor.rowcount > 0:
        print("Payment status updated!")
    else:
        print("Invoice not found.")

    conn.close()