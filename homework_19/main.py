from sqlalchemy.orm import (
    Session as SessionType,
    scoped_session,
    sessionmaker,
)

from models import Author, Book
from models.base import engine

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def create_author(session: SessionType, name:str) -> Author:
    """

    :param session:
    :param name:
    :return:
    """

    author = Author(name=name)
    print("create author", author)
    session.add(author)
    session.commit()
    print("saved author", author)

    return author

def create_books_for_author(
    session: SessionType,
    name: str,
    *book_names: str,
) -> list [Book]:
    """

    :param session:
    :param name:
    :param post_names:
    :return:
    """
    author = (
        session
        .query(Author)
        .filter_by(name=name)
        .one()
    )

    for book_name in book_names:
        book = Book(book_name=book_name, author=author)
        print("create book", book)
        session.add(book)

    session.commit()

    print("author's books: ", author.books)
    return author.books

def main():
    """

    :return:
    """
    # Base.metadata.create_all() # NEVER
    session = Session()
    john_tolkien = create_author(session, "Джон Р.Р. Толкиен")
    another_john_tolkien = session.get(Author, john_tolkien.id)
    print("another_john_tolkien: ", another_john_tolkien)
    viktor_pelevin = create_author(session, "Пелевин В.О.")
    another_viktor_pelevin = session.get(Author, viktor_pelevin.id)
    print("another_viktor_pelevin: ", another_viktor_pelevin)
    session.refresh(viktor_pelevin)

    create_books_for_author(
        session,
        "Джон Р.Р. Толкиен",
        "Хоббит",
        "Властелин колец",
        "Сильмарилион",
    )

    create_books_for_author(
        session,
        "Пелевин В.О.",
        "Чапаев и Пустота",
        "Empire V",
        "Омон Ра",
    )

if __name__ == '__main__':
    main()