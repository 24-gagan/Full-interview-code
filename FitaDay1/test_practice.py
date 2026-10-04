def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5


def even(n):
    return n % 2 == 0


def test_even():
    assert even(4) == True


def test_odd():
    assert 5 % 2 != 0


def max_num(a, b):
    return a if a > b else b


def test_max_num():
    assert max_num(2, 3) == 3


def test_min():
    assert min(2, 3) == 2


def reverse(s):
    return s[::-1]


def test_reverse():
    assert reverse("hello") == "olleh"


def test_sum():
    assert sum([1, 2, 3]) == 6


def test_count():
    assert len([1, 2, 3]) == 3
