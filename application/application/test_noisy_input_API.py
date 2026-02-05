import pytest
from unittest.mock import patch
import noisy_input_API as noisy_api


@pytest.mark.parametrize('input_value, expected_length', [
    (5, 5),
    (10, 10),
    (20, 20)
])
def test_get_data(input_value, expected_length):
    """Test the get_data function for various input values."""
    with patch('noisy_input_API.add_noise') as mock_add_noise:
        mock_add_noise.return_value = [1, 1, 1, 1, 1]  # Mocked output
        result = noisy_api.get_data(input_value)
        assert len(result) == expected_length


@pytest.mark.parametrize('input_data, expected_length', [
    ([0, 1, 1, 2, 3, 5], 6),  # Standard Fibonacci numbers
    ([], 0),  # Empty list
    ([1, 'a', 2.5, None], 3),  # Non-numeric values
    (10, 10),  # Valid input for how_much
    (0, 0),  # Edge case for zero
    (-5, 0),  # Edge case for negative values
    (100, 20)  # Exceeding available Fibonacci numbers
])
def test_get_data_edge_cases(input_data, expected_length):
    """Test the get_data function for edge cases."""
    if isinstance(input_data, int) and input_data < 0:
        with pytest.raises(ValueError):
            noisy_api.get_data(input_data)
    else:
        with patch('noisy_input_API.add_noise') as mock_add_noise:
            mock_add_noise.return_value = [1] * expected_length  # Mocked output
            result = noisy_api.get_data(input_data)
            assert len(result) == expected_length


@pytest.mark.parametrize('input_data, expected_length', [
    ([0, 1, 1, 2, 3, 5], 6),  # Standard Fibonacci numbers
    ([], 0),  # Empty list
    ([1, 'a', 2.5, None], 3)  # Non-numeric values
])
def test_add_noise(input_data, expected_length):
    """Test the add_noise function with various input scenarios."""
    if input_data:
        noisy_data = noisy_api.add_noise(input_data)
        assert len(noisy_data) == expected_length
        for original, noisy in zip(input_data, noisy_data):
            assert noisy != original  # Check that noise has been added
    else:
        noisy_data = noisy_api.add_noise(input_data)
        assert len(noisy_data) == expected_length
