from docling.document_converter import DocumentConverter
import os

from dotenv import load_dotenv
load_dotenv()

file_location = os.getenv('FILE_LOCATION')
source = file_location  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"