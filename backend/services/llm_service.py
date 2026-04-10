from google import genai
from config import settings
# client = genai.Client()


class LLMService:
  def __init__(self):
    self.client = genai.Client(api_key = settings.GEMINI_API)
    self.model = settings.GEMINI_MODEL
  
  def generate_response(self,query:str, context: str):
    """Generate answer using retrieved context"""
    prompt = f"""You are helpful assistant. Use the provided context to answer the question. Context : {context}
    Question :{query}
    Answer:"""
    response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 500,
            }
        )
    return response.text
llm_service = LLMService()


