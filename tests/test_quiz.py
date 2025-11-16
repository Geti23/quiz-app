from src.quiz import Quiz
from src.question import Question


class TestQuiz:
    """Tests for Quiz functionality"""

    def test_create_empty_quiz(self):
        quiz = Quiz(title="Math Quiz")
        assert quiz.title == "Math Quiz"
        assert len(quiz.questions) == 0

    def test_add_question_to_quiz(self):
        quiz = Quiz(title="Science Quiz")
        question = Question(
            text="What is H2O?",
            options=["Water", "Hydrogen", "Oxygen", "Salt"],
            correct_answer="Water",
        )
        quiz.add_question(question)
        assert len(quiz.questions) == 1

    def test_cannot_add_duplicate_questions(self):
        quiz = Quiz(title="History Quiz")
        question = Question(
            text="Who was the first president?",
            options=["Washington", "Lincoln", "Jefferson", "Adams"],
            correct_answer="Washington",
        )
        quiz.add_question(question)
        quiz.add_question(question)
        assert len(quiz.questions) == 1  # Should not add duplicate

    def test_get_question_by_index(self):
        quiz = Quiz(title="Geography Quiz")
        q1 = Question("Question 1?", ["A", "B"], "A")
        q2 = Question("Question 2?", ["C", "D"], "C")
        quiz.add_question(q1)
        quiz.add_question(q2)

        assert quiz.get_question(0) == q1
        assert quiz.get_question(1) == q2

    def test_submit_answer_and_track_score(self):
        quiz = Quiz(title="Test Quiz")
        q1 = Question("Q1?", ["A", "B"], "A")
        q2 = Question("Q2?", ["C", "D"], "C")
        quiz.add_question(q1)
        quiz.add_question(q2)

        quiz.submit_answer(0, "A")  # Correct
        quiz.submit_answer(1, "D")  # Incorrect

        result = quiz.get_result()
        assert result is not None
        assert result.score == 1
        assert result.total == 2
        assert result.percentage == 50.0
