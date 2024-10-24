from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-2,2)==0

def sub():
    assert sub(3,2)==1
    assert sub(10,4)==6    
    assert sub(10,13)==-3 