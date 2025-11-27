import uuid
from typing import List, Dict, Optional
from copy import deepcopy
from src.quiz import Quiz


class QuizDatabase:
    """
    In-memory database for storing and managing quizzes.

    Provides CRUD operations (Create, Read, Update, Delete) for Quiz objects.
    Data is stored in memory and will be lost when the application terminates.
    """

    def __init__(self) -> None:
        """Initialize an empty in-memory database"""
        self._storage: Dict[str, Quiz] = {}

    def add_quiz(self, quiz: Quiz) -> str:
        """
        Create - Add a new quiz to the database.

        Args:
            quiz: The Quiz object to store

        Returns:
            str: Unique ID assigned to the quiz
        """
        quiz_id = str(uuid.uuid4())
        # Store a deep copy and set the ID
        quiz_copy = deepcopy(quiz)
        quiz_copy.id = quiz_id
        self._storage[quiz_id] = quiz_copy
        return quiz_id

    def get_quiz(self, quiz_id: str) -> Optional[Quiz]:
        """
        Read - Retrieve a quiz from the database by ID.

        Args:
            quiz_id: The unique identifier of the quiz

        Returns:
            Quiz object if found, None otherwise
        """
        if quiz_id not in self._storage:
            return None
        # Return a deep copy to prevent external modifications
        return deepcopy(self._storage[quiz_id])

    def update_quiz(self, quiz_id: str, quiz: Quiz) -> bool:
        """
        Update - Modify an existing quiz in the database.

        Args:
            quiz_id: The unique identifier of the quiz to update
            quiz: The updated Quiz object

        Returns:
            bool: True if update successful, False if quiz not found
        """
        if quiz_id not in self._storage:
            return False
        # Store a deep copy and ensure ID is preserved
        quiz_copy = deepcopy(quiz)
        quiz_copy.id = quiz_id
        self._storage[quiz_id] = quiz_copy
        return True

    def delete_quiz(self, quiz_id: str) -> bool:
        """
        Delete - Remove a quiz from the database.

        Args:
            quiz_id: The unique identifier of the quiz to delete

        Returns:
            bool: True if deletion successful, False if quiz not found
        """
        if quiz_id not in self._storage:
            return False
        del self._storage[quiz_id]
        return True

    def list_quizzes(self) -> List[Quiz]:
        """
        List all quizzes in the database.

        Returns:
            List of all Quiz objects
        """
        # Return deep copies to prevent external modifications
        return [deepcopy(quiz) for quiz in self._storage.values()]

    def clear(self) -> None:
        """Remove all quizzes from the database"""
        self._storage.clear()

    def __len__(self) -> int:
        """Return the number of quizzes in the database"""
        return len(self._storage)

    def __repr__(self) -> str:
        """String representation for debugging"""
        return f"QuizDatabase(quizzes={len(self._storage)})"
