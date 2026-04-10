from pydantic_settings import BaseSettings

class Settings(BaseSettings):
 
  GEMINI_API :str
  API_TITLE: str = "RAG Engine"
  API_VERSION: str = "1.0.0"

  # GEMINI_API :str = GEMINI_API
  GEMINI_MODEL:str
  EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
  # Vector DB
  CHROMA_PERSIST_DIR: str = "./chroma_data"

  CHUNK_SIZE: int = 500
  CHUNK_OVERLAP: int = 100
  class Config:
      env_file = ".env"
settings = Settings()