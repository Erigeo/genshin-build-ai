import json
import re # Add this for cleaning the string
from app.ai.gemini_service import GeminiService

class GeminiParser:
    def __init__(self):
        self.gemini = GeminiService()

    def parse_hutao_build(self, ocr_text: str) -> dict:
        prompt = f"""
        Você é um parser técnico de builds de Genshin Impact.
        Extraia os dados abaixo e retorne APENAS um JSON válido.
        Não explique nada.
        Não use blocos de código markdown.
        Se não encontrar, use null.
        
        Texto OCR: {ocr_text}
        ... (rest of your prompt)
        """
        
        raw = self.gemini.generate(prompt)
        
        if not raw:
            raise ValueError("Gemini retornou uma resposta vazia")

        # Clean the response: remove markdown backticks if present
        clean_json = re.sub(r'```json|```', '', raw).strip()

        try:
            return json.loads(clean_json)
        except json.JSONDecodeError as e:
            print(f"DEBUG: Raw response was: {raw}") # Helps you see what went wrong
            raise ValueError(f"Erro ao decodificar JSON: {str(e)}")