import json
import falcon
from falcon import App, Request, Response
from books import BOOKS

class BooksListResource:
    def on_get(self, req: Request, res: Response):
        books_as_list = [
            {"id": books_id, "name": name}
            for books_id, name in BOOKS.items()
        ]

        res.text = json.dumps(books_as_list)

class BooksDetailsResource:
    def on_get(self, req: Request, res: Response, book_id: str):
        try:
            book_id = int(book_id)
            name = BOOKS[book_id]
        except ValueError:
            res.status = falcon.HTTP_400
            result = {"message": f"not valid id {book_id!r}"}
        except KeyError:
            res.status = falcon.HTTP_404
            result = {"message": f"book #{book_id} not found"}
        else:
            result = {"id": book_id, "name": name}

        res.text = json.dumps(result)

books_list = BooksListResource()
book_details = BooksDetailsResource()

app = App()

app.add_route("/books", books_list)
app.add_route("/books/{book_id}", book_details)
#/books