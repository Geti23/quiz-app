from typing import Dict, List, Optional
from src.question import Question
from src.result import QuizResult
import time


class Quiz:
    """Represents a quiz with multiple questions"""

    def __init__(self, title: str, time_limit_seconds: Optional[int] = None) -> None:
        self.title = title
        self.questions: List[Question] = []
        self.answers: Dict[int, str] = {}  # Maps question index to submitted answer
        self.time_limit_seconds = time_limit_seconds
        self.start_time: Optional[float] = None

    def add_question(self, question: Question) -> None:
        """Add a question to the quiz, avoiding duplicates"""
        if question not in self.questions:
            self.questions.append(question)

    def get_question(self, index: int) -> Question:
        """Get a question by its index"""
        return self.questions[index]

    def submit_answer(self, question_index: int, answer: str) -> None:
        """Submit an answer for a specific question"""
        # Start timer on first answer submission
        if self.start_time is None:
            self.start_time = time.time()

        self.answers[question_index] = answer

    def get_elapsed_time(self) -> float:
        """Get the elapsed time since the quiz started"""
        if self.start_time is None:
            return 0
        return time.time() - self.start_time

    def is_time_expired(self) -> bool:
        """Check if the time limit has been exceeded"""
        if self.time_limit_seconds is None:
            return False
        return self.get_elapsed_time() > self.time_limit_seconds

    def get_result(self) -> QuizResult:
        """Calculate and return the quiz result"""
        score = 0
        total = len(self.questions)

        for index, answer in self.answers.items():
            if index < len(self.questions):
                question = self.questions[index]
                if question.check_answer(answer):
                    score += 1

        return QuizResult(score, total)

    def get_questions_by_difficulty(self, difficulty: str) -> List[Question]:
        """Get all questions with a specific difficulty level"""
        return [q for q in self.questions if q.difficulty == difficulty]

    def get_questions_by_category(self, category: Optional[str]) -> List[Question]:
        """Get all questions in a specific category"""
        return [q for q in self.questions if q.category == category]

    def get_incorrect_answers(self) -> List[int]:
        """Get a list of indices for incorrectly answered questions"""
        incorrect = []
        for index, answer in self.answers.items():
            if index < len(self.questions):
                question = self.questions[index]
                if not question.check_answer(answer):
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

    def get_score_by_category(self, category: Optional[str]) -> Dict[str, float]:
        """Get the score for questions in a specific category"""
        category_questions = []
        score = 0

        for index, question in enumerate(self.questions):
            if question.category == category:
                category_questions.append(index)
                if index in self.answers and question.check_answer(self.answers[index]):
                    score += 1

        total = len(category_questions)
        percentage = (score / total * 100) if total > 0 else 0.0

        return {"score": score, "total": total, "percentage": percentage}
