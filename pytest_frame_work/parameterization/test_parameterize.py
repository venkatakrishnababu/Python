import pytest
@pytest.mark.parametrize("input,expected",[(2,4),(3,9),(4,8),(5,24)])
def test_square(input,expected):
    assert input**2==expected
@pytest.mark.parametrize("a,b,c",[(1,2,3),(2,3,5),(2,2,2)])
def test_add(a,b,c):
    assert a+b==c