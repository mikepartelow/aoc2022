"""Solutions for Advent of Code 2022 Day 11"""
import copy
import math
from lib import assert_answer


def solve(monkeys, part2=False):
    """Solve it."""
    monkeys = copy.deepcopy(monkeys)

    monkey_rounds = 10_000 if part2 else 20

    lcm = math.lcm(*[m["testmod"] for m in monkeys])

    for _ in range(monkey_rounds):
        for _, monkey in enumerate(monkeys):
            while monkey["items"]:
                monkey["inspections"] += 1
                item = monkey["items"].pop(0)

                if not part2:
                    item = monkey["op"](item) // 3
                else:
                    item = monkey["op"](item)

                if item % monkey["testmod"] == 0:
                    other = monkey["if_true"]
                else:
                    other = monkey["if_false"]

                if part2:
                    item = item % lcm
                monkeys[other]["items"].append(item)

    monkeys.sort(key=lambda m: m["inspections"], reverse=True)

    return monkeys[0]["inspections"] * monkeys[1]["inspections"]


def part_one(filename):
    """Part 1"""
    return solve(filename)


def part_two(filename):
    """Part 2"""
    return solve(filename, part2=True)


monkeys0 = [
    dict(
        items=[79, 98],
        op=lambda o: o * 19,
        testmod=23,
        if_true=2,
        if_false=3,
        inspections=0,
    ),
    dict(
        items=[54, 65, 75, 74],
        op=lambda o: o + 6,
        testmod=19,
        if_true=2,
        if_false=0,
        inspections=0,
    ),
    dict(
        items=[79, 60, 97],
        op=lambda o: o * o,
        testmod=13,
        if_true=1,
        if_false=3,
        inspections=0,
    ),
    dict(
        items=[74],
        op=lambda o: o + 3,
        testmod=17,
        if_true=0,
        if_false=1,
        inspections=0,
    ),
]

monkeys1 = [
    dict(
        items=[50, 70, 89, 75, 66, 66],
        op=lambda o: o * 5,
        testmod=2,
        if_true=2,
        if_false=1,
        inspections=0,
    ),
    dict(
        items=[85],
        op=lambda o: o**2,
        testmod=7,
        if_true=3,
        if_false=6,
        inspections=0,
    ),
    dict(
        items=[66, 51, 71, 76, 58, 55, 58, 60],
        op=lambda o: o + 1,
        testmod=13,
        if_true=1,
        if_false=3,
        inspections=0,
    ),
    dict(
        items=[79, 52, 55, 51],
        op=lambda o: o + 6,
        testmod=3,
        if_true=6,
        if_false=4,
        inspections=0,
    ),
    dict(
        items=[69, 92],
        op=lambda o: o * 17,
        testmod=19,
        if_true=7,
        if_false=5,
        inspections=0,
    ),
    dict(
        items=[71, 76, 73, 98, 67, 79, 99],
        op=lambda o: o + 8,
        testmod=5,
        if_true=0,
        if_false=2,
        inspections=0,
    ),
    dict(
        items=[82, 76, 69, 69, 57],
        op=lambda o: o + 7,
        testmod=11,
        if_true=7,
        if_false=4,
        inspections=0,
    ),
    dict(
        items=[65, 79, 86],
        op=lambda o: o + 5,
        testmod=17,
        if_true=5,
        if_false=0,
        inspections=0,
    ),
]

assert_answer(solve, monkeys0, 10605)
assert_answer(solve, monkeys1, 151312)

assert_answer(solve, (monkeys0, True), 2713310158)
assert_answer(solve, (monkeys1, True), 51382025916)
