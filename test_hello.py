from hello import add


# write a test function for add
def test_add():
    assert add(1, 2) == 3
    assert add(1, 1) == 2
    assert add(1, 0) == 1
    assert add(1, -1) == 0
