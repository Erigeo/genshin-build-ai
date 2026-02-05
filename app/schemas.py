from pydantic import BaseModel

class HuTaoStats(BaseModel):
    hp: float
    em: float = 0
    crit_rate: float
    crit_dmg: float
    pyro_bonus: float = 0


class EvaluationResponse(BaseModel):
    score: int
    rank: str
    pros: list[str]
    cons: list[str]
