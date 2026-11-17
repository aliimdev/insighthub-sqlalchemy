from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import Db
from app.services.user_service import (
    create_user,
    get_users,
    search_users_by_name,
    update_user,
    delete_user,
)
from app.schemas.user import UserRegisterIn, UserUpdateIn, UserOut

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# Create a new user with their profile.
@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user_endpoint(data: UserRegisterIn, session: Db):

    user = create_user(
        session=session,
        email=data.email,
        full_name=data.full_name,
        password=data.password,
        bio=data.bio,
    )

    return user


# Get a list of users.
@router.get("/", response_model=list[UserOut])
def read_users(
    session: Db,
    limit: int = 5,
):
    return get_users(session=session, limit=limit)


# Search users by their full name.
@router.get("/search", response_model=list[UserOut])
def search_users(name: str, session: Db):
    return search_users_by_name(session=session, name=name)


# Update a user's profile.
@router.patch("/{user_id}", response_model=UserOut)
def edit_user(user_id: int, data: UserUpdateIn, session: Db):
    user = update_user(
        session=session,
        user_id=user_id,
        full_name=data.full_name,
        bio=data.bio,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


# Delete a user.
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_user(user_id: int, session: Db):
    deleted = delete_user(session=session, user_id=user_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    session.commit()
