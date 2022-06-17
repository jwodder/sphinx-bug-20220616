"""
Demonstration of a bug in Sphinx

Visit <https://github.com/jwodder/sphinx-bug-20220616> for more information.
"""

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "sphinx-bug-20220616@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/sphinx-bug-20220616"

from collections.abc import Iterable, Iterator
from typing import AnyStr


def func(args: Iterable[AnyStr]) -> Iterator[AnyStr]:
    """A function that does stuff"""
    ...
