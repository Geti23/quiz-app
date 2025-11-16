# Quiz Application

A flexible, feature-rich quiz application built with Python using Test-Driven Development (TDD) methodology.

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-failing-red.svg)]()

## Features

- **Multiple Choice Questions** - Support for questions with multiple answer options
- **Timed Quizzes** - Optional time limits with automatic tracking
- **Comprehensive Scoring** - Detailed results with percentages and pass/fail thresholds
- **Difficulty Levels** - Categorize questions by difficulty (easy, medium, hard)
- **Categories** - Organize questions by topic or category
- **Answer Review** - Review incorrect answers and get detailed feedback
- **Test-Driven** - Built with TDD principles for reliability and maintainability

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

Code to be implemented...
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

Code and Tests to be implemented...

### Questions with Difficulty and Category

Code and Tests to be implemented

### Review Incorrect Answers

Code and Tests to be implemented

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
