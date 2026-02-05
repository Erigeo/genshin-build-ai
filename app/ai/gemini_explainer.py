from app.ai.gemini_service import GeminiService

class GeminiExplainer:
    def __init__(self):
        self.gemini = GeminiService()

    def explain(self, character: str, build: dict, evaluation: dict) -> str:
        prompt = f"""
Explique de forma curta e clara a avaliação abaixo
para um jogador de Genshin Impact.

Personagem: {character}
Build: {build}
Avaliação: {evaluation}
"""
        return self.gemini.generate(prompt)
