from src.database import QuizDatabase
from src.quiz import Quiz
from src.question import Question


class TestQuizDatabase:
    """Tests for in-memory database CRUD operations"""

    def test_create_quiz_in_database(self):
        """UNIT: QuizDatabase.add_quiz creates and returns an id"""
        db = QuizDatabase()
        quiz = Quiz(title="Math Quiz")

        # Create (Add) operation
        quiz_id = db.add_quiz(quiz)
        assert quiz_id is not None
        assert isinstance(quiz_id, str)

    def test_read_quiz_from_database(self):
        """UNIT: QuizDatabase.get_quiz returns stored quiz"""
        db = QuizDatabase()
        quiz = Quiz(title="Science Quiz")
        quiz_id = db.add_quiz(quiz)

        # Read operation
        retrieved_quiz = db.get_quiz(quiz_id)
        assert retrieved_quiz is not None
        assert retrieved_quiz.title == "Science Quiz"

    def test_update_quiz_in_database(self):
        """UNIT: QuizDatabase.update_quiz updates stored quiz data"""
        db = QuizDatabase()
        quiz = Quiz(title="Original Title")
        quiz_id = db.add_quiz(quiz)

        # Update operation
        quiz.title = "Updated Title"
        quiz.add_question(Question("New Q?", ["A", "B"], "A"))

        success = db.update_quiz(quiz_id, quiz)
        assert success is True

        # Verify update
        updated_quiz = db.get_quiz(quiz_id)
        assert updated_quiz.title == "Updated Title"
        assert len(updated_quiz.questions) == 1

    def test_delete_quiz_from_database(self):
        """UNIT: QuizDatabase.delete_quiz removes quiz and returns success flag"""
        db = QuizDatabase()
        quiz = Quiz(title="To Be Deleted")
        quiz_id = db.add_quiz(quiz)

        # Delete operation
        success = db.delete_quiz(quiz_id)
        assert success is True

        # Verify deletion
        deleted_quiz = db.get_quiz(quiz_id)
        assert deleted_quiz is None
        assert db.__len__() == 0

    def test_list_all_quizzes(self):
        """UNIT: QuizDatabase.list_quizzes returns all quizzes"""
        db = QuizDatabase()
        quiz1 = Quiz(title="Quiz 1")
        quiz2 = Quiz(title="Quiz 2")

        db.add_quiz(quiz1)
        db.add_quiz(quiz2)

        all_quizzes = db.list_quizzes()
        assert len(all_quizzes) == 2
        assert all(isinstance(q, Quiz) for q in all_quizzes)

    def test_get_nonexistent_quiz(self):
        """UNIT: get_quiz returns None for unknown id"""
        db = QuizDatabase()
        result = db.get_quiz("nonexistent_id")
        assert result is None

    def test_update_nonexistent_quiz(self):
        """UNIT: update_quiz returns False for nonexistent id"""
        db = QuizDatabase()
        quiz = Quiz(title="Test")
        success = db.update_quiz("nonexistent_id", quiz)
        assert success is False

    def test_delete_nonexistent_quiz(self):
        """UNIT: delete_quiz returns False for nonexistent id"""
        db = QuizDatabase()
        success = db.delete_quiz("nonexistent_id")
        assert success is False

    def test_database_generates_unique_ids(self):
        """UNIT: database generates unique ids for each add_quiz call"""
        db = QuizDatabase()
        quiz1 = Quiz(title="Quiz 1")
        quiz2 = Quiz(title="Quiz 2")

        id1 = db.add_quiz(quiz1)
        id2 = db.add_quiz(quiz2)

        assert id1 != id2

    def test_clear_database(self):
        """UNIT: clear removes all stored quizzes"""
        db = QuizDatabase()
        db.add_quiz(Quiz(title="Quiz 1"))
        db.add_quiz(Quiz(title="Quiz 2"))

        db.clear()
        assert len(db.list_quizzes()) == 0

    def test_quiz_id_is_stored_in_quiz_object(self):
        """UNIT: stored quiz retains its id after add_quiz"""
        db = QuizDatabase()
        quiz = Quiz(title="Test Quiz")

        # Add quiz to database
        quiz_id = db.add_quiz(quiz)

        # Retrieve quiz and verify ID is set
        retrieved_quiz = db.get_quiz(quiz_id)
        assert retrieved_quiz.id == quiz_id
        assert retrieved_quiz.id is not None

    def test_quiz_id_persists_after_update(self):
        """UNIT: quiz id persists through update operations"""
        db = QuizDatabase()
        quiz = Quiz(title="Original")
        quiz_id = db.add_quiz(quiz)

        # Update the quiz
        updated_quiz = Quiz(title="Updated")
        db.update_quiz(quiz_id, updated_quiz)

        # Verify ID is still the same
        retrieved = db.get_quiz(quiz_id)
        assert retrieved.id == quiz_id
