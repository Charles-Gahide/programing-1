import time
time.sleep(10)
import pytest
import student

def test_initialisation():
    c = student.Counter()
    assert c.get_count() == 0

@pytest.mark.parametrize("n", [
    x for x in range(1, 6)
])
def test_increment(n):
    c = student.Counter()
    for _ in range(n):
        c.increment()
    assert c.get_count() == n

def test_set_count():
    c = student.Counter()
    with pytest.raises(AttributeError):
        c.set_count(5)

def test_reset():
    c = student.Counter()
    c.increment()
    c.reset()
    assert c.get_count() == 0

def test_private_field():
    c = student.Counter()
    with pytest.raises(AttributeError):
        print(c.count)
