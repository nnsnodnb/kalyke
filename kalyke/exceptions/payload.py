class RelevanceScoreOutOfRangeException(Exception):
    _relevance_score: float

    def __init__(self, relevance_score: float) -> None:
        self._relevance_score = relevance_score

    def __str__(self) -> str:
        return f"The system uses the relevance_score, a value between 0 and 1. Did set {self._relevance_score}."
