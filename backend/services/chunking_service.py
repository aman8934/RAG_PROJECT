from config import settings
import uuid


class ChunkingService:
  def __init__(self, chunk_size = settings.CHUNK_SIZE, overlap = settings.CHUNK_OVERLAP):
    self.chunk_size = chunk_size
    self.overlap = overlap
  def chunk_text(self, text:str, metadate: dict = None):
    print("ENTERING INTO CHUNKING TEXTS")
    chunks =[]
    steps = self.chunk_size - self.overlap

    for i in range(0,len(text), steps):
      chunk_text = text[i: i+self.chunk_size]
      if len(chunk_text)>50:
        chunk = {
          "id":str(uuid.uuid4()),
          "text":self.chunk_text,
          "metadata":{
            "start_pos":i,
            "end_pos":min(i+self.chunk_size,len(text))
          }
        }
        chunks.append(chunk)

chunking_service = ChunkingService()