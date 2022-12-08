"""Solutions for Advent of Code 2022 Day 8"""
# pylint: disable=invalid-name
import os
import math
from lib import assert_answer, input_path


def parse_forest(lines):
    """Parse a matrix of trees out of the input lines."""
    forest = []

    for line in lines:
        forest.append([int(ch) for ch in line])

    return forest


def tree_is_visible(forest, y, x):
    """Returns True if a tree is visible from outside the forest."""
    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for offset in offsets:
        yy, xx = y + offset[0], x + offset[1]
        if not inbounds(forest, yy, xx):
            return True

        while True:
            if forest[yy][xx] >= forest[y][x]:
                break

            yy += offset[0]
            xx += offset[1]

            if not inbounds(forest, yy, xx):
                return True

    return False


def inbounds(forest, y, x):
    """Returns True if (y, x) are within the bounds of forest."""
    return 0 <= y < len(forest) and 0 <= x < len(forest[0])


def viewing_distance(forest, y, x, offset):
    """Returns the viewing distance for the tree at (y, x)"""
    vd = 0

    yy, xx = y + offset[0], x + offset[1]
    while inbounds(forest, yy, xx):
        vd += 1

        if forest[yy][xx] >= forest[y][x]:
            break

        yy += offset[0]
        xx += offset[1]

    return vd


def scenic_score(forest, y, x):
    """Returns the Scenic Score for the given tree."""
    viewing_distances = []

    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for offset in offsets:
        if (vd := viewing_distance(forest, y, x, offset)) != 0:
            assert vd > 0
            viewing_distances.append(vd)

    return math.prod(viewing_distances)


def solve(filename, part2=False):
    """Solve it."""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        forest = parse_forest(file.read().splitlines())

    visible_trees = []
    scenic_scores = []

    if filename.endswith("example.txt"):
        assert scenic_score(forest, 1, 2) == 4
        assert scenic_score(forest, 3, 2) == 8

    # pylint: disable=consider-using-enumerate
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            if part2:
                scenic_scores.append(scenic_score(forest, y, x))
            else:
                if tree_is_visible(forest, y, x):
                    visible_trees.append((y, x, forest[y][x]))

    if part2:
        return max(scenic_scores)

    return len(visible_trees)


def part_one(filename):
    """Part 1"""
    return solve(filename)


def part_two(filename):
    """Part 2"""
    return solve(filename, part2=True)


assert_answer(part_one, input_path("example.txt"), 21)
assert_answer(part_one, input_path("input.txt"), 1849)

# very sneaky: for the first time, Eric didn't tell us the answer
# to the part 2 example! I guess that's a thing now.
assert_answer(part_two, input_path("example.txt"), 16)
assert_answer(part_two, input_path("input.txt"), 201600)
