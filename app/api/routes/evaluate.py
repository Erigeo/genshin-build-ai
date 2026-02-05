from fastapi import APIRouter, UploadFile, File, Query
from app.ocr.ocr_service import OCRService
from app.ai.gemini_parser import GeminiParser
from app.evaluators.hutao import HuTaoEvaluator
from app.ai.gemini_explainer import GeminiExplainer

router = APIRouter()

@router.post("/evaluate-build")
async def evaluate_build(
    character: str = Query(...),
    image: UploadFile = File(...)
):
    image_bytes = await image.read()

    ocr_text = OCRService.extract_text(image_bytes)

    parser = GeminiParser()
    structured = parser.parse_hutao_build(ocr_text)

    evaluator = HuTaoEvaluator(structured)
    evaluation = evaluator.evaluate()

    explainer = GeminiExplainer()
    explanation = explainer.explain(character, structured, evaluation)

    return {
        "character": character,
        "structured_build": structured,
        "evaluation": evaluation,
        "analysis": explanation
    }
