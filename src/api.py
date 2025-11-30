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
    docs_url=None,      # disables /docs (Swagger UI)
    redoc_url=None,     # disables /redoc (ReDoc UI)
    openapi_url=None, 
)

# Singleton database instance
db: QuizDatabase = QuizDatabase()


# Pydantic models for request/response validation
class QuestionModel(BaseModel):
    pass


class QuizCreateModel(BaseModel):
    pass


class QuizResponseModel(BaseModel):
    pass


class AnswerSubmissionModel(BaseModel):
    pass


# Helper function to convert Quiz to dict
def quiz_to_dict(quiz: Quiz, quiz_id: Optional[str] = None) -> Dict[str, Any]:
    """Convert Quiz object to dictionary for JSON response"""
    pass


# ============================================================================
# CRUD ENDPOINTS
# ============================================================================


@app.post("/quizzes", response_model=QuizResponseModel, status_code=201)
async def create_quiz(quiz_data: QuizCreateModel) -> QuizResponseModel:
    """
    CREATE - Add a new quiz to the database.

    Returns the created quiz with its generated ID.
    """
    pass


@app.get("/quizzes/{quiz_id}")
async def get_quiz(quiz_id: str) -> Dict[str, Any]:
    """
    READ - Retrieve a specific quiz by ID.

    Returns the complete quiz with all questions.
    """
    pass


@app.get("/quizzes")
async def list_quizzes() -> Dict[str, Any]:
    """
    READ - List all quizzes in the database.

    Returns a list of all quizzes with their IDs and basic information.
    """
    pass


@app.put("/quizzes/{quiz_id}")
async def update_quiz(quiz_id: str, quiz_data: QuizCreateModel) -> Dict[str, Any]:
    """
    UPDATE - Modify an existing quiz.

    Replaces the quiz with the provided data.
    """
    pass


@app.delete("/quizzes/{quiz_id}")
async def delete_quiz(quiz_id: str) -> Dict[str, Any]:
    """
    DELETE - Remove a quiz from the database.

    Returns success message if deleted.
    """
    pass


# ============================================================================
# ADDITIONAL ENDPOINTS
# ============================================================================


@app.post("/quizzes/{quiz_id}/answers")
async def submit_answer(quiz_id: str, submission: AnswerSubmissionModel) -> Dict[str, Any]:
    """
    Submit an answer to a quiz question.

    Updates the quiz with the submitted answer.
    """
    pass


@app.get("/quizzes/{quiz_id}/results")
async def get_quiz_results(quiz_id: str) -> Dict[str, Any]:
    """
    Get the results of a completed quiz.

    Returns score, percentage, and detailed feedback.
    """
    pass


@app.delete("/quizzes")
async def clear_database() -> Dict[str, Any]:
    """
    Clear all quizzes from the database.

    WARNING: This will delete ALL quizzes!
    """
    pass


# ============================================================================
# HEALTH CHECK
# ============================================================================


@app.get("/")
async def root() -> Dict[str, Any]:
    """API health check and information"""
    pass


@app.get("/health")
async def health_check() -> Dict[str, Union[str, int]]:
    """Health check endpoint"""
    pass
