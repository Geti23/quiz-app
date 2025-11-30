"""
REST API for Quiz Application using FastAPI.

This module provides HTTP endpoints for CRUD operations on quizzes.
Run with: uvicorn src.api:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict, Any, Union
from src.quiz import Quiz
from src.question import Question
from src.database import QuizDatabase

# Initialize FastAPI app and database
app = FastAPI(
    title="Quiz API",
    description="REST API for managing quizzes with CRUD operations",
    version="1.0.0",
)

# Singleton database instance
db: QuizDatabase = QuizDatabase()


# Pydantic models for request/response validation
class QuestionModel(BaseModel):
    text: str = Field(..., min_length=1, description="Question text")
    options: List[str] = Field(..., description="Answer options")
    correct_answer: str = Field(..., description="Correct answer")
    difficulty: str = Field(default="medium", description="Difficulty level")
    category: Optional[str] = Field(None, description="Question category")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "text": "What is Python?",
                "options": ["Language", "Snake", "Framework", "Database"],
                "correct_answer": "Language",
                "difficulty": "easy",
                "category": "Programming",
            }
        }
    )


class QuizCreateModel(BaseModel):
    title: str = Field(..., min_length=1, description="Quiz title")
    time_limit_seconds: Optional[int] = Field(None, description="Time limit in seconds")
    questions: List[QuestionModel] = Field(default=[], description="List of questions")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Python Basics Quiz",
                "time_limit_seconds": 600,
                "questions": [
                    {
                        "text": "What is a list?",
                        "options": ["Array", "Collection", "Dictionary"],
                        "correct_answer": "Collection",
                        "difficulty": "easy",
                        "category": "Data Types",
                    }
                ],
            }
        }
    )


class QuizResponseModel(BaseModel):
    quiz_id: str
    title: str
    time_limit_seconds: Optional[int]
    question_count: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "quiz_id": "123e4567-e89b-12d3-a456-426614174000",
                "title": "Python Basics Quiz",
                "time_limit_seconds": 600,
                "question_count": 5,
            }
        }
    )


class AnswerSubmissionModel(BaseModel):
    question_index: int = Field(..., ge=0, description="Question index (0-based)")
    answer: str = Field(..., description="Submitted answer")

    model_config = ConfigDict(
        json_schema_extra={"example": {"question_index": 0, "answer": "Collection"}}
    )


# Helper function to convert Quiz to dict
def quiz_to_dict(quiz: Quiz, quiz_id: Optional[str] = None) -> Dict[str, Any]:
    """Convert Quiz object to dictionary for JSON response"""
    return {
        "quiz_id": quiz_id,
        "title": quiz.title,
        "time_limit_seconds": quiz.time_limit_seconds,
        "question_count": len(quiz.questions),
        "questions": [
            {
                "text": q.text,
                "options": q.options,
                "correct_answer": q.correct_answer,
                "difficulty": q.difficulty,
                "category": q.category,
            }
            for q in quiz.questions
        ],
    }


# ============================================================================
# CRUD ENDPOINTS
# ============================================================================


@app.post("/quizzes", response_model=QuizResponseModel, status_code=201)
async def create_quiz(quiz_data: QuizCreateModel) -> QuizResponseModel:
    """
    CREATE - Add a new quiz to the database.

    Returns the created quiz with its generated ID.
    """
    # Create Quiz object
    quiz = Quiz(title=quiz_data.title, time_limit_seconds=quiz_data.time_limit_seconds)

    # Add questions
    for q_data in quiz_data.questions:
        question = Question(
            text=q_data.text,
            options=q_data.options,
            correct_answer=q_data.correct_answer,
            difficulty=q_data.difficulty,
            category=q_data.category,
        )
        quiz.add_question(question)

    # Store in database
    quiz_id = db.add_quiz(quiz)

    return QuizResponseModel(
        quiz_id=quiz_id,
        title=quiz.title,
        time_limit_seconds=quiz.time_limit_seconds,
        question_count=len(quiz.questions),
    )


@app.get("/quizzes/{quiz_id}")
async def get_quiz(quiz_id: str) -> Dict[str, Any]:
    """
    READ - Retrieve a specific quiz by ID.

    Returns the complete quiz with all questions.
    """
    quiz = db.get_quiz(quiz_id)

    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return quiz_to_dict(quiz, quiz_id)


@app.get("/quizzes")
async def list_quizzes() -> Dict[str, Any]:
    """
    READ - List all quizzes in the database.

    Returns a list of all quizzes with their IDs and basic information.
    """
    quizzes = db.list_quizzes()

    # Note: We can't get the quiz_id from Quiz object, so we return without IDs
    # In a real app, you'd store the ID in the Quiz object or maintain a reverse mapping
    return {
        "total": len(quizzes),
        "quizzes": [
            {
                "quiz_id": q.id,
                "title": q.title,
                "time_limit_seconds": q.time_limit_seconds,
                "question_count": len(q.questions),
            }
            for q in quizzes
        ],
    }


@app.put("/quizzes/{quiz_id}")
async def update_quiz(quiz_id: str, quiz_data: QuizCreateModel) -> Dict[str, Any]:
    """
    UPDATE - Modify an existing quiz.

    Replaces the quiz with the provided data.
    """
    # Check if quiz exists
    existing_quiz = db.get_quiz(quiz_id)
    if existing_quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")

    # Create updated Quiz object
    updated_quiz = Quiz(title=quiz_data.title, time_limit_seconds=quiz_data.time_limit_seconds)

    # Add questions
    for q_data in quiz_data.questions:
        question = Question(
            text=q_data.text,
            options=q_data.options,
            correct_answer=q_data.correct_answer,
            difficulty=q_data.difficulty,
            category=q_data.category,
        )
        updated_quiz.add_question(question)

    # Update in database
    success = db.update_quiz(quiz_id, updated_quiz)

    if not success:
        raise HTTPException(status_code=500, detail="Failed to update quiz")  # pragma: no cover

    return {
        "message": "Quiz updated successfully",
        "quiz_id": quiz_id,
        "title": updated_quiz.title,
        "question_count": len(updated_quiz.questions),
    }


@app.delete("/quizzes/{quiz_id}")
async def delete_quiz(quiz_id: str) -> Dict[str, Any]:
    """
    DELETE - Remove a quiz from the database.

    Returns success message if deleted.
    """
    success = db.delete_quiz(quiz_id)

    if not success:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return {"message": "Quiz deleted successfully", "quiz_id": quiz_id}


# ============================================================================
# ADDITIONAL ENDPOINTS
# ============================================================================


@app.post("/quizzes/{quiz_id}/answers")
async def submit_answer(quiz_id: str, submission: AnswerSubmissionModel) -> Dict[str, Any]:
    """
    Submit an answer to a quiz question.

    Updates the quiz with the submitted answer.
    """
    quiz = db.get_quiz(quiz_id)

    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")

    if submission.question_index >= len(quiz.questions):
        raise HTTPException(status_code=400, detail="Invalid question index")

    # Submit answer
    quiz.submit_answer(submission.question_index, submission.answer)

    # Update quiz in database
    db.update_quiz(quiz_id, quiz)

    # Check if answer is correct
    question = quiz.questions[submission.question_index]
    is_correct = question.check_answer(submission.answer)

    return {
        "message": "Answer submitted",
        "question_index": submission.question_index,
        "submitted_answer": submission.answer,
        "is_correct": is_correct,
    }


@app.get("/quizzes/{quiz_id}/results")
async def get_quiz_results(quiz_id: str) -> Dict[str, Any]:
    """
    Get the results of a completed quiz.

    Returns score, percentage, and detailed feedback.
    """
    quiz = db.get_quiz(quiz_id)

    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")

    result = quiz.get_result()
    incorrect = quiz.get_incorrect_answers()

    return {
        "quiz_id": quiz_id,
        "title": quiz.title,
        "score": result.score,
        "total": result.total,
        "percentage": result.percentage,
        "is_perfect": result.is_perfect(),
        "is_passing": result.is_passing(),
        "summary": result.get_summary(),
        "incorrect_question_indices": incorrect,
    }


@app.delete("/quizzes")
async def clear_database() -> Dict[str, Any]:
    """
    Clear all quizzes from the database.

    WARNING: This will delete ALL quizzes!
    """
    db.clear()
    return {"message": "All quizzes deleted", "remaining_quizzes": len(db)}


# ============================================================================
# HEALTH CHECK
# ============================================================================


@app.get("/")
async def root() -> Dict[str, Any]:
    """API health check and information"""
    return {
        "message": "Quiz API is running",
        "version": "1.0.0",
        "total_quizzes": len(db),
        "documentation": "/docs",
    }


@app.get("/health")
async def health_check() -> Dict[str, Union[str, int]]:
    """Health check endpoint"""
    return {"status": "healthy", "database_size": len(db)}
