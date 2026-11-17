
from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict,
    Field,
    field_validator,
    AliasPath,
)
from datetime import datetime


class UserRegisterIn(BaseModel):
    # Validates user registration data.

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

    full_name: str = Field(min_length=1, max_length=150, description="User full name")

    email: EmailStr = Field(description="User email address")

    password: str = Field(min_length=8, description="User password")

    bio: str | None = Field(default=None, description="Optional user biography")

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        # Normalizes the email address to lowercase.
        return value.lower()


class UserUpdateIn(BaseModel):
    # Validates user profile update data.

    model_config = ConfigDict(str_strip_whitespace=True)

    full_name: str | None = Field(
        default=None, min_length=1, max_length=150, description="User full name"
    )

    bio: str | None = Field(default=None, description="Optional user biography")


class UserOut(BaseModel):
    # Defines the structure of user data returned by the API.

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int = Field(description="User unique ID")

    email: EmailStr = Field(description="User email address")

    created_at: datetime = Field(description="User registration date")

    full_name: str = Field(
        validation_alias=AliasPath("profile", "full_name"), description="User full name"
    )

    bio: str | None = Field(
        default=None,
        validation_alias=AliasPath("profile", "bio"),
        description="User biography",
    )
