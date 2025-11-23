from typing import List, Optional


class Question:
    """Represents a single quiz question with multiple choice options"""

    def __init__(
        self,
        text: str,
        options: List[str],
        correct_answer: str,
        difficulty: str = "medium",
        category: Optional[str] = None,
    ) -> None:
        self._validate_text(text)
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty
        self.category = category

    @staticmethod
    def _validate_text(text: str) -> None:
        """Validate that question text is not empty"""
        if not text or text.strip() == "":
            raise ValueError("Question text cannot be empty")

    def check_answer(self, answer: str) -> bool:
        """Check if the provided answer is correct"""
        return answer == self.correct_answer

    def __eq__(self, other: object) -> bool:
        """Check equality based on question text and options"""
        if not isinstance(other, Question):
            return False  # pragma: no cover
        return (
            self.text == other.text
            and self.options == other.options
            and self.correct_answer == other.correct_answer
        )

    def __hash__(self) -> int:
        """Make Question hashable for use in sets"""
        return hash((self.text, tuple(self.options), self.correct_answer))  # pragma: no cover

    def __repr__(self) -> str:
        """String representation for debugging"""
        return f"Question(text='{self.text[:30]}...', difficulty='{self.difficulty}')"
