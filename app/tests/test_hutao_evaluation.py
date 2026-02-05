from app.evaluators.hutao import HuTaoEvaluator

def test_good_hutao_build():
    stats = {
        "hp": 32000,
        "em": 150,
        "crit_rate": 65,
        "crit_dmg": 220,
        "pyro_bonus": 61.6
    }

    evaluator = HuTaoEvaluator(stats)
    result = evaluator.evaluate()

    assert result["rank"] in ["S", "A"]
    assert "EM muito baixo" not in " ".join(result["cons"])
