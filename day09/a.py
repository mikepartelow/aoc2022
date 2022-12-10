"""Solutions for Advent of Code 2022 Day 9"""
# pylint: disable=invalid-name
# This problem is gorgeous!
# But this code is not.
import os
from lib import assert_answer, input_path

MAX_ROWS = 21
MAX_COLS = 27

# MAX_ROWS = 5
# MAX_COLS = 6


def xlate(pos):
    """Translate between coordinates."""
    return (pos[0] + 5, pos[1] + 11)
    # return (pos[0], pos[1])


def rendertv(tail_visited):
    """Render tail visited."""
    rows = []

    tvpos = set(map(xlate, list(tail_visited)))

    for y in range(MAX_ROWS, -1, -1):
        row = ["."] * MAX_COLS
        for x in range(MAX_COLS):
            if (y, x) in tvpos:
                row[x] = "#"
        rows.append(row)

    return "\n".join("".join(row) for row in rows)


def render(hpos, tails, tail_visited):
    """Render the snake."""
    rows = []

    hpos = xlate(hpos)
    tails = list(map(xlate, tails))[::-1]
    tvpos = set(map(xlate, list(tail_visited)))

    for y in range(MAX_ROWS, -1, -1):
        row = ["."] * MAX_COLS
        for x in range(MAX_COLS):
            for idx, pos in enumerate(tails):
                if (y, x) == pos:
                    num = len(tails) - idx
                    row[x] = str(num)
            if (y, x) == hpos:
                row[x] = "H"
            if (y, x) in tvpos:
                row[x] = "#"

        rows.append(row)

    return "\n".join("".join(row) for row in rows)


def sign(n):
    """Return the sign of the int."""
    return -1 if n < 0 else 1


def increment(pos, inc):
    """Increment a position."""
    return (pos[0] + inc[0], pos[1] + inc[1])


def decrement(pos, inc):
    """Decrement a position."""
    return (pos[0] - inc[0], pos[1] - inc[1])


def distance_between(posa, posb):
    """Return absolute distance between two positions."""
    return tuple(map(abs, (posa[0] - posb[0], posa[1] - posb[1])))


def difference(posa, posb):
    """Return posa - posb."""
    return (posa[0] - posb[0], posa[1] - posb[1])


def touching(posa, posb):
    """Returns True if the two positions are within one square of each other."""
    return abs(posa[0] - posb[0]) < 2 and abs(posa[1] - posb[1]) < 2


def move_tail(hpos, tpos, inc):
    """Moves the tail at tpos to keep up with the head at hpos."""
    distance = distance_between(hpos, tpos)
    # assert sum(distance) < 4, f"{hpos} {tpos} {inc} {distance}"
    if distance[0] == 0 and distance[1] == 2 or distance[0] == 2 and distance[1] == 0:
        # If the head is ever two steps directly up, down, left, or right from the tail,
        # the tail must also move one step in that direction

        if distance[0] == 0:
            inc = (0, inc[1])
        else:
            inc = (inc[0], 0)

        assert inc[0] == 0 or inc[1] == 0, inc

        tpos = increment(tpos, inc)
    elif not touching(hpos, tpos):
        # Otherwise, if the head and tail aren't touching and aren't in the same row or column,
        # the tail always moves one step diagonally to keep up

        diff = difference(hpos, tpos)
        inc = (1 * sign(diff[0]), 1 * sign(diff[1]))
        tpos = increment(tpos, inc)

    distance1 = distance_between(hpos, tpos)

    assert sum(distance1) < 3, f"{hpos} {tpos} {inc} {distance1}"
    return tpos, inc


INCS = dict(
    # D=(y, x)
    R=(0, 1),
    U=(1, 0),
    L=(0, -1),
    D=(-1, 0),
)


def solve(filename, part2=False):
    """Solve it."""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        moves = file.read().splitlines()

    # count up all of the positions the tail visited at least once
    tail_visited = set([(0, 0)])

    # Assume the head and the tail both start at the same position, overlapping
    hpos = (0, 0)

    if part2:
        tails = [
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
        ]
    else:
        tails = [
            (0, 0),
        ]

    # print(render(hpos, tails, tail_visited))
    # print("")

    for move in moves:
        # print(move)
        direction, units = move.split()

        inc = INCS[direction]
        for _ in range(int(units)):
            hpos = increment(hpos, inc)
            tpos_prev = hpos
            tinc = inc
            for tidx, tpos in enumerate(tails):
                tpos, tinc = move_tail(tpos_prev, tpos, tinc)

                # we don't want to move all the tails in the direction of the head
                # we want to move the tails in the direction of *the previous tail*
                # so move_tail must also return its own inc

                tails[tidx] = tpos

                if tidx == len(tails) - 1:
                    tail_visited.add(tpos)

                tpos_prev = tpos

            # print(render(hpos, tails, tail_visited))
            # print("")

    # print(rendertv(tail_visited))

    return len(tail_visited)


def part_one(filename):
    """Part 1"""
    return solve(filename)


def part_two(filename):
    """Part 2"""
    return solve(filename, part2=True)


assert_answer(part_one, input_path("example.txt"), 13)
assert_answer(part_one, input_path("input.txt"), 6057)

assert_answer(part_two, input_path("example.txt"), 1)
assert_answer(part_two, input_path("example1.txt"), 36)
assert_answer(part_two, input_path("input.txt"), 2514)
