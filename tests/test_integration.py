from src.quiz import Quiz
from src.question import Question


class TestQuizIntegration:
    """End-to-end tests for complete quiz workflow"""

    def test_complete_quiz_flow(self):
        # Create quiz
        quiz = Quiz(title="Python Basics")

        # Add questions
        quiz.add_question(
            Question(
                "What is a list?", ["Array", "Dictionary", "Collection", "Database"], "Collection"
            )
        )
        quiz.add_question(
            Question("What is a tuple?", ["Mutable", "Immutable", "Function", "Class"], "Immutable")
        )

        # Take quiz
        quiz.submit_answer(0, "Collection")
        quiz.submit_answer(1, "Immutable")

        # Check results
        result = quiz.get_result()
        assert result is not None
        assert result.is_perfect() == True
        assert result.score == 2
