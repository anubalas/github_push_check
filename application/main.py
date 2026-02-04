from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
import enum

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)

class InventoryOperationType(enum.Enum):
    add = "add"
    remove = "remove"

class InventoryOperation(Base):
    __tablename__ = "inventory_operations"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    operation_type = Column(Enum(InventoryOperationType), nullable=False)
    number_of_products = Column(Integer, nullable=False)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    actual_count = Column(Integer, nullable=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Pydantic models
class ProductCreate(BaseModel):
    name: str
    price: float
    description: str = None

class ProductUpdate(BaseModel):
    name: str
    price: float

class InventoryOperationCreate(BaseModel):
    product_id: int
    operation_type: InventoryOperationType
    number_of_products: int

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Product API endpoints
@app.post("/products")
def create_product(product: ProductCreate, db: Session = next(get_db())):
    db_product = Product(**product.dict())
    db.add(db_product)
    try:
        db.commit()
        db.refresh(db_product)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Product already exists")
    return db_product

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = next(get_db())):
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}

@app.put("/products/{id}")
def update_product(id: int, product: ProductUpdate, db: Session = next(get_db())):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    return db_product

@app.get("/products")
def read_products(skip: int = 0, limit: int = 10, db: Session = next(get_db())):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@app.get("/products/{id}")
def read_product(id: int, db: Session = next(get_db())):
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Inventory Operation API endpoint
@app.post("/inventory/operations")
def create_inventory_operation(operation: InventoryOperationCreate, db: Session = next(get_db())):
    product = db.query(Product).filter(Product.id == operation.product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    inventory = db.query(Inventory).filter(Inventory.product_id == operation.product_id).first()
    if operation.operation_type == InventoryOperationType.add:
        if inventory:
            inventory.actual_count += operation.number_of_products
        else:
            new_inventory = Inventory(product_id=operation.product_id, actual_count=operation.number_of_products)
            db.add(new_inventory)
    elif operation.operation_type == InventoryOperationType.remove:
        if inventory and inventory.actual_count >= operation.number_of_products:
            inventory.actual_count -= operation.number_of_products
        else:
            raise HTTPException(status_code=400, detail="Not enough inventory to remove")
    db_operation = InventoryOperation(**operation.dict())
    db.add(db_operation)
    db.commit()
    return db_operation

# Inventory API endpoint
@app.get("/inventory")
def read_inventory(db: Session = next(get_db())):
    inventories = db.query(Inventory).all()
    return inventories
