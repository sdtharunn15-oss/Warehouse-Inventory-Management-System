from pydantic import BaseModel, EmailStr


# User Schemas

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


# Login

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# Product

class ProductCreate(BaseModel):
    product_name: str
    sku: str
    category: str
    price: float
    stock_quantity: int


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True


# Supplier

class SupplierCreate(BaseModel):
    supplier_name: str
    email: EmailStr
    phone: str


class SupplierResponse(SupplierCreate):
    id: int

    class Config:
        from_attributes = True


# Stock

class StockRequest(BaseModel):
    product_id: int
    quantity: int


class StockHistoryResponse(BaseModel):
    id: int
    product_id: int
    movement_type: str
    quantity: int

    class Config:
        from_attributes = True