from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict,
    Field,
    field_validator,
    AliasPath,
)
from datetime import datetime


class TagCreate(BaseModel):
    #Schema for validating tag creation data.

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(
        min_length=1,
        max_length=50,
        description="Tag name",
    )

    @field_validator("name")
    @classmethod
    def normalize_tag(cls, value: str) -> str:
        return value.title()


class TagOut(BaseModel):
    """Schema for returning basic tag information."""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="Unique ID of tag")

    name: str = Field(description="Tag name")

    created_at: datetime = Field(description="Tag creation date")


class TagDetailOut(TagOut):
    """Schema for returning a tag with its related documents."""

    document_ids: list[int] = Field(description="IDs of related documents")

    document_titles: list[str] = Field(description="Titles of related documents")
