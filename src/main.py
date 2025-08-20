#!/usr/bin/env python3
"""
src/main.py

Congratulations, you’ve opened the entrypoint.
Statistically, this is where side projects evolve legs, learn Kubernetes,
and start asking for a dedicated SRE.

Usage:
  python src/main.py
  python src/main.py --name Bob
  python src/main.py --spice    # adds extra chaos
"""

from __future__ import annotations
import argparse
import random
import textwrap

FORTUNES = [
    "Today’s bug is tomorrow’s feature.",
    "It works on your machine. Ship your machine.",
    "Refactor bravely; revert faster.",
    "Tabs vs spaces? Use whatever breaks CI.",
    "Naming things is hard. Choose chaos.",
]

ASCII_CONFETTI = textwrap.dedent(
    r"""
      *  .    ✦    . *
   ✦    .  *  .  ✦     *
      .    \ | /   .
    *    —  ( )  —   ✦
      .     /|\    .
   ✦    *    |   *    .
"""
)

def hello(name: str | None = None, spice: bool = False) -> str:
    target = name or "brave engineer"
    base = f"👋 Welcome, {target}! This boilerplate is ready to be over-engineered."
    seasoning = ""

    if spice:
        seasoning = (
            "\n🌶  Spice mode: ON\n"
            f"🔮 Fortune: {random.choice(FORTUNES)}\n"
            "⚠️  Warning: Side effects may include microservices."
        )

    return base + seasoning


def main() -> None:
    parser = argparse.ArgumentParser(
        description="The friendliest gateway to accidental complexity."
    )
    parser.add_argument("--name", help="Who to greet (defaults to ‘brave engineer’).")
    parser.add_argument(
        "--spice", action="store_true", help="Add chaos, confetti, and a fortune."
    )
    args = parser.parse_args()

    message = hello(args.name, args.spice)
    print(message)
    if args.spice:
        print(ASCII_CONFETTI)


if __name__ == "__main__":
    main()
