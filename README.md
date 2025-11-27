# Quiz Application

A flexible, feature-rich quiz application built with Python using Test-Driven Development (TDD) methodology.

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)]()

## Features

- ✅**Multiple Choice Questions** - Support for questions with multiple answer options
- ✅**Timed Quizzes** - Optional time limits with automatic tracking
- ✅**Comprehensive Scoring** - Detailed results with percentages and pass/fail thresholds
- ✅**Difficulty Levels** - Categorize questions by difficulty (easy, medium, hard)
- ✅**Categories** - Organize questions by topic or category
- ✅**Answer Review** - Review incorrect answers and get detailed feedback
- ✅**API and Database integration** - Basic API for Web usage and database to save all quizes
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

### REST API Guide

**REST API with FastAPI** (`src/api.py`)

* Full CRUD operations (Create, Read, Update, Delete)
* 10 endpoints ready to use
* Automatic request validation

**Easy Server Startup** (`run_api.py`)

* One command to start: `python run_api.py`

**Interactive API Docs** (Built-in!)

* Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc at [http://localhost:8000/redoc](http://localhost:8000/redoc)
* Test endpoints in browser via Swagger UI!

#### CRUD Operations

<pre class="font-ui border-border-100/50 overflow-x-scroll w-full rounded border-[0.5px] shadow-[0_2px_12px_hsl(var(--always-black)/5%)]"><table class="bg-bg-100 min-w-full border-separate border-spacing-0 text-sm leading-[1.88888] whitespace-normal"><thead class="border-b-border-100/50 border-b-[0.5px] text-left"><tr class="[tbody>&]:odd:bg-bg-500/10"><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] px-2 [&:not(:first-child)]:border-l-[0.5px]">Method</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] px-2 [&:not(:first-child)]:border-l-[0.5px]">Endpoint</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] px-2 [&:not(:first-child)]:border-l-[0.5px]">Description</th></tr></thead><tbody><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>POST</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/quizzes</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>CREATE</strong> - Add new quiz</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>GET</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/quizzes/{quiz_id}</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>READ</strong> - Get specific quiz</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>GET</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/quizzes</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>READ</strong> - List all quizzes</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>PUT</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/quizzes/{quiz_id}</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>UPDATE</strong> - Modify quiz</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>DELETE</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/quizzes/{quiz_id}</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>DELETE</strong> - Remove quiz</td></tr></tbody></table></pre>

#### Additional Endpoints

<pre class="font-ui border-border-100/50 overflow-x-scroll w-full rounded border-[0.5px] shadow-[0_2px_12px_hsl(var(--always-black)/5%)]"><table class="bg-bg-100 min-w-full border-separate border-spacing-0 text-sm leading-[1.88888] whitespace-normal"><thead class="border-b-border-100/50 border-b-[0.5px] text-left"><tr class="[tbody>&]:odd:bg-bg-500/10"><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] px-2 [&:not(:first-child)]:border-l-[0.5px]">Method</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] px-2 [&:not(:first-child)]:border-l-[0.5px]">Endpoint</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] px-2 [&:not(:first-child)]:border-l-[0.5px]">Description</th></tr></thead><tbody><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">POST</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/quizzes/{quiz_id}/answers</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Submit answer to question</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">GET</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/quizzes/{quiz_id}/results</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Get quiz results</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">DELETE</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/quizzes</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Clear all quizzes</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">GET</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">API info</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">GET</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">/health</code></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Health check</td></tr></tbody></table></pre>

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_quiz.py
```

### Running API Server

````bash
# Option A - Simple:
python run_api.py

# Option B - With uvicorn directly:
uvicorn quiz.api:app --reload --host 0.0.0.0 --port 8000

# Option C - With custom settings:
python run_api.py --host 0.0.0.0 --port 8080 --reload
````

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
