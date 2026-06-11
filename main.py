from fastapi import FastAPI
from app.database import Base, engine
import app.models

from app.routers import auth, products, suppliers, stock

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Warehouse Inventory Management System",
    description="""
Warehouse Inventory Backend System

Features:
- Authentication
- Product Management
- Supplier Management
- Stock Tracking
- Role Based Authorization
- Pagination
- Category Filtering
- Low Stock Alerts
""",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(suppliers.router)
app.include_router(stock.router)


@app.get("/")
def root():
    return {
        "message": "Warehouse Inventory Management System Running Successfully"
    }