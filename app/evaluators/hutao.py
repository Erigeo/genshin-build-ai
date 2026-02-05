class HuTaoEvaluator:
    def __init__(self, stats):
        self.stats = stats  # Dicionário com HP, ATK, EM, CR, CD, Pyro_Bonus
        self.score = 100
        self.pros = []
        self.cons = []

    def evaluate(self):
    # --- Extrair stats com valores padrão (robustez) ---
        em = self.stats.get('em', 0)
        crit_rate = self.stats.get('crit_rate', 0)
        crit_dmg = self.stats.get('crit_dmg', 0)
        hp = self.stats.get('hp', 0)
        pyro_bonus = self.stats.get('pyro_bonus', 0)

        # --- 1. Proficiência Elemental (EM) ---
        if em < 100:
            self.score -= 15
            self.cons.append(
                "EM muito baixo. Builds Vaporize perdem muito potencial de dano."
            )
        elif 100 <= em <= 300:
            self.pros.append(
                "Ótimo equilíbrio de Proficiência Elemental para Vaporize."
            )
        else:  # em > 300
            self.cons.append(
                "EM muito alto pode estar sacrificando atributos críticos."
            )

        # --- 2. Crit Value (CV) ---
        cv = (crit_rate * 2) + crit_dmg
        if cv < 180:
            self.score -= 20
            self.cons.append(
                f"Crit Value baixo ({cv:.1f}). Priorize substats de crítico."
            )
        elif cv >= 220:
            self.pros.append(
                f"Crit Value excelente ({cv:.1f})."
            )

        # --- 3. Proporção Crítica (1:2) ---
        if crit_rate > 0:
            ratio = crit_dmg / crit_rate
            if not (1.8 <= ratio <= 2.5):
                self.score -= 10
                self.cons.append(
                    f"Proporção Crítica desequilibrada (1:{ratio:.1f})."
                )
        else:
            self.score -= 20
            self.cons.append("Crit Rate zerado. Build inconsistente.")

        # --- 4. HP (fonte de ATK da Hu Tao) ---
        if hp < 28000:
            self.score -= 10
            self.cons.append(
                "HP baixo. O bônus da habilidade elemental será limitado."
            )
        elif hp > 40000:
            self.cons.append(
                "HP muito alto pode gerar diminishing returns."
            )

        # --- 5. Bônus Pyro ---
        if pyro_bonus < 46.6:
            self.score -= 10
            self.cons.append(
                "Bônus Pyro abaixo do ideal. Considere um cálice Pyro DMG."
            )
        else:
            self.pros.append(
                "Bônus Pyro adequado para maximizar o dano elemental."
            )

        # --- Rank Final ---
        final_score = max(0, min(100, self.score))
        if final_score >= 90:
            rank = "S"
        elif final_score >= 75:
            rank = "A"
        elif final_score >= 60:
            rank = "B"
        else:
            rank = "C"

        return {
            "score": final_score,
            "rank": rank,
            "pros": self.pros,
            "cons": self.cons
        }