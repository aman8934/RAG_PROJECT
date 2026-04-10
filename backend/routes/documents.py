from fastapi import APIRouter, UploadFile, File
from services.document_service import document_service
from services.chunking_service import chunking_service
from services.retrieval_service import retrieval_service

router = APIRouter(prefix = "/documents" , tags = ["documents"])

@router.post("/upload")

async def upload_document(file:UploadFile = File(...)):
  """Upload and process a document"""

  try:
    content = await file.read()
    # Extract text
    text = document_service.extract_text(content,file.filename)

    # Chunk text
    chunks = chunking_service.chunk_text(
      text,
      metadata = {"filename" : file.filename}
    )

    #Store in vectore DB
    retrieval_service.add_documents(chunks)

    return {
      "status":"success",
      "filename":file.filename,
      "chunks_created": len(chunks)
    }
  except Exception as e:
    return {"status" :"error" , "message":str(e)}
  
  