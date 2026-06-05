class HighlightDetector:
    """R6 Siege focused hype detector"""
    R6_KEYWORDS = ["clutch", "ace", "flick", "one tap", "headshot", "insane", "wtf", "ninja", "plant"]

    def detect(self, text: str) -> bool:
        lower = text.lower()
        return any(kw in lower for kw in self.R6_KEYWORDS)
