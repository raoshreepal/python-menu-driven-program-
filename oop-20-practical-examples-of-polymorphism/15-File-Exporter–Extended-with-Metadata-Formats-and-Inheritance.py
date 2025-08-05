'''
🔹Scenario: Export different documents (Invoice, Report) to various formats with metadata.
🔹Definition: Polymorphism via the export() method, format-dependent + document type dependent.
'''
class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_metadata(self):
        return f"Title: {self.title}, Author: {self.author}"

    def export(self):
        raise NotImplementedError("Subclass must implement export()")

class PDFExporter(Document):
    def export(self):
        return f"[PDF Export]\n{self.get_metadata()}\nExported as PDF"

class CSVExporter(Document):
    def export(self):
        return f"[CSV Export]\n{self.get_metadata()}\nExported as CSV"

class JSONExporter(Document):
    def export(self):
        return f"[JSON Export]\n{self.get_metadata()}\nExported as JSON"

# Multiple documents in different formats
exports = {
    "invoice_001": PDFExporter("Invoice Aug", "Account Dept"),
    "sales_data": CSVExporter("August Sales", "Sales Dept"),
    "employee_info": JSONExporter("HR List", "HR Dept")
}

for doc_id, exporter in exports.items():
    print(f"\n--- {doc_id.upper()} ---")
    print(exporter.export())
