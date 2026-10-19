from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Tag


# Retrieves an existing tag or creates a new one if it does not exist.

def get_or_create_tag(session: Session, name: str) -> Tag:
    stmt = select(Tag).where(Tag.name == name)
    tag = session.scalars(stmt).one_or_none()

    if tag is None:
        tag = Tag(name=name)
        session.add(tag)
    return tag
