from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Book(Base):
    book_name = Column(String(200), unique = False, nullable=False)
    author_id = Column(Integer, ForeignKey("my_authors.id"), nullable=False, unique=True)

    author = relationship("Author", back_populates="books")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(" 
            f"id={self.id}, " 
            f"book_name={self.book_name!r}, "
            f"author_id={self.author_id} )"
        )