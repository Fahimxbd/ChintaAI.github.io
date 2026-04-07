"""
EduMind AI - Core Q&A Engine
Version: 0.1.0-beta
Description: Keyword-based question answering engine for educational queries.
"""

import json
import os
import re
from typing import Optional


class EduMindQA:
    """
    EduMind AI Question-Answer Engine.
    Uses keyword matching against a curated knowledge base.
    Future versions will use NLP / transformer-based matching.
    """

    def __init__(self, knowledge_base_path: str = None):
        if knowledge_base_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            knowledge_base_path = os.path.join(base_dir, "..", "data", "knowledge_base.json")

        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
        self.all_entries = self._flatten_entries()

    def _load_knowledge_base(self, path: str) -> dict:
        """Load the JSON knowledge base."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base not found at: {path}")
        except json.JSONDecodeError:
            raise ValueError("Knowledge base JSON is malformed.")

    def _flatten_entries(self) -> list:
        """Flatten all subjects into a single searchable list."""
        entries = []
        for subject, questions in self.knowledge_base.get("subjects", {}).items():
            for q in questions:
                q["_subject_key"] = subject
                entries.append(q)
        return entries

    def _normalize(self, text: str) -> str:
        """Lowercase and remove punctuation for matching."""
        return re.sub(r"[^\w\s]", "", text.lower().strip())

    def _score_entry(self, query: str, entry: dict) -> int:
        """
        Score a knowledge base entry based on keyword match.
        Returns a score: higher = better match.
        """
        query_norm = self._normalize(query)
        score = 0

        # Check keywords
        for keyword in entry.get("keywords", []):
            if keyword.lower() in query_norm:
                score += 3  # Strong match on keyword

        # Check if words from question appear in query
        question_words = self._normalize(entry.get("question", "")).split()
        query_words = query_norm.split()
        overlap = set(question_words) & set(query_words)
        score += len(overlap)

        return score

    def ask(self, question: str) -> dict:
        """
        Main method to answer a question.

        Args:
            question (str): The student's question.

        Returns:
            dict: {
                'answer': str,
                'subject': str,
                'difficulty': str,
                'matched': bool,
                'confidence': float
            }
        """
        if not question or not question.strip():
            return {
                "answer": "Please enter a valid question.",
                "subject": "N/A",
                "difficulty": "N/A",
                "matched": False,
                "confidence": 0.0
            }

        # Score all entries
        scored = [(entry, self._score_entry(question, entry)) for entry in self.all_entries]
        scored.sort(key=lambda x: x[1], reverse=True)

        best_entry, best_score = scored[0]

        # Threshold: score must be at least 3 to count as a match
        if best_score >= 3:
            max_possible = len(best_entry.get("keywords", [])) * 3 + 10
            confidence = min(round(best_score / max_possible, 2), 1.0)
            return {
                "answer": best_entry["answer"],
                "subject": best_entry.get("subject", "General"),
                "difficulty": best_entry.get("difficulty", "unknown"),
                "matched": True,
                "confidence": confidence
            }
        else:
            # Return a fallback response
            import random
            fallbacks = self.knowledge_base.get("fallback_responses", ["I don't know."])
            return {
                "answer": random.choice(fallbacks),
                "subject": "Unknown",
                "difficulty": "N/A",
                "matched": False,
                "confidence": 0.0
            }

    def list_topics(self) -> list:
        """Return all available topics/subjects."""
        return list(self.knowledge_base.get("subjects", {}).keys())

    def get_all_questions(self) -> list:
        """Return all available questions (for demo/UI hints)."""
        return [entry["question"] for entry in self.all_entries]


if __name__ == "__main__":
    # Quick test
    ai = EduMindQA()
    test_questions = [
        "What is photosynthesis?",
        "Explain Newton's second law",
        "What is machine learning?",
        "What causes climate change?",
        "Tell me about quantum physics"  # Should trigger fallback
    ]
    for q in test_questions:
        result = ai.ask(q)
        print(f"\nQ: {q}")
        print(f"Subject: {result['subject']} | Matched: {result['matched']} | Confidence: {result['confidence']}")
        print(f"A: {result['answer'][:100]}...")
