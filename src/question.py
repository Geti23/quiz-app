class Question:
    """Represents a single quiz question with multiple choice options"""

    def __init__(self, text, options, correct_answer):
        pass

    def check_answer(self, answer):
        """Check if the provided answer is correct"""
        pass

    def __eq__(self, other):
        """Check equality based on question text and options"""
        pass

    def __hash__(self):
        """Make Question hashable for use in sets"""
        pass  # pragma: no cover
