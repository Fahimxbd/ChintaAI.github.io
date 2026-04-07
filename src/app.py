"""
EduMind AI - Flask Backend
Version: 0.1.0-beta
Run locally: python src/app.py
"""

from flask import Flask, request, jsonify, send_from_directory
import os
import sys

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qa_engine import EduMindQA

app = Flask(__name__, static_folder="../", static_url_path="")

# Initialize the Q&A engine
ai = EduMindQA()


@app.route("/")
def index():
    """Serve the main page."""
    return send_from_directory("../", "index.html")


@app.route("/api/ask", methods=["POST"])
def ask():
    """
    API endpoint to ask a question.
    Request body: { "question": "What is photosynthesis?" }
    Response: { "answer": "...", "subject": "Biology", "difficulty": "beginner", "matched": true }
    """
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' in request body"}), 400

    question = data["question"].strip()
    if len(question) > 500:
        return jsonify({"error": "Question too long (max 500 characters)"}), 400

    result = ai.ask(question)
    return jsonify(result)


@app.route("/api/topics", methods=["GET"])
def topics():
    """Return all available topics."""
    return jsonify({"topics": ai.list_topics()})


@app.route("/api/questions", methods=["GET"])
def all_questions():
    """Return all sample questions."""
    return jsonify({"questions": ai.get_all_questions()})


@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "ok",
        "version": "0.1.0-beta",
        "total_questions": len(ai.all_entries)
    })


if __name__ == "__main__":
    print("=" * 50)
    print("  EduMind AI — Beta v0.1.0")
    print("  Running at: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000)
