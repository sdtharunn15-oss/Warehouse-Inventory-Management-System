from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.permissions import admin_only
from app import models, schemas
from app.deps import get_db

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)


@router.post("/")
def create_supplier(
    supplier: schemas.SupplierCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):
    new_supplier = models.Supplier(**supplier.dict())

    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)

    return new_supplier


@router.get("/")
def get_suppliers(
    db: Session = Depends(get_db)
):
    return db.query(models.Supplier).all()


@router.put("/{supplier_id}")
def update_supplier(
    supplier_id: int,
    supplier: schemas.SupplierCreate,
    db: Session = Depends(get_db)
):

    db_supplier = db.query(
        models.Supplier
    ).filter(
        models.Supplier.id == supplier_id
    ).first()

    if not db_supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    db_supplier.supplier_name = supplier.supplier_name
    db_supplier.email = supplier.email
    db_supplier.phone = supplier.phone

    db.commit()

    return {
        "message": "Supplier updated successfully"
    }


@router.delete("/{supplier_id}")
def delete_supplier(
    supplier_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    supplier = db.query(
        models.Supplier
    ).filter(
        models.Supplier.id == supplier_id
    ).first()

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    db.delete(supplier)
    db.commit()

    return {
        "message": "Supplier deleted successfully"
    }