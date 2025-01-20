from fastapi import Depends, HTTPException
from fastapi_users import FastAPIUsers
from ..models.user import User

from ..config.initializes import fastapi_init


async def is_doctor(user: User = Depends(fastapi_init.current_user())):
    """
    Function checked if the user has role 'DOCTOR'.
    """
    if user.role != "DOCTOR":
        raise HTTPException(
            status_code=403,
            detail="Only doctors can access this route."
        )
    return user

async def is_active_user(user: User = Depends(fastapi_init.current_user())):
    """
    Check if the user is active.
    """
    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Inactive user."
        )
    return user
