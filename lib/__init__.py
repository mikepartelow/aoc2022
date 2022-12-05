"""Helper elves."""
import os
import inspect


def assert_answer(func, args, want):
    """Call func(*args), print the result, assert result == want"""
    if isinstance(args, tuple):
        got = func(*args)
    else:
        got = func(args)
    print(f"{func.__name__}({args}) -> {got}")
    assert got == want, f"got {got}, want {want}"


def input_path(filename):
    """Return the absolute path of /<directory of caller>/filename.

    Example: /foo/bar/baz.py calls input_path('spam.txt') -> /foo/bar/spam.txt
    """
    path = os.path.join(os.path.dirname(inspect.stack()[1].filename), filename)
    return os.path.normpath(path)
