"""Solutions for Advent of Code 2022 Day 3"""
import os
from lib import assert_answer, input_path


def parse_items(line):
    """Return a tuple of line split in halves."""
    line = line.strip()
    midline = int(len(line) / 2)
    return line[:midline], line[midline:]


def item_priority(item):
    """Return the uniquely elvish value of the given item."""
    if item.isupper():
        return int(ord(item)) - int(ord("A")) + 27
    return int(ord(item)) - int(ord("a")) + 1


def part_one(filename):
    """Part 1"""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        priorities = []

        for line in file:
            items0, items1 = parse_items(line)
            # print(f"items0, items1: ({items0}, {items1})")

            common_items = set(items0) & set(items1)
            assert len(common_items) == 1
            common_item = common_items.pop()
            # print(f" common_item: {common_item}")

            priorities.append(item_priority(common_item))

    return sum(priorities)


def part_two(filename):
    """Part 2"""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        elves = []
        priorities = []

        for line in file:
            elves.append(line.strip())
            if len(elves) == 3:
                badges = set(elves[0]) & set(elves[1]) & set(elves[2])
                assert len(badges) == 1

                badge = badges.pop()

                assert badge in elves[0]
                assert badge in elves[1]
                assert badge in elves[2]

                priorities.append(item_priority(badge))

                elves = []

        assert len(elves) == 0

        return sum(priorities)


assert_answer(item_priority, "a", 1)
assert_answer(item_priority, "m", 13)
assert_answer(item_priority, "z", 26)
assert_answer(item_priority, "A", 27)
assert_answer(item_priority, "M", 39)
assert_answer(item_priority, "Z", 52)

assert_answer(part_one, input_path("example.txt"), 157)
assert_answer(part_one, input_path("test0.txt"), 157)
assert_answer(part_one, input_path("input.txt"), 7793)

assert_answer(part_two, input_path("example.txt"), 70)
assert_answer(part_two, input_path("test1.txt"), 3)
assert_answer(part_two, input_path("input.txt"), 2499)
