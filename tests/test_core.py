"""Tests for mypackage.core."""

from mypackage.core import add


def test_add(sample_numbers: tuple[int, int]) -> None:
  a, b = sample_numbers
  assert add(a, b) == 5


def test_add_negative() -> None:
  assert add(-1, -1) == -2
