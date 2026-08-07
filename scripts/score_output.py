#!/usr/bin/env python3
"""Calculate the weighted manual quality score for one generated poster."""

from __future__ import annotations

import argparse
import json


WEIGHTS = {
    "fidelity": 25,
    "abstraction": 20,
    "traceability": 20,
    "composition": 15,
    "typography": 10,
    "color": 10,
}


def rating(value: str) -> float:
    number = float(value)
    if not 0 <= number <= 10:
        raise argparse.ArgumentTypeError("ratings must stay between 0 and 10")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in WEIGHTS:
        parser.add_argument(f"--{name}", type=rating, required=True)
    parser.add_argument("--minimum", type=float, default=75.0)
    args = parser.parse_args()
    ratings = {name: getattr(args, name) for name in WEIGHTS}
    score = sum(ratings[name] * weight / 10 for name, weight in WEIGHTS.items())
    report = {
        "score": round(score, 2),
        "minimum": args.minimum,
        "passed": score >= args.minimum,
        "ratings": ratings,
        "weights": WEIGHTS,
    }
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
