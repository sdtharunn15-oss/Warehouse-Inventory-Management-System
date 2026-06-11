from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.deps import get_db
from app.utils import hash_password, verify_password
from app.oauth2 import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(
        models.User
    ).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully"
    }


@router.post("/login")
def login(
    user: schemas.LoginRequest,
    db: Session = Depends(get_db)
):

    db_user = db.query(
        models.User
    ).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(
        {
            "user_id": db_user.id,
            "role": db_user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }