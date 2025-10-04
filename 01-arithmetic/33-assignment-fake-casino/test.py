import time
time.sleep(10)
import pytest
import student

@pytest.mark.parametrize("n, expected_result", [
    (6, ["6", "1", "1", "6", "3"]),
    (20, ["4", "1", "9", "8", "8"])
])
def test_fake_casino_prints_expected_sequence(capsys, n, expected_result):
    # Clear import-time prints
    capsys.readouterr()

    # Call our function
    student.fake_casino(n)

    actual_result = capsys.readouterr().out.strip().splitlines()
    assert actual_result == expected_result

def test_fake_casino_returns_none(capsys):
    # Clear import-time prints
    capsys.readouterr()

    result = student.fake_casino(6)

    # Discard output; we're only checking the return value here
    capsys.readouterr()

    assert result is None, "fake_casino(n) should only print the sequence, not return a value."
