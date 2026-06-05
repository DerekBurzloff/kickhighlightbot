class HighlightDetector:
    """Rainbow Six Siege hype detector"""
    R6_KEYWORDS = [
        "clutch", "ace", "flick", "one tap", "headshot", "insane", 
        "wtf", "ninja", "plant", "defuse", "1vX", "1v1", "1v2", "1v3",
        "crazy", "god", "sick", "aim", "peek"
    ]

    def detect(self, text: str) -> bool:
        if not text:
            return False
        lower = text.lower()
        score = sum(1 for kw in self.R6_KEYWORDS if kw in lower)
        return score >= 2
