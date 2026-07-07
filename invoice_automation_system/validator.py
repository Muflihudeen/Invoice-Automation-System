def validate_invoice(data):

    errors = []

    required = [

        "invoice_number",

        "vendor_name",

        "customer_name",

        "invoice_date",

        "total_amount"

    ]

    for field in required:

        if not data[field]:

            errors.append(f"{field} is missing")

    return errors