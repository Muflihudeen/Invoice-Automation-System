from database_manager import *
from pdf_processor import extract_invoice_data
from validator import validate_invoice
from exporter import *
from logger_manager import log_event
from report_generator import generate_report

create_table()

while True:

    print("\n===== SMART INVOICE PROCESSING SYSTEM =====")
    print("1. Process Invoice")
    print("2. View All Invoices")
    print("3. Search Invoice")
    print("4. Delete Invoice")
    print("5. Export CSV")
    print("6. Export Excel")
    print("7. Generate Report")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        pdf_path = input("Enter PDF path: ")

        data = extract_invoice_data(pdf_path)

        if data:

            errors = validate_invoice(data)

            if errors:
                print("\nValidation Errors:")
                for error in errors:
                    print("-", error)
            else:
                insert_invoice(data)

            log_event(
                f"Invoice {data['invoice_number']} processed successfully."
            )

    elif choice == "2":
        view_invoices()

    elif choice == "3":
        invoice_number = input("Enter Invoice Number: ")
        search_invoice(invoice_number)

    elif choice == "4":
        invoice_number = input("Enter Invoice Number to Delete: ")
        delete_invoice(invoice_number)

    elif choice == "5":
        export_csv()

    elif choice == "6":
        export_excel()

    elif choice == "7":
        generate_report()
        
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")