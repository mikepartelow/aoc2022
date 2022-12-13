"""Solutions for Advent of Code 2022 Day 13"""
# pylint: disable=unidiomatic-typecheck,eval-used,too-many-return-statements
import os
import itertools
import functools
from lib import assert_answer, input_path


def right_order(left, right):
    """Returns True if the packets left and right are In The Right Order (TM)"""
    assert left is not None
    assert right is not None

    for leftval, rightval in itertools.zip_longest(left, right):
        if leftval is None:
            return True

        if rightval is None:
            return False

        if type(leftval) == type(rightval) == type(42):
            if leftval < rightval:
                return True
            if leftval > rightval:
                return False
        elif isinstance(leftval, list) and isinstance(rightval, list):
            if (order_check := right_order(leftval, rightval)) is not None:
                return order_check
        elif isinstance(leftval, list):
            if (order_check := right_order(leftval, [rightval])) is not None:
                return order_check
        else:
            if (order_check := right_order([leftval], rightval)) is not None:
                return order_check

    return None


def solve(filename, part2=False):
    """Solve it."""
    right_order_indices = []

    with open(os.path.abspath(filename), encoding="utf-8") as file:
        lines = file.read().replace("\n\n", "\n").splitlines()

    if part2:
        packets = [eval(line) for line in lines] + [[[2]], [[6]]]
        packets = sorted(
            packets,
            key=functools.cmp_to_key(
                lambda leftval, rightval: -1 if right_order(leftval, rightval) else 1
            ),
        )
        return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

    pairs = [(lines[i], lines[i + 1]) for i in range(0, len(lines), 2)]

    for idx, pair in enumerate(pairs, start=1):
        if right_order(*map(eval, pair)):
            right_order_indices.append(idx)

    return sum(right_order_indices)


def part_one(filename):
    """Part 1"""
    return solve(filename)


def part_two(filename):
    """Part 2"""
    return solve(filename, part2=True)


assert_answer(
    right_order,
    (
        [],
        [
            [9, 5],
            [5, 5, [[3, 7, 1, 6, 10]]],
            [[2, 9, [], 10]],
            [3, [4, [3], [0, 8]], 2],
            [[1, [7, 6, 5]], 10, [1, [8, 0, 2, 6, 7], [4, 3], [9, 7, 10, 3], 7]],
        ],
    ),
    True,
)

assert_answer(right_order, ([[[]]], [[]]), False)
assert_answer(right_order, ([[4, 4], 4, 4], [[4, 4], 4, 4, 4]), True)
assert_answer(
    right_order,
    (
        [7, 7, 7, 7],
        [7, 7, 7],
    ),
    False,
)
assert_answer(part_one, input_path("example.txt"), 13)
assert_answer(part_one, input_path("input.txt"), 5580)

assert_answer(part_two, input_path("example.txt"), 140)
assert_answer(part_two, input_path("input.txt"), 26200)
