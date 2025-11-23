# Quiz Application

A flexible, feature-rich quiz application built with Python using Test-Driven Development (TDD) methodology.

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

## Features

- ✅**Multiple Choice Questions** - Support for questions with multiple answer options
- ✅**Timed Quizzes** - Optional time limits with automatic tracking
- ✅**Comprehensive Scoring** - Detailed results with percentages and pass/fail thresholds
- ✅**Difficulty Levels** - Categorize questions by difficulty (easy, medium, hard)
- ✅**Categories** - Organize questions by topic or category
- ✅**Answer Review** - Review incorrect answers and get detailed feedback
- 🔜**API and Database integration** - Basic API for Web usage and database to save all quizes
- ✅**Test-Driven** - Built with TDD principles for reliability and maintainability

## Installation

### Using pip

```bash
pip install -e .
```

### With development dependencies

```bash
pip install -e ".[dev]"
```

### From requirements.txt

```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from quiz import Quiz, Question

# Create a quiz
quiz = Quiz(title="Python Basics")

# Add questions
quiz.add_question(Question(
    text="What is a list in Python?",
    options=["Array", "Collection", "Dictionary", "Function"],
    correct_answer="Collection"
))

quiz.add_question(Question(
    text="What does 'len()' do?",
    options=["Returns length", "Creates list", "Deletes item", "Sorts data"],
    correct_answer="Returns length"
))

# Submit answers
quiz.submit_answer(0, "Collection")
quiz.submit_answer(1, "Returns length")

# Get results
result = quiz.get_result()
print(result.get_summary())  # Output: Score: 2/2 (100.0%)
print(f"Perfect score: {result.is_perfect()}")  # Output: Perfect score: True
```

### Timed Quiz

````python
from quiz import Quiz, Question

# Create a quiz with 5-minute time limit
quiz = Quiz(title="Timed Challenge", time_limit_seconds=300)

quiz.add_question(Question(
    text="What is 2 + 2?",
    options=["3", "4", "5", "6"],
    correct_answer="4"
))

# Submit answer (timer starts automatically)
quiz.submit_answer(0, "4")

# Check time
print(f"Elapsed time: {quiz.get_elapsed_time():.2f} seconds")
print(f"Time expired: {quiz.is_time_expired()}")
````

### Questions with Difficulty and Category

````python

from quiz import Quiz, Question

quiz = Quiz(title="Science Quiz")

# Add questions with metadata
quiz.add_question(Question(
    text="What is H2O?",
    options=["Water", "Hydrogen", "Oxygen", "Salt"],
    correct_answer="Water",
    difficulty="easy",
    category="Chemistry"
))

quiz.add_question(Question(
    text="What is the speed of light?",
    options=["299,792 km/s", "150,000 km/s", "500,000 km/s", "1,000,000 km/s"],
    correct_answer="299,792 km/s",
    difficulty="hard",
    category="Physics"
))

# Filter questions
easy_questions = quiz.get_questions_by_difficulty("easy")
chemistry_questions = quiz.get_questions_by_category("Chemistry")

# Get category-specific scores
quiz.submit_answer(0, "Water")
quiz.submit_answer(1, "150,000 km/s")

chemistry_score = quiz.get_score_by_category("Chemistry")
print(chemistry_score)  # {'score': 1, 'total': 1, 'percentage': 100.0}
````

### Review Incorrect Answers

````python
from quiz import Quiz, Question

quiz = Quiz(title="Review Example")

quiz.add_question(Question("Q1?", ["A", "B"], "A"))
quiz.add_question(Question("Q2?", ["C", "D"], "C"))

quiz.submit_answer(0, "A")  # Correct
quiz.submit_answer(1, "D")  # Incorrect

# Get incorrect answer indices
incorrect = quiz.get_incorrect_answers()
print(incorrect)  # [1]

# Get detailed answer information
details = quiz.get_answer_details(1)
print(f"Your answer: {details['submitted_answer']}")
print(f"Correct answer: {details['correct_answer']}")
print(f"Was correct: {details['is_correct']}")
````

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=quiz

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_quiz.py
```

### Code Formatting

```bash
# Format code with black
black src/ tests/

# Check code style with flake8
flake8 src/ tests/

# Type checking with mypy
mypy src/
```

### Test Coverage

Please find the coverage report in the htmlcov/index.html file

## Acknowledgments

- Built with Test-Driven Development (TDD) principles
- Developed with Python 3.9+ compatibility
- Tested with pytest framework
