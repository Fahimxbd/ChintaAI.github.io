"""
EduMind AI - Unit Tests
Run: python -m pytest tests/ -v
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from qa_engine import EduMindQA


class TestEduMindQA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize the AI engine once for all tests."""
        cls.ai = EduMindQA()

    def test_photosynthesis_question(self):
        """Should correctly answer photosynthesis question."""
        result = self.ai.ask("What is photosynthesis?")
        self.assertTrue(result["matched"])
        self.assertIn("chlorophyll", result["answer"].lower())
        self.assertEqual(result["subject"], "Biology")

    def test_newton_second_law(self):
        """Should correctly answer Newton's second law question."""
        result = self.ai.ask("Explain Newton's second law of motion")
        self.assertTrue(result["matched"])
        self.assertIn("F = ma", result["answer"])

    def test_pythagorean_theorem(self):
        """Should correctly answer Pythagorean theorem question."""
        result = self.ai.ask("What is the Pythagorean theorem?")
        self.assertTrue(result["matched"])
        self.assertIn("a² + b² = c²", result["answer"])

    def test_machine_learning(self):
        """Should correctly answer machine learning question."""
        result = self.ai.ask("What is machine learning?")
        self.assertTrue(result["matched"])
        self.assertEqual(result["subject"], "Computer Science")

    def test_unknown_question_returns_fallback(self):
        """Unknown questions should return matched=False."""
        result = self.ai.ask("What is the meaning of life in quantum foam?")
        self.assertFalse(result["matched"])
        self.assertIsInstance(result["answer"], str)

    def test_empty_question(self):
        """Empty question should return appropriate message."""
        result = self.ai.ask("")
        self.assertFalse(result["matched"])

    def test_list_topics_returns_list(self):
        """Should return a non-empty list of topics."""
        topics = self.ai.list_topics()
        self.assertIsInstance(topics, list)
        self.assertGreater(len(topics), 0)

    def test_get_all_questions(self):
        """Should return all available questions."""
        questions = self.ai.get_all_questions()
        self.assertIsInstance(questions, list)
        self.assertGreater(len(questions), 5)

    def test_confidence_is_float(self):
        """Confidence score should be a float between 0 and 1."""
        result = self.ai.ask("What is DNA?")
        self.assertIsInstance(result["confidence"], float)
        self.assertGreaterEqual(result["confidence"], 0.0)
        self.assertLessEqual(result["confidence"], 1.0)

    def test_climate_change_question(self):
        """Should correctly answer climate change question."""
        result = self.ai.ask("What causes climate change?")
        self.assertTrue(result["matched"])
        self.assertIn("greenhouse", result["answer"].lower())


if __name__ == "__main__":
    print("Running EduMind AI Tests...\n")
    unittest.main(verbosity=2)
