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


books_list = BooksListResource()

app = App()

app.add_route("/books", books_list)
#/books