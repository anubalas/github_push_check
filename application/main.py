from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel
import enum

# Database setup
DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# CORS configuration
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database models
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)

class InventoryOperationType(enum.Enum):
    add = "add"
    remove = "remove"

class InventoryOperation(Base):
    __tablename__ = "inventory_operation"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    product_id = Column(Integer, ForeignKey("product.id"))
    operation_type = Column(Enum(InventoryOperationType), nullable=False)
    number_of_products = Column(Integer, nullable=False)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    actual_count = Column(Integer, nullable=False)

Base.metadata.create_all(bind=engine)

# Pydantic models
class ProductCreate(BaseModel):
    name: str
    price: float
    description: str = None

class ProductUpdate(BaseModel):
    id: int
    name: str = None
    price: float = None
    description: str = None

class InventoryOperationCreate(BaseModel):
    product_id: int
    operation_type: InventoryOperationType
    number_of_products: int

# API Endpoints
@app.post("/products/", response_model=Product)
def add_product(product: ProductCreate):
    db = SessionLocal()
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()
    return db_product

@app.delete("/products/{product_id}")
def remove_product(product_id: int):
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        db.close()
        return {"message": "Product removed successfully."}
    db.close()
    return {"message": "Product not found."}

@app.put("/products/", response_model=Product)
def edit_product(product: ProductUpdate):
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product.id).first()
    if db_product:
        if product.name:
            db_product.name = product.name
        if product.price:
            db_product.price = product.price
        if product.description:
            db_product.description = product.description
        db.commit()
        db.refresh(db_product)
        db.close()
        return db_product
    db.close()
    return {"message": "Product not found."}

@app.post("/inventory/operations/", response_model=dict)
def perform_inventory_operation(operation: InventoryOperationCreate):
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == operation.product_id).first()
    if not db_product:
        db.close()
        return {"message": "Product not found."}
    # Logic to update inventory and log operation
    db.close()
    return {"message": "Operation performed successfully."}

@app.get("/inventory/", response_model=list)
def get_inventory():
    db = SessionLocal()
    inventory = db.query(Inventory).all()
    db.close()
    return inventory
