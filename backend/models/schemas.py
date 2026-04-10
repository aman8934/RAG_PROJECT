from pydantic import BaseModel
from typing import List, Optional

class DocumentUpload(BaseModel):
  filename: str
  content: bytes
class ChunkData(BaseModel):
  id:str
  text:str
  metadata:dict
  embedding:Optional[List[float]] = None
class QueryRequest(BaseModel):
  query:str
  top_k:int =5
class ChatMessage(BaseModel):
  role:str
  content:str
  source : Optional[List[str]]
class ChatResponse(BaseModel):
  answer:str
  sources: List[str]
  confidence:float