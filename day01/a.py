"""Solutions for Advent of Code 2022 Day 1"""
import os
import heapq
from lib import assert_answer, input_path


def part_one(filename):
    """Part 1"""
    max_calories = 0
    elf_calories = 0

    with open(os.path.abspath(filename), encoding="utf-8") as file:
        for line in file:
            item = line.strip()
            if item == "":
                max_calories = max(max_calories, elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(item)

    max_calories = max(max_calories, elf_calories)

    # print(f"   max_calories: {max_calories}")
    return max_calories


def part_two(filename):
    """Part 2"""
    calorie_heap = []
    elf_calories = 0

    with open(os.path.abspath(filename), encoding="utf-8") as file:
        for line in file:
            item = line.strip()
            if item == "":
                heapq.heappush(calorie_heap, -elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(item)

    heapq.heappush(calorie_heap, -elf_calories)
    max_calories = sum(-heapq.heappop(calorie_heap) for _ in range(3))

    # print(f"   max_calories: {max_calories}")
    return max_calories


assert_answer(part_one, input_path("example.txt"), 24000)
assert_answer(part_one, input_path("test0.txt"), 1)
assert_answer(part_one, input_path("input.txt"), 67450)

assert_answer(part_two, input_path("example.txt"), 45000)
assert_answer(part_two, input_path("test1.txt"), 203)
assert_answer(part_two, input_path("input.txt"), 199357)
