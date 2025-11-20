from typing import Dict, List
from src.question import Question
from src.result import QuizResult


class Quiz:
    """Represents a quiz with multiple questions"""

    def __init__(self, title: str) -> None:
        self.title = title
        self.questions: List[Question] = []
        self.answers: Dict[int, str] = {}  # Maps question index to submitted answer

    def add_question(self, question: Question) -> None:
        """Add a question to the quiz, avoiding duplicates"""
        if question not in self.questions:
            self.questions.append(question)

    def get_question(self, index: int) -> Question:
        """Get a question by its index"""
        return self.questions[index]

    def submit_answer(self, question_index: int, answer: str) -> None:
        """Submit an answer for a specific question"""
        self.answers[question_index] = answer

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
