import os

from dotenv import load_dotenv
from markitdown import MarkItDown

load_dotenv()

file_location = os.getenv('FILE_LOCATION')
md = MarkItDown(docintel_endpoint="<document_intelligence_endpoint>")
result = md.convert(file_location)
print(result.text_content)
