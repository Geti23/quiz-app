class QuizResult:
    """Represents the result of a completed quiz"""

    def __init__(self, score, total):
        self.score = score
        self.total = total
        self.percentage = (score / total * 100) if total > 0 else 0.0

    def is_perfect(self):
        """Check if the score is perfect (100%)"""
        pass

    def is_passing(self, threshold=60):
        """Check if the score meets the passing threshold"""
        pass

    def get_summary(self):
        """Get a formatted summary of the results"""
        pass
