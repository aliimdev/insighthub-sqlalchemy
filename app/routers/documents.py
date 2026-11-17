from fastapi import APIRouter, Depends, status, Query, HTTPException
from app.database import Db
from app.services.document_service import search_documents
from app.schemas.document import DocumentOut

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


# Search documents by keyword with pagination.
@router.get("/", response_model=list[DocumentOut])
def read_documents(
    session: Db,
    keyword: str | None = None,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=5, ge=1, le=100),
):
    documents = search_documents(
        session=session,
        keyword=keyword,
        page=page,
        page_size=page_size,
    )

    if not documents:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No documents found",
        )

    return documents
