from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.models import Tag

# Retrieves an existing tag or creates a new one if it does not exist.


def get_or_create_tag(session: Session, name: str) -> Tag | None:
    stmt = select(Tag).where(func.lower(Tag.name) == name.lower())

    tag = session.scalars(stmt).one_or_none()

    if tag is None:
        tag = Tag(name=name)
        session.add(tag)

        session.commit()
        session.refresh(tag)
        return tag
    else:
        return None
