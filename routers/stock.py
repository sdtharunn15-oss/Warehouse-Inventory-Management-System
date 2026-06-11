from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.deps import get_db
from app.permissions import admin_only
router = APIRouter(
    prefix="/stock",
    tags=["Stock Management"]
)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.deps import get_db

router = APIRouter(
    prefix="/stock",
    tags=["Stock Management"]
)

@router.post("/outward")
def stock_outward(
    stock: schemas.StockRequest,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    product = db.query(
        models.Product
    ).filter(
        models.Product.id == stock.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.stock_quantity < stock.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    product.stock_quantity -= stock.quantity


    if product.stock_quantity < 10:


     history = models.StockHistory(
        product_id=stock.product_id,
        movement_type="OUTWARD",
        quantity=stock.quantity
    )

    db.add(history)
    db.commit()

    return {
        "message": "Stock removed successfully",
        "alert": "Low Stock Alert"
    }

@router.get("/history")
def stock_history(
    db: Session = Depends(get_db)
):
    return db.query(
        models.StockHistory
    ).all()

@router.post("/inward")
def stock_inward(
    stock: schemas.StockRequest,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):
    ...