class ComplianceAnalyzer:
    def __init__(self):
        self.keywords = [
            "fraud", "bribe", "insider", "leak",
            "confidential", "illegal", "harassment"
        ]

    def analyze(self, text):
        score = 0
        for word in self.keywords:
            if word in text.lower():
                score += 10

        if score >= 30:
            risk = "High"
        elif score >= 10:
            risk = "Medium"
        else:
            risk = "Low"

        return risk, score
