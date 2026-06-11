from fastapi import Depends, HTTPException
from app.oauth2 import get_current_user


def admin_only(
    current_user=Depends(get_current_user)
):

    if current_user["role"] != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user