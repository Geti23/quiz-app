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
    
    def __init__(self):
        """Initialize an empty in-memory database"""
        pass
    
    def add_quiz(self, quiz: Quiz) -> str:
        """
        Create - Add a new quiz to the database.
        
        Args:
            quiz: The Quiz object to store
            
        Returns:
            str: Unique ID assigned to the quiz
        """
        pass
    
    def get_quiz(self, quiz_id: str) -> Optional[Quiz]:
        """
        Read - Retrieve a quiz from the database by ID.
        
        Args:
            quiz_id: The unique identifier of the quiz
            
        Returns:
            Quiz object if found, None otherwise
        """
        pass
    
    def update_quiz(self, quiz_id: str, quiz: Quiz) -> bool:
        """
        Update - Modify an existing quiz in the database.
        
        Args:
            quiz_id: The unique identifier of the quiz to update
            quiz: The updated Quiz object
            
        Returns:
            bool: True if update successful, False if quiz not found
        """
        pass
    
    def delete_quiz(self, quiz_id: str) -> bool:
        """
        Delete - Remove a quiz from the database.
        
        Args:
            quiz_id: The unique identifier of the quiz to delete
            
        Returns:
            bool: True if deletion successful, False if quiz not found
        """
        pass
    
    def list_quizzes(self) -> List[Quiz]:
        """
        List all quizzes in the database.
        
        Returns:
            List of all Quiz objects
        """
        pass
    
    def clear(self) -> None:
        """Remove all quizzes from the database"""
        pass
    
    def __len__(self) -> int:
        """Return the number of quizzes in the database"""
        pass
    
    def __repr__(self) -> str:
        """String representation for debugging"""
        pass