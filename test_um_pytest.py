from unnecessary_math import multiply
from unnecessary_math import myFun
from unnecessary_math import perryFun
def test_numbers_3_4():
    assert multiply(3,4) == 12 
          
def test_strings_a_3():
    assert multiply('a',3) == 'aaa'

def test_my_math():
    assert myFun('a', 'b') == 'ab'

def test_perry_func():
    assert perryFun('b') == 'b'
