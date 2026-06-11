Warehouse Inventory Management System

Project Overview

The Warehouse Inventory Management System is a backend application built using FastAPI. It provides secure authentication, product management, supplier management, stock tracking, and inventory monitoring functionalities. The system supports role-based access control using JWT authentication and includes advanced features such as pagination, category filtering, low-stock alerts, and inventory movement history tracking.



Tech Stack

* Python 3.9+
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* JWT Authentication
* Pytest
* Docker



Features

Authentication

* User Registration
* User Login
* JWT Token Authentication
* Role-Based Access Control (Admin / Staff)

Product Management

* Create Product
* View All Products
* View Product by ID
* Update Product
* Delete Product

Supplier Management

* Create Supplier
* View Suppliers
* Update Supplier
* Delete Supplier

Stock Management

* Stock Inward
* Stock Outward
* Stock History Tracking
* Low Stock Alerts

Business Rules

* SKU must be unique
* Product must exist before stock updates
* Stock quantity cannot become negative
* Every stock movement is tracked and stored

Validation

* Email validation
* Positive product price validation
* Positive stock quantity validation
* Proper HTTP exception handling

Bonus Features

* Pagination
* Category Filtering
* Low Stock Alerts
* Role-Based Authorization
* Docker Support
* Pytest Unit Testing
* Enhanced Swagger Documentation



Installation

Clone Repository

bash
git clone <repository-url>
cd warehouse_inventory_system


Create Virtual Environment

bash
python -m venv venv


Activate Virtual Environment

Windows:

bash
venv\Scripts\activate


Install Dependencies

bash
pip install -r requirements.txt




Run Application

bash
uvicorn main:app --reload


Application URL:

text
http://127.0.0.1:8000


Swagger Documentation:

text
http://127.0.0.1:8000/docs




API Endpoints

Authentication

| Method | Endpoint       | Description   |
| ------ | -------------- | ------------- |
| POST   | /auth/register | Register User |
| POST   | /auth/login    | Login User    |

Products

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | /products      | Create Product    |
| GET    | /products      | Get All Products  |
| GET    | /products/{id} | Get Product By ID |
| PUT    | /products/{id} | Update Product    |
| DELETE | /products/{id} | Delete Product    |

Suppliers

| Method | Endpoint        | Description       |
| ------ | --------------- | ----------------- |
| POST   | /suppliers      | Create Supplier   |
| GET    | /suppliers      | Get All Suppliers |
| PUT    | /suppliers/{id} | Update Supplier   |
| DELETE | /suppliers/{id} | Delete Supplier   |

Stock Management

| Method | Endpoint       | Description        |
| ------ | -------------- | ------------------ |
| POST   | /stock/inward  | Add Stock          |
| POST   | /stock/outward | Remove Stock       |
| GET    | /stock/history | View Stock History |



Pagination Example

http
GET /products?page=1&limit=10




Category Filter Example

http
GET /products?category=Electronics




Running Tests

bash
pytest


Expected Output:

text
1 passed


Docker Support

Build Docker Image:

bash
docker build -t warehouse-inventory .


Run Container:

bash
docker run -p 8000:8000 warehouse-inventory




Author

Developed as part of the Backend Development Assignment using FastAPI and SQLAlchemy.
