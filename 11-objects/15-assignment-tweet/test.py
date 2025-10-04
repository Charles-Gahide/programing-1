import time
time.sleep(10)
import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("message, max_length", [
    (message, max_length)
    for message in ['', 'abc', 'abcdefghijklmnop']
    for max_length in range(1, 20)
])
def test_valid_initialization(message, max_length):
    tweet = student.Tweet(message, max_length)

    assert tweet.get_message() == message[:max_length]
    assert tweet.get_max_length() == max_length


@pytest.mark.timeout(1)
def test_initialization_with_invalid_max_length():
    with pytest.raises(ValueError):
        student.Tweet('abc', -1)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("message", [
    "",
    "abc",
    "abcdefghijklmnop",
])
@pytest.mark.parametrize("max_length", [
    1,
    5,
    10,
    200
])
def test_set_message(message, max_length):
    # Arrange
    tweet = student.Tweet('', max_length)

    # Act
    tweet.set_message(message)

    # Assert
    assert tweet.get_message() == message[:max_length]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("message", [
    "",
    "abc",
    "abcdefghijklmnop",
])
@pytest.mark.parametrize("max_length", [
    1,
    5,
    10,
    200
])
def test_set_max_length(message, max_length):
    # Arrange
    tweet = student.Tweet(message, 100)

    # Act
    tweet.set_max_length(max_length)

    # Assert
    assert tweet.get_max_length() == max_length
    assert tweet.get_message() == message[:max_length]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("max_length", [-10, -1, 0])
def test_set_invalid_max_length(max_length):
    tweet = student.Tweet("abc", 10)

    with pytest.raises(ValueError):
        tweet.set_max_length(max_length)
