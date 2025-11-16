import pytest
from src.question import Question


class TestQuestion:
    """Tests for individual Question objects"""

    def test_create_multiple_choice_question(self):
        question = Question(text="What is 2 + 2?", options=["3", "4", "5", "6"], correct_answer="4")
        assert question is not None
        assert question.text == "What is 2 + 2?"
        assert len(question.options) == 4
        assert question.correct_answer == "4"

    def test_check_correct_answer(self):
        question = Question(
            text="What is the capital of France?",
            options=["London", "Paris", "Berlin", "Madrid"],
            correct_answer="Paris",
        )
        assert question is not None
        assert question.check_answer("Paris") == True
        assert question.check_answer("London") == False

    def test_question_requires_text(self):
        with pytest.raises(ValueError):
            Question(text="", options=["A", "B"], correct_answer="A")
