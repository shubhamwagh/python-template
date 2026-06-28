"""Shared pytest fixtures."""

import pytest


@pytest.fixture
def sample_numbers() -> tuple[int, int]:
  """Return a pair of integers for arithmetic tests."""
  return 2, 3
