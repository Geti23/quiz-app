from src.quiz import Quiz
from src.question import Question


class TestQuizReview:
    """Tests for reviewing quiz answers"""

    def test_get_incorrect_answers(self):
        quiz = Quiz(title="Review Quiz")
        q1 = Question("Q1?", ["A", "B"], "A")
        q2 = Question("Q2?", ["C", "D"], "C")
        q3 = Question("Q3?", ["E", "F"], "E")

        quiz.add_question(q1)
        quiz.add_question(q2)
        quiz.add_question(q3)

        quiz.submit_answer(0, "A")  # Correct
        quiz.submit_answer(1, "D")  # Incorrect
        quiz.submit_answer(2, "F")  # Incorrect

        incorrect = quiz.get_incorrect_answers()
        assert len(incorrect) == 2
        assert 1 in incorrect
        assert 2 in incorrect

    def test_get_answer_details(self):
        quiz = Quiz(title="Detail Quiz")
        question = Question("What is 5 + 5?", ["8", "10", "12"], "10")
        quiz.add_question(question)
        quiz.submit_answer(0, "8")

        details = quiz.get_answer_details(0)
        assert details["question"] == question
        assert details["submitted_answer"] == "8"
        assert details["correct_answer"] == "10"
        assert details["is_correct"] is False
