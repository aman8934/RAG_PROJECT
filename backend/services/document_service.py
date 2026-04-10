from pypdf import PdfReader
from docx import Document
import io


class DocumentService:
  @staticmethod
  def extract_pdf(file_bytes: bytes)-> str:
    """Extract text from PDF"""
    print("ENTERING INTO EXTRACTING PDF")
    pdf_reader = PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in pdf_reader.pages:
      text+=page.extract_text()
    return text
  @staticmethod
  def extract_docx(file_bytes: bytes) -> str:
    """Extract text from Word document"""
    doc = Document(io.BytesIO(file_bytes))
    text = "\n".join([para.text for para in doc.paragraphs])
    return text
  
  @staticmethod
  def extract_text(file_bytes: bytes, filename: str) -> str:
    """Extract text from various file types"""

    if filename.endswith(".docx"):
      return DocumentService.extract_docx(file_bytes)
    elif filename.endswith(".pdf"):
      return DocumentService.extract_pdf(file_bytes)
    elif filename.endswith(".txt"):
      return DocumentService.extract_text(file_bytes)
    else:
      raise ValueError(f"Unsopported file type: {filename}")
    
document_service = DocumentService()