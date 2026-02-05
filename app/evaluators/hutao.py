class HuTaoEvaluator:
    def __init__(self, data: dict):
        self.data = data

    def evaluate(self) -> dict:
        score = 0
        notes = []

        hp = self.data.get("hp")
        crit_rate = self.data.get("crit_rate")
        crit_dmg = self.data.get("crit_dmg")
        weapon = self.data.get("weapon")

        if weapon and "Homa" in weapon:
            score += 20
            notes.append("Staff of Homa é BiS")

        if hp:
            if hp >= 35000:
                score += 30
                notes.append("HP excelente")
            elif hp >= 30000:
                score += 20

        if crit_rate and crit_rate >= 65:
            score += 20
        if crit_dmg and crit_dmg >= 200:
            score += 20

        if score >= 85:
            rank = "S"
        elif score >= 70:
            rank = "A"
        elif score >= 55:
            rank = "B"
        else:
            rank = "C"

        return {
            "score": score,
            "rank": rank,
            "notes": notes
        }
