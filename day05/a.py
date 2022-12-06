"""Solutions for Advent of Code 2022 Day 5"""
import os
from lib import assert_answer, input_path


def parse_crates(line):
    """Returns a list of crates found in a line of text.
    Returns None if line contains no crates."""
    crates = []
    i = 1
    while i < len(line):
        if line[i].isnumeric():
            return None
        if line[i] == " ":
            crates.append(None)
        else:
            crates.append(line[i])
        i += 4
    return crates


def move_crates(stacks, count, src, dst, part2=False):
    """Move count crates in the stack from col src to col dst."""
    print(f" move_crates({stacks}, {count}, {src}, {dst}, {part2}")
    stacks = [s[:] for s in stacks]
    src, dst = src - 1, dst - 1
    temp = []
    while count > 0:
        crate = stacks[src].pop()
        temp.append(crate)
        count -= 1

    if part2:
        stacks[dst].extend(temp[::-1])
    else:
        stacks[dst].extend(temp)

    return stacks


def top_crates(stacks):
    """Returns a string of the top crates of each stack in the stacks."""
    tops = [s[-1] for s in stacks if s]
    return "".join(tops)


def solve(filename, part2=False):
    """Solve it."""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        stacks = [[], [], [], [], [], [], [], [], []]
        stacking = True

        for line in file:
            if stacking:
                if (crates := parse_crates(line)) is None:
                    stacking = False
                else:
                    for i, crate in enumerate(crates):
                        if crate is not None:
                            stacks[i].insert(0, crate)
            elif line.startswith("move "):
                parts = line.split()
                count, src, dst = map(int, (parts[1], parts[3], parts[5]))

                stacks = move_crates(stacks, count, src, dst, part2)

    return top_crates(stacks)


def part_one(filename):
    """Part 1"""
    return solve(filename)


def part_two(filename):
    """Part 2"""
    return solve(filename, part2=True)


assert_answer(parse_crates, "    [D]    ", [None, "D", None])
assert_answer(
    parse_crates,
    "                [M]     [V]     [L]",
    [None, None, None, None, "M", None, "V", None, "L"],
)
assert_answer(parse_crates, "[N] [C]", ["N", "C"])
assert_answer(parse_crates, "[Z] [M] [P]", ["Z", "M", "P"])
assert_answer(parse_crates, " 1   2   3", None)

stacks0 = [["Z", "N"], ["M", "C", "D"], ["P"]]
stacks1 = [["Z", "N", "D"], ["M", "C"], ["P"]]
stacks2 = [["Z"], ["M", "C"], ["P", "D", "N"]]
stacks3 = [[], ["M", "C", "Z"], ["P", "D", "N"]]
stacks4 = [[], ["M", "C"], ["P", "D", "N", "Z"]]
assert_answer(move_crates, (stacks0, 1, 2, 1), stacks1)
assert_answer(move_crates, (stacks1, 2, 1, 3), stacks2)
assert_answer(move_crates, (stacks2, 1, 1, 2), stacks3)
assert_answer(move_crates, (stacks3, 1, 2, 3), stacks4)

assert_answer(top_crates, stacks1, "DCP")
assert_answer(top_crates, stacks2, "ZCN")
assert_answer(top_crates, stacks3, "ZN")

assert_answer(part_one, input_path("example.txt"), "CMZ")
assert_answer(part_one, input_path("input.txt"), "CWMTGHBDW")

stacks5 = [[], ["M", "C"], ["P", "Z", "N", "D"]]
stacks6 = [["M", "C"], [], ["P", "Z", "N", "D"]]
assert_answer(move_crates, (stacks0, 1, 2, 1, True), stacks1)
assert_answer(move_crates, (stacks1, 3, 1, 3, True), stacks5)
assert_answer(move_crates, (stacks5, 2, 2, 1, True), stacks6)

assert_answer(part_two, input_path("example.txt"), "MCD")
assert_answer(part_two, input_path("input.txt"), "SSCGWJCRB")
