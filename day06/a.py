"""Solutions for Advent of Code 2022 Day 3"""
from lib import assert_answer, input_path


def marker_index(buf, marker_len):
    """YASW : Yet Another Sliding Window"""
    assert len(buf) > marker_len

    i, j = 0, 1
    while j < len(buf):
        while i < j and buf[j] in buf[i:j]:
            i += 1

        j += 1

        # at this point buf[j] could actually be in buf[i:j]
        # (part 2 example 0)
        # but we know that buf[i:j-1] wasn't in buf[i:j]
        # so if we've hit our length, we are done
        #
        # part 1 can be solved with the length check before
        # incrementing j
        # part 2 can't
        #

        if j - i == marker_len:
            return j

    return None


examples = (
    ("abcde", 4),
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
)

MARKER_LEN1 = 4

for example, answer in examples:
    assert_answer(marker_index, (example, MARKER_LEN1), answer)

with open(input_path("input.txt"), encoding="utf-8") as f:
    assert_answer(marker_index, (f.read(), MARKER_LEN1), 1034)

examples = (
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
)

MARKER_LEN2 = 14

for example, answer in examples:
    assert_answer(marker_index, (example, MARKER_LEN2), answer)

with open(input_path("input.txt"), encoding="utf-8") as f:
    assert_answer(marker_index, (f.read(), MARKER_LEN2), 2472)
