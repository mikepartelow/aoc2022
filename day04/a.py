"""Solutions for Advent of Code 2022 Day 3"""
import os
from lib import assert_answer, input_path


def part_one(filename):
    """Part 1"""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        overlaps = 0

        for line in file:
            ranges = line.split(',')
            lo_a, hi_a = [int(n) for n in ranges[0].split('-')]
            lo_b, hi_b = [int(n) for n in ranges[1].split('-')]

            if lo_a >= lo_b and hi_a <= hi_b or lo_b >= lo_a and hi_b <= hi_a:
                overlaps += 1

    return overlaps


def lhs_contains_rhs(lhs_lo, lhs_hi, rhs_lo, rhs_hi):
    """Returns True if rhs_lo-rhs_hi is contained within lhs_lo-lhs_hi"""
    return lhs_lo <= rhs_lo <= lhs_hi or lhs_lo <= rhs_hi <= lhs_hi


def part_two(filename):
    """Part 2"""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        overlaps = 0

        for line in file:
            ranges = line.split(',')

            range_a = [int(n) for n in ranges[0].split('-')]
            range_b = [int(n) for n in ranges[1].split('-')]

            if lhs_contains_rhs(*range_a, *range_b) or \
               lhs_contains_rhs(*range_b, *range_a):
                overlaps += 1

    return overlaps


assert_answer(part_one, input_path("example.txt"), 2)
assert_answer(part_one, input_path("input.txt"), 532)

assert_answer(part_two, input_path("example.txt"), 4)
assert_answer(part_two, input_path("input.txt"), 854)
