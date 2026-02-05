from app.ai.gemini_service import GeminiService

from dotenv import load_dotenv
load_dotenv()


def test_gemini_response():
    gemini = GeminiService()

    response = gemini.generate_build_analysis(
        character="Hu Tao",
        evaluation={
            "Score": 90,
            "Rank": "S",
            "Prós": ["Crit excelente"],
            "Contras": []
        }
    )

    assert isinstance(response, str)
    assert len(response) > 20
