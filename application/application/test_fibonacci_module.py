import pytest
import fibonacci_module as fb
from unittest.mock import patch, mock_open

@pytest.mark.parametrize('n, expected', [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (20, 6765),
    (30, 832040),
    (50, 12586269025),
])
def test_get_nth_fibonacci_valid(n, expected):
    """Test get_nth_fibonacci for valid indices."""
    result = fb.get_nth_fibonacci(n)
    assert result == expected

@pytest.mark.parametrize('n', [
    -1,
    -5,
    None,
    'a',
])
def test_get_nth_fibonacci_invalid(n):
    """Test get_nth_fibonacci with invalid inputs."""
    with pytest.raises(ValueError):
        fb.get_nth_fibonacci(n)

@pytest.mark.parametrize('n, expected', [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (20, 6765),
    (30, 832040),
    (50, 12586269025),
])
def test_f_binet(nth, expected):
    """Test f_binet function for valid Fibonacci indices."""
    result = fb.f_Binet(nth)
    assert result == expected

@pytest.mark.parametrize('n', [
    0,
])
def test_f_binet_zero(n):
    """Test f_binet function for input 0."""
    with pytest.raises(ValueError):
        fb.f_Binet(n)

@pytest.mark.parametrize('n', [
    -1,
    -5,
    -10,
])
def test_f_binet_negative(n):
    """Test f_binet function for negative indices."""
    with pytest.raises(ValueError):
        fb.f_Binet(n)

@pytest.mark.parametrize('n', [
    None,
    'a',
    1.5,
])
def test_f_binet_invalid(n):
    """Test f_binet function for invalid inputs."""
    with pytest.raises(TypeError):
        fb.f_Binet(n)

@pytest.mark.parametrize('input, expected', [
    (1, 1),  # Closest Fibonacci number to 1 is 1
    (2, 2),  # Closest Fibonacci number to 2 is 2
    (3, 3),  # Closest Fibonacci number to 3 is 3
    (4, 3),  # Closest Fibonacci number to 4 is 3
    (5, 5),  # Closest Fibonacci number to 5 is 5
    (6, 5),  # Closest Fibonacci number to 6 is 5
    (7, 8),  # Closest Fibonacci number to 7 is 8
    (8, 8),  # Closest Fibonacci number to 8 is 8
    (9, 8),  # Closest Fibonacci number to 9 is 8
    (10, 8), # Closest Fibonacci number to 10 is 8
    (11, 13),# Closest Fibonacci number to 11 is 13
    (12, 13),# Closest Fibonacci number to 12 is 13
    (0, 0),  # Edge case for input 0
])
def test_nearest_binet_fib(input, expected):
    """Test nearest_Binet_fib function for various inputs."""
    result = fb.nearest_Binet_fib(input)
    assert result == expected

@pytest.mark.parametrize('input', [
    -1,
    -5,
    None,
    'a',
    1.5,
])
def test_nearest_binet_fib_invalid(input):
    """Test nearest_Binet_fib with invalid inputs."""
    with pytest.raises(ValueError):
        fb.nearest_Binet_fib(input)

@pytest.mark.parametrize('num, expected', [
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (4, [0, 1, 1, 2]),
    (5, [0, 1, 1, 2, 3]),
    (6, [0, 1, 1, 2, 3, 5]),
    (7, [0, 1, 1, 2, 3, 5, 8]),
    (8, [0, 1, 1, 2, 3, 5, 8, 13]),
])
def test_fibList_valid(num, expected):
    """Test fibList function for valid positive integer inputs."""
    result = fb.fibList(num)
    assert result == expected

@pytest.mark.parametrize('num', [
    -1,
    -5,
    -10,
])
def test_fibList_negative(num):
    """Test fibList function for negative integer inputs."""
    result = fb.fibList(num)
    assert result == []

@pytest.mark.parametrize('num', [
    None,
    'a',
    1.5,
])
def test_fibList_invalid(num):
    """Test fibList function for non-integer inputs."""
    with patch('builtins.print') as mock_print:
        result = fb.fibList(num)
        mock_print.assert_called_once_with("Please enter a positive integer for the number of Fibonacci numbers to generate.")
        assert result == []

@pytest.mark.parametrize('num, expected', [
    (0, True),
    (1, True),
    (4, True),
    (9, True),
    (16, True),
    (25, True),
    (2, False),
    (3, False),
    (5, False),
    (10, False),
])
def test_is_square(num, expected):
    """Test is_square function for valid inputs."""
    result = fb.is_square(num)
    assert result == expected

@pytest.mark.parametrize('num', [
    -1,
    -4,
    -9,
])
def test_is_square_negative(num):
    """Test is_square function for negative inputs."""
    with pytest.raises(ValueError):
        fb.is_square(num)

@pytest.mark.parametrize('num', [
    None,
    'a',
    1.5,
])
def test_is_square_invalid(num):
    """Test is_square function for invalid inputs."""
    with pytest.raises(TypeError):
        fb.is_square(num)

@pytest.mark.parametrize('num, expected', [
    (0, True),
    (1, True),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, False),
    (8, True),
    (13, True),
    (21, True),
    (34, True),
    (35, False),
])
def test_is_fibonacci(num, expected):
    """Test is_fibonacci function for valid inputs."""
    result = fb.is_fibonacci(num)
    assert result == expected

@pytest.mark.parametrize('num', [
    -1,
    -5,
    -10,
])
def test_is_fibonacci_negative(num):
    """Test is_fibonacci function for negative inputs."""
    with pytest.raises(ValueError):
        fb.is_fibonacci(num)

@pytest.mark.parametrize('num', [
    None,
    'a',
    1.5,
])
def test_is_fibonacci_invalid(num):
    """Test is_fibonacci function for invalid inputs."""
    with pytest.raises(TypeError):
        fb.is_fibonacci(num)

@pytest.mark.parametrize('input, expected', [
    (0, (1, 1)),
    (1, (1, 1)),
    (2, (2, 2)),
    (3, (3, 3)),
    (5, (5, 5)),
    (8, (6, 6)),
    (13, (7, 7)),
])
def test_n_binet_valid(input, expected):
    """Test n_Binet function for valid Fibonacci number inputs."""
    result = fb.n_Binet(input)
    assert result == expected

@pytest.mark.parametrize('input', [
    -1,
    -5,
    -10,
])
def test_n_binet_negative(input):
    """Test n_Binet function for negative inputs."""
    with pytest.raises(ValueError):
        fb.n_Binet(input)

@pytest.mark.parametrize('input', [
    None,
    'a',
    1.5,
])
def test_n_binet_invalid(input):
    """Test n_Binet function for invalid inputs."""
    with pytest.raises(TypeError):
        fb.n_Binet(input)

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize('x, m, b, expected', [
    (0, 1, 0, 0),
    (1, 1, 0, 1),
    (1, 2, 3, 5),
    (2, 2, 2, 6),
    (3, -1, 5, 2),
    (10, 0, 5, 5),
    (0, 0, 0, 0),
    (-1, 1, 1, 0),
    (-5, 2, 3, -7),
])
def test_fitLogPrediction(x, m, b, expected):
    """Test the fitLogPrediction function with various inputs."""
    result = fitLogPrediction(x, m, b)
    assert result == expected

@pytest.mark.parametrize('x, m, b', [
    (None, 1, 1),
    (1, None, 1),
    (1, 1, None),
])
def test_fitLogPrediction_invalid_input(x, m, b):
    """Test fitLogPrediction with invalid inputs."""
    with pytest.raises(TypeError):
        fitLogPrediction(x, m, b)

@pytest.mark.parametrize('x, m, b, expected', [
    (0, 0, 0, 1),
    (1, 0, 0, 1),
    (1, 1, 0, 2),
    (2, 1, 1, 3),
    (3, 1, 1, 5),
    (4, 1, 2, 8),
    (5, 1, 3, 13),
])
def test_fitFibPrediction(x, m, b, expected):
    """Test the fitFibPrediction function with various inputs."""
    result = fitFibPrediction(x, m, b)
    assert result == expected

@pytest.mark.parametrize('x, m, b', [
    (None, 1, 1),
    (1, None, 1),
    (1, 1, None),
])
def test_fitFibPrediction_invalid_input(x, m, b):
    """Test fitFibPrediction with invalid inputs."""
    with pytest.raises(TypeError):
        fitFibPrediction(x, m, b)

# Additional tests for other functions can be added here.

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

@pytest.mark.parametrize('value, expected', [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (20, 6765),
    (30, 832040),
    (50, 12586269025),
])
def test_nearest_saved_fib(value, expected):
    """Test nearest_saved_fib function with various noisy inputs."""
    result = fb.nearest_saved_fib(value)
    assert result == expected

@pytest.mark.parametrize('value', [
    None,
    -1,
    1000,
])
def test_nearest_saved_fib_invalid(value):
    """Test nearest_saved_fib with invalid inputs."""
    with pytest.raises(ValueError):
        fb.nearest_saved_fib(value)

@pytest.mark.parametrize('num, expected', [
    (1, 1),
    (2, 2),
    (3, 3),
    (10, 10),
])
def test_ensure_positive_int_valid(num, expected):
    """Test ensure_positive_int with valid positive integers."""
    result = fb.ensure_positive_int(num)
    assert result == expected

@pytest.mark.parametrize('num', [
    -1,
    -10,
    -5,
])
def test_ensure_positive_int_negative(num):
    """Test ensure_positive_int with negative integers."""
    with pytest.raises(ValueError):
        fb.ensure_positive_int(num)

@pytest.mark.parametrize('num', [
    None,
    'string',
    1.5,
])
def test_ensure_positive_int_non_integer(num):
    """Test ensure_positive_int with non-integer inputs."""
    with pytest.raises(ValueError):
        fb.ensure_positive_int(num)

@pytest.mark.parametrize('n, expected', [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (20, 6765),
    (30, 832040),
    (50, 12586269025),
])
def test_sum_of_fibonacci_valid(n, expected):
    """Test sum_of_fibonacci for valid non-negative integers."""
    result = fb.sum_of_fibonacci(n)
    assert result == expected

@pytest.mark.parametrize('n', [
    -1,
    -5,
    None,
    'a',
])
def test_sum_of_fibonacci_invalid(n):
    """Test sum_of_fibonacci with invalid inputs."""
    with pytest.raises(ValueError):
        fb.sum_of_fibonacci(n)
