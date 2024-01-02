import pytest
import function

@pytest.mark.skip(reason="no")
def test_find_primes():
    assert function.find_primes(3)==False
    assert function.find_primes(5)==True

@pytest.mark.parametrize("num1,res",[(3,False),(5,True)])
def test_find_primes2(num1,res):
    assert function.find_primes(num1 )==res


@pytest.mark.check
def test_sort_list():
    assert function.sort_list([3,6,2,8])==[3,6,2,8].sort()
    assert function.sort_list(['a',6,2,8])==['a',6,2,8].sort()

