"""Solutions for Advent of Code 2022 Day 2"""
import os
from lib import assert_answer, input_path

THROW_SCORE = dict(
    A=1,
    B=2,
    C=3,
    X=1,
    Y=2,
    Z=3,
)

I_WIN = set(["C X", "A Y", "B Z"])


def part_one(filename):
    """Part 1"""
    my_score = 0

    with open(os.path.abspath(filename), encoding="utf-8") as file:
        for line in file:
            elfos_throw, my_throw = [THROW_SCORE[t] for t in line.split()]
            my_score += my_throw
            if my_throw == elfos_throw:
                my_score += 3
            elif line.strip() in I_WIN:
                my_score += 6

    return my_score


NEED_SCORE = dict(
    XA=3,
    XB=1,
    XC=2,
    YA=1,
    YB=2,
    YC=3,
    ZA=2,
    ZB=3,
    ZC=1,
)

RESULT_SCORE = dict(
    X=0,
    Y=3,
    Z=6,
)


def part_two(filename):
    """Part 2"""
    my_score = 0
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        for line in file:
            elfos_throw, my_result = line.split()
            my_score += NEED_SCORE[my_result + elfos_throw] + RESULT_SCORE[my_result]

    return my_score


assert_answer(part_one, input_path("example.txt"), 15)
assert_answer(part_one, input_path("test0.txt"), 30)
assert_answer(part_one, input_path("input.txt"), 8392)

assert_answer(part_two, input_path("example.txt"), 12)
assert_answer(part_two, input_path("test0.txt"), 30)
assert_answer(part_two, input_path("test1.txt"), 15)
assert_answer(part_two, input_path("input.txt"), 10116)
