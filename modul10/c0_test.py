from c0 import Point

def test_move_in_place():
    p = Point(3, 8)

    p.move(2, -1)

    assert p.x() == 5
    assert p.y() == 7

def test_move_and_moved_are_different():
    p1 = Point(0, 0)

    p2 = p1.moved(10, 10)  # new object
    p1.move(1, 1)          # mutate existing

    assert p1.x() == 1
    assert p1.y() == 1

    assert p2.x() == 10
    assert p2.y() == 10

    # And ensure they're not the same object
    assert p1 is not p2