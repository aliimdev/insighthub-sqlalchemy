from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from app.schemas import UserOut, TagOut


class DocumentOut(BaseModel):
    #Schema for returning document information with its author and tags.

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="Unique ID of document")

    user_id: int = Field(description="Unique ID of document owner")

    title: str = Field(description="Document title")

    content: str | None = Field(default=None, description="Document content")

    created_at: datetime = Field(description="Document creation date")

    updated_at: datetime = Field(description="Document last update date")

    author: UserOut = Field(description="Author information")

    tags: list[TagOut] = Field(description="List of associated tags")
