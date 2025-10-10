import time
time.sleep(10)
import pytest
import student

@pytest.mark.parametrize("n, expected_result", [
    (10, ["6.8", "1.2", "3.5", "3.0", "7.6"]),
    (20, ["13.1", "1.5", "6.2", "5.2", "15.0"])
])
def test_fake_casino_revisited_prints_expected_sequence(capsys, n, expected_result):
    # Clear import-time prints
    capsys.readouterr()

    # Call our function
    student.fake_casino_revisited(n)

    actual_result = capsys.readouterr().out.strip().splitlines()
    assert actual_result == expected_result

def test_fake_casino_revisited_returns_none(capsys):
    # Clear import-time prints
    capsys.readouterr()

    result = student.fake_casino_revisited(10)

    # Discard output; we're only checking the return value here
    capsys.readouterr()

    assert result is None, "fake_casino(n) should only print the sequence, not return a value."
