import pytest
from application.app import app
from flask import json

@pytest.fixture
def client():
    """A test client for the Flask application."""
    with app.test_client() as client:
        yield client


def test_app_initialization():
    """Test that the Flask app is initialized correctly."""
    assert app is not None


def test_views_import():
    """Test that the views module is imported without errors."""
    try:
        import application.app.views
    except ImportError:
        pytest.fail("Failed to import views module")


def test_index_view(client):
    """Test the index view to ensure it renders the index.html template with the correct title."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Home</title>' in response.data
    assert b'<!DOCTYPE html>' in response.data


def test_test_script_view(client):
    """Test the test_script view to ensure it renders the test_script.html template."""
    response = client.get('/test_script.html')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    assert b'test_script' in response.data


def test_fib_usage_view(client):
    """Test the fib_usage view to ensure it renders the usage.html template."""
    response = client.get('/fib/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    assert b'usage' in response.data


def test_myFib(client):
    """Test the myFib view to ensure it handles various inputs correctly."""
    # Test valid input
    response = client.get('/fib/10')
    assert response.status_code == 200
    assert b'First 10 Fibonacci numbers' in response.data

    # Test invalid input (non-integer)
    response = client.get('/fib/abc')
    assert response.status_code == 200
    assert b'Could not interpret abc as an integer' in response.data

    # Test negative integer
    response = client.get('/fib/-5')
    assert response.status_code == 200
    assert b'Invalid input. -5 must be a positive integer' in response.data

    # Test input exceeding 10,000
    response = client.get('/fib/10001')
    assert response.status_code == 200
    assert b'Truncated output after 10000 numbers' in response.data


@pytest.mark.parametrize('input_value, expected_output', [
    (0, {'sum_of_fibonacci': 0}),
    (1, {'sum_of_fibonacci': 0}),
    (2, {'sum_of_fibonacci': 1}),
    (3, {'sum_of_fibonacci': 2}),
    (4, {'sum_of_fibonacci': 4}),
    (5, {'sum_of_fibonacci': 7}),
    (10, {'sum_of_fibonacci': 54}),
])
def test_fibonacci_sum_valid(client, input_value, expected_output):
    """Test the fibonacci_sum function with valid inputs."""
    response = client.get(f'/fibonacci/sum/{input_value}')
    assert response.status_code == 200
    assert json.loads(response.data) == expected_output

@pytest.mark.parametrize('input_value, expected_output', [
    ('foo', {'error': 'Invalid input'}),
    ('-1', {'error': 'Invalid input'}),
    ('3.5', {'error': 'Invalid input'}),
])
def test_fibonacci_sum_invalid_input(client, input_value, expected_output):
    """Test the fibonacci_sum function with invalid inputs."""
    response = client.get(f'/fibonacci/sum/{input_value}')
    assert response.status_code == 400
    assert json.loads(response.data) == expected_output


def test_fibonacci_sum_negative_input(client):
    """Test the fibonacci_sum function with negative input."""
    response = client.get('/fibonacci/sum/-10')
    assert response.status_code == 400
    assert json.loads(response.data) == {'error': 'Invalid input'}


def test_fibonacci_sum_large_input(client):
    """Test the fibonacci_sum function with input exceeding 10,000."""
    response = client.get('/fibonacci/sum/10001')
    assert response.status_code == 400
    assert json.loads(response.data) == {'error': 'Input exceeds maximum limit'}
