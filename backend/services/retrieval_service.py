import chromadb
from config import settings
from .embedding_service import embedding_service

class RetrievalService:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_PERSIST_DIR)
        self.collection = self.client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )
    
    def add_documents(self, chunks: list):
        """Add document chunks to vector DB"""
        ids = [chunk["id"] for chunk in chunks]
        documents = [chunk["text"] for chunk in chunks]
        embeddings = embedding_service.embed_batch(documents)
        metadatas = [chunk["metadata"] for chunk in chunks]
        
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )
    
    def retrieve(self, query: str, top_k: int = 5) -> list:
        """Retrieve relevant chunks for a query"""
        query_embedding = embedding_service.embed_text(query)
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        retrieved_docs = []
        if results["documents"]:
            for i, doc in enumerate(results["documents"][0]):
                retrieved_docs.append({
                    "text": doc,
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i] if results["distances"] else 0
                })
        
        return retrieved_docs

retrieval_service = RetrievalService()