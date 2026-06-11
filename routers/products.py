from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.permissions import admin_only
from app import models, schemas
from app.deps import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    existing_product = db.query(
        models.Product
    ).filter(
        models.Product.sku == product.sku
    ).first()

    if existing_product:
        raise HTTPException(
            status_code=400,
            detail="SKU already exists"
        )

    new_product = models.Product(**product.dict())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.get("/")
def get_products(
    page: int = 1,
    limit: int = 10,
    category: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(models.Product)

    if category:
        query = query.filter(
            models.Product.category == category
        )

    skip = (page - 1) * limit

    products = query.offset(skip).limit(limit).all()

    return products

@router.get("/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(
        models.Product
    ).filter(
        models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.put("/{product_id}")
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    db_product = db.query(
        models.Product
    ).filter(
        models.Product.id == product_id
    ).first()

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db_product.product_name = product.product_name
    db_product.sku = product.sku
    db_product.category = product.category
    db_product.price = product.price
    db_product.stock_quantity = product.stock_quantity

    db.commit()

    return {
        "message": "Product updated successfully"
    }


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    product = db.query(
        models.Product
    ).filter(
        models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }