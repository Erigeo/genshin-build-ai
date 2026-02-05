from fastapi import FastAPI
from app.api.routes.evaluate import router as evaluate_router

app = FastAPI(title="Genshin Build AI")

app.include_router(evaluate_router, prefix="/api")
