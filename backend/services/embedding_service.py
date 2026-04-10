from sentence_transformers import SentenceTransformer
from config import settings

class EmbeddingService:
  def __init__(self):
    self.model = SentenceTransformer(settings.EMBEDDING_MODEL)
  def embed_text(self,text:str) ->list:
    """Generate embedding for a single text"""
    embedding = self.model.encode(text, convert_to_tensor = False)
    return embedding.toList()
  def embed_batch(self,texts: list) -> list:
    """Generate embeddings for multiple texts"""
    embedding = self.model.encode(texts, convert_to_tensor = False)
    return [e.toList() for e in embedding]

embedding_service = EmbeddingService()