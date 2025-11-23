from src.quiz import Quiz
from src.question import Question


class TestQuestionDifficulty:
    """Tests for question difficulty levels"""
    
    def test_question_has_difficulty_level(self):
        question = Question(
            text="What is 2 + 2?",
            options=["3", "4", "5", "6"],
            correct_answer="4",
            difficulty="easy"
        )
        assert question.difficulty == "easy"
    
    def test_question_default_difficulty_is_medium(self):
        question = Question("Q?", ["A", "B"], "A")
        assert question.difficulty == "medium"
    
    def test_filter_questions_by_difficulty(self):
        quiz = Quiz(title="Mixed Quiz")
        easy_q = Question("Easy?", ["A", "B"], "A", difficulty="easy")
        hard_q = Question("Hard?", ["C", "D"], "C", difficulty="hard")
        
        quiz.add_question(easy_q)
        quiz.add_question(hard_q)
        
        easy_questions = quiz.get_questions_by_difficulty("easy")
        assert len(easy_questions) == 1
        assert easy_questions[0].difficulty == "easy"