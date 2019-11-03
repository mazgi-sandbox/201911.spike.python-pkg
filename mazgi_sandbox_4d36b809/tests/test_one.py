import pytest
from ..one.one_class import OneClass


def test_one():
    obj = OneClass()
    assert True == True
    assert obj.use_two() == 'func() in two'
