"""
Demonstration of a bug in Sphinx

Visit <https://github.com/jwodder/sphinx-bug-20220616> for more information.
"""

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "sphinx-bug-20220616@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/sphinx-bug-20220616"

from collections import deque
from collections.abc import Iterable, Iterator
from typing import AnyStr, TypeVar

T = TypeVar("T")


def anystr_iters(args: Iterable[AnyStr]) -> Iterator[AnyStr]:
    """
    The `AnyStr` parameters will be left off from the argument and return value
    of this function.
    """
    ...


def deque_func(queue: deque[str]) -> str:
    """This function is rendered fine."""
    ...


def deque_anystr_func(queue: deque[AnyStr]) -> str:
    """
    The `AnyStr` param will be left off from the argument of this function.
    """
    ...


def typevar_paramed(seq: list[T]) -> tuple[T]:
    """This function is rendered fine."""
    ...
