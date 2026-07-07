# Database Schema

## Database Name

invoices.db

## Table: invoices

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| invoice_number | TEXT (Primary Key) | Unique invoice number |
| vendor_name | TEXT | Vendor or company name |
| customer_name | TEXT | Customer name |
| invoice_date | TEXT | Invoice issue date |
| due_date | TEXT | Invoice due date |
| tax_amount | REAL | Tax amount |
| total_amount | REAL | Total invoice amount |
| currency | TEXT | Currency used |
| payment_status | TEXT | Payment status (Pending/Paid) |
| processing_date | TEXT | Date and time the invoice was processed |