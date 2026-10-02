#!/usr/bin/env python3
"""Render a bounded Langton's ant simulation in the terminal."""

import argparse
import sys


MAX_STEPS = 100_000
MAX_CELLS = 250_000
MOVES = ((0, -1), (1, 0), (0, 1), (-1, 0))
ARROWS = "^>v<"


def simulate(steps):
    black = set()
    x = y = direction = 0
    for _ in range(steps):
        point = (x, y)
        if point in black:
            black.remove(point)
            direction = (direction - 1) % 4
        else:
            black.add(point)
            direction = (direction + 1) % 4
        dx, dy = MOVES[direction]
        x, y = x + dx, y + dy
    return black, (x, y), direction


def main():
    parser = argparse.ArgumentParser(
        description="Simulate Langton's ant and print its grid using ASCII characters."
    )
    parser.add_argument("--steps", type=int, default=10_000, help="moves to simulate (0–100000)")
    args = parser.parse_args()
    if not 0 <= args.steps <= MAX_STEPS:
        parser.error(f"--steps must be between 0 and {MAX_STEPS}")

    black, ant, direction = simulate(args.steps)
    cells = black | {ant}
    min_x = min(x for x, _ in cells)
    max_x = max(x for x, _ in cells)
    min_y = min(y for _, y in cells)
    max_y = max(y for _, y in cells)
    width, height = max_x - min_x + 1, max_y - min_y + 1

    print(f"Steps: {args.steps}")
    print(f"Black squares: {len(black)}")
    print(f"Ant: {ARROWS[direction]} at ({ant[0]}, {ant[1]})")
    # ponytail: cap terminal output at 250,000 cells; lower --steps to render larger runs.
    if width * height > MAX_CELLS:
        print(f"Grid omitted: {width}×{height} exceeds the {MAX_CELLS}-cell display limit.")
        return 0

    lines = []
    for y in range(max_y, min_y - 1, -1):
        lines.append(
            "".join(
                ARROWS[direction] if (x, y) == ant else "#" if (x, y) in black else "."
                for x in range(min_x, max_x + 1)
            )
        )
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
