from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from .base import Base

class Author(Base):

    name = Column(String(200), unique=True)

    books = relationship("Book", back_populates="author")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(" 
            f"id={self.id}, " 
            f"name={self.name!r})"
        )