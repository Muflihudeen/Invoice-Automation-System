import pdfplumber
import re


def extract_invoice_data(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:

            text = ""

            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        # Debug: Show the extracted text
        print("\n========== PDF CONTENT ==========")
        print(text)
        print("=================================\n")

        data = {
            "invoice_number": "",
            "vendor_name": "",
            "customer_name": "",
            "invoice_date": "",
            "due_date": "",
            "tax_amount": "",
            "total_amount": "",
            "currency": "",
            "payment_status": "Pending"
        }

        patterns = {
            "invoice_number": r"Invoice\s*Number[:\s]*(.+)",
            "vendor_name": r"Vendor[:\s]*(.+)",
            "customer_name": r"Customer[:\s]*(.+)",
            "invoice_date": r"Invoice\s*Date[:\s]*(.+)",
            "due_date": r"Due\s*Date[:\s]*(.+)",
            "tax_amount": r"Tax[:\s]*([\d.]+)",
            "total_amount": r"Total[:\s]*([\d.]+)",
            "currency": r"Currency[:\s]*(.+)"
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)

            if match:
                data[key] = match.group(1).strip()

        return data

    except Exception as e:
        print("Error reading PDF:", e)
        return None