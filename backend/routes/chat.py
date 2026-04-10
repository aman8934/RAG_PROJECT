from fastapi import APIRouter
from models.schemas import QueryRequest , ChatResponse
from services.retrieval_service import retrieval_service
from services.llm_service import llm_service

router = APIRouter(prefix = "/chat",tags = ["chat"])

@router.post("/query" , response_model = ChatResponse)
async def query_rag(request:QueryRequest):
  """Query the RAG system"""
  try:
    retrieved = retrieval_service.retrieve(request.query , top_k = request.top_k)

    # Build context
    context = "\n".join([doc["text"] for doc in retrieved])

    # generate answer
    answer = llm_service.generate_response(request.query,context)

    # extract source 
    sources = [ doc["metadata"].get("filename","Unknown") for doc in retrieved]
    return ChatResponse(
      answer = answer,
      sources = list(set(sources)),
      confidence = 0.8
    )
  except Exception as e:
    return ChatResponse(
      answer = f"Error : {str(e)}",
      sources=[],
      confidence = 0.0
    )
