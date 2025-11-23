from src.quiz import Quiz
from src.question import Question


class TestQuizCategories:
    """Tests for organizing questions by category"""

    def test_question_has_category(self):
        question = Question(
            text="What is photosynthesis?",
            options=["A", "B", "C", "D"],
            correct_answer="A",
            category="Biology",
        )
        assert question.category == "Biology"

    def test_quiz_can_get_questions_by_category(self):
        quiz = Quiz(title="Science Quiz")
        bio_q = Question("Bio?", ["A", "B"], "A", category="Biology")
        chem_q = Question("Chem?", ["C", "D"], "C", category="Chemistry")

        quiz.add_question(bio_q)
        quiz.add_question(chem_q)

        bio_questions = quiz.get_questions_by_category("Biology")
        assert len(bio_questions) == 1
        assert bio_questions[0].category == "Biology"

    def test_quiz_get_score_by_category(self):
        quiz = Quiz(title="Categorized Quiz")
        bio_q1 = Question("Bio1?", ["A", "B"], "A", category="Biology")
        bio_q2 = Question("Bio2?", ["C", "D"], "C", category="Biology")
        chem_q = Question("Chem?", ["E", "F"], "E", category="Chemistry")

        quiz.add_question(bio_q1)
        quiz.add_question(bio_q2)
        quiz.add_question(chem_q)

        quiz.submit_answer(0, "A")  # Correct
        quiz.submit_answer(1, "D")  # Incorrect
        quiz.submit_answer(2, "E")  # Correct

        bio_score = quiz.get_score_by_category("Biology")
        assert bio_score["score"] == 1
        assert bio_score["total"] == 2
        assert bio_score["percentage"] == 50.0
