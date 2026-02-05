from fastapi import FastAPI
from app.evaluators.hutao import HuTaoEvaluator
from app.schemas import HuTaoStats, EvaluationResponse

app = FastAPI(title="Genshin Build AI")

@app.post("/evaluate/hutao", response_model=EvaluationResponse)
def evaluate_hutao(stats: HuTaoStats):
    evaluator = HuTaoEvaluator(stats.dict())
    return evaluator.evaluate()
