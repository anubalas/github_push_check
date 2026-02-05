import pytest
from unittest.mock import patch
from application.run import app


@pytest.fixture
def client():
    """A test client for the Flask application."""
    with app.test_client() as client:
        yield client


def test_run_with_debug(client):
    """Test that the Flask app runs in debug mode."""
    with patch('application.run.app.run') as mock_run:
        app.run(debug=True)
        mock_run.assert_called_once_with(debug=True)


def test_run_without_debug(client):
    """Test that the Flask app runs without debug mode."""
    with patch('application.run.app.run') as mock_run:
        app.run(debug=False)
        mock_run.assert_called_once_with(debug=False)
