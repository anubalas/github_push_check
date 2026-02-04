"""
Unit tests for the create_product, delete_product, update_product, read_products, read_product, create_inventory_operation, and read_inventory functions in main.py.
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from application.main import app, ProductCreate, ProductUpdate, Product, InventoryOperationCreate, InventoryOperationType, Inventory

@pytest.fixture
def client():
    """Create a TestClient for the FastAPI app."""
    return TestClient(app)

@pytest.fixture
def mock_db():
    """Mock the database session for testing."""
    with patch('application.main.SessionLocal') as mock:
        yield mock

@pytest.mark.parametrize("product_data, expected_status, expected_detail", [
    ({"name": "Test Product", "price": 10.0}, 201, None),
    ({"name": "", "price": 10.0}, 422, "field required"),
    ({"name": "Test Product", "price": -5.0}, 422, "value is not a valid float"),
])
def test_create_product(client, mock_db, product_data, expected_status, expected_detail):
    """Test creating a product with various inputs."""
    mock_db.return_value.__enter__.return_value.commit = MagicMock()
    mock_db.return_value.__enter__.return_value.refresh = MagicMock()
    response = client.post("/products", json=product_data)
    assert response.status_code == expected_status
    if expected_detail:
        assert expected_detail in response.json()["detail"]

@pytest.mark.parametrize("product_id, expected_status, expected_detail", [
    (1, 200, None),
    (999, 404, "Product not found"),
])
def test_read_product(client, mock_db, product_id, expected_status, expected_detail):
    """Test reading a product by ID."""
    mock_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first = \
        MagicMock(return_value=Product(id=1, name="Test Product", price=10.0) if product_id == 1 else None)
    response = client.get(f"/products/{product_id}")
    assert response.status_code == expected_status
    if expected_detail:
        assert expected_detail in response.json()["detail"]

@pytest.mark.parametrize("skip, limit, expected_count", [
    (0, 10, 2),
    (1, 1, 1),
    (0, 0, 0),
])
def test_read_products(client, mock_db, skip, limit, expected_count):
    """Test reading products with pagination."""
    mock_db.return_value.__enter__.return_value.query.return_value.offset.return_value.limit.return_value.all = \
        MagicMock(return_value=[Product(id=1, name="Product 1", price=10.0), Product(id=2, name="Product 2", price=20.0)][skip:skip+limit])
    response = client.get(f"/products?skip={skip}&limit={limit}")
    assert response.status_code == 200
    assert len(response.json()) == expected_count

@pytest.mark.parametrize("product_id, product_data, expected_status, expected_detail", [
    (1, {"name": "Updated Product", "price": 15.0}, 200, None),
    (999, {"name": "Updated Product", "price": 15.0}, 404, "Product not found"),
])
def test_update_product(client, mock_db, product_id, product_data, expected_status, expected_detail):
    """Test updating a product with various inputs."""
    mock_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first = \
        MagicMock(return_value=Product(id=1, name="Test Product", price=10.0) if product_id == 1 else None)
    mock_db.return_value.__enter__.return_value.commit = MagicMock()
    response = client.put(f"/products/{product_id}", json=product_data)
    assert response.status_code == expected_status
    if expected_detail:
        assert expected_detail in response.json()["detail"]

@pytest.mark.parametrize("product_id, expected_status, expected_detail", [
    (1, 204, None),
    (999, 404, "Product not found"),
])
def test_delete_product(client, mock_db, product_id, expected_status, expected_detail):
    """Test deleting a product by ID."""
    mock_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first = \
        MagicMock(return_value=Product(id=1, name="Test Product", price=10.0) if product_id == 1 else None)
    mock_db.return_value.__enter__.return_value.commit = MagicMock()
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == expected_status
    if expected_detail:
        assert expected_detail in response.json()["detail"]

@pytest.mark.parametrize("operation_data, expected_status, expected_detail", [
    ({"product_id": 1, "operation_type": "add", "number_of_products": 5}, 200, None),
    ({"product_id": 999, "operation_type": "add", "number_of_products": 5}, 404, "Product not found"),
    ({"product_id": 1, "operation_type": "remove", "number_of_products": 10}, 400, "Not enough inventory to remove"),
])
def test_create_inventory_operation(client, mock_db, operation_data, expected_status, expected_detail):
    """Test creating an inventory operation with various inputs."""
    mock_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first = \
        MagicMock(return_value=Product(id=1, name="Test Product", price=10.0) if operation_data["product_id"] == 1 else None)
    mock_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first = \
        MagicMock(return_value=Inventory(actual_count=5) if operation_data["operation_type"] == "remove" else None)
    mock_db.return_value.__enter__.return_value.commit = MagicMock()
    response = client.post("/inventory/operations", json=operation_data)
    assert response.status_code == expected_status
    if expected_detail:
        assert expected_detail in response.json()["detail"]

@pytest.mark.parametrize("expected_status, expected_detail", [
    (200, None),
    (204, None),
])
def test_read_inventory(client, mock_db, expected_status, expected_detail):
    """Test reading inventory records."""
    mock_db.return_value.__enter__.return_value.query.return_value.all = \
        MagicMock(return_value=[Inventory(product_id=1, actual_count=10), Inventory(product_id=2, actual_count=5)])
    response = client.get("/inventory")
    assert response.status_code == expected_status
    if expected_detail:
        assert expected_detail in response.json()["detail"]
