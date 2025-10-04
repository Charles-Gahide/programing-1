import time
time.sleep(10)
import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("people_count, bus_capacity, expected", [
    (0, 1, 0),
    (0, 10, 0),
    (0, 100, 0),
    (1, 1, 1),
    (1, 10, 1),
    (1, 100, 1),
    (10, 1, 10),
    (10, 10, 1),
    (10, 100, 1),
    (55, 1, 55),
    (55, 10, 6),
    (55, 100, 1),
    (104, 1 , 104),
    (104, 10, 11),
    (104, 100, 2),
    (4201, 1, 4201),
    (4201, 10, 421),
    (4201, 100, 43)
])
def test_buses_needed(people_count, bus_capacity, expected):
    actual = student.buses_needed(people_count=people_count, bus_capacity=bus_capacity)

    assert actual == expected
