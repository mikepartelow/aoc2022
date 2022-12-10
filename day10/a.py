"""Solutions for Advent of Code 2022 Day 10"""
# pylint: disable=invalid-name
import os
from lib import assert_answer, input_path


def fancy_cycles(cycles):
    """Returns True if the cycle is a fancy signal cycle."""
    return cycles == 20 or cycles > 20 and (cycles - 20) % 40 == 0


def pixel(pos, X):
    """Returns a pixel for position pos given register value X."""
    # the sprite is 3 pixels wide, and the X register sets the horizontal
    # position of the middle of that sprite
    # If the sprite is positioned such that one of its three pixels is the pixel
    # currently being drawn,
    # the screen produces a lit pixel (#)

    assert pos < 40
    if X - 1 <= pos <= X + 1:
        return "#"
    return "."


def execute(program):
    """Executes the program using Part 1 rules. Returns register X  and the sum of the signals."""
    # consider the signal strength (the cycle number multiplied by the value of the X register)
    # during the 20th cycle and every 40 cycles after that
    # (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).
    X = 1
    cycles = 1
    signals = []

    for instruction in program:
        if instruction == "noop":
            cycles += 1
        elif instruction.startswith("addx"):
            _, num = instruction.split()

            cycles += 1
            if fancy_cycles(cycles):
                print(f"f1: {cycles} {X} {cycles * X}")
                signals.append(cycles * X)
            cycles += 1

            X += int(num)
        else:
            assert False, instruction

        if fancy_cycles(cycles):
            print(f"f2: {cycles} {X} {cycles * X}")
            signals.append(cycles * X)

    return X, sum(signals)


def render(program):
    """Renders the program under Part 2 rules. Returns the rendered image."""
    X = 1
    lines = []
    line = ""

    for instruction in program:
        if instruction == "noop":
            line += pixel(len(line), X)
        elif instruction.startswith("addx"):
            _, num = instruction.split()
            line += pixel(len(line), X)
            if len(line) == 40:
                lines.append(line)
                line = ""
            line += pixel(len(line), X)

            X += int(num)
        else:
            assert False, instruction

        if len(line) == 40:
            lines.append(line)
            line = ""

    assert len(lines) == 6, len(lines)
    assert len(lines[0]) == 40, len(lines[0])

    image = "\n".join(lines)

    return image


def solve(filename, part2=False):
    """Solve it."""
    with open(os.path.abspath(filename), encoding="utf-8") as file:
        program = file.read().splitlines()

    if part2:
        return render(program)

    _, signal = execute(program)
    return signal


def part_one(filename):
    """Part 1"""
    return solve(filename)


def part_two(filename):
    """Part 2"""
    return solve(filename, part2=True)


p0 = """noop
addx 3
addx -5
"""

assert_answer(execute, p0.splitlines(), (-1, 0))
assert_answer(part_one, input_path("example.txt"), 13140)
assert_answer(part_one, input_path("input.txt"), 16480)

image0 = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
""".strip()

image1 = """
###..#....####.####.#..#.#....###..###..
#..#.#....#....#....#..#.#....#..#.#..#.
#..#.#....###..###..#..#.#....#..#.###..
###..#....#....#....#..#.#....###..#..#.
#....#....#....#....#..#.#....#....#..#.
#....####.####.#.....##..####.#....###..
""".strip()
assert_answer(part_two, input_path("example.txt"), image0)
assert_answer(part_two, input_path("input.txt"), image1)
