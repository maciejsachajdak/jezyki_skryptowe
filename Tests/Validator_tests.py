from Validator import Validator
import pytest

@pytest.fixture
def valid():
    return Validator()


def test_check(valid):
    assert valid.check("abc")==True

def test_check_false(valid):
    assert valid.check("bbb") == False
