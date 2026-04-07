"""
EduMind AI - Command Line Interface
Usage: python src/cli.py
       python src/cli.py --question "What is photosynthesis?"
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qa_engine import EduMindQA


def print_banner():
    print("\n" + "=" * 60)
    print("    🎓  EduMind AI — Education Assistant (Beta v0.1.0)")
    print("=" * 60)
    print("    Type your question and press Enter.")
    print("    Commands: 'topics' | 'examples' | 'exit'")
    print("=" * 60 + "\n")


def format_answer(result: dict) -> str:
    lines = [
        f"📚 Subject: {result['subject']}",
        f"📊 Difficulty: {result['difficulty'].capitalize()}",
        f"✅ Match: {'Found' if result['matched'] else 'Not Found'}",
        f"🎯 Confidence: {int(result['confidence'] * 100)}%",
        "",
        f"💬 Answer:",
        "-" * 50,
        result["answer"],
        "-" * 50,
    ]
    return "\n".join(lines)


def interactive_mode(ai: EduMindQA):
    print_banner()
    while True:
        try:
            user_input = input("🤖 You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye! Keep learning! 🎓")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "q"):
            print("\nGoodbye! Keep learning! 🎓\n")
            break
        elif user_input.lower() == "topics":
            print(f"\n📂 Available subjects: {', '.join(ai.list_topics())}\n")
        elif user_input.lower() == "examples":
            print("\n📋 Sample questions:")
            for i, q in enumerate(ai.get_all_questions(), 1):
                print(f"  {i}. {q}")
            print()
        else:
            result = ai.ask(user_input)
            print("\n" + format_answer(result) + "\n")


def single_question_mode(ai: EduMindQA, question: str):
    result = ai.ask(question)
    print(format_answer(result))


def main():
    parser = argparse.ArgumentParser(
        description="EduMind AI — Intelligent Education Assistant"
    )
    parser.add_argument(
        "--question", "-q",
        type=str,
        help="Ask a single question and exit",
        default=None
    )
    args = parser.parse_args()

    ai = EduMindQA()

    if args.question:
        single_question_mode(ai, args.question)
    else:
        interactive_mode(ai)


if __name__ == "__main__":
    main()
