import re

class GenshinStatsParser:
    @staticmethod
    def parse(text: str) -> dict:
        def find(pattern):
            match = re.search(pattern, text)
            return float(match.group(1)) if match else 0

        return {
            "hp": find(r"HP\s*\+?(\d+)"),
            "crit_rate": find(r"CRIT Rate\s*\+?([\d.]+)%"),
            "crit_dmg": find(r"CRIT DMG\s*\+?([\d.]+)%"),
            "em": find(r"Elemental Mastery\s*\+?(\d+)")
        }
