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


def tree_is_visible(forest, y, x, height=None, offsets=None):
    """Returns True if a tree is visible from outside the forest."""
    if y == 0 or x == 0 or y == len(forest) - 1 or x == len(forest[0]) - 1:
        return True

    if offsets is None:
        offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))

    if height is None:
        height = forest[y][x]

    for offset in offsets:
        yy, xx = y + offset[0], x + offset[1]
        neighbor = forest[yy][xx]

        if neighbor < height and tree_is_visible(forest, yy, xx, height, (offset,)):
            return True

    return False


def inbounds(y, x, forest):
    """Returns True if (y, x) are within the bounds of forest."""
    return 0 <= y < len(forest) and 0 <= x < len(forest[0])


def viewing_distance(forest, y, x, offset):
    """Returns the viewing distance for the tree at (y, x)"""
    vd = 0

    yy, xx = y + offset[0], x + offset[1]
    while inbounds(yy, xx, forest):
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


def part_one(filename):
    """Part 1"""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        forest = parse_forest(file.read().splitlines())

    visible_trees = []

    # pylint: disable=consider-using-enumerate
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            if tree_is_visible(forest, y, x):
                visible_trees.append((y, x, forest[y][x]))

    return len(visible_trees)


def part_two(filename):
    """Part 2"""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        forest = parse_forest(file.read().splitlines())

    if filename.endswith("example.txt"):
        assert scenic_score(forest, 1, 2) == 4
        assert scenic_score(forest, 3, 2) == 8

    scenic_scores = []

    # pylint: disable=consider-using-enumerate
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            score = scenic_score(forest, y, x)
            scenic_scores.append(score)

    return max(scenic_scores)


assert_answer(part_one, input_path("example.txt"), 21)
assert_answer(part_one, input_path("input.txt"), 1849)

# very sneaky: for the first time, Eric didn't tell us the answer
# to the part 2 example! I guess that's a thing now.
assert_answer(part_two, input_path("example.txt"), 16)
assert_answer(part_two, input_path("input.txt"), 201600)
