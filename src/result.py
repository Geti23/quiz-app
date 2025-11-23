class QuizResult:
    """Represents the result of a completed quiz"""

    def __init__(self, score: int, total: int) -> None:
        self.score = score
        self.total = total
        self.percentage = self._calculate_percentage(score, total)

    @staticmethod
    def _calculate_percentage(score: int, total: int) -> float:
        """Calculate percentage score"""
        return (score / total * 100) if total > 0 else 0.0

    def is_perfect(self) -> bool:
        """Check if the score is perfect (100%)"""
        return self.score == self.total

    def is_passing(self, threshold: int = 60) -> bool:
        """Check if the score meets the passing threshold"""
        return self.percentage >= threshold

    def get_summary(self) -> str:
        """Get a formatted summary of the results"""
        return f"Score: {self.score}/{self.total} ({self.percentage:.1f}%)"

    def __repr__(self) -> str:
        """String representation for debugging"""
        return (
            f"QuizResult(score={self.score}, total={self.total}, percentage={self.percentage:.1f}%)"
        )
