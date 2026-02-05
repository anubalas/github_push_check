import fibonacci_module as fb
import pytest
from unittest.mock import patch, mock_open
import os

####    Tests for Fibonacci Numbers    ####

def test_fibList():
    """Test the fibList function with various inputs."""
    print("Sample inputs for list of Fibonacci numbers")
    assert fb.fibList(0) == []
    assert fb.fibList(1) == [0]
    assert fb.fibList(2) == [0, 1]
    assert fb.fibList(3) == [0, 1, 1]
    assert fb.fibList(5) == [0, 1, 1, 2, 3]
    assert fb.fibList(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    assert fb.fibList(100)  # Add more assertions as needed

def test_fibList_invalid_input():
    """Test the fibList function with invalid inputs."""
    print("Intentionally using invalid inputs")
    with pytest.raises(ValueError):
        fb.fibList(-1)  # Expected: ValueError
    with pytest.raises(TypeError):
        fb.fibList("foo")  # Expected: TypeError


def test_is_square():
    """Test the is_square function with various inputs."""
    print("Tests for is_square function:")
    testList = [0, 1, 2, 3, 4, 8, 9, 16, 25.0, 120.9999999, 1e4, -1, -4, "string", None]
    print("  Number   Perfect Square?")
    for val in testList:
        try:
            result = fb.is_square(val)
            print("  ", val, "      ", result)
        except Exception as e:
            print("  ", val, "      Exception raised:", e)


def test_is_fibonacci():
    """Test the is_fibonacci function with various inputs."""
    print("Tests for is_fibonacci function:")
    testList = [
        (0, "Y"), (1, "Y"), (2, "Y"), (3, "Y"), (4, "N"),
        (5, "Y"), (12, "N"), (13, "Y"), (42, "N"), (144, "Y"),
        (63245986,"Y"), (102334155, "Y"), (218922995834555169026, "Y")
    ]
    print("  Number   Fibonacci?   Expected")
    for val in testList:
        assert fb.is_fibonacci(val[0]) == (val[1] == "Y")
        print("  ", val[0], "      ", fb.is_fibonacci(val[0]), "      ", val[1])
        if (val[0] == 63245986):
            print("     (Now exceeds numerical precision)")


def test_binet_formula():
    """Test Binet's formula for Fibonacci numbers."""
    print("Tests for Binet's Formula:")
    testList = [
        (0, 1), (1, 1), (2, 2), (3, 3), (4, 4),
        (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
        (10, 10), (11, 11), (12, 12), (13, 13), (14, 14),
        (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)
    ]
    print("  Number   Fibonacci?   Nearest n   Nearest fib   n range")
    for val in testList:
        nrange = fb.n_Binet(val[0])
        assert round(nrange[0]) == val[1]
        print("  ", val[0], "      ", val[1], "      ", round(nrange[0]), "      ", fb.nearest_Binet_fib(val[0]), "      ", nrange)


def test_n_Binet_edge_cases():
    """Test the n_Binet function with edge cases and large integers."""
    edge_cases = [
        (0, (1, 1)),  # 0 is the first Fibonacci number
        (1, (1, 1)),  # 1 is the second Fibonacci number
        (2, (2, 2)),  # 2 is the third Fibonacci number
        (3, (3, 3)),  # 3 is the fourth Fibonacci number
        (4, (4, 4)),  # 4 is not a Fibonacci number
        (5, (5, 5)),  # 5 is the fifth Fibonacci number
        (1000000000000000000, (None, None)),  # Large non-Fibonacci number
        (5702887, (None, None)),  # Large Fibonacci number
        (9227465, (None, None)),  # Large Fibonacci number
        (100000000000000000000, (None, None)),  # Very large non-Fibonacci number
    ]
    print("Tests for n_Binet function edge cases:")
    for val in edge_cases:
        result = fb.n_Binet(val[0])
        assert result == val[1]
        print("  ", val[0], "      ", result, "      ", val[1])


def test_nearest_Binet_fib():
    """Test the nearest_Binet_fib function with various inputs."""
    print("Testing nearest_Binet_fib function")
    # Valid Fibonacci numbers
    assert fb.nearest_Binet_fib(0) == 0  # Nearest Fibonacci to 0 is 0
    assert fb.nearest_Binet_fib(1) == 1  # Nearest Fibonacci to 1 is 1
    assert fb.nearest_Binet_fib(2) == 2  # Nearest Fibonacci to 2 is 2
    assert fb.nearest_Binet_fib(3) == 3  # Nearest Fibonacci to 3 is 3
    assert fb.nearest_Binet_fib(5) == 5  # Nearest Fibonacci to 5 is 5
    assert fb.nearest_Binet_fib(8) == 8  # Nearest Fibonacci to 8 is 8
    assert fb.nearest_Binet_fib(13) == 13  # Nearest Fibonacci to 13 is 13
    assert fb.nearest_Binet_fib(21) == 21  # Nearest Fibonacci to 21 is 21
    assert fb.nearest_Binet_fib(34) == 34  # Nearest Fibonacci to 34 is 34
    assert fb.nearest_Binet_fib(55) == 55  # Nearest Fibonacci to 55 is 55

    # Invalid Fibonacci numbers
    assert fb.nearest_Binet_fib(4) == 3  # Nearest Fibonacci to 4 is 3
    assert fb.nearest_Binet_fib(6) == 5  # Nearest Fibonacci to 6 is 5
    assert fb.nearest_Binet_fib(7) == 8  # Nearest Fibonacci to 7 is 8
    assert fb.nearest_Binet_fib(9) == 8  # Nearest Fibonacci to 9 is 8
    assert fb.nearest_Binet_fib(10) == 8  # Nearest Fibonacci to 10 is 8
    assert fb.nearest_Binet_fib(12) == 13  # Nearest Fibonacci to 12 is 13

    # Edge cases with large integers
    assert fb.nearest_Binet_fib(144) == 144  # Nearest Fibonacci to 144 is 144
    assert fb.nearest_Binet_fib(233) == 233  # Nearest Fibonacci to 233 is 233
    assert fb.nearest_Binet_fib(377) == 377  # Nearest Fibonacci to 377 is 377
    assert fb.nearest_Binet_fib(1000) == 987  # Nearest Fibonacci to 1000 is 987
    assert fb.nearest_Binet_fib(100000) == 10946  # Nearest Fibonacci to 100000 is 10946
    assert fb.nearest_Binet_fib(1000000000) == 1346269  # Nearest Fibonacci to 1 billion is 1346269

@patch('builtins.open', new_callable=mock_open)
@patch('os.path.isfile')
def test_make_saved_Fibonacci_file_creates_file(mock_isfile, mock_open):
    """Test that make_saved_Fibonacci_file creates a binary file if it does not exist."""
    mock_isfile.return_value = False  # Simulate that the file does not exist
    fb.make_saved_Fibonacci_file()
    mock_open.assert_called_once_with('savedFibonacciNumbers.bin', 'wb')

@patch('builtins.open', new_callable=mock_open)
@patch('os.path.isfile')
def test_make_saved_Fibonacci_file_does_not_overwrite(mock_isfile, mock_open):
    """Test that make_saved_Fibonacci_file does not overwrite if the file exists."""
    mock_isfile.return_value = True  # Simulate that the file exists
    fb.make_saved_Fibonacci_file()
    mock_open.assert_not_called()

@patch('builtins.open', new_callable=mock_open)
@patch('os.path.isfile')
def test_make_saved_Fibonacci_file_handles_creation_error(mock_isfile, mock_open):
    """Test that make_saved_Fibonacci_file handles file creation errors appropriately."""
    mock_isfile.return_value = False  # Simulate that the file does not exist
    mock_open.side_effect = IOError("File creation error")  # Simulate an IOError
    with pytest.raises(IOError):
        fb.make_saved_Fibonacci_file()

@patch('builtins.open', new_callable=mock_open)
@patch('os.path.isfile')
def test_get_nth_saved_Fibonacci_number_valid_index(mock_isfile, mock_open):
    """Test get_nth_saved_Fibonacci_number with valid index."""
    mock_isfile.return_value = True  # Simulate that the file exists
    mock_open.return_value.read.side_effect = [b'0', b'1', b'1', b'2', b'3']  # Simulate file content
    assert fb.get_nth_saved_Fibonacci_number(1) == 0
    assert fb.get_nth_saved_Fibonacci_number(2) == 1
    assert fb.get_nth_saved_Fibonacci_number(3) == 1
    assert fb.get_nth_saved_Fibonacci_number(4) == 2
    assert fb.get_nth_saved_Fibonacci_number(5) == 3

@patch('builtins.open', new_callable=mock_open)
@patch('os.path.isfile')
def test_get_nth_saved_Fibonacci_number_out_of_bounds(mock_isfile, mock_open):
    """Test get_nth_saved_Fibonacci_number with out-of-bounds index."""
    mock_isfile.return_value = True  # Simulate that the file exists
    mock_open.return_value.read.side_effect = [b'0', b'1', b'1', b'2', b'3']  # Simulate file content
    with pytest.raises(ValueError):
        fb.get_nth_saved_Fibonacci_number(6)  # Index exceeds saved Fibonacci numbers

@patch('builtins.open', new_callable=mock_open)
@patch('os.path.isfile')
def test_get_nth_saved_Fibonacci_number_invalid_input(mock_isfile, mock_open):
    """Test get_nth_saved_Fibonacci_number with invalid input."""
    with pytest.raises(ValueError):
        fb.get_nth_saved_Fibonacci_number(0)  # Invalid index (0 is not valid)
    with pytest.raises(ValueError):
        fb.get_nth_saved_Fibonacci_number(-1)  # Invalid index (negative)
