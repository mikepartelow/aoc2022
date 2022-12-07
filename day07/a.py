"""Solutions for Advent of Code 2022 Day 7"""
import os
from collections import defaultdict
from lib import assert_answer, input_path


TOTAL_AVAILABLE_SPACE = 70000000
UPDATE_SIZE = 30000000
ROOT_DIR = "root"


def compute_sizes(lines):
    """Parse the lines and compute directory sizes."""
    sizes = defaultdict(int)
    path = []

    line = lines.pop(0)
    while lines:
        assert line.startswith("$ cd") or line.startswith("$ ls")

        if line.startswith("$ cd"):

            match line.split(" ")[2]:
                case "/":
                    path = [ROOT_DIR]
                case "..":
                    assert path
                    path.pop()
                case dirname:
                    path.append(dirname)

            line = lines.pop(0)

        elif line.startswith("$ ls"):

            line = lines.pop(0)
            while line and not line.startswith("$ "):
                cwd = "/".join(path)

                if not line.startswith("dir "):
                    size = int(line.split(" ")[0])

                    while cwd:
                        sizes[cwd] += size
                        cwd = "/".join(cwd.split("/")[:-1])

                line = lines.pop(0) if lines else None

    return sizes


def solve(filename, part2=False):
    """Solve it."""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        sizes = compute_sizes(file.read().splitlines())

    if filename.endswith("example.txt"):
        assert sizes[f"{ROOT_DIR}/a/e"] == 584
        assert sizes[f"{ROOT_DIR}/a"] == 94853
        assert sizes[f"{ROOT_DIR}/d"] == 24933642
        assert sizes[ROOT_DIR] == 48381165

    if part2:
        unused_space = TOTAL_AVAILABLE_SPACE - sizes[ROOT_DIR]
        minimum_delete_space = UPDATE_SIZE - unused_space

        if filename.endswith("example.txt"):
            assert unused_space == 21618835
            assert minimum_delete_space == 8381165

        return min(v for v in sizes.values() if v >= minimum_delete_space)

    # part1
    return sum(v for v in sizes.values() if v <= 100000)


def part_one(filename):
    """Part 1"""
    return solve(filename)


def part_two(filename):
    """Part 2"""
    return solve(filename, part2=True)


assert_answer(part_one, input_path("example.txt"), 95437)
assert_answer(part_one, input_path("input.txt"), 1517599)

assert_answer(part_two, input_path("example.txt"), 24933642)
assert_answer(part_two, input_path("input.txt"), 2481982)
