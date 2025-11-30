"""
API Endpoint Tests - Status Code Verification

Tests that verify all API endpoints return the correct HTTP status codes.
These are End-to-End tests that test the REST API through HTTP.
"""

import pytest
from fastapi.testclient import TestClient
from src.api import app, db


@pytest.fixture(autouse=True)
def clear_database():
    """Clear database before each test to ensure clean state"""
    db.clear()
    yield
    db.clear()


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def sample_quiz_data():
    """Sample quiz data for testing"""
    return {
        "title": "Test Quiz",
        "time_limit_seconds": 600,
        "questions": [
            {
                "text": "What is 2+2?",
                "options": ["3", "4", "5", "6"],
                "correct_answer": "4",
                "difficulty": "easy",
                "category": "Math"
            }
        ]
    }


class TestHealthEndpoints:
    """Tests for health check and info endpoints"""
    
    def test_root_endpoint_returns_ok(self, client):
        """Test GET / returns 200 OK"""
        response = client.get("/")
        assert response.status_code == 200
    
    def test_health_endpoint_returns_ok(self, client):
        """Test GET /health returns 200 OK"""
        response = client.get("/health")
        assert response.status_code == 200


class TestCreateQuizEndpoint:
    """Tests for POST /quizzes (CREATE operation)"""
    
    def test_create_quiz_returns_created(self, client, sample_quiz_data):
        """Test POST /quizzes returns 201 Created"""
        response = client.post("/quizzes", json=sample_quiz_data)
        assert response.status_code == 201
    
    def test_create_quiz_with_minimal_data_returns_created(self, client):
        """Test POST /quizzes with minimal data returns 201"""
        minimal_quiz = {
            "title": "Minimal Quiz",
            "questions": []
        }
        response = client.post("/quizzes", json=minimal_quiz)
        assert response.status_code == 201
    
    def test_create_quiz_with_invalid_data_returns_error(self, client):
        """Test POST /quizzes with invalid data returns 422"""
        invalid_quiz = {
            "title": "",  # Empty title should fail validation
            "questions": []
        }
        response = client.post("/quizzes", json=invalid_quiz)
        assert response.status_code == 422


class TestReadQuizEndpoints:
    """Tests for GET endpoints (READ operations)"""
    
    def test_get_quiz_returns_ok(self, client, sample_quiz_data):
        """Test GET /quizzes/{quiz_id} returns 200 OK"""
        # First create a quiz
        create_response = client.post("/quizzes", json=sample_quiz_data)
        quiz_id = create_response.json()["quiz_id"]
        
        # Then get it
        response = client.get(f"/quizzes/{quiz_id}")
        assert response.status_code == 200
    
    def test_get_nonexistent_quiz_returns_not_found(self, client):
        """Test GET /quizzes/{invalid_id} returns 404 Not Found"""
        response = client.get("/quizzes/nonexistent-id-123")
        assert response.status_code == 404
    
    def test_list_quizzes_returns_ok(self, client):
        """Test GET /quizzes returns 200 OK"""
        response = client.get("/quizzes")
        assert response.status_code == 200
    
    def test_list_quizzes_when_empty_returns_ok(self, client):
        """Test GET /quizzes returns 200 OK even when database is empty"""
        db.clear()
        response = client.get("/quizzes")
        assert response.status_code == 200


class TestUpdateQuizEndpoint:
    """Tests for PUT /quizzes/{quiz_id} (UPDATE operation)"""
    
    def test_update_quiz_returns_ok(self, client, sample_quiz_data):
        """Test PUT /quizzes/{quiz_id} returns 200 OK"""
        # Create a quiz first
        create_response = client.post("/quizzes", json=sample_quiz_data)
        quiz_id = create_response.json()["quiz_id"]
        
        # Update it
        updated_data = {
            "title": "Updated Quiz",
            "time_limit_seconds": 900,
            "questions": sample_quiz_data["questions"]
        }
        response = client.put(f"/quizzes/{quiz_id}", json=updated_data)
        assert response.status_code == 200
    
    def test_update_nonexistent_quiz_returns_not_found(self, client, sample_quiz_data):
        """Test PUT /quizzes/{invalid_id} returns 404 Not Found"""
        response = client.put("/quizzes/nonexistent-id-123", json=sample_quiz_data)
        assert response.status_code == 404
    
    def test_update_quiz_with_invalid_data_returns_error(self, client, sample_quiz_data):
        """Test PUT /quizzes/{quiz_id} with invalid data returns 422"""
        # Create a quiz first
        create_response = client.post("/quizzes", json=sample_quiz_data)
        quiz_id = create_response.json()["quiz_id"]
        
        # Try to update with invalid data
        invalid_data = {
            "title": "",  # Empty title should fail
            "questions": []
        }
        response = client.put(f"/quizzes/{quiz_id}", json=invalid_data)
        assert response.status_code == 422


class TestDeleteQuizEndpoint:
    """Tests for DELETE /quizzes/{quiz_id} (DELETE operation)"""
    
    def test_delete_quiz_returns_ok(self, client, sample_quiz_data):
        """Test DELETE /quizzes/{quiz_id} returns 200 OK"""
        # Create a quiz first
        create_response = client.post("/quizzes", json=sample_quiz_data)
        quiz_id = create_response.json()["quiz_id"]
        
        # Delete it
        response = client.delete(f"/quizzes/{quiz_id}")
        assert response.status_code == 200
    
    def test_delete_nonexistent_quiz_returns_not_found(self, client):
        """Test DELETE /quizzes/{invalid_id} returns 404 Not Found"""
        response = client.delete("/quizzes/nonexistent-id-123")
        assert response.status_code == 404
    
    def test_clear_all_quizzes_returns_ok(self, client):
        """Test DELETE /quizzes returns 200 OK"""
        response = client.delete("/quizzes")
        assert response.status_code == 200


class TestAnswerSubmissionEndpoint:
    """Tests for POST /quizzes/{quiz_id}/answers"""
    
    def test_submit_answer_returns_ok(self, client, sample_quiz_data):
        """Test POST /quizzes/{quiz_id}/answers returns 200 OK"""
        # Create a quiz
        create_response = client.post("/quizzes", json=sample_quiz_data)
        quiz_id = create_response.json()["quiz_id"]
        
        # Submit an answer
        answer_data = {
            "question_index": 0,
            "answer": "4"
        }
        response = client.post(f"/quizzes/{quiz_id}/answers", json=answer_data)
        assert response.status_code == 200
    
    def test_submit_answer_to_nonexistent_quiz_returns_not_found(self, client):
        """Test POST /quizzes/{invalid_id}/answers returns 404"""
        answer_data = {
            "question_index": 0,
            "answer": "4"
        }
        response = client.post("/quizzes/nonexistent-id/answers", json=answer_data)
        assert response.status_code == 404
    
    def test_submit_answer_with_invalid_index_returns_bad_request(self, client, sample_quiz_data):
        """Test POST /quizzes/{quiz_id}/answers with invalid index returns 400"""
        # Create a quiz with 1 question
        create_response = client.post("/quizzes", json=sample_quiz_data)
        quiz_id = create_response.json()["quiz_id"]
        
        # Try to answer question at invalid index
        answer_data = {
            "question_index": 999,  # Invalid index
            "answer": "4"
        }
        response = client.post(f"/quizzes/{quiz_id}/answers", json=answer_data)
        assert response.status_code == 400


class TestResultsEndpoint:
    """Tests for GET /quizzes/{quiz_id}/results"""
    
    def test_get_results_returns_ok(self, client, sample_quiz_data):
        """Test GET /quizzes/{quiz_id}/results returns 200 OK"""
        # Create a quiz
        create_response = client.post("/quizzes", json=sample_quiz_data)
        quiz_id = create_response.json()["quiz_id"]
        
        # Get results (even without answers)
        response = client.get(f"/quizzes/{quiz_id}/results")
        assert response.status_code == 200
    
    def test_get_results_for_nonexistent_quiz_returns_not_found(self, client):
        """Test GET /quizzes/{invalid_id}/results returns 404"""
        response = client.get("/quizzes/nonexistent-id/results")
        assert response.status_code == 404


class TestAPIDocumentationEndpoints:
    """Tests for auto-generated API documentation"""
    
    def test_swagger_docs_returns_ok(self, client):
        """Test GET /docs returns 200 OK"""
        response = client.get("/docs")
        assert response.status_code == 200
    
    def test_redoc_docs_returns_ok(self, client):
        """Test GET /redoc returns 200 OK"""
        response = client.get("/redoc")
        assert response.status_code == 200
    
    def test_openapi_json_returns_ok(self, client):
        """Test GET /openapi.json returns 200 OK"""
        response = client.get("/openapi.json")
        assert response.status_code == 200


class TestCRUDWorkflow:
    """End-to-End test for complete CRUD workflow"""
    
    def test_complete_crud_workflow_returns_ok(self, client, sample_quiz_data):
        """Test complete CREATE -> READ -> UPDATE -> DELETE workflow"""
        
        # CREATE - Should return 201
        create_response = client.post("/quizzes", json=sample_quiz_data)
        assert create_response.status_code == 201
        quiz_id = create_response.json()["quiz_id"]
        
        # READ - Should return 200
        read_response = client.get(f"/quizzes/{quiz_id}")
        assert read_response.status_code == 200
        
        # UPDATE - Should return 200
        updated_data = {
            "title": "Updated Title",
            "time_limit_seconds": 900,
            "questions": sample_quiz_data["questions"]
        }
        update_response = client.put(f"/quizzes/{quiz_id}", json=updated_data)
        assert update_response.status_code == 200
        
        # DELETE - Should return 200
        delete_response = client.delete(f"/quizzes/{quiz_id}")
        assert delete_response.status_code == 200
        
        # Verify deletion - Should return 404
        verify_response = client.get(f"/quizzes/{quiz_id}")
        assert verify_response.status_code == 404


class TestQuizCompletionWorkflow:
    """End-to-End test for quiz taking workflow"""
    
    def test_complete_quiz_taking_workflow_returns_ok(self, client):
        """Test CREATE quiz -> SUBMIT answers -> GET results workflow"""
        
        # CREATE quiz with multiple questions
        quiz_data = {
            "title": "Math Quiz",
            "time_limit_seconds": 600,
            "questions": [
                {
                    "text": "What is 2+2?",
                    "options": ["3", "4", "5"],
                    "correct_answer": "4"
                },
                {
                    "text": "What is 3+3?",
                    "options": ["5", "6", "7"],
                    "correct_answer": "6"
                }
            ]
        }
        create_response = client.post("/quizzes", json=quiz_data)
        assert create_response.status_code == 201
        quiz_id = create_response.json()["quiz_id"]
        
        # SUBMIT answers
        answer1_response = client.post(
            f"/quizzes/{quiz_id}/answers",
            json={"question_index": 0, "answer": "4"}
        )
        assert answer1_response.status_code == 200
        
        answer2_response = client.post(
            f"/quizzes/{quiz_id}/answers",
            json={"question_index": 1, "answer": "6"}
        )
        assert answer2_response.status_code == 200
        
        # GET results
        results_response = client.get(f"/quizzes/{quiz_id}/results")
        assert results_response.status_code == 200