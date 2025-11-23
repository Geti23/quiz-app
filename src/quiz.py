from typing import Dict, List, Optional
from src.question import Question
from src.result import QuizResult
import time


class Quiz:
    """
    Represents a quiz with multiple questions, answer tracking, and scoring.

    Supports features like:
    - Time limits
    - Question categorization and difficulty levels
    - Answer review and detailed feedback
    """

    def __init__(self, title: str, time_limit_seconds: Optional[int] = None) -> None:
        self.title = title
        self.questions: List[Question] = []
        self.answers: Dict[int, str] = {}  # Maps question index to submitted answer
        self.time_limit_seconds = time_limit_seconds
        self.start_time: Optional[float] = None

    # Question Management

    def add_question(self, question: Question) -> None:
        """Add a question to the quiz, avoiding duplicates"""
        if question not in self.questions:
            self.questions.append(question)

    def get_question(self, index: int) -> Question:
        """Get a question by its index"""
        return self.questions[index]

    # Answer Submission and Timing

    def submit_answer(self, question_index: int, answer: str) -> None:
        """Submit an answer for a specific question"""
        self._start_timer_if_needed()
        self.answers[question_index] = answer

    def _start_timer_if_needed(self) -> None:
        """Start the timer on first answer submission"""
        if self.start_time is None:
            self.start_time = time.time()

    def get_elapsed_time(self) -> float:
        """Get the elapsed time since the quiz started"""
        if self.start_time is None:
            return 0  # pragma: no cover
        return time.time() - self.start_time

    def is_time_expired(self) -> bool:
        """Check if the time limit has been exceeded"""
        if self.time_limit_seconds is None:
            return False  # pragma: no cover
        return self.get_elapsed_time() > self.time_limit_seconds

    # Scoring and Results

    def get_result(self) -> QuizResult:
        """Calculate and return the quiz result"""
        score = self._calculate_score()
        total = len(self.questions)
        return QuizResult(score, total)

    def _calculate_score(self) -> int:
        """Calculate the total number of correct answers"""
        score = 0
        for index, answer in self.answers.items():
            if self._is_answer_correct(index, answer):
                score += 1
        return score

    def _is_answer_correct(self, index: int, answer: str) -> bool:
        """Check if an answer at a given index is correct"""
        if index >= len(self.questions):
            return False  # pragma: no cover
        return self.questions[index].check_answer(answer)

    # Answer Review

    def get_incorrect_answers(self) -> List[int]:
        """Get a list of indices for incorrectly answered questions"""
        incorrect = []
        for index, answer in self.answers.items():
            if not self._is_answer_correct(index, answer):
                incorrect.append(index)
        return incorrect

    def get_answer_details(self, question_index: int) -> Dict:
        """Get detailed information about a specific answer"""
        question = self.questions[question_index]
        submitted_answer = self.answers.get(question_index)

        return {
            "question": question,
            "submitted_answer": submitted_answer,
            "correct_answer": question.correct_answer,
            "is_correct": question.check_answer(submitted_answer) if submitted_answer else False,
        }

    # Filtering and Categorization

    def get_questions_by_difficulty(self, difficulty: str) -> List[Question]:
        """Get all questions with a specific difficulty level"""
        return [q for q in self.questions if q.difficulty == difficulty]

    def get_questions_by_category(self, category: Optional[str]) -> List[Question]:
        """Get all questions in a specific category"""
        return [q for q in self.questions if q.category == category]

    def get_score_by_category(self, category: Optional[str]) -> Dict[str, float]:
        """Get the score for questions in a specific category"""
        category_indices = self._get_category_question_indices(category)
        score = self._calculate_category_score(category_indices)
        total = len(category_indices)
        percentage = (score / total * 100) if total > 0 else 0.0

        return {"score": score, "total": total, "percentage": percentage}

    def _get_category_question_indices(self, category: Optional[str]) -> List[int]:
        """Get indices of all questions in a category"""
        return [
            index for index, question in enumerate(self.questions) if question.category == category
        ]

    def _calculate_category_score(self, indices: List[int]) -> int:
        """Calculate score for a list of question indices"""
        score = 0
        for index in indices:
            if index in self.answers and self._is_answer_correct(index, self.answers[index]):
                score += 1
        return score

    def __repr__(self) -> str:
        """String representation for debugging"""
        return f"Quiz(title='{self.title}', questions={len(self.questions)})"
