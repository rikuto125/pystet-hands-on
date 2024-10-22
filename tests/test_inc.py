import pytest
from src.inc import inc


def test_answer():
    assert inc(3) == 4
