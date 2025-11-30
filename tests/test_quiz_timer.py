from src.quiz import Quiz
from src.question import Question


class TestQuizTimer:
    """Tests for quiz timing functionality"""

    def test_quiz_has_time_limit(self):
        """UNIT: Quiz stores configured time limit"""
        quiz = Quiz(title="Timed Quiz", time_limit_seconds=300)
        assert quiz.time_limit_seconds == 300

    def test_quiz_starts_timer_on_first_answer(self):
        """INTEGRATION: submitting first answer starts quiz timer"""
        quiz = Quiz(title="Timed Quiz", time_limit_seconds=60)
        quiz.add_question(Question("Q1?", ["A", "B"], "A"))

        quiz.submit_answer(0, "A")
        assert quiz.start_time is not None

    def test_quiz_tracks_elapsed_time(self):
        """INTEGRATION: elapsed time tracked after starting timer"""
        import time

        quiz = Quiz(title="Timed Quiz", time_limit_seconds=60)
        quiz.add_question(Question("Q1?", ["A", "B"], "A"))

        quiz.submit_answer(0, "A")
        time.sleep(0.1)
        elapsed = quiz.get_elapsed_time()
        assert elapsed >= 0.1

    def test_quiz_can_check_if_time_expired(self):
        """INTEGRATION: time expiration detection after waiting"""
        import time

        quiz = Quiz(title="Timed Quiz", time_limit_seconds=0.1)
        quiz.add_question(Question("Q1?", ["A", "B"], "A"))

        quiz.submit_answer(0, "A")
        time.sleep(0.2)
        assert quiz.is_time_expired() is True
