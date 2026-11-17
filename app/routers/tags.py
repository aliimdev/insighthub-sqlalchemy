from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated


from app.database import Db
from app.services.tag_service import get_or_create_tag
from app.schemas.tag import TagCreate, TagOut

router = APIRouter(
    prefix="/tags",
    tags=["Tags"],
)


#  create a new tag.
@router.post(
    "/",
    response_model=TagOut,
    status_code=status.HTTP_200_OK,
)
def create_or_get_tag(
    data: TagCreate,
    session: Db,
):
    tag = get_or_create_tag(
        session=session,
        name=data.name,
    )

    if tag is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="tag already exist"
        )

    return tag
