from src.result import QuizResult


class TestQuizResult:
    """Tests for quiz results and scoring"""

    def test_perfect_score(self):
        result = QuizResult(score=5, total=5)
        assert result is not None
        assert result.is_perfect() is True

    def test_passing_grade(self):
        result = QuizResult(score=6, total=10)
        assert result is not None
        assert result.is_passing(threshold=60) is True
        assert result.is_passing(threshold=70) is False

    def test_result_summary(self):
        result = QuizResult(score=8, total=10)
        summary = result.get_summary()
        assert summary is not None
        assert "8" in summary
        assert "10" in summary
        assert "80" in summary
