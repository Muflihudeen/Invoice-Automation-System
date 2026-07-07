# System Architecture Overview

## Workflow

```
User
   │
   ▼
Select Invoice PDF
   │
   ▼
PDF Processor
   │
   ▼
Extract Invoice Data
   │
   ▼
Validator
   │
   ▼
SQLite Database
   │
   ├──────────────► View Invoices
   │
   ├──────────────► Search Invoice
   │
   ├──────────────► Delete Invoice
   │
   ├──────────────► Export CSV
   │
   ├──────────────► Export Excel
   │
   └──────────────► Generate Report
                      │
                      ▼
                 System Logs
```

## Modules

- **main.py** – Main menu and application flow
- **pdf_processor.py** – Reads invoice PDF files and extracts invoice details
- **validator.py** – Validates extracted invoice data
- **database_manager.py** – Handles SQLite database operations
- **exporter.py** – Exports invoice data to CSV and Excel
- **report_generator.py** – Generates invoice summary reports
- **logger_manager.py** – Records system events and activities
- **config.py** – Stores project configuration values