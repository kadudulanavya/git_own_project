from src1.maths import add,sub,mul,div
def test_add():
    assert add(2,3)==5
    assert add(3,3)==6
    assert add(4,3)==7
def test_sub():
    assert sub(2,3)==-1
    assert sub(3,3)==0
    assert sub(4,3)==1
def test_mul():
    assert mul(2,3)==6
    assert mul(3,3)==9
    assert mul(4,3)==12
def test_div():
    assert div(2,2)==1


