"""Helper elves."""
import os
import inspect


def assert_answer(func, filename, want):
    """Call func(filename), print the result, assert result == want"""
    got = func(filename)
    print(f"{func.__name__}({filename}) -> {got}")
    assert got == want, f"got {got}, want {want}"


def input_path(filename):
    """Return the absolute path of /<directory of caller>/filename.

    Example: /foo/bar/baz.py calls input_path('spam.txt') -> /foo/bar/spam.txt
    """
    path = os.path.join(os.path.dirname(inspect.stack()[1].filename), filename)
    return os.path.normpath(path)
