import os
import heapq

THROW_SCORE = dict(
    A=1,
    B=2,
    C=3,
    X=1,
    Y=2,
    Z=3,
)

I_WIN = set([
    'C X',
    'A Y',
    'B Z'
])

def part_one(filename):
    my_score = 0

    with open(os.path.abspath(filename)) as f:
        for line in f:
            elfos_throw, my_throw = [THROW_SCORE[t] for t in line.split()]
            my_score += my_throw
            if my_throw == elfos_throw:
                my_score += 3
            elif line.strip() in I_WIN:
                my_score += 6

    return my_score

NEED_SCORE = dict(
    XA=3,
    XB=1,
    XC=2,
    YA=1,
    YB=2,
    YC=3,
    ZA=2,
    ZB=3,
    ZC=1,
)

RESULT_SCORE = dict(
    X = 0,
    Y = 3,
    Z = 6,
)

def part_two(filename):
    my_score = 0
    with open(os.path.abspath(filename)) as f:
        for line in f:
            parts = line.split()
            my_score += NEED_SCORE[parts[1]+parts[0]] + RESULT_SCORE[parts[1]]

    return my_score

def assert_answer(fn, filename, want):
    got = fn(filename)
    print(f"{fn.__name__}({filename}) -> {got}")
    assert got == want, f"got {got}, want {want}"

assert_answer(part_one, 'example.txt', 15)
assert_answer(part_one, 'test0.txt', 30)
assert_answer(part_one, 'input.txt', 8392)

assert_answer(part_two, 'example.txt', 12)
assert_answer(part_two, 'test0.txt', 30)
assert_answer(part_two, 'test1.txt', 15)
assert_answer(part_two, 'input.txt', 10116)
