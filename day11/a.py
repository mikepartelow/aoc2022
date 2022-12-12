"""Solutions for Advent of Code 2022 Day 11"""
import copy
from lib import assert_answer


def solve(monkeys, part2=False):
    """Solve it."""
    monkeys = copy.deepcopy(monkeys)

    monkey_rounds = 10_000 if part2 else 20

    for monkey_round in range(monkey_rounds):
        if monkey_round % 100 == 0:
            print(monkey_round)

        # The monkeys take turns inspecting and throwing items.
        # On a single monkey's turn, it inspects and throws all
        # of the items it is holding one at a time and in the order listed

        for _, monkey in enumerate(monkeys):
            # After each monkey inspects an item but before it tests your worry level,
            # your relief that the monkey's inspection didn't damage the item causes
            # your worry level to be divided by three and rounded down to the nearest integer.

            while monkey["items"]:
                monkey["inspections"] += 1
                item = monkey["items"].pop(0)

                if not part2:
                    item = monkey["op"](item) // 3
                else:
                    item = monkey["op"](item)

                if monkey["test"](item):
                    other = monkey["if_true"]
                else:
                    other = monkey["if_false"]

                # print(f" m{mid} throws {item} to m{other}")
                monkeys[other]["items"].append(item)

        # if round == 0:
        #     assert monkeys[0]['items'] == [20, 23, 27, 26], monkeys[0]['items']
        #     assert monkeys[1]['items'] == [2080, 25, 167, 207, 401, 1046]
        #     assert monkeys[2]['items'] == []
        #     assert monkeys[3]['items'] == []

        # if round == 19:
        #     assert monkeys[0]['items'] == [10, 12, 14, 26, 34], monkeys[0]['items']
        #     assert monkeys[1]['items'] == [245, 93, 53, 199, 115], monkeys[1]['items']
        #     assert monkeys[2]['items'] == []
        #     assert monkeys[3]['items'] == []

        if part2 and monkey_round == 0:
            assert monkeys[0]["inspections"] == 2
            assert monkeys[1]["inspections"] == 4
            assert monkeys[2]["inspections"] == 3
            assert monkeys[3]["inspections"] == 6

        if part2 and monkey_round == 19:
            assert monkeys[0]["inspections"] == 99, monkeys[0]["inspections"]
            assert monkeys[1]["inspections"] == 97, monkeys[1]["inspections"]
            assert monkeys[2]["inspections"] == 8, monkeys[2]["inspections"]
            assert monkeys[3]["inspections"] == 103, monkeys[3]["inspections"]

        if part2 and monkey_round == 999:
            assert monkeys[0]["inspections"] == 5204
            assert monkeys[1]["inspections"] == 4792
            assert monkeys[2]["inspections"] == 199
            assert monkeys[3]["inspections"] == 5192

    monkeys.sort(key=lambda m: m["inspections"], reverse=True)
    print(list(map(lambda m: m["inspections"], monkeys)))
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
        test=lambda x: x % 23 == 0,
        if_true=2,
        if_false=3,
        inspections=0,
    ),
    dict(
        items=[54, 65, 75, 74],
        op=lambda o: o + 6,
        test=lambda x: x % 19 == 0,
        if_true=2,
        if_false=0,
        inspections=0,
    ),
    dict(
        items=[79, 60, 97],
        op=lambda o: o * o,
        test=lambda x: x % 13 == 0,
        if_true=1,
        if_false=3,
        inspections=0,
    ),
    dict(
        items=[74],
        op=lambda o: o + 3,
        test=lambda x: x % 17 == 0,
        if_true=0,
        if_false=1,
        inspections=0,
    ),
]

monkeys1 = [
    dict(
        items=[50, 70, 89, 75, 66, 66],
        op=lambda o: o * 5,
        test=lambda x: x % 2 == 0,
        if_true=2,
        if_false=1,
        inspections=0,
    ),
    dict(
        items=[85],
        op=lambda o: o**2,
        test=lambda x: x % 7 == 0,
        if_true=3,
        if_false=6,
        inspections=0,
    ),
    dict(
        items=[66, 51, 71, 76, 58, 55, 58, 60],
        op=lambda o: o + 1,
        test=lambda x: x % 13 == 0,
        if_true=1,
        if_false=3,
        inspections=0,
    ),
    dict(
        items=[79, 52, 55, 51],
        op=lambda o: o + 6,
        test=lambda x: x % 3 == 0,
        if_true=6,
        if_false=4,
        inspections=0,
    ),
    dict(
        items=[69, 92],
        op=lambda o: o * 17,
        test=lambda x: x % 19 == 0,
        if_true=7,
        if_false=5,
        inspections=0,
    ),
    dict(
        items=[71, 76, 73, 98, 67, 79, 99],
        op=lambda o: o + 8,
        test=lambda x: x % 5 == 0,
        if_true=0,
        if_false=2,
        inspections=0,
    ),
    dict(
        items=[82, 76, 69, 69, 57],
        op=lambda o: o + 7,
        test=lambda x: x % 11 == 0,
        if_true=7,
        if_false=4,
        inspections=0,
    ),
    dict(
        items=[65, 79, 86],
        op=lambda o: o + 5,
        test=lambda x: x % 17 == 0,
        if_true=5,
        if_false=0,
        inspections=0,
    ),
]

assert_answer(solve, monkeys0, 10605)
assert_answer(solve, monkeys1, 151312)

# assert_answer(solve, (monkeys0, True), 2713310158)
